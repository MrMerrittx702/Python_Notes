
#class declaration
class MyClass:

  #constructor
  def __init__(self):#takes 1 parameter self is a reference to the object
    self.student_list = [] #list of students

  #method to add student to the students list
  def addStudent (self,student):#takes 2 parameters
    self.student_list.append(student)

  #print each student in the students list
  def list_students(self):
    for student in self.student_list:
      print(student)



#class declaration
class Student():

  #attributes
  class_size = 0

  #constructor
  def __init__(self, name, grade):#takes 3 parameters
    Student.class_size += 1
    self.name = name
    self.grade = grade
    self.id = Student.class_size

  #method to return the string representation of the object
  def __str__(self):#takes 1 parameter self is a reference to the object
    return self.name


  #method to print the number of students
  def report_size(self):#takes 1 parameter 
    print("The class has %d students" %Student.class_size)#format string %d is replaced with Student.class_size



computer_science = MyClass()

john = Student("john", 9)
jane = Student("jane", 9)

computer_science.addStudent(john)
computer_science.addStudent(jane)

john.report_size()
computer_science.list_students()





    




