import tkinter as tk
from time import strftime

# Create a function to update the time
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)  # Update the time every 1 second (1000 ms)

# Create a tkinter window
root = tk.Tk()
root.title("Digital Clock")

# Create a label to display the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

# Call the time function to display the time
time()

# Run the tkinter main loop
root.mainloop()





































































