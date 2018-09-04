from app.forms import EmployeeForm
from app.models import Employee
from flask import render_template, flash, redirect, url_for, request
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


@app.route('/employee/edit/<int:emp_id>', methods=['GET', 'POST'])
def edit_employee(emp_id):
    employee = Employee.query.get(emp_id)
    form = EmployeeForm(request.form)
    if form.validate_on_submit():
        form = EmployeeForm(request.form)
        employee.name=form.name.data
        employee.employee_id = form.employee_id.data
        employee.email = form.email.data
        db.session.add(employee)
        db.session.commit()
        flash('تم تحديث بيانات الموظف {}'.format(employee.name))
        return render_template('add_employee.html', emp_id=employee.employee_id, form=form)
    form = EmployeeForm()
    form.name.data = employee.name
    form.employee_id.data = employee.employee_id
    form.email.data = employee.email
    return render_template('edit_employee.html', form=form)


@app.route('/employee/delete/<int:emp_id>')
def delete_employee(emp_id):
    employee = Employee.query.get(emp_id)
    db.session.delete(employee)
    db.session.commit()
    flash('تم حذف بيانات الموظف {}'.format(employee.name))
    return redirect(url_for('list_employee'))
