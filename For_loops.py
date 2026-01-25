'''🧩 Python For Loop Practice Questions
🔹 1. Print Numbers 0 to n-1
👉 Input a number n, and print all numbers from 0 to n-1.
Example:
Input → 5
Output → 0 1 2 3 4'''

# n = int(input("Enter a number:"))
# for i in range(0,n):
#  print(i)


'''🔹 2. Print First 10 Natural Numbers
👉 Print numbers from 1 to 10 using a for loop.'''

# n = 10
# for i in range(1,11):
#     print(i)


'''🔹 3. Sum of First n Natural Numbers
👉 Input a number n and find the sum of numbers from 1 to n.
(Hint: use a variable to store the total.)'''

# n = int(input("Emter a number:"))
# total=0
# for i in range(1,n+1):
#     total+=i
#     print("Sum:",total)

'''🔹 4. Print Even Numbers Between 1 and 50
👉 Print all even numbers in that range.'''

# n = 51
# for i in range(1,51):
#     if i%2==0:
#         print(i)
    

'''🔹 5. Print Odd Numbers Between 1 and 50
👉 Similar to above, but print only odd numbers.'''

# n = 51
# for i in range(1,n):
#     if i%2!=0:
#         print(i)


'''🔹 6. Multiplication Table
👉 Input a number and print its multiplication table up to 10.
Example:
Input → 5
Output →
5 x 1 = 5  
5 x 2 = 10  
...  
5 x 10 = 50'''

# n = int(input("Enter a number upto 10:"))
# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")   


'''🔹 7. Factorial of a Number
👉 Input a number and calculate its factorial using a for loop.
Example: 5! = 5 × 4 × 3 × 2 × 1 = 120'''

# n = int(input("Enter a number to find it's factorial:"))
# fact = 1
# for i in range(1,n+1):
#     fact *=i
#     print("Factorial",fact)


'''🔹 8. Print Each Character of a String
👉 Input a string and print each character one by one.
Example:
Input → "Python"'''

# n = str(input("Enter a string:"))
# for ch in n:
#     print(ch)


'''🔹 9. Print Squares of Numbers
👉 For numbers 1 to 10, print their squares.'''

# for i in range(1,11):
#  print(f"Square of {i} is {i**2}")

'''🔹 10. Print Sum of Even Numbers
👉 Find the sum of all even numbers between 1 and n.'''

# even = int(input("Enter a number:"))
# n = 0
# for i in range(2,even+1,2):
#  n+=i
#  print("Sum of even number",n)

# a = str(input("Enter a string:"))
# for char in a:
#     print(char)

'''13. Print a Pattern (Stars)
👉 Input a number n and print this pattern:'''

# n = int(input("Enter a number of rows:"))
# for i in range(1,n+1):
#     print("*"*i)

