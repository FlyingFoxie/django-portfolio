from django.forms import ModelForm, TextInput
from django.forms.models import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User #import django default user model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout

from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = [
			'username', 
			'email', 
			'password1', 
			'password2'
			]

class profileForm(ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'
		widgets = {
			'birthday':TextInput(attrs={'type': 'date'}),
		}
		exclude = ['user']

	def __init__(self, *args, **kwargs):
		super(profileForm, self).__init__(*args,**kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.form_id = 'id-profileForm'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-10'
		self.fields['profile_pic'].label = "Profile Pic"
		self.fields['name'].label = "Name"
		self.fields['phone'].label = "Phone"
		self.fields['email'].label = "Email"
		self.fields['address'].label = "Address"
		self.fields['birthday'].label = "Birthday"
		self.fields['headline'].label = "Headline"
		self.helper.layout = Layout(
		        'profile_pic',
		        'name',
		        'phone',
		        'email',
		        'address',
		        'birthday',
		        'headline',
		  )

