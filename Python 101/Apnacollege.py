'''
Write a program to input 2 numbers and print sum
a = int(input("Enter number one "))
b = int(input("Enter number two "))
print("Sum of two number is: ",a + b)
'''
'''
Write a program to input side of a square and print its area
a = float(input("Enter side of a square "))
print("Sum of square is : ", a*a)
'''
'''Write a program to input 2 floating point numbers and print average
a = float(input("Enter number one: "))
b = float(input("Enter number two: "))
print("Average of a and b is: ",(a+b)/2)'''

'''Write a program to check if a number entered by the user is odd or even
a = int(input("Enter an number"))
if(a%2==0):
    print("Number is even")
else:
    print("Number is odd")'''

'''Write a program to find the greatest of 3 numbers entered by the user

a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
c = int(input("Enter the number 3: "))

if(a>b and a>c):
 print(a)
elif(b>a and b>c):
 print(b)
else:
 print(c)'''

'''WAP to check if a number is a multiple of 7 or not
a = int(input("Enter number one: "))
if(a%7==0):
    print("Yes multiple of 7")
else:
    print("No not a multiple of 7")'''

'''WAP to ask the user to enter names of their 3 favourite movies & store them in list
movie = []
movie.append(input("Enter movie 1: "))
movie.append(input("Enter movie 2: "))
movie.append(input("Enter movie 3: "))
print(movie)'''

'''WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)
listInput = ['a','b','b','a']

copyOfListInput = listInput.copy()
copyOfListInput.reverse()

if(listInput == copyOfListInput):
    print("List is a palindrome")
else:
    print("List is not a palindrome")'''

'''WAP to count the number of students with the "A" grade in the following tuple
tupple = ("C","D","A","A","B","B","A")
print(tupple.count("A"))
Store the above values in a list & store them from "A" to "D"
list = ["C","D","A","A","B","B","A"]
list.sort()
print(list)'''


'''Store following word meanings in a python dictionary
table: "a piece of furniture", "list of facts & figures"
cat: "a small animal"

dictionary = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat": "a small animal"
    }

print(dictionary)'''

'''You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classroms are needed by all studetds
"python", "Java","C++","python","JavaScript"
"Java","python", "Java","C++","C"

subjects = {"python", "Java","C++","python","JavaScript",
       "Java","python", "Java","C++","C"
       }
print(len(subjects))
'''

'''WAP to input marks from user for 3 subject

marks = {}

mark = int(input("Enter marks for Physics: "))
marks.update({"Physics":mark})

mark = int(input("Enter marks for Chemistry: "))
marks.update({"Chemistry":mark})

mark = int(input("Enter marks for Maths: "))
marks.update({"Maths":mark})

print(marks)'''