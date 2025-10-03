print('heelo world')
print('helo world')
print('heo world')
print('heeo world')


def is_palindrome_number(num):
    """Check if a given integer is a palindrome number."""
    original = str(num)
    reversed_num = original[::-1]
    return original == reversed_num

if __name__ == "__main__":
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)
        if is_palindrome_number(number):
            print(f"{number} is a palindrome number.")
        else:
            print(f"{number} is not a palindrome number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")