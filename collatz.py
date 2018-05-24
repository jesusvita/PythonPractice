def collatz(number):
    number = int(number)
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1
        
while True:
    try:
        number = int(input("Give me a number: "))
        break
    except ValueError:
        print("This is not a number, try again.")

while number != 1:
    number = collatz(number)
    print(number)
