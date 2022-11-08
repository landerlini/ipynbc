from copy import copy
import re


def parse_cell(cell):
    """
    Parse a cell of the notebook

    :param cell: a dictionaty obtained from nbconvert
    :return:
    """
    cell = copy(cell)
    if cell['cell_type'] == 'code':
        cell['execution_count'] = 1
        if re.match(r".*ipynbc:skip.*", cell['source'].split('\n')[0]):
            return None

        if re.match(r".*ipynbc:keep.*", cell['source'].split('\n')[0]):
            cell['source'] = "\n".join(cell['source'].split('\n')[1:])
            return cell

        if len(cell['outputs']) == 0:
            return None
        cell['metadata']['tags'] = ['remove_input']
        return cell

    return cell
