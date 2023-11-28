import os
import json
import sys
sys.path.append('..')
from pydantic import BaseModel
from typing import Union
from fastapi import FastAPI, Request
from Structure.node import Employee
from Structure.tree import Tree
from ExportImport.JsonExporter import Exporter

my_app = FastAPI()
employees = Tree()

class Item(BaseModel):
    name: str
    supervisorName: str

@my_app.get("/getEmployees")
async def root():
    data = json.dumps(employees.topSupervisor, indent=2)
    return data

@my_app.post("/createEmployee")
async def create_item(item: Item):
    employees.createEmployee(item.name, item.supervisorName)
    return {"message": "request processed"}

@my_app.put("/updateEmployee")
async def update_item(item: Item):
    employees.updateEmployee(item.name, item.supervisorName)
    return {"message": "request processed"}