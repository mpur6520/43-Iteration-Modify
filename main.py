#maru puran
#november 3 2023
#analyze and modify a program to get a better understanding of while loops as well as review on things such as input concatenation and functions


#declares and initializes a variable called number with integer value of 6, outside loop
number = int(input("Please enter a number to be multiplied: ")) #CHANGED: 6 changed to take in user input (which is then converted to an integer)

#declares and initializes a variable called counter with integer value of 1, outside loop
counter = 1 

#begins the loop to run with condition as long as the counter variable (currently assigned 1 when the program is newly ran) is less than 13, outside loop
while counter < 13: 
  #prints the product of the counter variable (changes every time the loop is run) and the number variable, inside loop
  print(counter, "multiplied by", number, "equals", counter*number) #CHANGED: message inside of the print statement, now displays what's being multiplied and what the numbers mean - use commas to put variable numbers and strings together without a syntax error
  #adds 1 to the counter variable (sum of counter variable current value + 1), inside loop 
  counter = counter + 2  #CHANGED: instead of counter + 1, change to counter + 2


#outside of the loop, prints only when the loop has finished running and the program can continue
print("\nThe loop has finished.") #CHANGED: added this statement to alert the user the loop has finished running




