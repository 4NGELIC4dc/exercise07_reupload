#decimal to octal
num=input("Enter a decimal integer: ")
if num.isnumeric():
    print("Quotient Remainder Octal")
    octal=0
    n=1
    number=""
    while num != 0:
        num=int(num)
        remainder=num%8
        num//=8
        octal=octal+remainder*n
        n*=10
        number=str(remainder)+number
        print("%5d%8d%12s"%(num, remainder, number))
    print("The octal representation is: ", octal)
else:
    print("Please input a valid decimal value.")

#octal to decimal
num=input("Enter a string of octal digits: ")
if "8" in num or "9" in num or not num.isnumeric():
    print("Please input a valid octal value.")
else:
    num=int(num)
    n=1
    decimal=0
    while num != 0:
        remainder=num%10
        num//=10
        decimal+=remainder*n
        n*=8
    print("The integer value is: ", decimal)