def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    answer = summation(a, b)
    print("\nThe summation of", a, "and", b, "is", answer)

def summation(num1, num2):
    return num1 + num2

main()