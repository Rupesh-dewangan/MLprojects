import tkinter as tk
from tkinter import ttk, messagebox



root= tk.Tk()
root.title("Login")
root.geometry('600x400')
root.minsize(200,200)
root.maxsize(300,700)


root.iconbitmap('D:\\Learnings\\My Projects\\Machine Learning\\Used Car Price Prediction\\images\\car.ico')
root.configure(bg='lightblue')

labels = ["Present Price", "Kms Driven", "Fuel Type", "Seller Type", "Transmission", "Owner", "Age"]
#entries = []

entry_price = ttk.Entry(root)
entry_kms = ttk.Entry(root)
entry_owner = ttk.Entry(root)
entry_age = ttk.Entry(root)

combo_fuel = ttk.Combobox(root, values=["Petrol", "Diesel", "CNG"])
combo_seller = ttk.Combobox(root, values=["Individual", "Dealer"])
combo_trans = ttk.Combobox(root, values=["Manual", "Automatic"])

widgets = [
    entry_price,
    entry_kms,
    combo_fuel,
    combo_seller,
    combo_trans,
    entry_owner,
    entry_age
]
for i, label in enumerate(labels):
    ttk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="w")
    widgets[i].grid(row=i, column=1, padx=10, pady=5, sticky="ew")

root.mainloop()