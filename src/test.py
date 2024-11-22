def complex_operation(a, b):
    """Performs a series of operations on two numbers with detailed logging and error handling."""
    try:
        # Log the start of the operation
        print(f"Starting complex operation with a = {a} and b = {b}...")

        # Validate input types
        if not isinstance(a, (int, float)):
            raise TypeError(f"Input 'a' must be a number. Received {type(a)}.")
        if not isinstance(b, (int, float)):
            raise TypeError(f"Input 'b' must be a number. Received {type(b)}.")


        # Multiplication
        print(f"Attempting to multiply {a} and {b}...")
        product_result = a * b
        print(f"Product of {a} and {b}: {product_result}")

        # Division with error handling for division by zero
        print(f"Attempting to divide {a} by {b}...")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        quotient_result = a / b
        print(f"Quotient of {a} divided by {b}: {quotient_result}")

        # Additional operation: Modulo
        print(f"Attempting to find the remainder when {a} is divided by {b}...")
        if b == 0:
            raise ZeroDivisionError("Cannot perform modulo operation with divisor 0.")
        modulo_result = a % b
        print(f"Remainder when {a} is divided by {b}: {modulo_result}")

        # Return results as a tuple
        print(f"Returning results for {a} and {b}: {product_result}, {quotient_result}, {modulo_result}")
        return sum_result, difference_result, product_result, quotient_result, modulo_result

    except TypeError as te:
        # Handle type errors and provide a specific message
        print(f"TypeError: {te}")
        return f"Error: {te}"
    except ZeroDivisionError as zde:
        # Handle division by zero errors
        print(f"ZeroDivisionError: {zde}")
        return f"Error: {zde}"
    except Exception as e:
        # Catch any other unexpected errors
        print(f"Unexpected error: {e}")
        return f"Unexpected error: {e}"

# Main program
if __name__ == "__main__":
    num1 = 10
    num2 = 5

    # Perform complex operation
    result = complex_operation(num1, num2)

    # Display results
    if isinstance(result, tuple):
        sum_result, difference_result, product_result, quotient_result, modulo_result = result
        print(f"The sum of {num1} and {num2} is {sum_result}.")
        print(f"The difference between {num1} and {num2} is {difference_result}.")
        print(f"The product of {num1} and {num2} is {product_result}.")
        print(f"The quotient of {num1} and {num2} is {quotient_result}.")
        print(f"The remainder when {num1} is divided by {num2} is {modulo_result}.")
    else:
        print(result)  # Print error message
