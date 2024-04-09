import tkinter as tk
from tkinter import messagebox

def generate_resume():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    summary = summary_text.get("1.0", "end-1c")
    education = education_text.get("1.0", "end-1c")
    experience = experience_text.get("1.0", "end-1c")

    resume = f"""
    ---------------------------------------------------
                          RESUME
    ---------------------------------------------------
    Name      : {name}
    Email     : {email}
    Phone     : {phone}
    Address   : {address}

    ---------------------------------------------------
                          SUMMARY
    ---------------------------------------------------
    {summary}

    ---------------------------------------------------
                        EDUCATION
    ---------------------------------------------------
    {education}

    ---------------------------------------------------
                        EXPERIENCE
    ---------------------------------------------------
    {experience}
    """
    messagebox.showinfo("Generated Resume", resume)

# Create main window
root = tk.Tk()
root.title("Resume Generator")

# Name
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# Email
email_label = tk.Label(root, text="Email:")
email_label.grid(row=1, column=0, sticky="e")
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1)

# Phone
phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=2, column=0, sticky="e")
phone_entry = tk.Entry(root)
phone_entry.grid(row=2, column=1)

# Address
address_label = tk.Label(root, text="Address:")
address_label.grid(row=3, column=0, sticky="e")
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1)

# Summary
summary_label = tk.Label(root, text="Summary:")
summary_label.grid(row=4, column=0, sticky="ne")
summary_text = tk.Text(root, width=40, height=5)
summary_text.grid(row=4, column=1, sticky="w")

# Education
education_label = tk.Label(root, text="Education:")
education_label.grid(row=5, column=0, sticky="ne")
education_text = tk.Text(root, width=40, height=5)
education_text.grid(row=5, column=1, sticky="w")

# Experience
experience_label = tk.Label(root, text="Experience:")
experience_label.grid(row=6, column=0, sticky="ne")
experience_text = tk.Text(root, width=40, height=5)
experience_text.grid(row=6, column=1, sticky="w")

# Generate button
generate_button = tk.Button(root, text="Generate Resume", command=generate_resume)
generate_button.grid(row=7, columnspan=2)

# Run the application
root.mainloop()
