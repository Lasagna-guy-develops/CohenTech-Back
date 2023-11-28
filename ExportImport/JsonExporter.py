import os
import json
from Structure.tree import Tree

class Exporter:
    def __init__(self):
        self.name = "instance"

    def exportToJson(self, tree):
        data = self.treeToJson(tree)
        self.writeFile(data, os.getcwd() + '/Static/Data.json')

    def treeToJson(self, tree):
        json_str = json.dumps(tree.topSupervisor, indent=2)
        return json_str

    def writeFile(self, data, file):
        with open(file, 'w+') as outfile:
            json.dump(data, outfile)
    