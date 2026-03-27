try:
    print("enter num 1:")
    num1 = int(input())

    print("enter num 2:")
    num2 = int(input())

    print(f"sum is:{num1+num2}")

except Exception as e:
    print("Invalid input!", e)

print("this line is very important!")

#it only catches the error within try block not outside