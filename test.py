from Structure.tree import Tree
from ExportImport.JsonExporter import Exporter
import json

def main():
    arbolito = Tree()
    arbolito.createEmployee("Sebas", None)
    arbolito.createEmployee("Juan", "Sebas")
    arbolito.createEmployee("Pedro", "Juan")

    # for emp in arbolito.topSupervisor.allUnderlings():
    #     print(emp.name)
    # for emp in arbolito.topSupervisor.underlingList:
    #     print(emp.name)
    # json_str = json.dumps(arbolito.topSupervisor, indent=2)
    # ob = Exporter()
    # ob.exportToJson(arbolito)
    obj = Importer()
    arb = obj.importFromJson()

if __name__ == "__main__":
    main()
