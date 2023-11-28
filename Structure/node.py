class Employee(dict):
    def __init__(self, name, supervisorName):
        super().__init__()
        self.__dict__ = self
        self.name = name
        self.supervisorName = supervisorName
        self.version = 1
        self.underlingList = []

    def allUnderlings(self):
        if not self.underlingList:
            return self
        else:
            allUnderlingsList = []
            for underling in self.underlingList:
                allUnderlingsList.append(underling.allUnderlings())
            return allUnderlingsList
        
    def sharedSupervisor(self):
        supervisor = self.searchName(self.supervisorName)
        return supervisor.underlingList
    
    def searchName(self, name):
        if self.name == name:
            return self
        else:
            employee = None
            for underling in self.underlingList:
                if underling.searchName(name):
                    employee = underling.searchName(name)
            return employee
        
    def from_dict(dict_):
        node = Employee(dict_['name'], dict_['supervisorName'])
        node.underlingList = list(map(node.from_dict, node.underlingList))
        return node