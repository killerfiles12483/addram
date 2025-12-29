import tkinter as tk
from tkinter import messagebox
import sys

def show_lesson():
    # Hide the main root window
    root = tk.Tk()
    root.withdraw()
    
    # The lesson message
    title = "SECURITY ALERT: BAD DECISIONS DETECTED"
    message = (
        "You have made a series of critical errors:\n\n"
        "1. YOU TRIED TO DOWNLOAD RAM.\n"
        "   - This is physically impossible. You cannot download hardware.\n\n"
        "2. YOU BLINDLY RAN A SCRIPT.\n"
        "   - You downloaded 'payload.py' and executed it without reading the code.\n\n"
        "3. YOU ALLOWED ARBITRARY CODE EXECUTION.\n"
        "   - That script downloaded THIS file ('%15.ram.py') and ran it automatically.\n\n"
        "RESULT:\n"
        "If this file contained ransomware, your files would be encrypted right now.\n"
        "If this was a RAT (Remote Access Trojan), I would have control of your PC.\n\n"
        "Fortunately, this is just a lesson. NEVER run files you download blindly.\n"
        "The computer owner is liable for this stupidity (see TOS Clause 69)."
    )
    
    # Show the popup
    messagebox.showwarning(title, message)
    
    # Clean up
    root.destroy()

if __name__ == "__main__":
    show_lesson()