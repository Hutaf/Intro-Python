# Composite types
# 1. Tuples: A type of data that is immutable (can't be modified after its creation)
#  and can hold a group of values. Tuples can contain mixed data types.

# dog = ('Bruce', 'cocker spaniel', 19, False)
# print(dog[0])		# output: Bruce
# dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)


# 2. List:  A type of data that is mutable and can hold a group of values. 
# Usually meant to store a collection of related data.

# empty_list = []
# ninjas = ['Rozen', 'KB', 'Oliver']
# print(ninjas[2]) 	# output: Oliver
# ninjas[0] = 'Francis'
# ninjas.append('Michael')
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
# ninjas.pop()
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
# ninjas.pop(1)
# print(ninjas)	# output: ['Francis', 'Oliver']

# 3. Dicts.:A group of key-value pairs.
#  Dictionary elements are indexed by unique keys which are used to access values.
#  When you're ready, you can find more built-in dictionary methods

# empty_dict = {}
# new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
# new_person['name'] = 'Jack'	# updates if the key exists
# new_person['hobbies'] = ['climbing', 'coding']	# adds a key-value pair if the key doesn't exist
# print(new_person)	
# # output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
# w = new_person.pop('weight')	# removes the specified key and returns the value
# print(w)		# output: 160.2
# print(new_person)	
# # output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        

#### Type Casting ####

# print("Hello" + 42)			# output: TypeError
# print("Hello" + str(42))		# output: Hello 42

# total = 35
# user_val = "26"
# #total = total + user_val		# output: TypeError
# total = total + int(user_val)		# total will be 61
# print (total)