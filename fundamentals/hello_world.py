# 1. TASK: print "Hello World"
print( "Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Hutaf"
print("Hello", name + "!")	# with a comma (I used a + to concatenate strings without inserting whitespace)
print( "Hello "+ name+ "!")	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 4
print("Hello", name, "!")	# with a comma
#print( "Hello "+ name+ "!")	# with a +	-- this one should give us an error!
# 4. print "I love to eat {fave_food1} and {fave_food2}." with the foods in variables
fave_food1 = "French toast"
fave_food2 = "Greek yogurt"
print( "I love to eat {} and {}.".format(fave_food1, fave_food2) ) # with .format()
print( f"I love to eat {fave_food1} and {fave_food2}." ) # with an f string

print("I love to eat %s and %s." % (fave_food1, fave_food2))		#  with %

# 5. String built-in function [OPTIONAL]
MyName= "Hutaf R. Aljohani"
print (MyName.islower()) # return T/F based upon wether the string in lowercase or not.
print ((MyName.lower())) # return a copy of a string in lowercase.
print (MyName.isupper()) # return T/F based upon wether a string in uppercase or not.
print ((MyName.upper())) # return a copy of string in uppercase.
print (MyName.replace("R","O")) # return a copy of string after replacing the old substring with the new substring.
print (MyName.endswith("no")) # returns T/F based upon whether the string ends with the substring or not.
print (MyName.split(".")) # return a copy of string after splitting it based upon the sep 
print (MyName.find("a")) # returns the index of the start of the first occurrence of substring within string.
print (MyName.count("a")) # returns number of occurrences of substring  within string.
print (MyName.capitalize()) # returns a copy of string after converting the first character to uppercase.
