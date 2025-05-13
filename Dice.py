import random

def roll_dice():
    """
    Simulates rolling a six-sided die.
    
    Returns:
        int: A random integer between 1 and 6, inclusive.
    """
    return random.randint(1, 6)  #this is  a module to find therandom integer between two integers
def main():
    print("welcome to the dice roller simulator")

    while True:
        input("Press Enter to roll the dice...")

        result= roll_dice()
        print(f"you rolled a {result}!")

        choice=input("Do you want to roll again? (y/n): ").strip().lower()
        if choice !="y":
            print("Thanks for playing!")
            break

if __name__=="__main__":
    main()