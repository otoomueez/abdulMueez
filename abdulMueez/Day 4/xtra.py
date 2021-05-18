
# class Object:
#     def __init__(self, pname, dob):
#         self.pname = pname
#         self.dob = dob

# class Person(Object):
#     def __init__ (self, name, dob):
#         self.name = name
#         self.dob = dob
    
#     def display(self):
#         print(str(self.name))
#         print(str(self.dob))

#     def walk(self):
#         prin
        

# create an object
class Object:
    def __init__(self, house, road):
        self.house = house
        self.road = road

# Create a class for Person, a constructor which takes the persons name and DOB
class Person(Object):
  def __init__(self, name, date_of_birth, age,house, road):
# initialize super function to inherit from Object
      super().__init__(house, road)
      self.name = name
      self.date_of_birth = date_of_birth
      self.age = age
# functions to print and return
  def speak(self):
      print("Hello")
  def walk (self):
      print("Walking away")
  def get_name(self):
      return self.name
  def get_age(self):
      return self.age

# Class called Student that inherits from Person
class Student(Person):
 def __init__(self,name, date_of_birth,age,house, road,course_names):
# initialize super function to inherit from class Person
     super().__init__(name, date_of_birth, age,house, road)
     self.course_names = course_names
# Create a class for Student, a constructor which takes a String List of course names

 def get_courses(self):
     return self.course_names
 def speak(self):
     print("I'm so tired")


# y = Object("Zantola hotel",'R40')
y = Person("Jojo Mensah", "31-01-2000",str(25),"Zantola hotel",'R40')
y.speak()
y.walk()
print(y.get_name())
print(y.get_age())
#Student and list of course names
z = Student("Jojo Mensah", "31-01-2000",str(25),"Zantola hotel",'R40',["Calculus","Electronics", "ICT"])
print(z.get_courses())
z.speak()