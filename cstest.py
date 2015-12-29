#!/usr/bin/env python
#Test class for class scheduler

import class_scheduler

class CStester:
	quarter1 = class_scheduler.Quarter("")

	def course_test(self):
		print "---------"
		print "Testing Course class...",
		course1 = class_scheduler.Course("ECE 15", 4)
		if course1.course_name == "ECE 15" and course1.course_units == 4:
			print "PASS"
		else:
			print "FAIL"
		#print course1.course_name, str(course1.course_units)
		print

	def const_test(self):
		print "---------"
		print "Testing Quarter constructor...",
		self.quarter1 = class_scheduler.Quarter("FA12")
		if self.quarter1.quarter == "FA12":
			print "PASS"
		else:
			print "FAIL"
		#print self.quarter1.quarter
		print

	def add_course_test(self):
		print "---------"
		print "Testing Quarter add_course function...",
		self.quarter1.add_course("ECE 15", 4)
		self.quarter1.add_course("MATH 20D", 4)
		
		if self.quarter1.course_list[0] == class_scheduler.Course("ECE 15", 4) and self.quarter1.course_list[1] == class_scheduler.Course("MATH 20D", 4):
			print "PASS"
		else:
			print "FAIL"
		#for course in self.quarter1.course_list:
		#	print course.course_name, str(course.course_units) + " units"
		print

	def calc_units_test(self):
		print "---------"
		print "Testing Quarter calc_units function...",
		total = 0
		total = self.quarter1.calc_units()
		if total == 8:
			print "PASS"
		else:
			print "FAIL"
		#print "Total: " + str(total) + " units"
		print


	def display_test(self):
		print "----------"
		print "Testing Quarter display() function...",
		print "User verification"
		self.quarter1.display()
		print	

tester = CStester()	
print "Course class tests:"
tester.course_test()
print "Quarter class tests:"
tester.const_test()
tester.add_course_test()
tester.calc_units_test()
tester.display_test()
print "Finished all tests."
