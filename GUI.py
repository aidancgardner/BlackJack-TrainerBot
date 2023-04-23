# AIDAN GARDNER MARCH 20, 2023

import tkinter as tk
from tkinter import messagebox
import game_logic
from PIL import Image, ImageTk

# for scaling cards
def resize_card(card):
    card_img = Image.open(card)
    # resize
    resized_img = card_img.resize((187, 272)) 
    new_card_img = ImageTk.PhotoImage(resized_img)
    return new_card_img

# deck initialize
deck = game_logic.Deck()
deck.shuffle()
dealer_card = deck.deal()
player_card1 = deck.deal()
player_card2 = deck.deal()
round_num = 1
win_num = 0

# GUI
# Create the main window
window = tk.Tk()
window.geometry("1080x720")
window.configure(bg="green")
window.title("Ace of Spades")

#Create the dealer label
dealer_card_image = resize_card(f'cards/{dealer_card.value}_of_{dealer_card.suit}.png')
dealer_label = tk.Label(window, image=dealer_card_image)
dealer_label.pack(expand=True)
dealer_label.place(relx=0.5, rely=0.30, anchor=tk.CENTER)

# Create a frame to hold the player labels
player_frame = tk.Frame(window)
player_frame.configure(bg="green")
player_frame.pack(pady=20)

# Create the  first player label
player_card_image1 = resize_card(f'cards/{player_card1.value}_of_{player_card1.suit}.png')
player_label1 = tk.Label(player_frame, image=player_card_image1)
player_label1.pack(side=tk.LEFT, padx=10, pady=10)

# Create the second player label
player_card_image2 = resize_card(f'cards/{player_card2.value}_of_{player_card2.suit}.png')
player_label2 = tk.Label(player_frame, image=player_card_image2)
player_label2.pack(side=tk.RIGHT, padx=10, pady=10)

# Position the player frame in the middle of the window
player_frame.place(relx=0.5, rely=0.70, anchor=tk.CENTER)

# Create a label for the dealer title
dealer_title = tk.Label(window, text="Dealer")
dealer_title.pack()
dealer_title.place(relx=0.5, rely=0.10, anchor=tk.CENTER)

# create player label
player_title = tk.Label(window, text="Player")
player_title.pack()
player_title.place(relx=0.5, rely=0.50, anchor=tk.CENTER)

# player choice function
def player_choice(choice):
    global  deck, dealer_card, player_card1, player_card2, round_num, dealer_label, dealer_card_image, player_label1, player_card_image1, player_label2, player_card_image2
    global round_num, correct_percentage, last_choice, correct_count
    update_strat()
    print('correct choice was:', strat)
    if choice == strat:
        print('your choice was correct')

        # update last choice
        last_choice = 'Correct'
        last_choice_label.configure(text=F"Last Choice: {last_choice}")

        # update percentage
        correct_count += 1
        compute_correct_percentage = (correct_count / round_num) * 100
        correct_percentage = format(compute_correct_percentage, ".2F")
        correct_percentage_label.configure(text=F"Correct Percentage: {correct_percentage}%")
    else:
        print("your choice was wrong")
        messagebox.showinfo("Wrong", F"The correct choice was {strat}")

        # update last choice
        last_choice = 'Wrong'
        last_choice_label.configure(text=F"Last Choice: {last_choice}")

        # update percentage
        compute_correct_percentage = (correct_count / round_num) * 100
        correct_percentage = format(compute_correct_percentage, ".2F")
        correct_percentage_label.configure(text=F"Correct Percentage: {correct_percentage}%")

    # remake deck
    deck = game_logic.Deck()
    deck.shuffle()
    dealer_card = deck.deal()
    player_card1 = deck.deal()
    player_card2 = deck.deal()

    # update round num
    round_num += 1
    round_num_label.configure(text=f"Round: {round_num}")

    # acquire card images again
    dealer_card_image = resize_card(f'cards/{dealer_card.value}_of_{dealer_card.suit}.png')
    player_card_image1 = resize_card(f'cards/{player_card1.value}_of_{player_card1.suit}.png')
    player_card_image2 = resize_card(f'cards/{player_card2.value}_of_{player_card2.suit}.png')

    # update labels
    dealer_label.configure(image=dealer_card_image)
    player_label1.configure(image=player_card_image1)
    player_label2.configure(image=player_card_image2)

def update_strat():
    global strat
    strat_obj = game_logic.Strategy(dealer_card, player_card1, player_card2)
    strat = strat_obj.correct_choice()


#Create a frame to hold the action buttons
button_frame = tk.Frame(window)
button_frame.configure(bg="green")
button_frame.pack(side=tk.BOTTOM, pady=20)

#Create the action buttons
double_button = tk.Button(button_frame, text="Double", command=lambda: player_choice("Double"))
double_button.pack(side=tk.LEFT, padx=20)

hit_button = tk.Button(button_frame, text="Hit", command=lambda: player_choice("Hit"))
hit_button.pack(side=tk.LEFT, padx=20)

stand_button = tk.Button(button_frame, text="Stand", command=lambda: player_choice("Stand"))
stand_button.pack(side=tk.LEFT, padx=20)

split_button = tk.Button(button_frame, text="Split", command=lambda: player_choice("Split"))
split_button.pack(side=tk.LEFT, padx=20)

#___________________________________

# Create the stats frame
stats_frame = tk.Frame(window, bg="green")
stats_frame.pack(side=tk.TOP, padx=20, pady=10, anchor=tk.NE)

# Create the round_num label
round_num_label = tk.Label(stats_frame, text=f"Round: {round_num}", bg="green", fg="white")
round_num_label.pack(side=tk.LEFT, padx=5)

# Create the correct_percentage label
correct_count = 0
correct_percentage = 0
correct_percentage_label = tk.Label(stats_frame, text=F"Correct Percentage: {correct_percentage}%", bg="green", fg="white")
correct_percentage_label.pack(side=tk.LEFT, padx=5)

# Create the last_choice label
last_choice = None
last_choice_label = tk.Label(stats_frame, text=F"Last Choice: {last_choice}", bg="green", fg="white")
last_choice_label.pack(side=tk.LEFT, padx=5)

window.mainloop()