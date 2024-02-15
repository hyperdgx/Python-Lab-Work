a = 1
print("Output: ",type(a))

#Output: <class 'int'>

#Let's See Some Magic In Python VM
myValue_1 = 125
myValue_2 = 0b10101
myValue_3 = 0o74521
myValue_4 = 0xABF5921

print("Value 1: ",myValue_1, "\t", "Type of Value 1: ",type(myValue_1))
print("Value 1: ",myValue_2, "\t", "Type of Value 1: ",type(myValue_2))
print("Value 1: ",myValue_3, "\t", "Type of Value 1: ",type(myValue_3))
print("Value 1: ",myValue_4, "\t", "Type of Value 1: ",type(myValue_4))
print("\n")

#Above PVM changes it into Integer

#Base Conversion
print("#---# Base Conversion #---# \n")

#Decimal Form (Base 10)
#Example: 0,1,2,3,4,5,6,7,8,9

#Binary to Decimal
myBinaryValue = 0b10101
myDecimalValue = myBinaryValue
print("Decimal of",bin(myBinaryValue),": ",myDecimalValue)

#Octal to Decimal
myOctalValue = 0o124
myDecimalValue = myOctalValue
print("Decimal of",oct(myOctalValue),": ",myDecimalValue)

#Hexadecimal to Decimal
myHexadecimalValue = 0x11A
myDecimalValue = myHexadecimalValue
print("Decimal of",hex(myHexadecimalValue),": ",myDecimalValue,"\n")


#Binary Form (Base 2)
#Example: 0,1 (0b or 0B)

#Decimal to Binary
myDecimalValue = 16
myBinaryValue = bin(myDecimalValue)
print("Binary of",myDecimalValue,": ",myBinaryValue)

#Octal to Binary
myOctalValue = 0o16
myBinaryValue = bin(myOctalValue)
print("Binary of",oct(myOctalValue),": ",myBinaryValue)

#Hexadecimal to Binary
myHexadecimalValue = 0x16
myBinaryValue = bin(myHexadecimalValue)
print("Binary of",hex(myHexadecimalValue),": ",myBinaryValue,"\n")


#Octal Form (Base 8)
#Example: 0,1,2,3,4,5,6,7 (0o or 0O)

#Decimal to Octal
myDecimalValue = 12
myOctalValue = oct(myDecimalValue)
print("Octal of",myDecimalValue,": ",myOctalValue)

#Binary to Octal
myBinaryValue = 0b1001
myOctalValue = oct(myBinaryValue)
print("Octal of",bin(myBinaryValue),": ",myOctalValue)

#Hexadecimal to Octal
myHexadecimalValue = 0x102A
myOctalValue = oct(myDecimalValue)
print("Octal of",hex(myHexadecimalValue),": ",myOctalValue,"\n")


#Hexadecimal Form (Base 16)
#Example: 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F (0x or 0X)

#Decimal to Hexadecimal
myDecimalValue = 12
myHexadecimalValue = hex(myDecimalValue)
print("Hexadecimal of",myDecimalValue,": ",myHexadecimalValue)

#Binary to Hexadecimal
myBinaryValue = 0b10101
myHexadecimalValue = hex(myBinaryValue)
print("Hexadecimal of",bin(myBinaryValue),": ",myHexadecimalValue)

#Ocatal to Hexadecimal
myOctalValue = 0o121
myHexadecimalValue = hex(myOctalValue)
print("Hexadecimal of",oct(myBinaryValue),": ",myHexadecimalValue)