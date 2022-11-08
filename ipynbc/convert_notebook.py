from traitlets.config import Config
import nbformat as nbf
from nbconvert.exporters import HTMLExporter
from typing import Union
from copy import copy
from ipynbc.parse_cell import parse_cell

def convert_notebook(input_file: str, output_file: Union[str, None] = None):
    c = Config()
    c.TagRemovePreprocessor.remove_input_tags = ('remove_input',)
    c.TagRemovePreprocessor.enabled = True
    c.HTMLExporter.preprocessors = ["nbconvert.preprocessors.TagRemovePreprocessor"]
    c.HTMLExporter.exclude_input_prompt = True
    c.HTMLExporter.exclude_output_prompt = True

    nb = nbf.read(open(input_file, encoding='utf-8'), as_version=4)
    modified = copy(nb)
    modified['cells'] = [parse_cell(c) for c in nb['cells'] if parse_cell(c) is not None]
    output = HTMLExporter(config=c).from_notebook_node(modified)

    output_file = output_file if output_file is not None else input_file.replace(".ipynb", ".html")
    with open(output_file, "w", encoding='utf-8') as f:
        f.write(output[0])


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("inputfile", nargs=1, help="Input file name", type=str)
    parser.add_argument("outputfile", nargs=1, help="Output file name", default=None)

    args = parser.parse_args()

    convert_notebook(args.inputfile, args.output_file)