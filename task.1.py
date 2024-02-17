import tkinter as tk

def change_text():
    button_clicks[0] += 1
    if button_clicks[0] % 2 == 1:
        label.config(text="Новий текст")
    else:
        label.config(text="Початковий текст")
    update_title()

def update_title():
    root.title(f"Зміна напису - Кількість клацань: {button_clicks[0]}")

root = tk.Tk()
root.title("Зміна напису")

# Отримання розмірів екрану
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Встановлення розмірів вікна на весь екран
root.geometry(f"{screen_width}x{screen_height}")

label_text = "Початковий текст"
label = tk.Label(root, text=label_text, font=("None", 16))
label.pack(pady=20)

button_clicks = [0]
button = tk.Button(root, text="Змінити текст", command=change_text)
button.pack()

update_title()

root.mainloop()
