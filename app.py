import re
import math
import tkinter as tk
from tkinter import messagebox

def calculate_entropy(password):
    charset = 0
    if re.search(r"[a-z]",password): charset +=26
    if re.search(r"[A-Z]",password): charset +=26
    if re.search(r"\d",password): charset +=10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]",password): charset +=32
    if charset == 0:
        return 0
    return round(len(password) * math.log2(charset), 2)

def check_password_strength():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error","please enter a password.")
        return
    
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]",password) is None
    digit_error = re.search(r"\d",password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]",password) is None

    errors = [length_error,lowercase_error,uppercase_error,digit_error,special_char_error]
    score = errors.count(False)

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else :
        strength = "strong"

    entropy = calculate_entropy(password)

    result_text.set(f"passwprd strength: {strength} | Entropy : {entropy} bits")
    feedback = ""
    if length_error : feedback += "- At least 8 characters required\n"
    if lowercase_error: feedback += "- Add lowercase letters\n"
    if uppercase_error: feedback += "- Add uppercase letters\n"
    if digit_error: feedback += "- Add numbers\n"
    if special_char_error: feedback += "- Add special characters\n"

    feedback_text.set(feedback if feedback else "✅ Your password is secure!")


    #----------------GUI-----------------#

app = tk.Tk()
app.title("🔐 Cybersecurity Password Strength Checker")
app.geometry("500x300")
app.resizable(False,False)

tk.Label(app, text="Enter Password" ,font=("Arial",12)).pack(pady=10)
entry = tk.Entry(app, show="*" ,font=("Arial", 14),width=30)
entry.pack()

tk.Button(app,text="Check Strength", font=("Arial", 12),command=check_password_strength).pack(pady=10)
result_text = tk.StringVar()
tk.Label(app, textvariable=result_text, font=("Arial", 12), fg="blue").pack()

feedback_text = tk.StringVar()
tk.Label(app, textvariable=feedback_text,font=("Arial",10), justify="left",fg="red").pack(pady=5)

app.mainloop()