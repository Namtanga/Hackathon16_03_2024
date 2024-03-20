def fibonacci_sequence(n):
    # Initialize the first two terms of the sequence
    fibonacci = [0, 1]
    
    # Generate the Fibonacci sequence up to term n
    for i in range(2, n):
        # Compute the next term by summing the two preceding terms
        next_term = fibonacci[i - 1] + fibonacci[i - 2]
        # Append the next term to the sequence
        fibonacci.append(next_term)
    
    return fibonacci

# Ask the user to input the value of n
n = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Generate the Fibonacci sequence
sequence = fibonacci_sequence(n)


# Print the generated Fibonacci sequence
print("Fibonacci sequence up to term", n, ":", sequence)

def main():
    # Prompting the user to enter their age
    age = int(input("Please enter your age: "))

    # Checking if the age is greater than or equal to 18
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

if __name__ == "__main__":
    main()
