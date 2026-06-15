# print("hello pr")
# age = 16
# print(age)
# x = 5
# print(type(x))
# x = "HELLO WORLD" 
# str
# print(type(x))
# x = 20
# int
# print(type(x))
# x = 20.5 
# float
# print(type(x))
# x = 1j
# complex
# print(type(x))
# x = ["apple","banana","cherry"]
# list
# print(type(x))
# x = ("apple","banana","cherry")
# tuple
# print(type(x))
# x = range(6)
# range
# print(type(x))
# x = {"name":"john","age":36}
# dict
# print(type(x))
# x={"apple","banana","cherry"}
# set
# print(type(x))
# x = frozenset({"apple","banana","cherry"})
# frozenset
# print(type(x))
# x = True 
# bool
# print(type(x))
# x = b"Hello"
# bytes
# print(type(x))
# x = bytearray(5)
# bytearray
# print(type(x))
# x = memoryview(bytes(5))
# memoryview
# print(type(x))
# x = None
 
# print(type(x))

# print(x == 1)
# print(x == 2)

# print(x != 1)
# print(x != 2)
# x = 4
# print(x < 5 and x < 10)
# print(x > 5 and x > 10)
# print(x > 3 and x > 10)
# print(not(x > 3 or x > 10))

# x = 10
# y = 10
# print(x is y)

# y = ["BMW","MCLAREN"]
# X = "BMW"
# print(x in y)

# # 0000001
# # 1111110


# name = input("please enter your name")
# print("HELLO",name)

# x = input("Enter first value for sum: ")
# y = input("Enter second value for sum: ")
# z = x + y
# print("Sum: ",z)
# z = int(x) + int(y)
# print("sum:" ,z)



# #write a program to calculate hyptone between two sides
# #write a program to print this pattern using just print function

# a = float(input("Enter first side of the diagram "))
# b = float(input("Enter second side of the diagram"))
# c = (a ** 2 + b ** 2) ** 0.5
# print(c)

# print("+----------+")
# print("|          |")
# print("|          |")
# print("|          |")
# print("|          |")
# print("|          |")
# print("+----------+")

# #another way of printing above diagram or construction

# print("+"+"-"*10+"+")
# print(("|"+" "*10+"|\n")*5, end="")
# print("+"+"-"*10+"+")

# #
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# #choose the largest number
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2
# # print the result
# print("The larger number is:",larger_number)

# #
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number"))

# largest_number = number1

# if number2 > largest_number:
#     larger_number = number2

# if number3 > larger_number:
#     larger_number = number3

# print("The largest number is:", largest_number)

# #
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number"))

# largest_number = max(number1,number2,number3)
# lowest_number = min(number1,number2,number3)
# #print the result
# print("The largest number is :", largest_number)
# print("The lowest number is:", lowest_number)

# #while True :
# #   print("I'm stuck inside a loop.")

# #store the current largest number here.
# largest_number = -999999999
# #input the first value.
# number = int(input("Enter a number or type -1 to stop: "))
# #If the number is not equal to -1'continue.
# while number != -1:
#     #Is number larger than largest_number?
#     if number > largest_number:
#         #Yes 'update largest_number.
#         largest_number = number1
#         #input the next number.
#     number = int(input("Enter a number or type -1 to stop: "))
#     #print the largest number.
# print("The largest number is:", largest_number)


# #1 to 50 code execution

# number = int(input("Enter the number:"))

# count = 1

# while count <= number:
#     print(count)
#     count += 1

# #for horizontal countdown

# number = int(input("Enter the number"))
# count = 1
# while count<=number:
#     print(" ",count,end=" ")
#     count+= 1

# #write a program that reads a sequence of numbers and counts how many numbers are even and how many are odd.THe program terminates when zero is entered.

# number = int(input("Enter the number:"))

# count = 1
# even = 0
# odd = 0
# def new_func():
#     count += 1

# while count<=number:
#     if count % 2 == 0:
#         even +=1
#     else:
#         odd +=1

# print("Even= ", even)
# print("Odd=", odd)

# #counter varaiable must be used to exit in between loop

# #forloop

# #!st
# for counter in range(100):
#     print("counter:",counter)

# #2nd 
# for counter in range(2,8):
#     print("The value of counter is currently: ", counter)

# #3rd 
# for counter in range(2,8,3):
#     print("The value of counter is currently: ", counter)

# #another loop

# power = 1
# for expo in range(16):
#     print("2 to the power of",expo,"is",power)
#     power *= 2

# #Break example

# print("The break instruction")
# for counter in range(1,6):
#     if counter == 3:
#         break
#     print("Inside the loop.",counter)
# print("Outside the loop.")

# #continue example

# print("The break instruction")
# for counter in range(1,6):
#     if counter == 3:
#         continue
#     print("Inside the loop.",counter)
# print("Outside the loop.")

# #practice example

# counter = 1
# while counter < 5:
#     print(counter)
#     count += 1
# else:
#     print("else:,counter")

# # 

# var = 10
# print(var > 0)  
# print(not (var <= 0)) 

# print(var != 0)
# print(not (var == 0))

# #list

# numbers =[10,5,7,2,1]

# print(numbers)
# print(type(numbers))

# numbers = [10,5,7,2,1]

# #numbers[0] => numbers address + ((number of bytes occupied * index)) => 0x0000 = 10
# #numbers[1] => numbers address + ((number of bytes occupied * index)) => 0x0002 = 5
# #numbers[2] => numbers address + ((number of bytes occupied * index)) => 0x0004 = 7

# print("first element content : ", numbers[10])
# print("second element content : ", numbers[5])
# print("third element content : ", numbers[7])
# print("fourth element content : ", numbers[2])
# print("fifth element content : ", numbers[1])

# numbers[0] = 111
# print("numbers[0]: ", numbers[0])
# print(numbers)

# number[1] = numbers[4]
# print(numbers)
# print(len(numbers))
# del numbers[3]
# print(numbers)
# print(len(numbers))

# print(numbers[-1])
# print(numbers[-2])
# print(numbers[-3])
# print(numbers[-4])
# #print(numbers[-5]) will cause error
# #print(numbers[4]) out of range

# #there once was a hat . The hat contained no rabbit,but a list of five numbers:1,2,3,4, and 5.
# #1
# numbers=[1,2,3,4,5]
# print(numbers)
# print(len(numbers))
# #2
# numbers=[1,2,3,4,5]
# del numbers[4]
# print(numbers)
# print(len(numbers))

# #3
# numbers=[1,2,3,4,5]
# del numbers[2]
# numbers.insert(2,8)
# print(numbers)
# print(len(numbers))

# #how to dynamically traverse a list

# my_list = [1,2,3,4,5,6,7,8,9,10]
# for iterator in range(len(my_list)):
#     print(my_list[iterator])

# #dryrun

# iterator

# #write a program to insert 10 numbers starting from 1 to 10 in a list

# list=[]

# for iterator in range(1,11):
#     list.append(iterator)

# print(list)

# #
# my_list =[10,20,30,40,50,60,70,80,90,100]

# for index in range(len(list)):
#     list[index] +=1 #list[index] +1

# print(list)




# #write a program to calculate sum of all the elements in the list

# my_list =[10,20,30,40,50,60,70,80,90,100]
# total=0

# for element in my_list:
#     total+=element
# print(total)



# #
# my_list =[10,1,8,3,5]
# total = 0

# for element in my_list:

#     total+= element
# print(total)

# #value swapping
# variable1 =1
# variable2 =2

# print("Variable1:",variable1)
# print("variable2:",variable2)

# variable1,variable2 = variable2,variable1

# print("Variable1:",variable1)
# print("variable2:",variable2)

# #
# list = [10,20,30,30,40,50,60,70,80,90,100]

# list[4],list[]

# #sorting of a List:
# my_list = [10,6,2,4] #list to sort
# swapped = True #It,s a little fake, we need it to enter the whilw loop.
# while swapped:
#     swapped = False #no swaps so far
#     for i in range(len(my_list)-1):
#         if my_list[i] > my_list[i+1]:
#             swapped = True #a swap occured:
#             my_list[i],my_list = my_list[i+1],my_list[i]
# print(my_list)

# my_list = [0,10,6,2,4]
# my_list.sort()
# my_list.reverse()
# print(my_list)
# #
# ist = ["D","F","A","Z"]

# ist.sort()

# print(ist)

# #
# a = 3
# b = 1
# c = 2

# ist =[a,c,b]

# ist.sort()

# print(ist)

# #A slice is a element of python syntax that allows to create a brand new copy of a list  ,or parts of list

# list_1 = [1]
# list_2=list_1[:]
# list_1[0]=2
# print(list_1)
# print(list_2)

# my_list = [10,8,6,4,2]
# new_list = my_list[1:-1]
# print(new_list)

# my_list = [10,8,6,4,2]
# new_list = my_list[-5:3]
# print(new_list)

# del my_list[:]
# print(my_list)

# my_list = [0,3,12,8,2]
# print(5 in my_list)
# print(5 not in my_list)
# print(12 in my_list)

# row = ["WHITE_PAWN" for i in range(8)]
# squares = [index ==2 for index in range(1,11)]



# #
# board[0][1] = "KNIGHT"
# board[0][6] = "KNIGHT"
# board[7][1] = "KNIGHT"
# board[7][6] = "KNIGHT"

# print("_____________")

# for elment in board:
#     print(element)

# var = 1
# while var < 10:
#     print("#")
#     var = var<<1'

# #monday
 
# def message():
#     print("Enter a value:")
#     temp = int(input())
#     return temp

# print("Step 1")
# a = message()

# print("Step 2")
# a = message()

# print("Step 3")
# a = message()

# print("a:", a)
# print("b:", b)
# print("c:", c) 

# def hello(n):
#     print("hello,",n)

# name = input("Enter your name")
# hello(name)
# #
# def message(number):
#     print("Enter a number",number)

# number = 1234
# message(1)
# print(number)

# #a compilier cannot interitate when a code is in form (1 , a=1,b=2)
# #it can only copile in form (2,b=3,c=6) format

# def boring_function():
#     print("'Boredom Mode' ON'.")
#     return 123

# print("this lesson is interesting!")
# boring_function
# print("this lesson is boring...")

# #
# def checkMyVar(variable):
#     if(variable == 10):
#         print("Variable is 10"):
#     else:
#         print("variable is not up to the mark")
#         return
    
# checkMyVar(5)
# print()

# #
# def scope_test():
#     x = 123
# scope_test()
# print(x)

# #
# def mult(x):
#     var = 7
#     return x * var

# #
# def my_function():
#     global var
#     var = 2
#     print("Do I Know that variable?",var)

# var = 1
# my_function()
# print(var)

# #
# var = 2
# print(var)

# def return_var():
#     global varv
#     var = 5
#     return var

# print(return_var())
# print(var)

# #
# def my_function(n):
#     print("I got you", n)
#     n += 1
#     print("i have",n)

# var = 1
# my_function(var)
# print(var)

# #
# def my_function(my_list_1):
#     print("Print #1:",my_list_1)
#     print("Print #2:",my_list_2)
#     my_list_1 = [0,1]
#     print("Print #3:",my_list_1)
#     print("Print #4:",my_list_2)
    
# my_list_2 = [2,3]
# my_function(my_list_2)
# print("Print #5:, my_list_2")

# #
# def my_function(my_list_1):
#     print("Print #1:",my_list_1)
#     print("Print #2:",my_list_2)
#     del my_list_1[0]
#     print("Print #3:",my_list_1)
#     print("Print #4:",my_list_2)
    
# my_list_2 = [2,3]
# my_function(my_list_2)
# print("Print #5:, my_list_2")

# #
# def countDown(number):
#     print(number)
#     if number == 0:
#         return
#     else:
#         countDown(number -1)
# print("Starting Recursion")
# countDown(5)
# print("Completed Recursion")

# #
# def factorial(number):
#     if number == 0:
#         return 1
#     else:
#         return number*factorial(number-1)
# print(factorial(5))

# #
# tuple_1 = (1,2,3)
# for elem in tuple_1:
#     print(elem)

# tuple_2 = (1,2,3,4)
# print(5 in tuple_2)
# print(5 not in tuple_2)

# tuple_3 = (1,2,3,4)
# print(len(tuple_3))
# print(5 not in tuple_3)

# tuple_4 = tuple_1 + tuple_2
# tuple_5 = tuple_3 + 2
# print(tuple_4)
# print(tuple_5)

# #
# my_tuple = tuple((1,2,"string"))
# print(my_tuple)
# print(type(my_tuple))

# my_list = [2,4,6]
# print(my_list)
# print(type(my_list))
# tup = tuple(my_list)
# print(tup)
# print(type(tup))

# #
# t1 = (1,)
# t2 = (2,)
# t3 = (3,var)

# t1,t2,t3 = t2,t3,t1

# print(t1,t2,t3)
# print(type(t1),type(t2),type(t3))

# #use of dictionary

# dictionary = {
# "cat":"chat",
# "dog":"chien",
# "horse":"cheval"
# }
# phone_numbers = {'boss':5551234567, 'Suzy': 22657854318}
# empty_dictionary = {}

# print(dictionary)
# print(type(dictionary))
# print(phone_numbers)
# print(type(phone_numbers))
# print(empty_dictionary)
# print(type(empty_dictionary))

# print(dictionary['cat'])
# print(phone_numbers['Suzy'])

# words = ['cat','lion','horse']

# for word in words:
#     if word in dictionary:
#         print(word,"->",dictionary[word])
#     else:
#         print(word,"is not in dictionary")

# print(dictionary.keys())

# for key in dictionary.keys():
#     print(key,"->",dictionary[key])

# for key,value in dictionary.items():
#     print(key,"->",value)

# print(dictionary.values())

# for value in dictionary.values():
#     print(value)

# pol_eng_dictionary = {
#     "zamek":"castle",
#     "woda":"water",
#     "gleba":"soil"
#      }
# print("pol_eng_dictionary: ",pol_eng_dictionary)
# copy_dictionary = pol_eng_dictionary.copy()

# print("copy_dictionary: ",copy_dictionary)

# pol_eng_dictionary["zamek"] = "lock"
# item = pol_eng_dictionary["zamek"]
# print(item)

# phonebook = {}

# print(phonebook)
# phonebook["Adam"] = 3456783958
# print(phonebook)

# del phonebook["Adam"]
# print(phonebook)

# pol_eng_dictionary = {"kwait":"flower"}

# pol_eng_dictionary.update(
#     {
#         "gleba":"soil"
#     })
# print(pol_eng_dictionary)

# pol_eng_dictionary.popitem()
# print(pol_eng_dictionary)

# #class creation

# class ThisIsMyFirstClass:
#     name = "Aditya"
#     age = 20

#     def getname():
#         pass

# firstObject = ThisIsMyFirstClass()
# print(firstObject)

# class Student:
#     def __init__(self):
#         self.name = ""
#         self.age = 0
#         self.gender = ""
#         self.grade = ""

# mayur = Student()
# print(mayur)
# mayur.name = "Mayur Valvi"
# mayur.age = "20"
# mayur.gender = "Male"
# mayur.grade = "10th"

# print(mayur.name)
# print(mayur.age)
# print(mayur.gender)
# print(mayur.grade)

# #

# class ExampleClass:
#     def __init__(self,val = 1):
#         self.first = val

#     def set_second(self,val):
#         self.second = val

# example_object_1 = ExampleClass(1)
# example_object_2 = ExampleClass(2)
# example_object_2.set_second(3)
# example_object_3 = ExampleClass(4)
# example_object_3.third = 5 

# print(example_object_1)

# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)

# #
# class ExampleClass:
#     def __init__(self,val = 1):
#         self.first = val

#     def set_second(self,val):
#         self.second = val

# example_object_1 = ExampleClass(1)
# example_object_2 = ExampleClass(2)
# example_object_2.set_second(3)
# example_object_3 = ExampleClass(4)
# example_object_3.third = 5 

# print(example_object_1)

# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)
# example_object_3.example_method()

# #
# class Class:
#     def method(self,par):
#         print("method",par)

# obj = Class()
# obj.method(1)

# #
# class Classy:
#     varia = 2
#     def method(self):
#         print(self.varia,self.var)

# obj = Classy()
# obj.var = 3
# obj.method()

# # 
# class Star:
#     def __init__(self,name,galaxy):
#         self.name = name
#         self.galaxy = galaxy

# sun = Star('Sun','Milky Way')
# print(sun)

# #
# class Star:
#     def __init__(self,name,galaxy):
#         self.name = name
#         self.galaxy = galaxy

#     def __str__(self):
#         return self.name + ' in ' + self.galaxy
    
# sun = Star('Sun','Milky Way')
# print(sun)

# #
# class Vehicle:
#     pass

# class LandVehicle(Vehicle):
#     pass

# class TrackedVehicle(LandVehicle):
#     pass

# for cls1 in [Vehicle,LandVehicle,TrackedVehicle]:
#     for cls2 in [Vehicle, LandVehicle,TrackedVehicle]:
#         print(issubclass(cls1, cls2), end = "\t ")
#     print()

# #
# class Super:
#     supVar = 1

# class Sub(Super):
#     subVar = 2

# obj = Sub()
# print(obj.subVar)
# print(obj.supVar)

# #subclass didnt call it parent class which causes error
# class Super:
#     def __init__(self):
#         self.supVar = 11

# class Sub(Super):
#     def __int__(self):
#         super().__int__()
#         self.subVar = 12

# obj = Sub()
# print(obj.subVar)
# print(obj.supVar)

# #
# class level1:
#     variable_1 = 100
#     def __init__(self):
#         self.var_1 = 101
#     def fun_1(self):
#         return 102
    
# class level2(level1):
#     variable_2 = 200
#     def __init__(self):
#         super().__init__()
#         self.var_2 = 201
#     def fun_2(self):
#         return 202
    
# class level3(level2):
#     variable_3 = 300 
#     def __init__(self):
#         super().__init__()
#         self.var_3 = 301
#     def fun_3(self):
#         return 302
    
# obj = level3()
# print(obj.variable_1, obj.var_1, obj.fun_1())
# print(obj.variable_2, obj.var_2, obj.fun_2())
# print(obj.variable_3, obj.var_3, obj.fun_3())

# #
# class Super:
#     def __init__(self,name):
#         self.name = name 

#     def __str__(self):
#         return "My name is " + self.name + "."
    
# class Sub(Super):
#     def __init__(self, name):
#         pass
#         Super.__init__(self,name)

# obj = Sub("Andy")
# print(obj)    

# #
# class SuperA:
#     var_a = 10
#     def fun_a(self):
#         return 11
    
# class SuperB:
#     var_b = 20
#     def fun_b(self):
#         return 21
    
# class Sub(SuperA,SuperB):
#     pass

# obj = Sub()
# print(obj.var_a,obj.fun_a())
# print(obj.var_b,obj.fun_b())

# #
# class Level1:
#     var = 100
#     def fun(self):
#         return 101
    
# class Level2:
#     var = 200
#     def fun(self):
#         return 201
    
# class Level1(Level2):
#     pass

# obj = Level1()
# print(obj.var, obj.fun())

# #
# class left:
#     var = "L"
#     var_left = "LL"
#     def fun(self):
#         return"Left"
# class right:
#     var = "R"
#     var_right = "RR"
#     def fun(self):
#         return "Right"
    
# class Sub(left,right):
#     pass
# obj = Sub()
# print(obj.var,obj.var_left,obj.var_right,obj.fun())

# #
# class One:
#     def do_it(self):
#         print("do_it from One")

#     def doanything(self):
#         self.do_it()

# class Two(One):
#     def do_it(self):
#         print("do_it from Two")

# one = One()
# two = Two()
# one.doanything()
# two.doanything()

# #
# class One:
#     def do_it(self):
#         print("do_it from One")

#     def doanything(self):
#         self.do_it()

# class Two(One):
#     def do_it(self):
#         print("do_it from Two")

# class Three(Two):
#     def do_it(self):
#         super().do_it()

# one = One()
# two = Two()
# three = Three()
# one.doanything()
# two.doanything()
# three.doanything()

# #
# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print("Division failed")
#         return None
#     else:
#         print("Everything went fine")
#         return n
    
# print("---------------")
# print('reciprocal(2):',reciprocal(2))
# print("----------------")
# print('reciprocal(2):',reciprocal(0))
# print("----------------")

# #
# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print("Division failed")
#         return None
#     else:
#         print("Everything went fine")
#     finally:
#         print("It is time to say goodbye")
#         return n
    
# print("---------------")
# print('reciprocal(2):',reciprocal(2))
# print("----------------")
# print('reciprocal(2):',reciprocal(0))
# print("----------------")

# #
# try:
#     1 = int("Hello")
# except Exception as e:
#     print(e)
#     print(e.__str__)

# #
# class MyZeroDivisonError(ZeroDivisionError):
#     pass

# def do_the_divison(mine):
#     if mine:
#         raise MyZeroDivisonError("some worse news")
#     else:
#         raise ZeroDivisionError("some bad news")
    
# do_the_divison(False)


# #
# city = "Bhopal"
# print(city[0])
# print(city[2])

# print(city[-1])
# print(city[5])

# print(city[-3])
# print(city[3])

# #
# text =' Hello Python World! '
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())

# print(text.strip())

# print('Python' in text)
# print(text.find('Python'))
# print(text.count("l"))

# #
# csv = 'Rahul,22,Bhopal,Engineer'
# parts = csv.split(",")
# print(parts)
# print(parts[0])
# rejoined = ' | '.join(parts)
# print(rejoined)

# print('hello128'.isalnum())
# print('12345'.isdigit())
# print('Python'.isalphal())
# print(' '.isspace())

# email = 'student@gmail.com'
# print(email.endswith('.com'))
# print(email.startwith('stu'))
# #

# name, marks, rank = 'Anita',90.567,3

# print(f'Hello,{name}!')

# print(f'Marks:{marks:.2f}')
# print(f'Marks:{marks:0f}')
# print(f'Count:{1000000:,}')

# print(f'{name:<15}|{marks:>8.2f}|Rank:{rank}')

# price,gst = 500,0.18
# print(f'Price:Rs.{price} | GST:Rs.{price*gst:.2f} | Total:Rs.{price*(1+gst):.2f}')

# #
# name, marks, rank = 'Anita',90.567,3

# print(f'Hello,{name}!')

# print(f'Marks:{marks:.2f}')
# print(f'Marks:{marks:0f}')
# print(f'Count:{1000000:,}')

# print(f'{name:<15}|{marks:>8.2f}|Rank:{rank}')
# print(f'hello {name:^10}')
# print(f'hello {name:>10}')
# print(f'hello {name:<10}')
# print(f'hello {name:^11}')

# price,gst = 500,0.18
# print(f'Price:Rs.{price} | GST:Rs.{price*gst:.2f} | Total:Rs.{price*(1+gst):.2f}')

# #
# #string = "Hello,How are you doing today"
# #Count vowels in the string
# #Print you from the string 
# #Print the string in reverse order
# #non_palin,palin = "abcdef","axttxa"
# #check if the string is palindrome or not


# string = "Hello,How are you doing today"
# count = 0

# while count<= float('inf') :
#     if string in range('A','E','I','O','U','a','e','i','o','u'):
#       print(count)
#       count+= 1
    
# #
# with open('data.txt',"r") as file:
#     data = file.read()

# print(data)

# #
# with open('students.txt', 'w') as f:
#     f.write('Rahul Sharma,85,Bhopal\n')
#     f.write('Priya Verma,92,Indore\n')
#     f.write('Amit Kumar,73,Jabalpur\n')

# with open('students.txt', 'a') as f:
#     f.write('Sneha Joshi,88,Bhopal\n')

# with open('students.txt', 'r') as f:
#     content = f.read()
# print(content)

# with open('students.txt', 'r') as f:
#     for line in f:
#         name, marks, city = line.strip().split(',')
#         print(f'{name:<15} | {marks:>5} | {city}')
#         print("------------")

# #
# import csv

# records = [
#     ['Name','Marks','City','Grade'],
#     ['Rahul',85,'Bhopal','B'],
#     ['Priya',92,'Indore','A'],
#     ['Amit',73,'Jabalpur','B'],   
# ]
# with open('students.csv','w',newline='') as f:
#     csv.writer(f).writerows(records)

# with open('students.csv','r') as f:
#     for row in csv.DictReader(f):
#         print(f'{row["Name"]}: {row["Marks"]} marks ({row["City"]})')

# #
# import csv

# records = [
#     ['Name','Age','Marks1','Marks2','Marks3'],
#     ['Jeet',20,10,20,30],
#     ['Nikhil',30,40,40,50],
#     ['Samay',25,50,50,60,70],
# ]
# with open('students.csv','w',newline='') as f:
#     csv.writer(f).writerows(records)

# with open('students.csv','r') as f:
#     for row in csv.DictReader(f):
#         print(f'{row["Name"]}: {row["Age"]} age {row["Marks1"]} marks1 {row["Marks2"]} marks2 {row["Marks3"]} marks3')

# #
# import csv

# records = [
#     ['Name','Marks','City','Grade'],
#     ['Rahul',85,'Bhopal','B'],
#     ['Priya',92,'Indore','A'],
#     ['Amit',73,'Jabalpur','B'],   
# ]
# with open('students.csv','w',newline='') as f:
#     csv.writer(f).writerows(records)

# name = input("Enter Student Name for Search:")

# found = False

# with open('students.csv','r') as f:
#     for row in csv.DictReader(f):
#         if row["Name"] == name:
#             print(f'Found {name}')
#             print(f'{row["Name"]}: {row["Marks"]} marks ({row["City"]})')
#             found = True
#             break

# if not found :
#     print("Student Not found!!")

# #numpy library to write array

import numpy as np

arr1d = np.array([1,2,3,4,5])
arr2d = np.array([[85,90,78],[72,88,95],[91,76,83]]) #3 students x 3 subjects

print(arr2d.shape) #(3,3)
print(arr2d.dtype) # int64
print(arr2d.ndim)  #2(2-dimensional)                

# #
# zeroes = np.zeroes((3,4))
# print(zeroes)
# ones = np.ones((2,5))
# print(ones)
# rng = np.arange(0,50,5)
# print(rng)

# lin = np.linspace(0,1,11)
# print(lin)

# random = np.random.randint(40,100,(5,3))
# print(random)

# #
# arr = np.array([10,20,30,40,50])

# print(arr * 2)

# print(arr + 5)

# print(arr **2)

# #

# marks_2d = np.array([[85,90,78],[72,88,95],[91,76,83]])

# print(np.mean(marks_2d))

# print(np.mean(marks_2d,axis=1))

# print(np.mean(marks_2d,axis=0))

# print(np.mean(marks_2d))

# print(np.std(marks_2d))

# #

# arr = np.array([55,83,43,91,67,78,35,88])

# print(arr[arr > 70])

# #panda

import pandas as pd

data = {
    'Name': ['Rahul','Priya','Amit','Sneha','Vikram'],
    'Age': [22,21,23,20,24],
    'Marks': [85,92,78,88,73],
    'City': ['Bhopal','Indore','Bhopal','Jabalpur','Indore'],
}
df = pd.DataFrame(data)
print(df)

print(df.shape)

print(df.head(3))

print(df.dtypes)

print(df.describe())

#Select columns
print("df['Name]: \n", df['Name'])
print(df[['Name','Marks']])

# #filter rows
print(df[df['Marks'] >= 85])
print(df[df['City'] == 'Bhopal'])
print( df[ (df['Marks'] >=80) & (df['City'] =='Indore')])

def get_grade(x):
    if x >= 90:
        return 'A'
    elif x>= 75:
        return 'B'
    else:
        return 'C'
    
df['Grade'] = df['Marks'].apply(get_grade)
print(df['Grade'])
print("---------------")
print(df)

#groupBy - like excel pivot

city_avg = df.groupby('City') ['Marks'].mean()
print(city_avg)

#example
#print(df.groupby('City)['Marks'].mean())

df.groupby('City') ['Marks'].mean()

#Read real CSV file
df2 = pd.read_csv('students.csv')
#cleaning
df2['Name'] = df2['Name'].str.strip()

df2['Marks'] = df2['Marks'].str.replace('#', '')

df2['Grade'] = df2['Grade'].str.replace('*', '')

df2['City'] = df2['City'].str.replace('#', '')

print(df)

df2.to_csv('clean_output.csv', index=False)  #save



#
