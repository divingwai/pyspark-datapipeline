

(UPDATE_CLIENT_WF,
UPDATE_SHOP_WF,
UPDATE_SALE_WF) = range(0,3)


def get_client_workflow(spark, target_db: str):

    _spark = spark

    _notebooks = []

    def build_dependencies(notebooks):
        ordered_notebooks = []

        remained_noteoboks = [ n.name for n in notebooks]

        for  iternation in range(0,  len (notebooks)):
            for i in range(0, len)
                xxxx

        return ordered_notebooks


    def wrapped_workflow():
        pass

        def execute(target_db = target_db):
            
            ordered_noteboks = build_dependencies(_notebooks)

            for notebook in ordered_noteboks:
                notebook.execute(spark, target_db)
        

    return wrapped_workflow()


workflow1 = get_client_workflow(spark = 'spark', target_db='target_db')

all_notebooks = workflow1.get_notebooks()

for notebook in all_notebooks:
    functions = notebook.get_functions()


workflow1.execute('spark', 'target_db')
