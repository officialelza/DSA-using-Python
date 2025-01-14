def simple_interest (p, t, r):
    return (p * t * r) / 100

def main():
    p = int(input("Enter the principle amount: "))

    t = int(input("Enter the time period in years: "))

    r = int(input("Enter the rate of interest per annum: "))

    si = simple_interest(p, t, r)
    print(f"Simple Interest: {si}")

if __name__ == "__main__":
    main()