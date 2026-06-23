# Student Management System

## Overview

This project is a simple student management system developed in Python using Object-Oriented Programming principles. The application allows management of students, teachers, courses, and grades through a menu-driven interface.

The project was developed to demonstrate the use of classes, inheritance, dictionaries, lists, functions, and file handling.

---

## Features

### Student Management

* Add new students
* Store student information including name, age, and student ID
* Enroll students in courses
* Assign grades to students
* Calculate student GPA

### Teacher Management

* Add new teachers
* Assign courses to teachers
* View teacher information and assigned courses

### Course Management

* Create courses
* Enroll students in courses
* Calculate course average grades
* Display course information

### Data Storage

The application stores information using Python dictionaries and lists:

* Students are stored using their Student ID as the key
* Teachers are stored using their Teacher ID as the key
* Student grades are stored in dictionaries
* Course information is maintained within the system

### File Export

The system can export current data to a text file for record-keeping purposes.

---

## Object-Oriented Design

The application uses inheritance to reduce code duplication and improve organization.

### Person

Base class containing:

* Name
* Age
* ID Number

### Student

Inherits from Person and adds:

* Grade management
* GPA calculation

### Teacher

Inherits from Person and adds:

* Course assignment functionality

### Course

Manages:

* Students
* Teachers
* Course statistics

---

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* Dictionaries
* Lists
* File Handling

---

## Skills Demonstrated

* Object-Oriented Programming
* Inheritance
* Data Structures
* File Operations
* Program Organization
* Python Fundamentals

---

## Author

Argyris Leakos
