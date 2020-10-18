##### Assignment: Basic For Loops #1 #####

# Task 1: Basic - Print all integers from 0 to 150. Hint:use a for loop and range

for x in range(151):
    print(x)


# Task 2: Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for x in range(5, 1001,5):
    print(x)

# Task 3: Counting, the Dojo Way - Print integers 1 to 100.
#  If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo"

for x in range(1, 101):
    if(x % 5 == 0 and x % 10 !=0):
        print("Coding")    
    elif(x % 10 == 0):
        print("Coding Dojo")
    else:
        print(x)
        continue

# Task 4: Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum
sum = 0
for x in range(0, 500001):
    if(x % 2 !=0):
        sum=sum+x
    else:
        continue
print(sum)

# Task 5: Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
 
for x in range(2018, -1,-4):
     print(x)

# Task 6: Flexible Counter (optional) - Set three variables: lowNum, highNum, mult. Starting at lowNum and 
# going through highNum, print only the integers that are a multiple of mult. 
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3
for x in range(1,highNum+1):
    if(x%mult==0):
        print(x)
    else:
        continue
