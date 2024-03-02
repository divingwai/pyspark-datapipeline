from typing import List


class Cell:

    def __init__(self, code: function) -> None:
        self.code = code

    def get_code(self) -> str:
        return self.code

class Notebook:

    def __init__(self, name) -> None:
        self._name = name
        self._cells = []
    
    def add_cell(self, cell: Cell):
        self._cells.append(cell)

    def get_cells(self):
        return self._cells
    
    def remove_cell(self, cell: Cell):
        self._cells.remove(cell)

class Workflow:

    def __init__(self, name):
        self._name = name
        self._notebooks = []

    def get_notebooks(self) -> List[Notebook]:
        return self._notebooks
        
    def add_notebook(self, notebook: Notebook):
        self._notebooks.append(notebook)

    def remove_notebook(self, notebook):
        self._notebooks.remove(notebook)

