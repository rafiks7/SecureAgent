def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

if __name__ == "__main__":
    num1 = 10
    num2 = "5"

    sum_result = add_numbers(num1, num2)
    difference_result = subtract_numbers(num1, num2)

    print("The sum of " + str(num1) + " and " + str(num2) + " is " + str(sum_result) + ".")
    print(f"The difference between {num1} and {num2} is {difference_result}.")
