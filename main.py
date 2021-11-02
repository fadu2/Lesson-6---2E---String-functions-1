# import math
# # Warm-up solution
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))

# x = (-b + math.sqrt(math.pow(b,2) - 4 * a * c))/ (2 * a)
# print("Value of x =", x)

#****Today's Lesson*****
# String functions 1
# lower() - converts a string to lowercase 
school = "REGIS"
print(school.lower())  # regis 
print("JOHN".lower())  # john
print("FOOD".lower())  # food 

# upper() - converts a string to uppercase 
name = "john"
print(name.upper())  # JOHN 
print("python".upper())  # PYTHON 

# title() - converts the first letter of every word to uppercase and all others to lowercase 
s = "i love python"
print(s.title()) # I Love Python  

s = "I lOVE pYTHON"
print(s.title())

name = "jOhN"
print(name.title())  # John 

# capitalize() - converts the first letter of a string to uppercase and all others to lowercase 
name = "joey"
print(name.capitalize())  # Joey 

s = "i love python"
print(s.capitalize()) # I love python 
s = "i LOVE PYTHon"
print(s.capitalize()) # I love python 

# lstrip() - removes whitespace from the left side of a string 
name = "  John"
print(name)  #...John
print(name.lstrip())  #John

# lstrip(char)  - removes characters from the left side of a string 
name = "Zach"
print(name.lstrip("Z"))  # ach 
print("Matthew".lstrip("aM"))  # tthew 
print("Matthew".lstrip("a"))  # Matthew

# rstrip() - removes whitespace from the right 
word = "hello  "
word2 = "world"
print(word.rstrip())  #hello
print(word + word2)  # hello  world 
print(word.rstrip() + word2) # helloworld 

# rstrip(char) - removes characters from the right 
school = "Regis"
print(school.rstrip("s"))  # Regi 
print(school.rstrip("is"))  # Reg
print(school.rstrip("si"))  # Reg  

print("noon".rstrip("no"))

# strip() - removes whitespace from both sides 
print("  hello   ".strip()) #hello

#strip(char) - removes characters from both sides 
word = "racecar"
print(word.strip("ra"))  # cec 
print("Jake".strip("Je"))   # ak 

data = "?@hello?#?"
print(data.strip("?@#")) # hello 














