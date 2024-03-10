import tkinter as tk
from tkinter import ttk

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from_currency.get()
        to_currency = combo_to_currency.get()

        if from_currency == to_currency:
            result_label.config(text=f"{amount} {from_currency} = {amount} {to_currency}")
        else:
            converted_amount = amount / exchange_rates[from_currency] * exchange_rates[to_currency]
            result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

    except ValueError:
        result_label.config(text="Будь ласка, введіть коректну суму.")

exchange_rates = {'USD': 1.0, 'EUR': 0.85, 'GBP': 0.73}

root = tk.Tk()
root.title("Конвертер валют")
root.configure(bg="black")

entry_amount = ttk.Entry(root, style="Black.TEntry")
entry_amount.grid(row=0, column=0, padx=10, pady=10)

entry_amount.configure(foreground="orange")

combo_from_currency = ttk.Combobox(root, values=list(exchange_rates.keys()), style="Black.TCombobox")
combo_from_currency.set("USD")
combo_from_currency.grid(row=0, column=1, padx=10, pady=10)

combo_to_currency = ttk.Combobox(root, values=list(exchange_rates.keys()), style="Black.TCombobox")
combo_to_currency.set("USD")
combo_to_currency.grid(row=0, column=2, padx=10, pady=10)

convert_button = ttk.Button(root, text="Конвертувати", command=convert_currency, style="Black.TButton")
convert_button.grid(row=1, column=0, columnspan=3, pady=10)

result_label = ttk.Label(root, text="", style="Black.TLabel")
result_label.grid(row=2, column=0, columnspan=3, pady=10)

style = ttk.Style()
style.configure("Black.TEntry", fieldbackground="black", foreground="orange")
style.configure("Black.TCombobox", fieldbackground="black", foreground="orange")
style.configure("Black.TButton", background="black", foreground="orange")
style.configure("Black.TLabel", background="black", foreground="orange")

root.mainloop()

