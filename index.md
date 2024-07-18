# From Text to Insight: Large Language Models for Materials Science Data Extraction

## About this book

Structured data is at the heart of machine learning. LLMs offer a convenient way to generate structured data based on unstructured inputs.
This book gives hands-on examples of the different steps in the extraction workflow using LLMs.

## How to use this book?

This book is based on Jupyter notebooks. That is, beyond simply reading along, you can also run the notebooks yourself.
You have different options to do so.

### Running it on your own machine
If you have a reasonably modern computer you will be able to run many of the notebooks on your own hardware.
Note, however, that certain notebooks will need to be run on GPUs. Those notebooks have a notebook about this on the top of the notebook.

In addition to hardware, you will also need some software. All relevant dependencies can be installed via the package for this online book.

Overall, you will need to run through the following steps.

0. Use Python 3.11 (the code might also work on other versions, but we only tested 3.11)

1. (Optional, but recommended) Create a [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/): `python3 -m venv .venv`

   Then activate the environment

   `source .venv/bin/activate`

2. Clone the repository

    `git clone https://github.com/lamalab-org/matextract-book.git`

3. Install dependencies

    `cd package && pip install . `


### `matextract` package

Running the commands above will install a package called `matextract`. We will import it in all notebooks as it sets some plotting styles, but also useful defaults:

- we turn on caching - [a very effective way to save money if you use LLMs](https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/)
- we load some environment variables, such as API keys that you can edit in the `.env` file


## Table of Contents

```{tableofcontents}
```

## Acknowledgment

The work on this book was supported by the [Carl-Zeiss Foundation](https://www.carl-zeiss-stiftung.de) as well as Intel and Merck via the AWASES programme.
