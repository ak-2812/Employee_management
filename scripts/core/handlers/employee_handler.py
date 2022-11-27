from scripts.logging.application_logging import logger
from scripts.config.app_constants import Response_json, Message, Table
from scripts.utilities.db_utility import RDBMSUtility
import uuid
import re
import copy


class organization:
    @staticmethod
    def add_employee_handler(req_json):
        """
        Handler Function to add Employee
        :param req_json:
        :type req_json:
        :return: Returns JSON Structure with output
        :rtype:
        """
        try:
            logger.info("inside add_employee_handler")
            if validate_email(req_json.email) and validate_phone(req_json.phone):
                if req_json.department in ["Technology", "Marketing", "Sales", "HR", "Business", "Management"]:
                    emp_id = uuid.uuid1().hex[:4]
                    query = f"""INSERT INTO employee_details(emp_id, name, email, phone, country, department) VALUES 
                    ('{emp_id}',
                    '{req_json.name}',
                    '{req_json.email}',
                    '{req_json.phone}',
                    '{req_json.country}',
                    '{req_json.department}')"""
                    logger.info("Employee add_query" + query)
                    RDBMSUtility().execute_query(qry=query, required=False)
                    Response_json.success_json['emp_Id'] = emp_id
                    Response_json.success_json['message'] = Message.add_message
                    return Response_json.success_json
                else:
                    Response_json.error_json['message'] = Message.department_validation
                    return Response_json.error_json
            else:
                Response_json.error_json['message'] = Message.validation
                return Response_json.error_json
        except Exception as e:
            logger.error("Unable to add Employee" + str(e))
            raise Exception("Unable to add Employee" + str(e))

    @staticmethod
    def list_employee_details():
        """
        Handler Function to list Employee from Database
        :return: Returns JSON Structure with output
        :rtype:
        """
        try:
            logger.info("Inside list_employee_details")
            query = f"""select * from employee_details"""
            result = RDBMSUtility().execute_query(qry=query, required=True)
            logger.info("list Employee query" + query)
            response = copy.deepcopy(Table.employee_table)
            response["body_content"] = result
            return response
        except Exception as e:
            logger.error("Unable to list Employee details" + str(e))
            raise Exception("Unable to list Employee details" + str(e))

    @staticmethod
    def update_employee_handler(req_json):
        """
        Handler Function to update Employee
        :param req_json:
        :type req_json:
        :return: Returns JSON Structure with output
        :rtype:
        """
        try:
            logger.info("Inside update_employee_handler")
            if validate_email(req_json.email) and validate_phone(req_json.phone):
                update_query = f"""update employee_details set name = '{req_json.name}', 
                                                                email = '{req_json.email}',
                                                            phone = '{req_json.phone}',
                    country = '{req_json.country}',
                    department = '{req_json.department}' where emp_id = '{req_json.emp_id}'"""
                logger.info("Update employee details " + update_query)
                RDBMSUtility().execute_query(qry=update_query, required=False)
                Response_json.success_json['message'] = Message.update_message
                return Response_json.success_json
            else:
                Response_json.error_json['message'] = Message.validation
                return Response_json.error_json
        except Exception as e:
            logger.error("Unable to update Employee Details" + str(e))
            raise Exception("Unable to update Employee Details" + str(e))

    @staticmethod
    def delete_employee_handler(req_json):
        """
        Function to return deleted status
        :param req_json:
        :type req_json:
        :return: Returns JSON Structure with output
        :rtype:
        """
        try:
            logger.info("Inside delete employee handler")
            query = f"""delete from employee_details where emp_id = '{req_json.emp_id}'"""
            RDBMSUtility().execute_query(qry=query, required=False)
            response = Response_json.success_json
            response['message'] = Message.delete_message
            return response
        except Exception as e:
            logger.error("Unable to Delete Employee Details" + str(e))
            raise Exception("Unable to Delete Employee Details" + str(e))


def validate_email(email):
    """
    Function to Validate email
    :param email:
    :type email:
    :return: returns True/False by validating
    :rtype:
    """
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    query = f"""select emp_id from employee_details where email = '{email}'"""
    result = RDBMSUtility().execute_query(qry=query, required=True)
    if re.fullmatch(regex, email) and result:
        return True
    else:
        return False


def validate_phone(phone):
    """
    Function to validate phone
    :param phone:
    :type phone:
    :return: returns True/False by validating
    :rtype:
    """
    regex = "^\\+?[1-9][0-9]{7,14}$"
    if re.match(regex, phone):
        return True
    else:
        return False
