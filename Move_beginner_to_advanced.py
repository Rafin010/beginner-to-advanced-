#Write a function which converts the input string to uppercase.

from audioop import add
from shlex import join


def make_upper_case(s):
    return s.upper()

#This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
#এই কাতা হল একটি প্রদত্ত সংখ্যাকে জোড় সংখ্যা হলে আট দ্বারা এবং অন্যথায় নয় দ্বারা গুণ করা।
def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
    

'''
Build a function that returns an array of integers from n to 1 where
একটি ফাংশন তৈরি করুন যা n থেকে 1 পর্যন্ত পূর্ণসংখ্যার একটি অ্যারে প্রদান করে যেখানে
n>0.
Example : n=5 --> [5,4,3,2,1]
''' 
def reverse_seq(n):
   return list(range(n, 0, -1))
print(reverse_seq(5))
print(reverse_seq(3))
        
'''
We need a function that can transform a number (integer) into a string.
--------------------------------------------------------------------------------------------
আমাদের এমন একটি ফাংশন দরকার যা একটি সংখ্যাকে (পূর্ণসংখ্যা) একটি স্ট্রিংয়ে রূপান্তর করতে পারে।
এই অর্জনের উপায় কি আপনি জানেন?
'''
def number_to_string(num):
    return str(num)
print(number_to_string(123))
print(number_to_string(999))
print(number_to_string(-100))


'''
Write a function that takes an array of words and smashes them together into a sentence and returns the sentence.
You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful,
there shouldn't be a space at the beginning or the end of the sentence!

একটি ফাংশন লিখুন যা শব্দের অ্যারে নেয় এবং সেগুলিকে একটি বাক্যে একত্রিত করে এবং বাক্যটি ফেরত দেয়। 
আপনি শব্দগুলিকে জীবাণুমুক্ত করার বা বিরাম চিহ্ন যোগ করার যেকোন প্রয়োজন উপেক্ষা করতে পারেন,
তবে আপনার প্রতিটি শব্দের মধ্যে স্পেস যোগ করা উচিত। 
সতর্ক থাকুন,বাক্যের শুরুতে বা শেষে একটি স্থান থাকা উচিত নয়!

['hello', 'world', 'this', 'is', 'great']
'''

def smash(words):
    return " ".join(words)

words = ['hello', 'world', 'this', 'is', 'great']
sentence = smash(words)
print(sentence)

'''
Write a function that accepts an integer n and a string s as parameters,
and returns a string of s repeated exactly n times.

একটি ফাংশন লিখুন যা একটি পূর্ণসংখ্যা n এবং একটি স্ট্রিং sকে পরামিতি হিসাবে গ্রহণ করে এবং s-এর একটি স্ট্রিং ঠিক n বার পুনরাবৃত্তি 
করে।
'''
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

টিমি এবং সারাহ মনে করেন যে তারা প্রেমে পড়েছেন, কিন্তু তারা যেখানে থাকেন তার আশেপাশে, 
তারা প্রত্যেকে একটি করে ফুল বাছাই করলেই তারা জানতে পারবেন।
 ফুলের একটিতে যদি জোড় সংখ্যার পাপড়ি থাকে এবং অন্যটিতে বিজোড় সংখ্যক পাপড়ি থাকে তার মানে তারা প্রেমে পড়েছে।

একটি ফাংশন লিখুন যা প্রতিটি ফুলের পাপড়ির সংখ্যা নেবে এবং যদি তারা প্রেমে থাকে তবে সত্য এবং না থাকলে মিথ্যা হবে।
'''
def lovefunc(flower1, flower2):
    return (flower1 % 2) != (flower2 % 2)

print(lovefunc(4, 5))  
print(lovefunc(2, 4))  
print(lovefunc(7, 3))  


    

