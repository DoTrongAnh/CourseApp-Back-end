from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Echo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['created']

class CourseOutline(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	description = models.CharField(max_length=1000)
	courseName = models.CharField(max_length=200)
	courseCode = models.CharField(max_length=10)
	hours = models.CharField(max_length=20)
	gradeNote = models.CharField(max_length=1000)
	credits = models.IntegerField(null=True)
	exam = models.CharField(max_length=1000)
	calculator = models.BooleanField()
	author = models.CharField(max_length=200)
	term = models.CharField(max_length=200)

	class Meta:
		ordering = ['created']

class Lab(models.Model):
	outline = models.OneToOneField(CourseOutline, related_name='lab', on_delete=models.CASCADE)
	type = models.CharField(max_length=50)
	number = models.IntegerField()
	safetyTaught = models.BooleanField()
	safetyExamined = models.BooleanField()

class AU(models.Model):
	outline = models.OneToOneField(CourseOutline, related_name='AU', on_delete=models.CASCADE)
	math = models.FloatField()
	naturalScience = models.FloatField()
	complementary = models.FloatField()
	engineerScience = models.FloatField()
	engineerDesign = models.FloatField()

class Grades(models.Model):
	outline = models.OneToOneField(CourseOutline, related_name='grades', on_delete=models.CASCADE)
	Ap = models.FloatField()
	A = models.FloatField()
	Am = models.FloatField()
	Bp = models.FloatField()
	B = models.FloatField()
	Bm = models.FloatField()
	Cp = models.FloatField()
	C = models.FloatField()
	Cm = models.FloatField()
	Dp = models.FloatField()
	D = models.FloatField()

class CourseOutcome(models.Model):
	GradAttribute = models.TextChoices('GradAttribute','A1 A2 A3 A4 A5 A6 A7 A8 A9 A10 A11 A12')
	GradLevel = models.TextChoices('GradLevel', 'I D A')
	outline = models.ForeignKey(CourseOutline, related_name='courseOutcomes', on_delete=models.CASCADE)
	courseOutcome = models.CharField(max_length=200)
	attribute = models.CharField(blank=True, choices=GradAttribute.choices, max_length=10)
	level = models.CharField(blank=True, choices=GradLevel.choices, max_length=3)

class Section(models.Model):
	outline = models.ForeignKey(CourseOutline, related_name='sections', on_delete=models.CASCADE)
	days = ArrayField(models.CharField(max_length=5, blank=True), size=7)
	name = models.CharField(max_length=10)
	timestart = models.CharField(max_length=30, blank=True)
	timeend = models.CharField(max_length=30, blank=True)
	location = models.CharField(max_length=30, blank=True)
	SectionType = models.TextChoices('SectionType','lecture tutorial lab')
	type = models.CharField(blank=True, choices=SectionType.choices, max_length=10)
	studentPerSupervisor = models.CharField(max_length=10, blank=True)

class Instructor(models.Model):
	outline = models.ForeignKey(CourseOutline, related_name='instructors', on_delete=models.CASCADE)
	Role = models.TextChoices('Role','instructor coordinator ta')
	role = models.CharField(blank=True, choices=Role.choices, max_length=15)
	fname = models.CharField(blank=True, max_length=100)
	lname = models.CharField(blank=True, max_length=100)
	phone = models.CharField(blank=True, max_length=20)
	office = models.CharField(blank=True, max_length=20)
	email = models.CharField(blank=True, max_length=200)
	section = models.CharField(max_length=10)

class Component(models.Model):
	outline = models.ForeignKey(CourseOutline, related_name='components', on_delete=models.CASCADE)
	name = models.CharField(blank=True, max_length=200)
	outcomes = ArrayField(models.IntegerField())
	weight = models.FloatField()

class Textbook(models.Model):
	outline = models.ForeignKey(CourseOutline, related_name='textbooks', on_delete=models.CASCADE)
	title = models.CharField(blank=True, max_length=200)
	author = models.CharField(blank=True, max_length=200)
	editionYear = models.CharField(blank=True, max_length=200)
	publisher = models.CharField(blank=True, max_length=200)
	required = models.BooleanField(blank=True)