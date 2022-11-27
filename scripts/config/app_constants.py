class Employee:
    add_employee = '/add_employee'
    list_employee = '/list_employee'
    update_employee = '/update_employee'
    delete_employee = '/delete_employee/{}'


class Status:
    success = 'success'
    error = 'error'
    warning = 'warning'


class Message:
    add_message = 'Added Successfully'
    validation = "Please Enter Valid Email or Phone"
    update_message = "Updated Details Successfully"
    delete_message = "Employee Deleted Successfully"
    department_validation = "Please Enter a Valid Department"


class Response_json:
    success_json = {'status': "OK",
                    'message': ''}
    error_json = {'status': "Error",
                  'message': ''}


class Table:
    employee_table = {
        "header_content": [
            {"key": "name",
             "label": "Name"},
            {"key": "emp_id",
             "label": "Employee ID"},
            {"key": "email",
             "label": "Email"},
            {"key": "phone",
             "label": "Phone"},
            {"key": "country",
             "label": "Country"},
            {"key": "department",
             "label": "Department"}],
        "body_content": []
    }
