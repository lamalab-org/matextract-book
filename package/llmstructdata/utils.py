import os


def convert_pdf_with_nougat(pdf_path, output_dir, model="0.1.0-small", batch_size=1, no_skipping=False):
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