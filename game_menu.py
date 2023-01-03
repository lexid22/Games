from hangman import hangman
from number_guess import number_guess

def main():
    while True:
        
        if menu() == True:
            break


def menu():
    
    

    choice = input("""
                      A: Play Hangman
                      B: Play Number guess
                      C: Exit

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        hangman()
    elif choice == "B" or choice =="b":
        number_guess()
    elif choice=="C" or choice=="c":
        return True
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()
        