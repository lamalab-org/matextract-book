from setuptools import setup

setup(
    name="llmstructdata",
    version="0.1.1",
    description="Style and Imports for the Structured Data Extraction Book",
    author="Mara Wilhelmi, Sherjeel Shabih, Martino Rios Garcia, Maria Victoria Gil Matellanes, Santiago Miret, Christoph Koch, Pepe Marquez, and Kevin Maik Jablonka",
    author_email="mail@kjablonka.com",
    license="MIT",
    packages=["llmstructdata"],
    install_requires=[
        "accelerate",
        "bert-score",
        "bitsandbytes",
        "chromadb",
        "crossrefapi == 1.0.3",
        "datasets",
        "deepdiff",
        "diskcache",
        "evaluate",
        "huggingface-hub",
        "imutils",
        "instructor",
        "jupyter",
        "langchain-community",
        "langchain-openai",
        "langchain",
        "langchainhub",
        "litellm",
        "matplotlib",
        "mendeleev",
        "munkres",
        "numpy",
        "opencv-python",
        "pandas",
        "pandas<=2.0.0",  # https://github.com/rdkit/rdkit/issues/7159
        "paperscraper",
        "pdf2image",
        "peft",
        "pillow",
        "pint",
        "plotly",
        "pubchempy",
        "pydantic",
        "pymatgen",
        "pymatviz",
        "pystow",
        "pytesseract",
        "python-doctr",
        "python-dotenv",
        "rdkit",
        "requests",
        "rxnscribe @ git+https://github.com/thomas0809/RxnScribe.git",
        "scikit-learn",
        "seaborn",
        "sentence-transformers",
        "torch",
        "transformers",
        "trl",
        "unstructured",
        # "nougat-ocr",
    ],
    long_description="""
# Style and Imports for the Structured Data Extraction Book
""",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Typing :: Typed",
    ],
)
