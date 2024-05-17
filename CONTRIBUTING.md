## Contributing a section 

Thank you for considering contributing to the book. Feel free to make a pull request to submit changes! Here is a small [guide](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project) to help.

### Style and formatting

Please use a spell checker and ensure that your text is grammatically correct. We use American English spelling.
A tool such as Grammarly can be helpful in this regard.

### Code formatting

Please use `ruff` to format and lint your code. The `pre-commit` hook will run `ruff` on your code before you commit it.
To install the pre-commit hook, run the following command in the root directory of the repository:

```bash
pre-commit install
```

### Explanations 

We aim that the book is accessible to a wide audience. A first year undergraduate student should be able to understand the content. Please keep this in mind when writing your section.

We can add value to the book by providing explanations of the concepts and techniques used in the code. Please provide explanations of the code and the concepts used in the code.


### Quarto 

We use `quarto` to build the book. Consider the documentation for `quarto` to get an overview of the features available.
In the current setup, you must add your section to the `quarto` configuration file `_quarto.yml` to include it in the book. 
You can add `.qmd` and `.ipynb` files.
You can test the book by running: 
```console
quarto preview
```

## Plotting style 

Use the `book.mplstyle` file to set the plotting style for the book. 

## Margin Notes

Right column notes are intended to provide supplementary information that gives context, serves as a reminder, or offers additional details about the main text. They are not essential for comprehending the main text and can be considered similar to footnotes within the text.
