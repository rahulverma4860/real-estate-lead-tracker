import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import datetime


# -------------------------------
# iCloud Drive CSV file location
# -------------------------------
ICLOUD_FOLDER = os.path.expanduser(
    "~/Library/Mobile Documents/com~apple~CloudDocs/LeadTracker"
)
CSV_FILE = os.path.join(ICLOUD_FOLDER, "leads.csv")


# -------------------------------
# Create iCloud folder if missing
# -------------------------------
def ensure_icloud_folder():
    os.makedirs(ICLOUD_FOLDER, exist_ok=True)


# -------------------------------
# Create CSV file with headers
# -------------------------------
def create_csv_if_not_exists():
    ensure_icloud_folder()

    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Date Added",
                "Full Name",
                "Phone Number",
                "Email",
                "Source",
                "Area / Property",
                "Budget",
                "Notes"
            ])


# -------------------------------
# Save lead data
# -------------------------------
def save_lead():
    full_name = entry_name.get().strip()
    phone_number = entry_phone.get().strip()
    email = entry_email.get().strip()
    source = entry_source.get().strip()
    area_property = entry_area.get().strip()
    budget = entry_budget.get().strip()
    notes = text_notes.get("1.0", tk.END).strip()
    date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Basic validation
    if not full_name or not phone_number:
        messagebox.showerror("Missing Information", "Full Name and Phone Number are required.")
        return

    create_csv_if_not_exists()

    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            date_added,
            full_name,
            phone_number,
            email,
            source,
            area_property,
            budget,
            notes
        ])

    messagebox.showinfo("Success", "Lead saved successfully to iCloud Drive.")
    clear_form()


# -------------------------------
# Clear form after saving
# -------------------------------
def clear_form():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_source.delete(0, tk.END)
    entry_area.delete(0, tk.END)
    entry_budget.delete(0, tk.END)
    text_notes.delete("1.0", tk.END)


# -------------------------------
# Main window
# -------------------------------
root = tk.Tk()
root.title("Real Estate Lead Tracker")
root.geometry("500x550")
root.resizable(False, False)

# Title
label_title = tk.Label(root, text="Real Estate Lead Tracker", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

# Form Frame
frame = tk.Frame(root)
frame.pack(pady=10)

# Full Name
tk.Label(frame, text="Full Name").grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_name = tk.Entry(frame, width=40)
entry_name.grid(row=0, column=1, padx=10, pady=5)

# Phone Number
tk.Label(frame, text="Phone Number").grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_phone = tk.Entry(frame, width=40)
entry_phone.grid(row=1, column=1, padx=10, pady=5)

# Email
tk.Label(frame, text="Email").grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_email = tk.Entry(frame, width=40)
entry_email.grid(row=2, column=1, padx=10, pady=5)

# Source
tk.Label(frame, text="Source").grid(row=3, column=0, sticky="w", padx=10, pady=5)
entry_source = tk.Entry(frame, width=40)
entry_source.grid(row=3, column=1, padx=10, pady=5)

# Area / Property
tk.Label(frame, text="Area / Property").grid(row=4, column=0, sticky="w", padx=10, pady=5)
entry_area = tk.Entry(frame, width=40)
entry_area.grid(row=4, column=1, padx=10, pady=5)

# Budget
tk.Label(frame, text="Budget").grid(row=5, column=0, sticky="w", padx=10, pady=5)
entry_budget = tk.Entry(frame, width=40)
entry_budget.grid(row=5, column=1, padx=10, pady=5)

# Notes
tk.Label(frame, text="Notes").grid(row=6, column=0, sticky="nw", padx=10, pady=5)
text_notes = tk.Text(frame, width=30, height=6)
text_notes.grid(row=6, column=1, padx=10, pady=5)

# Save Button
button_save = tk.Button(root, text="Save Lead", width=20, bg="green", fg="white", command=save_lead)
button_save.pack(pady=20)

# Make sure CSV exists before app starts
create_csv_if_not_exists()

# Run app
root.mainloop()