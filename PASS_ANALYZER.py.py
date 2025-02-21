import tkinter as tk
from tkinter import messagebox
import re
import hashlib

def check_password_strength():
    password = entry.get()
    strength = 0
    criteria = [
        (r"[a-z]", "Lowercase letter"),
        (r"[A-Z]", "Uppercase letter"),
        (r"\d", "Number"),
        (r"[@$!%*?&#]", "Special character"),
        (r".{8,}", "At least 8 characters")
    ]
    
    passed_criteria = [desc for pattern, desc in criteria if re.search(pattern, password)]
    strength = len(passed_criteria)
    
    if strength == 5:
        result_label.config(text="Strong Password ✅", fg="green")
    elif strength >= 3:
        result_label.config(text="Moderate Password ⚠️", fg="orange")
    else:
        result_label.config(text="Weak Password ❌", fg="red")
    
    messagebox.showinfo("Password Criteria", "\n".join(passed_criteria) if passed_criteria else "No criteria met")

def hash_password():
    password = entry.get()
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    hashed_label.config(text=f"SHA-256: {hashed_pw}")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("400x300")

tk.Label(root, text="Enter Password:").pack(pady=5)
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack(pady=5)

hash_button = tk.Button(root, text="Hash Password", command=hash_password)
hash_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=5)

hashed_label = tk.Label(root, text="", wraplength=380, font=("Arial", 10))
hashed_label.pack(pady=5)

root.mainloop()
