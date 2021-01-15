# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 18:10:30 2020

@author: anhtr
"""


from rest_framework import serializers
from api.models import *

class EchoSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Echo
        fields = ['id', 'message', 'created']

class LabSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lab
		fields = ['type','number','safetyTaught','safetyExamined']

class AUSerializer(serializers.ModelSerializer):
	class Meta:
		model = AU
		fields = ['math','naturalScience','complementary','engineerScience','engineerDesign']

class GradesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Grades
		fields = ['Ap','A','Am','Bp','B','Bm','Cp','C','Cm','Dp','D']

class OutcomeSerializer(serializers.ModelSerializer):
	class Meta:
		model = CourseOutcome
		fields = ['courseOutcome','attribute','level']

class SectionSerializer(serializers.ModelSerializer):
	days = serializers.ListField(child=serializers.CharField())

	class Meta:
		model = Section
		fields = ['days','name','timestart','timeend','location','type','studentPerSupervisor']

class InstructorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Instructor
		fields = ['role','fname','lname','phone','office','email','section']

class ComponentSerializer(serializers.ModelSerializer):
	outcomes = serializers.ListField(child=serializers.IntegerField())

	class Meta:
		model = Component
		fields = ['name','outcomes','weight']

class TextbookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Textbook
		fields = ['title','author','editionYear','publisher','required']

class CourseOutlineSerializer(serializers.ModelSerializer):
	lab = LabSerializer()
	AU = AUSerializer()
	grades = GradesSerializer()
	courseOutcomes = OutcomeSerializer(many=True)
	sections = SectionSerializer(many=True)
	instructors = InstructorSerializer(many=True)
	components = ComponentSerializer(many=True)
	textbooks = TextbookSerializer(many=True)

	class Meta:
		model = CourseOutline
		fields = ['id','created','description','courseName','courseCode','hours',
		'gradeNote','credits','exam','calculator','author','term','lab','AU','grades',
		'courseOutcomes','sections','instructors','components','textbooks']

	def create(self, validated_data):
		lab_data = validated_data.pop('lab')
		AU_data = validated_data.pop('AU')
		grades_data = validated_data.pop('grades')
		outcome_data = validated_data.pop('courseOutcomes')
		section_data = validated_data.pop('sections')
		instructor_data = validated_data.pop('instructors')
		component_data = validated_data.pop('components')
		textbook_data = validated_data.pop('textbooks')
		outline = CourseOutline.objects.create(**validated_data)
		Lab.objects.create(outline=outline,**lab_data)
		AU.objects.create(outline=outline,**AU_data)
		Grades.objects.create(outline=outline,**grades_data)
		for outcome in outcome_data:
			CourseOutcome.objects.create(outline=outline,**outcome)
		for section in section_data:
			Section.objects.create(outline=outline,**section)
		for instructor in instructor_data:
			Instructor.objects.create(outline=outline,**instructor)
		for component in component_data:
			Component.objects.create(outline=outline,**component)
		for textbook in textbook_data:
			Textbook.objects.create(outline=outline,**textbook)
		return outline