from setuptools import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()
setup(
    name="matextract",
    version="0.1.1",
    description="Style and Imports for the Structured Data Extraction Book",
    author="Mara Wilhelmi, Martino Rios Garcia, Sherjeel Shabih, Maria Victoria Gil Matellanes, Santiago Miret, Christoph Koch, Pepe Marquez, and Kevin Maik Jablonka",
    author_email="mail@kjablonka.com",
    license="MIT",
    packages=["matextract"],
    python_requires=">=3.9,<=3.11",
    install_requires=required,
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
