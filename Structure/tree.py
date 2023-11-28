from Structure.node import Employee

class Tree:

    def __init__(self):
        self.mainTreeNode = []
        self.nonSupervisedEmployees = []
        self.topSupervisor = None
    
    def createEmployee(self, employeeName, supervisorName):
        if not self.topSupervisor:
            employee = Employee(employeeName, None)
            self.mainTreeNode.append(employee)
            self.topSupervisor = employee
        elif not supervisorName:
            self.nonSupervisedEmployees.append(Employee(employeeName, None))
        else:
            supervisor = self.topSupervisor.searchName(supervisorName)
            if not supervisor: raise ValueError("No supervisor with said name")
            employee = Employee(employeeName, supervisor.name)
            self.mainTreeNode.append(employee)
            supervisor.underlingList.append(employee)

    def updateEmployee(self, employeeName, newSupervisorName):
        employee = self.topSupervisor.searchName(employeeName)
        newSupervisor = self.topSupervisor.searchName(newSupervisorName)
        oldSupervisor = self.topSupervisor.searchName(employee.supervisorName)
        employee.version += 1
        oldSupervisor.underlingList.remove(employee)

        employee.supervisor = newSupervisor.name
        newSupervisor.underlingList.append(employee)