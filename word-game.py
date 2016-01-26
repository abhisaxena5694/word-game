import random
import string

def score(list_of_words):
    count = 0
    count = len(list_of_words) * 10
    count += (len(list_of_words)//5) * 10
    print "Your score is %s " % count
    

def start(letter):
    print "So, your starting letter is '%s'.Let's start with the game." % letter.upper()
    print "Enter the first word."
    list_of_words = []
    first_word = raw_input(">")
    list_of_words.append(first_word)
    next_word = None
    
    while True:
        next_word = raw_input(">")
        
        if next_word == '' or next_word[0] == ' ':
            print "Your text is invalid. Please enter again."
            continue
        
        elif first_word[len(first_word) - 1] == next_word[0]:
            list_of_words.append(next_word)
            first_word = next_word
            continue
        else:
            print "The last letter of your previous word didn't match the first letter of this word. Game Over!" 
            score(list_of_words)
            break 
            
def random_letter():
    # list_of_alphabets = string.letters
    letter = random.choice(string.letters)
    # return letter
    start(letter)
    
def player_name(name):
    letter = random.choice(name)
    # return letter
    start(letter)

def player_choice(name):
    print """Enter MY NAME if you want to start with a letter of your name, or RANDOM if you want to go for a random alphabet."""
    choice = raw_input(">")
    while choice != "MY NAME" or choice != "RANDOM":
        if choice.upper() == "MY NAME":
            player_name(name)
            break
        elif choice.upper() == "RANDOM":
            random_letter()
            break
        else:
            choice = raw_input("I did not understand. Please enter your choice again.\n>")
            continue
        break
    

def main():
    
    print "Welcome to the Word Game."
    
    name = raw_input("What's your name?\n>")
    
    print """Hi! %s, the following are the rules of this game. 
    - You'll get an English alphabet. 
    - You have to enter a word starting from that alphabet. 
    - The next word will start from the last letter of the previous word you entered.
    - In the same way, you enter the third word and so on..
    - You'll get 10 points for every word and additional 10 points for every 5 words.
    - You have a choice between a random letter a letter of your name for your first word.""" % name
    
    player_choice(name)
    
     
    
    
main()
