import time
from wonderwords import RandomSentence
import random

# dictionary to store player information
player_dict = {}

def register():
    """Register a new player and add to player_dict"""
    name = input("Enter your name: ")
    player_dict[name] = {"best_score": None, "last_score": None}
    print("Player registered successfully.")

def save_score(name, score):
    """Update player's score in player_dict"""
    if player_dict[name]["best_score"] is None or score > player_dict[name]["best_score"]:
        player_dict[name]["best_score"] = score
    player_dict[name]["last_score"] = score




def typing_test():
    sent_list = []
    sent_para = ""
    for i in range(5):
        sent = RandomSentence()
        random_sent = sent.sentence()
        sent_list.append(random_sent)
        sent_para += random_sent +  " "

        def error_rate(sent_para, typed_para):
            error_count = 0

            length = len(sent_para)

            for character in range(length):
                try: 
                    if sent_para[character] != typed_para[character]:
                        error_count += 1

                except:
                    error_count += 1

            error_percent = error_count/length * 100
            return error_percent

    print("Type the below paragraph as quickly as possible with as few mistakes to get a high score: \n")
    print(sent_para)
    print("\n")

    start_time = time.time()
    typed_para = input()
    end_time = time.time()

    time_taken = end_time - start_time

    error_percent = error_rate(sent_para, typed_para)
    print("\n")

    if error_percent > 50:
        print(f"Your error rate {error_percent} was quite high and hence your accurate speed could not be computed.")

    else:
        speed = len(typed_para)/time_taken
        print("******YOUR SCORE REPORT******")
        print(f"Your speed is {speed} words/sec")
        print(f"The error rate is {error_percent}")

while True:
    print("\nWelcome to the speed typing test!")
    print("What would you like to do?")
    print("1. Register a new player")
    print("2. Take the typing test")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        name = input("Enter your name: ")
        if name not in player_dict:
            print("Player not found. Please register first.")
        else:
            score = typing_test()
            save_score(name, score)
            #print(f"Your score: {score:.2f} wpm")
            #print(f"Best score: {player_dict[name]['best_score']:.2f} wpm")
            #print(f"Last score: {player_dict[name]['last_score']:.2f} wpm")

    elif choice == "3":
        break

    else:
        print("Invalid choice. Please try again.")