#!/usr/bin/env python
#Argument parser to parse First name, last name, age

import argparse

parser = argparse.ArgumentParser(description = 'This is an argument parser.')

parser.add_argument('-f', dest = 'first_name', help = 'Enter in your first name')
parser.add_argument('-l', dest = 'last_name', help = 'Enter in your last name')
parser.add_argument('-a', dest = 'age', type = int, help = 'Enter in your age')

args= parser.parse_args()

if args.first_name is None:
	args.first_name = raw_input("Enter first name: ")

if args.last_name is None:
	args.last_name = raw_input("Enter last name: ")

if args.age is None:
	args.age = int(raw_input("Enter age: "))

sayHello = "Hello " + args.first_name + " " + args.last_name + ","

sayAge = "you are " + str(args.age) + " years old."

print sayHello, sayAge

