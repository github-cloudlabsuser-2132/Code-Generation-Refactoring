#A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases

def get_integers(count):
    arr = []
    print(f"Enter {count} integers:")
    for _ in range(count):
        while True:
            try:
                arr.append(int(input()))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    return arr

def calculate_sum(arr):
    return sum(arr)

def main():
    MAX = 100
    try:
        n = int(input("Enter the number of elements (1-100): "))
        if not 1 <= n <= MAX:
            print("Invalid input. Please provide a digit ranging from 1 to 100.")
            exit(1)
        arr = get_integers(n)
        total = calculate_sum(arr)
        print("Sum of the numbers:", total)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        exit(1)

if __name__ == "__main__":
    main()
