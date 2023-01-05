import re

def bruteforce_prediction(password: str,all_char: int ) -> tuple:
    # Calculate the number of attempts
    length = len(password)
    attempts = all_char ** length

    # Calculate the probability of guessing the password on the first attempt
    probability = 1 / attempts
    return (attempts, probability)


def analyse_input(password: str) -> str:
    all_char = 0
    if re.search(r'\d', password):
        digits = 10  # 10 digits
        print("  digits")
        all_char += digits

    if re.search(r'[a-z]', password):
        lower_leters = 26 #26 lowercase letters
        print("  lowercase letters")
        all_char += lower_leters

    if re.search(r'[A-Z]', password):
        upper_letters = 26 #26 uppercase letters
        print("  uppercase letters")
        all_char += upper_letters
      
    if re.search(r'[^A-Za-z0-9]', password):
        special_char = 40 #special characters, in regex I defined all the charaters which are not uppercase, lowercase or numbers
        print("  special characters")
        all_char += special_char

    return bruteforce_prediction(password, all_char)

# Asks user input and then returns the result
password = input("Enter secure password: ")
print("In the password there are:")
attempts, probability = analyse_input(password)
print(f"Number of attempts: {attempts}")
print(f"Probability of guessing on the first attempt: {probability}") # Shows the result with 20 digits after comma
