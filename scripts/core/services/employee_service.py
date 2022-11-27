from fastapi import APIRouter
from scripts.logging.application_logging import logger
from scripts.config.app_constants import Employee
from scripts.core.models.employee_model import add_employee, update_employee, delete_employee
from scripts.core.handlers.employee_handler import organization

router = APIRouter()


@router.post(Employee.add_employee)
async def add_employee(req_json: add_employee):
    """
    Function to add Employee
    :param req_json:
    :type req_json:
    :return: Returns JSON Structure with output
    :rtype:
    """
    try:
        logger.info("Starting add_employee")
        response = organization.add_employee_handler(req_json)
        return response
    except Exception as e:
        logger.error("Unable to Add Employee" + str(e))
        raise Exception("Unable to Add Employee" + str(e))


@router.get(Employee.list_employee)
def list_employee_details():
    """
    Function to return the list of employees
    :return: Returns JSON Structure with output
    :rtype:
    """
    try:
        logger.info("Listing Employee details")
        response = organization.list_employee_details()
        return response
    except Exception as e:
        logger.error("Unable to list Employee Details" + str(e))
        raise Exception("Unable to list Employee Details" + str(e))


@router.put(Employee.update_employee)
def update_employee_details(req_json: update_employee):
    """
    Function to update Employee details
    :param req_json:
    :type req_json:
    :return: Returns JSON Structure with output
    :rtype:
    """
    try:
        logger.info("Starting to update Employee details")
        response = organization.update_employee_handler(req_json)
        return response
    except Exception as e:
        logger.error("Unable to update Employee Details" + str(e))
        raise Exception("Unable to update Employee Details" + str(e))


@router.delete(Employee.delete_employee)
def delete_employee(req_json: delete_employee):
    """
    Function to delete the employee details
    :param req_json:
    :type req_json:
    :return: Returns JSON Structure with output
    :rtype:
    """
    try:
        logger.info("Deleting the selected Employee_id")
        response = organization.delete_employee_handler(req_json)
        return response
    except Exception as e:
        logger.error("Unable to Delete Employee Details" + str(e))
        raise Exception("Unable to Delete Employee Details" + str(e))