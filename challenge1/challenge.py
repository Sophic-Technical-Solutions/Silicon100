#Challenge Exercise
#This program will demonstrate multiplication and addition based on user input


#User input to calculate the product of this number times 5
input_number_for_product = int(input("Enter your number for the product calculation: "))

#Calculate the product of the input number times 5
product = (input_number_for_product * 5)

#Print the product result
print("The result of your number times 5 is " + str(product) + "\n")


#User input for the first number to be added
first_number_for_sum = int(input("Enter the first number for addition calculation: "))

#User input for the first number to be added
second_number_for_sum = int(input("Enter the second number for addition calculation: "))

#Calculate the sum of the two input values
sum = (first_number_for_sum + second_number_for_sum)

#Print the added result
print("The sum of your numbers is " + str(sum))