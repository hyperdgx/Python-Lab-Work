myNumber = eval(input("Enter Any Number: "))
print("Your Number:",myNumber,type(myNumber))

splitString = input("Enter Name: ")
print(splitString,type(splitString))
data = splitString.split()
print(data,type(data))

dd,mm,yyyy = map(int, input("Enter Date of Birth (DD/MM/YYYY): ").split())

print("Date:",dd,mm,yyyy)