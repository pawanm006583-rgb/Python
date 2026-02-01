'''1. Print Numbers 1 to 10
Write a program to print numbers from 1 to 10 using a while loop.
Hint: Start with i = 1, loop while i <= 10.'''

# i=1
# while i >=1 and i<=10:
#     print(i)
#     i+=1


'''2. Print Even Numbers
Print all even numbers from 1 to 20 using a while loop.
Hint: Use the condition if i % 2 == 0.'''

# i = 1
# while i<=20:
#     if i%2==0:
#         print(i)
#     i+=1


'''3. Sum of First N Natural Numbers
Take an integer input n and find the sum of numbers from 1 to n using a while loop.
Example:
If n = 5, output should be 15.'''

# n = int(input("Enter a number:"))
# i = 1
# sum = 0
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)


'''4. Table of a Number
Take a number as input and print its multiplication table (from 1 to 10).
Example:
Input → 5
Output →
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50'''

# n = int(input("Enter the number for its multiplication table:"))
# i = 1
# while i<=10:
#     print(f"{n}X{i} = {n*i}")
#     i+=1


'''5. Countdown Timer
Take an integer input n and print a countdown from n to 1.
Example:
Input → 5
Output → 5 4 3 2 1'''

n = int(input("Enter a number for count down:"))
while n>=0:
    print(n)
    n-=1