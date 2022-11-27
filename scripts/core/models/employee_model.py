from pydantic import BaseModel


class add_employee(BaseModel):
    name: str
    email: str
    phone: str
    country: str
    department: str


class update_employee(BaseModel):
    name: str
    emp_id: str
    email: str
    phone: str
    country: str
    department: str


class delete_employee(BaseModel):
    emp_id: str

