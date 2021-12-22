
#Write a function to calculate area and perimeter of a rectangle. 

l=int(input("Length : "))
w=int(input("Width : "))
area=l*w
perimeter=2*(l+w)
print("Area of Rectangle : ",area)
print("Perimeter of Rectangle : ",perimeter)



#Write a function to calculate area and circumference of a circle.

PI = 3.14
radius = float(input(' Please Enter the radius of a circle: '))

diameter = 2 * radius
circumference = 2 * PI * radius
area = PI * radius * radius

print(" \nDiameter Of a Circle = %.2f" %diameter )
print(" Circumference Of a Circle = %.2f" %circumference)
print(" Area Of a Circle = %.2f" %area)

#Write a function to calculate power of a number raised to other. E.g.-ab. 
def power(x, y):
  
    if (y == 0): return 1
    elif (int(y % 2) == 0):
        return (power(x, int(y / 2)) *
               power(x, int(y / 2)))
    else:
        return (x * power(x, int(y / 2)) *
                   power(x, int(y / 2)))
  

x = 2; y = 3
print(power(x, y))

#Write a function to tell user if he/she is able to vote or not. ❑ ( Consider minimum age of voting to be 18.)

age = int(input("Enter Age : "))

# condition to check voting eligibility
if age>=18:
        status="Eligible"
else:
    status="Not Eligible"

print("You are ",status," for Vote.")

#Write a function to check if a number is even or not. 

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

#   Write a function to check if a number is prime or not.



if num > 1:

   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
 
else:
   print(num,"is not a prime number")
 #Write a function to find factorial of a number but also store the  factorials calculated in a dictionary as done in the Fibonacci series  example. 
n=int (input("enter the number:"))
result=1
for i in range(n,0,-1):
    result=result*i
print("factorial of",n,"is",result)
 

#Write a Python program to detect the number of local variables declared  in a function 
def abc():
    x = 1
    y = 2
    str1= "w3resource"
    print("Python Exercises")

print(abc.__code__.co_nlocals)
