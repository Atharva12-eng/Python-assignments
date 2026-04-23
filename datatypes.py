print("Enter your integer value:")
num1=int(input())
print("Your integer value is:",num1)
print(type(num1))



print("Enter your float value:")
num2=float(input())
print("Your float value is:",num2)
print(type(num2))



print("Enter your string:")
str1=input()
print("Your string is:")
print(type(str1))



print("Enter your boolean value:")
b=bool(input())
print("Your boolean value is:",b)
print(type(b))



print("\n Complex number= real part + imaginary part\n")
print("Enter the real part:")
rpart=float(input())
print("Enter the imaginary part:")
ipart=float(input())

num=complex(rpart,ipart)
print("Ypour complex value is:",num)
print(type(num))