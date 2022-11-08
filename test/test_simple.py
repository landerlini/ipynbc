from ipynbc.convert_notebook import convert_notebook
import os.path

here = os.path.dirname(__file__)


def test_simple():
    input_file = os.path.join(here, 'notebooks', "Simple.ipynb")
    output_file = os.path.join(here, 'notebooks', "Simple.html")

    convert_notebook(input_file, output_file)