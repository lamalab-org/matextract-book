import os
import tempfile
import backoff
import requests
import pubchempy as pcp
import diskcache as dc
from rdkit import Chem


CACTUS = "https://cactus.nci.nih.gov/chemical/structure/{0}/{1}"


def convert_pdf_with_nougat(
    pdf_path, output_dir, model="0.1.0-small", batch_size=1, no_skipping=False
):
    """
    Converts a PDF to Markdown using NOUGAT.

    :param pdf_path: Path to the PDF to be converted.
    :param output_dir: Output directory for the converted files.
    :param model: Model tag to use (default: 0.1.0-small).
    :param batch_size: Batch size for processing (default: 1).
    :param no_skipping: Flag to disable the failure detection heuristic.
    """
    cmd = f"nougat {pdf_path} -o {output_dir} -m {model} -b {batch_size}"
    if no_skipping:
        cmd += " --no-skipping"
    os.system(cmd)


def convert_pdf_to_markdown_text(
    pdf_path, model="0.1.0-small", batch_size=1, no_skipping=False
):
    with tempfile.TemporaryDirectory() as output_dir:
        convert_pdf_with_nougat(pdf_path, output_dir, model, batch_size, no_skipping)
        markdown_files = [
            os.path.join(output_dir, f)
            for f in os.listdir(output_dir)
            if f.endswith(".md")
        ]
        if len(markdown_files) == 0:
            raise ValueError("No markdown files found in the output directory.")

        with open(markdown_files[0], "r") as f:
            return f.read()

        raise ValueError("Multiple markdown files found in the output directory.")


def canonicalize_smiles(smiles: str) -> str:
    """Canonicalize smiles using RDKit"""
    mol = Chem.MolFromSmiles(smiles)
    return Chem.MolToSmiles(mol)


@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_time=10)
def cactus_request_w_backoff(inp, rep="SMILES"):
    url = CACTUS.format(inp, rep)
    response = requests.get(url, allow_redirects=True, timeout=10)
    response.raise_for_status()
    resp = response.text
    if "html" in resp:
        return None
    return resp


cache = dc.Cache("cache")


@cache.memoize()
def name_to_smiles(name: str) -> str:
    """Use the chemical name resolver https://cactus.nci.nih.gov/chemical/structure.
    If this does not work, use pubchem.
    """
    try:
        smiles = cactus_request_w_backoff(name, rep="SMILES")
        if smiles is None:
            raise Exception
        return canonicalize_smiles(smiles)
    except Exception:
        try:
            compound = pcp.get_compounds(name, "name")
            return canonicalize_smiles(compound[0].canonical_smiles)
        except Exception:
            return None
