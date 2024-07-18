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

Overall, you will need to run through the following steps:

0. (Optional, but recommended) Create a [conda environment](https://docs.anaconda.com/miniconda/) with `jupyter` installed

   `conda create -n matextract python=3.9 jupyterlab`.

   Then activate the environment

   `conda activate matextract`

1. Clone the repository

    `git clone https://github.com/lamalab-org/matextract-book.git`

2. Install dependencies

    `cd package && pip install . `


## Table of Contents

```{tableofcontents}
```

## Acknowledgment

The work on this book was supported by the [Carl-Zeiss Foundation](https://www.carl-zeiss-stiftung.de) as well as Intel and Merck via the AWASES programme.
