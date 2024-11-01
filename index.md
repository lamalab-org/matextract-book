# From Text to Insight: Large Language Models for Chemical Data Extraction

## About this book

Structured data is at the heart of machine learning. LLMs offer a convenient way to generate structured data based on unstructured inputs.
This book gives hands-on examples of the different steps in the extraction workflow using LLMs.

You can find more background on the topics covered in this book in our [review article](https://arxiv.org/abs/2407.16867).

## How to use this book?

This book is based on Jupyter notebooks. That is, beyond simply reading along, you can also run the notebooks yourself.
You have different options to do so.

### Running it on your own machine

If you have a reasonably modern computer you will be able to run many of the notebooks on your own hardware.
Note, however, that certain notebooks will need to be run on GPUs. Those notebooks have a note about this on the top of the notebook.

In addition to hardware, you will also need some software. All relevant dependencies can be installed via the package for this online book.

Overall, you will need to run through the following steps. Note that we currently only support Linux and Mac. If you want to run the notebooks on Windows,
we recommend that you [install WSL](https://learn.microsoft.com/en-us/windows/wsl/install) and then run the notebooks from the Linux environment.

0. Use Python 3.11 (the code might also work on other versions, but we only tested 3.11)

1. Clone the repository

    `git clone https://github.com/lamalab-org/matextract-book.git`

    Then, go into the folder

    `cd matextract-book`

2. (Optional, but recommended) Create a [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/):

    `python3 -m venv .venv`

    Then activate the environment

    `source .venv/bin/activate`


3. Install dependencies

    `cd package && pip install .`

### `matextract` package

Running the commands above will install a package called `matextract`. We will import it in all notebooks as it sets some plotting styles, but also useful defaults:

- we turn on caching - [a very effective way to save money if you use LLMs](https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/)
- we load some environment variables, such as API keys that you can edit in the `.env` file. This `.env` file needs to be in the root directory of the repository - i.e., where the `.env.example` file is placed. If you want to know more on how and why to use environment variables and `.env` files, you can check [this article](https://medium.com/@sujathamudadla1213/what-is-the-use-of-env-8d6b3eb94843).

## Table of Contents

```{tableofcontents}
```

## Acknowledgment

This work was supported by:

- [Carl-Zeiss Foundation](https://www.carl-zeiss-stiftung.de/) (Mara Schilling-Wilhelmi, and Kevin Maik Jablonka)
- Intel and Merck (via AWASES programme, Mara Schilling-Wilhelmi, and Kevin Maik Jablonka)
- [FAIRmat](https://www.fairmat-nfdi.eu/fairmat/) (Sherjeel Shabih, Christoph T. Koch, José A. Márquez, and Kevin Maik Jablonka)
- [Spanish AEI](https://www.aei.gob.es/) (Martiño Ríos-García, and María Victoria Gil)
- [CSIC](https://www.csic.es/) (Martiño Ríos-García, and María Victoria Gil)

## Citation

If you use this book in your research, please cite it as follows:

```bibtex
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
