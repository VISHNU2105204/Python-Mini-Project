import random

def main():
    print("Hi, Welcome to the Number Guessing Game!")
    print("Select a range by entering two integers (a and b).")
    a, b = map(int, input("Enter the starting and ending numbers (a b): ").split())

    answer = random.randint(a, b)
    attempt = 0

    while True:
        guess = int(input("Enter your guess: "))
        attempt += 1

        if guess == answer:
            print(f"Congratulations! You guessed the number {answer} in {attempt} attempts.")
            break
        elif guess < answer:
            print("Enter a correct number.")
        else:
            print("Enter a correct number.")

main()
