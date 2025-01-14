#arithmetic progression

def check_fn(x, num):

    if num == 1:
        return True
    
    x.sort()
    difference = x[1] - x[0]

    for i in range(2, num):
        if (x[i] - x[i - 1]) != difference:
            return False
        
    return True

def main():
    myarray  = eval(input("Enter the array:"))
    num = len(myarray)

    print(f"Original array: {myarray}")
    myarray.sort()
    print(f"Revised array: {myarray}")

    print(f"Is the given array an arithmetic progression? {check_fn(myarray, num)}")

if __name__ == "__main__":
    main()

