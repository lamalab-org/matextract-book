<h1 align="center">
  From Text to Insight: Large Language Models for Materials Science Data Extraction
</h1>

<p align="center">
    <a href="https://github.com/lamalab-org/matextract-book/actions/workflows/tests.yml">
        <img alt="Test and build" src="https://github.com/lamalab-org/matextract-book/actions/workflows/publish.yml/badge.svg" />
    </a>
    <a href="https://github.com/lamalab-org/matextract-book/blob/main/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg" alt="Contributor Covenant"/>
    </a>
</p>

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./_static/images/logo_white.png">
  <img alt="MatExtract" src="./_static/images/logo_white.png" width='300px'>
</picture>
</p>

MatExtract is a guide to structured (materials) data extraction using LLMs.
Read it on [matextract.pub](https://matextract.pub).

For more details, see our [review article](https://arxiv.org/abs/2407.16867).

## Installation

To install the package and its dependencies:

```bash
pip install -e .
```

For development, we recommend using a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install -e .
```

## Citation

If you find our work useful, please cite our review article:

``` bibtex
@article{Schilling_Wilhelmi_2025,
  title={From text to insight: large language models for chemical data extraction},
  ISSN={1460-4744},
  url={http://dx.doi.org/10.1039/D4CS00913D},
  DOI={10.1039/d4cs00913d},
  journal={Chemical Society Reviews},
  publisher={Royal Society of Chemistry (RSC)},
  author={Schilling-Wilhelmi, Mara and Ríos-García, Martiño and Shabih, Sherjeel and Gil, María Victoria and Miret, Santiago and Koch, Christoph T. and Márquez, José A. and Jablonka, Kevin Maik},
  year={2025}
}
```
