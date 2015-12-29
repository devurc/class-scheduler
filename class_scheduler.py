#!/usr/bin/env python
#Program to create a class scheduler

class Quarter:
	
	quarter = ""
	course_list = []
	
	def __init__(self, quarter):
		self.quarter = quarter
	
	#Func to add a course to the quarter
	def add_course(self, course, units):
		self.course_list.append(Course(course, units))

	def calc_units(self):
		total = 0 
		for course in self.course_list:
			total += course.course_units
		return total

	def display(self):
		for course in self.course_list:
			print course.course_name, str(course.course_units) + " units"			
		print "Total Units: " + str(self.calc_units())

	def __lt__ (self, quarter):
		return int(self.quarter[2:]) < int(quarter[2:]) 

	def __gt___(self, quarter):
		return int(self.quarter[2:]) > int(quarter[2:])				

	
class Course:
	
	course_name = ""
	course_units = 0
	
	def __init__(self, name, units):
		self.course_name = name
		self.course_units = units

	def __eq__(self, other):
		return self.course_name == other.course_name and self.course_units == other.course_units
