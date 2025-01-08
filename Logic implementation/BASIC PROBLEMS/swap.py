def main():
    a = int(input('Enter number a: '))
    b = int(input('Enter number b: '))

    print(f"Original numbers a: {a} and b: {b}")

    a , b = b , a

    print(f"Swapped numbers a: {a} and b: {b}")
    
if __name__ == "__main__":
    main()