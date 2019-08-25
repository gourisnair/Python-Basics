a = 'Hello, World!'

#string is also an array
print(a[0])

#use ''' or """ to indicate multiline strings

b = '''India is my country. All Indians are my Brothers and Sisters
I love my country and I am proud of its rich and varied heritage.
I shall always strive to be worthy of it.
I shall give my parents, teachers and all elders respect and treat everyone with courtesy.
To my country and my people, I pledge my devotion.
In their well being and prosperity alone, lies my happiness. Jai Hind!'''

print(b)

#Slicing of strings
print(a[7:12]) #prints from 8 to 12 inclusive

#Negative indexing: to start slicing from the end
print(a[-12:-7])

#String length
print(len(a))

#String methods

#strip(): removes white spaces from beginning or end
print(a.strip())
#lower(): returns string in lower case
print(a.lower())
#upper(): returns string in upper case
print(a.upper())
#replace(): replaces a string with another strings
print(a.replace("Hello", "Fellow"))
#split(): splits the string into substrings where it finds the instances of the seperator
print(a.split(","))


#to check if a substring present or not
txt = "An apple a day keeps the doctor away"
x = 'apple' in txt
print(x)

y = 'apple' not in txt
print(y)

print('apple' in txt)

#String concatenation
a = 'Happy'
b = ' coding!'
print(a+b)

#String format
#format(): formats the argument and places them where the placeholders{} are
age = 20
msg = 'My name is Google and I am {} years old'
print(msg.format(age))

#format() takes unlimited number of arguments
a = 1
b = 2
c = 3
txt = 'I am {}, she is {} and he is {}'
print(txt.format(a, b, c))

#use index numbers for proper placing of the arguments
txt = 'I am {2}, she is {0} and he is {1}'
print(txt.format(a, b, c))
