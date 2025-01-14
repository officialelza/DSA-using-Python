def sum_of_digits(number):

    if number == 0:
        return 0
    
    return number % 10 + sum_of_digits(number // 10)

def main():
    number = int(input("Enter a number: "))
    
    print(f"Sum of digits of {number} is {sum_of_digits(number)}")

if __name__ == "__main__":
    main()
