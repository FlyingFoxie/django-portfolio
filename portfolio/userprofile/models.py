from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)
	birthday = models.DateField(null=True)
	headline = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="neko.png", null=True, blank=True)

	@property
	def calculate_age(self):
		return int((datetime.now().date() - self.birthday).days / 365.25)

	def __str__(self):
		return self.name

class Education(models.Model):
	profile = models.ForeignKey(Profile, default=None, on_delete=models.CASCADE, related_name='education')
	institute = models.CharField(max_length=200, null=True)
	course = models.CharField(max_length=200, null=True)
	start_date = models.DateField(null=True)
	end_date = models.DateField(null=True)

	def __str__(self):
		name = self.institute + '({})'.format(self.profile.name)
		return name

class Skill(models.Model):
	profile = models.ForeignKey(Profile, default=None, on_delete=models.CASCADE, related_name='skill')
	skills = models.CharField(max_length=200, null=True)
	skills_description = RichTextUploadingField(null=True)
	skills_level = models.IntegerField(
		default=1,
		validators=[MaxValueValidator(100), MinValueValidator(1)]
		)

	def __str__(self):
		name = self.skills + '({})'.format(self.profile.name)
		return name

class Experience(models.Model):
	profile = models.ForeignKey(Profile, default=None, on_delete=models.CASCADE, related_name='experience')	
	company_name = models.CharField(max_length=200, null=True)
	company_address = models.CharField(max_length=200, null=True)
	job_title = models.CharField(max_length=200, null=True)
	start_date = models.DateField(null=True)
	end_date = models.DateField(null=True)
	job_description = RichTextUploadingField(null=True)

	@property
	def duration(self):
		days_diff = int((self.end_date-self.start_date).days)
		years_diff = str(int(days_diff/365))
		months_diff = str(int((days_diff%365)/30))
		return years_diff + ' years and ' + months_diff + ' months'
		

	def __str__(self):
		name = self.company_name + '({})'.format(self.profile.name)
		return name
