
# - - -BASIC FUNCTIONS (NEED TO KNOW)- - -
    # how to make text appear
print('hello world') # 'print' means to write text, for example print('hello world') writes 'hello world' in terminal

    # - - -true and false- - -
True   # => True
False  # => False

not True   # => False
not False  # => True
#---------------------------
    #- - -if, elif, and else- - -

number = 5
#---------
if number > 5:
    print('number is larger than 5')
    #elif is the opposite of if
elif number < 5:
    print('number is less than 5')
    # detailed (for dummies):else would be any other option, which in this case is the variable would be 5. In other cases, we could use if and else without elif if we just wanted greater or less than.
    # simple: else runs when no other conditions are true—in this case, it sets the variable to 5. You can also use just if and else (without elif) when you only need simple greater-than or less-than checks.
else:
    print('number is 5')

    #---lines-------------------
    #statements typically end with a new line, however you can continue a line with, \, to denote that the line should continue

    #---example---
#   total = one + \
#           two + \
#           three
#--------------------------
#- - -PYTHON SYNTAX- - -
    #---python keywords---
    #and	as	assert
    #break	class	continue
    #def	del	elif
    #else	except	False
    #finally	for	from
    #global	if	import
    #in	is	lambda
    #None	nonlocal	not
    #or	pass	raise
    #return	True	try
    #while	with	yield
    #---------------------
#---comments---
#comments can be made with the # key and does not interfere with the code, python essentially ignores them
'''
multiline comments can be made with three quotation
marks and are also ignored by python
'''
#----------------------------

#blank lines, also known as whitespace, most of the time with a comment, is ignored by python also

#----------------------

#---input---

#you can ask for user input by using the 
input()
#function
'''
example
lets say that i wanted to ask a player for their name at the begining of my project
you would use
'''
name = input("placeholder")

'''
by putting the input in a variable, you can use this variable anywhere in your project.
'''
#written by @CappySucksAtCoding on github.

#---waiting for the user---
'''
the following line of the code displays a prompt,
saying press enter to exit, and waits for the user to
follow.
'''
input("\n\nPress the enter key to exit.")
'''
\n\n is used to create two new lines before displaying the actual line,
once the user presses the key, the program ends.
'''
#---------------------------

#---the semicolon---

'''
#the semicolon allows multiple statements on  a single line given that neither statement starts a new code block
'''

#-----------------
'''
groups of individual statements, which make a single code block are called suites.
compound or complex statements, such as if, while, def, and class are required
to have a header line and a suite.

header lines begin with a keyword and terminate with a colon and
are followed by one or more lines which make up the suite.
for example-
'''
'''
if expression :
    suite
elif expression :
    suite
else :
    suite
'''

# - - -VARIABLES SECTION- - -

one = '1' #string- for TEXT
one = 1   #number- for MATH

#number
print(one) #comes out as "1"

#string
money = '$5'
print(money) #comes out as "$5"
#also, python accepts triple quotation marks, ''' or """, to make the string span accross multiple lines

#- - -DATA TYPES- - -
    #---int---

'''
    "int" stands for integer.
    An integer is a positive or negative number with no decimal point.
    python does not allow the comma to be used as a delimiter, instead use an underscore.
'''
#example
x=int(123_456)
print(x) #will print 123456

    #---float---
'''
a float is a number that does include a decimal, and can be postive or negative.
unlike int, float has a maximum size, inf, which stands for infinity.
if you did-
x=10e400, python would type inf.
e stands for 10 to the power of.
'''
    #---sequence---
'''
a sequence is simple, it is an ordered sequence of characters, strings, lists, and tuples.
you could set x with-
x=str("hello world")
- if i were to type print(x) it would print "hello world"
'''
    #---bool---
'''
bool is basically just true or false.
if i were to type print(10>5) it would print True,
because 10 is greater than five. you can do this vice versa.
'''
    #---dictionary---
'''
dictionary, or dict, can be used to store large amounts of data.
dict is also the most flexible data type in python.
dictionaries are set up like-
{key : value, key : key : key : value, key : value}
for example, we could use this
'''
dict = {
"name": "John",
"client": "Code",
"subject": "Python"
}

'''
you can print out the dict with, print(dict)
the output would be-
{'name': 'John', 'client': 'Code', 'subject': 'Python'}
if you wanted to only print the client, you could use print(dict["client"])-
the output would be "Code"
'''
    #---strings---
'''
strings can be represented with str.
a string would be-
text = "hello"
'''
    #---list---
'''
a list is a list of values
for example-
numbers = [1,2,3]
'''
#--------------------------------------------------------------------
#ADDING MORE
