from setuptools import setup

setup(
    name="llmstructdata",
    version="0.1.1",
    description="Style and Imports for the Structured Data Extraction Book",
    author="Mara Wilhelmi, Sherjeel Shabih, Martino Rıos Garcıa, Santiago Miret,Christoph Koch, Pepe Marquez, and Kevin Maik Jablonka",
    author_email="mail@kjablonka.com",
    license="MIT",
    packages=["llmstructdata"],
    install_requires=[
        "pandas",
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
