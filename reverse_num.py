numbers = int(input("Enter a 4 digit number: "))
reverse = 0
reverse = reverse * 10 + numbers % 10
numbers = numbers // 10
reverse = reverse * 10 + numbers % 10
numbers = numbers // 10
reverse = reverse * 10 + numbers % 10
numbers = numbers // 10
reverse = reverse * 10 + numbers % 10
numbers = numbers // 10
print(f"The reversed number is {reverse}")
# The reversed number is 4321