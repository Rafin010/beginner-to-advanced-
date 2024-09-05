#Write a function which converts the input string to uppercase.
# hello bro
from audioop import add
from shlex import join

def make_upper_case(s):
    return s.upper()

#This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9


#Build a function that returns an array of integers from n to 1 where
def reverse_seq(n):
   return list(range(n, 0, -1))
print(reverse_seq(5))
print(reverse_seq(3))
        
 
#We need a function that can transform a number (integer) into a string.
def number_to_string(num):
    return str(num)
print(number_to_string(123))
print(number_to_string(999))
print(number_to_string(-100))


'''
Write a function that takes an array of words and smashes them together into a sentence and returns the sentence.
You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful,
there shouldn't be a space at the beginning or the end of the sentence!

['hello', 'world', 'this', 'is', 'great']
'''

def smash(words):
    return " ".join(words)

words = ['hello', 'world', 'this', 'is', 'great']
sentence = smash(words)
print(sentence)


#Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

def repeat_str(repeat, string):
    return string * repeat
print(repeat_str(3, "Hello "))
print(repeat_str(5, "Python "))
print(repeat_str(0, "Python "))

'''
Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, 
rounded to the smallest value.
'''
def litres(time):
    return int(time * 0.5)  
print(litres(3))
print(litres(2.75))
print(litres(1.75))

'''
Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each.
If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

Write a function that will take the number of petals of each flower and return true if they are in love and 
false if they aren't.
'''
def lovefunc(flower1, flower2):
    return (flower1 % 2) != (flower2 % 2)

print(lovefunc(4, 5))  
print(lovefunc(2, 4))  
print(lovefunc(7, 3))  

'''
Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. 
It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

Ribonucleic acid, RNA, is the primary messenger molecule in cells. 
RNA differs slightly from DNA its chemical structure and contains no Thymine. 
In RNA Thymine is replaced by another nucleic acid Uracil ('U').

Create a function which translates a given DNA string into RNA.
'''
def dna_to_rna(dna):
    return dna.replace("T", "U")
dna_string = "GATTACA"
run_string = dna_to_rna(dna_string)
print(run_string)

'''
After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

Write a code that gives out the total amount for different days(d).
'''
def car_rental_cost(d):
    if d >= 7:
        return 40 * d - 50
    elif d >= 3:
         return 40 * d - 20
    else:
        return 40 * d

days = int(input("Enter the number of days you want to rent the car: "))
total_cost = car_rental_cost(days)
print(f"The total cost for {days} days is ${total_cost}.")

#You get an array of numbers, return the sum of all of the positives ones.
#আপনি সংখ্যার একটি অ্যারে পাবেন, সমস্ত ধনাত্মকগুলির সমষ্টি ফেরত দিন।
def sum_positives(arr):
    return sum([i for i in arr if i > 0])

print(sum_positives([1, -4, 7, 12])) 
print(sum_positives([-3, -2, 0, 5, 10])) 
print(sum_positives([-1, -2, -3])) 
print(sum_positives([0, 1, 2, 3])) 

    
#Write a function to split a string and convert it into an array of words.

#"Robin Singh" ==> ["Robin", "Singh"]
#"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]

string1 = "Robin Singh"
string2 = "I love arrays they are my favorite"

word1 = string1.split()
word2 = string2.split()

print(word1)
print(word2)

#Given an array of integers, return a new array with each value doubled.

def maps(a):
    return a * 2
num = [1, 2, 3]
test = list(map(maps, num))
print(test)


'''
Write a function which calculates the average of the numbers in a given list.
Note: Empty arrays should return 0.
'''
'''
numbers = [30, 55, 3, 10, 2]
average = sum(numbers)/len(numbers)
print("Average of list: ", round(average,3))
'''
def find_average(numbers):
    if not numbers:
        return 0
    return sum(numbers)/len(numbers)

numbers_list = [20,10,30,40,60,50,90,80,70]
avarage = find_average(numbers_list)
print(f"The avarage number is: {avarage}")

#1. Create a loop that iterates over the list [-1, 2, 3, 0, -4] and checks whether each number is positive or negative

number = [-1,2,3,0,-4]

for i in number:
    if i > 0:
        print(f"{i} is positive")
    elif i < 0:
        print(f"{i} is negative")
    else:
        print(f"{i} is neither positive nor negative")


#2. Create a loop that iterates over the list ["France", "Japan", "USA"] and searches for “USA” in the list


countries  = ["France", "Japan", "USA"]

for country in countries:
    if "USA" in country:
        print(f"Found: {country}")

#3. Create a loop that iterates over the list [1, 10, 9, 4] and checks whether each number is greater than 3

num1 = [1, 10, 9, 4]

for n in num1:
    if n > 3:
        print("is True")
    else:
        print("is False")    

#4. Create code with a nested loop that searches the list of lists [[50, 48, -40], [57, 99, 80], [49, 40, 45]] and prints out all the numbers greater than or equal to 50

list_of_lists = [[50, 48, -40], [57, 99, 80], [49, 40, 45]]

for sublist in list_of_lists:
    for j in sublist:
        if j >= 50:
            print(j)

#5. Create a loop to check whether the list [3, 5, 11, 12, 1] contains at least one number higher than 10, and print “This list contains a number higher than 10” if it does. Include a break statement. 

list_ = [3, 5, 11, 12, 1]

for num in list_:
    if num > 10:
        print(f"{num} is greater than 10")
        break
