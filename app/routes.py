from app.forms import EmployeeForm
from app.models import Employee
from flask import render_template, flash
from app import app, db



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/employee', methods=['GET', 'POST'])
def add_employee():
    form = EmployeeForm()
    if form.validate_on_submit():
        employee = Employee(name=form.name.data, employee_id=form.employee_id.data, email=form.email.data)
        db.session.add(employee)
        db.session.commit()
        flash('تم إدخال بيانات الموظف {}'.format(employee.name))
    return render_template('add_employee.html', form=form)


@app.route('/employee_list', methods=['GET'])
def list_employee():
    employees = Employee.query.all()
    return render_template('list_employee.html', employees=employees)

