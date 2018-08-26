from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class EmployeeForm(FlaskForm):
    name = StringField('الاسم', validators=[DataRequired()])
    employee_id = StringField('الرقم الوظيفي', validators=[DataRequired()])
    email = StringField('البريد الإلكتروني')
    submit = SubmitField('إدخال')