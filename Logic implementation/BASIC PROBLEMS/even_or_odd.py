def is_even(n):
    return("Even" if (n%2==0) else "Odd")

def bool_is_even(n):
    return("Even" if ((n&1) == 0) else "Odd")

num  = int(input("Enter a number : "))
bool_num = int(input("Enter a boolean : "))
print(f"Number is {is_even(num)}")
print(f"Bool Number is {bool_is_even(bool_num)}")

