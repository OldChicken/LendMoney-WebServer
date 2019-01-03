
# coding: utf-8

# In[1]:


from wtforms.fields import *
from wtforms.validators import DataRequired, Length
from wtforms_tornado import Form
 
 
class SmsForm(Form):
 
    mobile = StringField(validators=[DataRequired(message='手机号码格式不正确'), Length(min=11, max=11, message='手机号码格式不正确')])

