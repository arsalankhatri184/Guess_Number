import tkinter as tk
import random
# create the main window
root = tk.Tk()
root.title("Guess the Number")
root.geometry('450x250+500+250')
root.resizable(False,False)
root.config(bg='sky blue')
# generate a random number
number = random.randint(1, 10)
# write code for restart
def restart_game():
    global number
    number = random.randint(1, 10)
    result_label.config(text="")
    entry.delete(0, tk.END)
# create a function to check the guess
def check_guess():
    # get the user's guess
    guess = int(entry.get())
    # compare the guess to the random number
    if guess == number:
        result_label.config(text="Congratulations, you guessed it!",bg='sky blue',font=("Arial",14))
        result_label.place(x=80,y=50)
    elif guess < number:
        result_label.config(text="Too low, try again.",bg='sky blue',font=("Arial",14))
        result_label.place(x=150,y=50)
    else:
        result_label.config(text="Too high, try again.",bg='sky blue',font=("Arial",14))
        result_label.place(x=150,y=50)
    # clear the entry widget
    # entry.delete(0, tk.END)

# create a label for instructions
label = tk.Label(root, text="Guess a number between 1 & 10",bg='sky blue',font=("Arial",20,'bold'))
label.place(x=10,y=10)
# create an entry widget for user input
entry = tk.Entry(root, width=20,font=("Arial",25))
entry.place(x=40,y=100)
# create a button to submit the guess
button = tk.Button(root, text="Submit",bg='blue',fg='white',width=7,command=check_guess,font=("Arial",18,'bold'))
button.place(x=170,y=160)
# create a button to restart the game
restart_button = tk.Button(root, text="Restart",bg='blue',fg='white',width=7,command=restart_game, font=("Arial", 18,'bold'))
restart_button.place(x=40, y=160)
# create a button to close window
restart_button = tk.Button(root, text="Close",bg='red',fg='white',width=7,command=root.destroy, font=("Arial", 18,'bold'))
restart_button.place(x=298, y=160)
# create a label to display the result
result_label = tk.Label(root, text="",bg='sky blue',)
result_label.pack()
# run the main loop
root.mainloop()
