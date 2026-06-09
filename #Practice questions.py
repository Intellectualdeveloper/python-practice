#- Write a program that utilizes the concept of conditional execution, takes a string as input, and:
#1. prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen  ⁠if the inputted string is "Spathiphyllum" (upper-case)
# prints "No, I want a big Spathiphyllum!"  if the inputted string is "spathiphyllum" (lower-case)
# prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.

plant = input("Enter a plant name: ")  #= for assigning values == for comparing values

if plant == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!") 

elif plant == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")

else :
    print("Spathiphyllum")

#Write a program to print a series like this:
#1, 2, 3, 4, 5….50
number = int(input("Enter the number:"))

count=1
while count<= number:
    print(count)
    count+=1
#1, t, 3, t, 5, t, 7, t, 9……50
number =int(input("Enter the number"))

count=1
while count<=number:
    print(count,", t ,",end=" ")
    count+=2

#1, 2, t, 3, 4, t, 5, 6, t…..50
Number = int(input("Enter the number"))

count=1
while count<= Number:
    print(count*2-1,",",count*2,", t ,",end=" ")
    count+=1
#1, 2, t, 4, 5, t, 7, 8, t…..50
#use if else for the multiple of 3
Number=(int(input("Enter the number")))

count=1
while count<=Number :
    if count%3==0:
        print("t",end=", ")
    else:
        print(count,end=", ")  
    count+=1  


#1, 2, fiz, 4, buz, fiz, 7, 8, fiz, buz, 11, fiz, 13, 14, fizbuz, 16……50

Number=(int(input("Enter the number")))

count=1
while count<=Number :
    if count%3==0:
        print("fiz",end=" ")
    elif count%5==0:
        print("buz",end=" ")
    else:
        print(count,end=" ")
    count+=1

#Practice Question:
#Once upon a time there was a land – a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course – their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:
#1. if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was what they called tax relief)
#2. ⁠if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
#Your task is to 
#1. write a tax calculator.
#It should accept one floating-point value: the income.
#2. Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you
#Note: this happy country never returned any money to its citizens. If the calculated tax was less than zero, it would only mean no tax at all (the tax was equal to zero). Take this into consideration during your calculations.

income =float(input("Enter the income"))
if income>0 and income <=85528:
    print(income*18/100-556.02)
elif income >85528:
    print(14839.02+(income-85528)*32/100)
elif income<=0:
    print(0)

#Practice Question:
#As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.
#Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:
#1. if the year number isn't divisible by four, it's a common year;
#2. ⁠otherwise, if the year number isn't divisible by 100, it's a leap year;
#otherwise, 
#3. if the year number isn't divisible by 400, it's a common year;
#4. ⁠otherwise, it's a leap year.
#Write code – it only reads a year number, and needs to be completed with the instructions implementing the test we've just described.
#The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.
#It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period.    

year = int(input("Enter the year"))

if year%4 != 0:
    print("Common year")
elif year%100 !=0:
    print("it's a leap year")
elif year%400 !=0:
    print("it's a common year")
else:
    print("it's a leap year")

#Do you know what Mississippi is? 
#It's the name of one of the states and rivers in the United States. The Mississippi River is about 2,340 miles long, which makes it the second longest river in the #United States (the longest being the Missouri River). It's so long that a single drop of water needs 90 days to travel its entire length!
#The word Mississippi is also used for a slightly different purpose: to count mississippily.
#If you're not familiar with the phrase, we're here to explain to you what it means: it's used to count seconds.
#The idea behind it is that adding the word Mississippi to a number when counting seconds aloud makes them sound closer to clock-time, and therefore "one Mississippi, two Mississippi, three Mississippi" will take approximately an actual three seconds of time! It's often used by children playing hide-and-seek to make sure the seeker does an honest count.
#Your task is very simple here: write a program that uses a for loop to "count mississippily" to five. Having counted to five, the program should print to the screen the final message "Ready or not, here I come!"


count=1
while count<=5:
    print(count,"Mississippi")
    count+=1

print("Ready or not ,Here I come")

for i in range(1,5):
    print(count,)