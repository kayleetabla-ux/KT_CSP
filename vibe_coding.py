def fibonacci_sequence():
    # Step 1: Input validation
    while True:
        try:
            n = int(input("Enter the number of Fibonacci numbers to print (1-20): "))
            if 1 <= n <= 20:
                break
            else:
                print("Please enter a number between 1 and 20.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Step 2: Generate Fibonacci sequence
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b

    # Step 3: Output the sequence with number of digits
    output = " ".join(f"{num}({len(str(num))})" for num in fib_sequence)
    print(output)

# Run the function
fibonacci_sequence()