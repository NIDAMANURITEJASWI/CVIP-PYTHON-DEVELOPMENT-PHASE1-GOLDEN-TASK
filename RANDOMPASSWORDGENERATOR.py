import tkinter as tk
import random
import string
def random_password():
    l = int(l_entry.get())
    if l < 8:
        p_label.config(text="Password length must be at least 9 characters")
        return
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(l))
    p_label.config(text="Generated Password: " + password)
window = tk.Tk()
window.title("Password Generator")
l_label = tk.Label(window, text="Password length:")
l_label.pack()
l_entry = tk.Entry(window)
l_entry.pack()
generate_button = tk.Button(window, text="Generate Random Password", command=random_password)
generate_button.pack()
p_label = tk.Label(window, text="")
p_label.pack()
window.mainloop()
