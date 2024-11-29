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
@misc{schillingwilhelmi2024textinsightlargelanguage,
      title={From Text to Insight: Large Language Models for Materials Science Data Extraction},
      author={Mara Schilling-Wilhelmi and Martiño Ríos-García and Sherjeel Shabih and María Victoria Gil and Santiago Miret and Christoph T. Koch and José A. Márquez and Kevin Maik Jablonka},
      year={2024},
      eprint={2407.16867},
      archivePrefix={arXiv},
      primaryClass={cond-mat.mtrl-sci},
      url={https://arxiv.org/abs/2407.16867},
}
```
