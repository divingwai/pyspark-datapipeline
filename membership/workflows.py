import dnadb.models

workflow = dnadb.models.Workflow('membership')

notebook1 = dnadb.models.Notebook('customer')

def function1(spark):
    print('cell 1')

def function2(spark):
    print('cell 2')

cell1 = dnadb.models.Cell(function1)

cell2 = dnadb.models.Cell(function2)


notebook1.add_cell(cell1)
notebook1.add_cell(cell2)


notebook2 = dnadb.models.Notebook('restaurant')

notebook3 = dnadb.models.Notebook('shop')

workflow.add_notebook(notebook1)
workflow.add_notebook(notebook2)
workflow.add_notebook(notebook3)

