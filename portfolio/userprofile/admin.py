from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Profile)
#admin.site.register(Experience)

class EducationInLine(admin.TabularInline):
	model = Education
class SkillInLine(admin.TabularInline):
	model = Skill
class ExperienceInLine(admin.TabularInline):
	model = Experience


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	inlines=[
		EducationInLine,
		SkillInLine,
		ExperienceInLine
	]