import tkinter as tk
from tkinter import messagebox

USERNAME = "ayesha"
PASSWORD = "1234"

NAME     = "Ayesha Malik"
STUDENT_ID = "STU-2401"
COURSE   = "BS Computer Science"
SEMESTER = "2nd Semester"
EMAIL    = "ayesha@uni.edu.pk"
PHONE    = "0300-1234567"
CGPA     = "3.72"
ATTENDANCE = "89%"
FEE      = "Paid"

SUBJECTS = [
    ("Programming Fundamentals", "85%", "A"),
    ("Calculus",                 "78%", "B+"),
    ("Physics",                  "91%", "A+"),
    ("English",                  "80%", "A"),
    ("Islamic Studies",          "95%", "A+"),
]

BG      = "#1e1e2e"
SURFACE = "#2a2a3e"
PURPLE  = "#6c63ff"
WHITE   = "#e8eaf6"
GREY    = "#9090b0"
GREEN   = "#00d4aa"
RED     = "#ff6b6b"
YELLOW  = "#ffb800"

window = tk.Tk()
window.title("Student Portal")
window.geometry("700x500")
window.resizable(False, False)
window.configure(bg=BG)


def clear():
    for w in window.winfo_children():
        w.destroy()


def show_login():
    clear()

    tk.Label(window, text="Student Portal", font=("Segoe UI", 24, "bold"),
             fg=PURPLE, bg=BG).pack(pady=(70, 4))

    tk.Label(window, text="Sign in to continue", font=("Segoe UI", 11),
             fg=GREY, bg=BG).pack()

    box = tk.Frame(window, bg=SURFACE, padx=40, pady=30)
    box.pack(pady=25)

    tk.Label(box, text="Username", font=("Segoe UI", 10), fg=GREY, bg=SURFACE).pack(anchor="w")
    user_entry = tk.Entry(box, font=("Segoe UI", 12), bg=BG, fg=WHITE,
                          insertbackground=WHITE, relief="flat", width=28,
                          highlightthickness=1, highlightbackground=GREY, highlightcolor=PURPLE)
    user_entry.pack(ipady=6, pady=(2, 12))

    tk.Label(box, text="Password", font=("Segoe UI", 10), fg=GREY, bg=SURFACE).pack(anchor="w")
    pass_entry = tk.Entry(box, font=("Segoe UI", 12), bg=BG, fg=WHITE,
                          insertbackground=WHITE, relief="flat", width=28, show="*",
                          highlightthickness=1, highlightbackground=GREY, highlightcolor=PURPLE)
    pass_entry.pack(ipady=6, pady=(2, 20))

    def login():
        if user_entry.get() == USERNAME and pass_entry.get() == PASSWORD:
            show_portal()
        else:
            messagebox.showerror("Error", "Wrong username or password!\nHint: ayesha / 1234")

    tk.Button(box, text="Login", command=login, font=("Segoe UI", 12, "bold"),
              bg=PURPLE, fg="white", relief="flat", width=20, pady=7, cursor="hand2").pack()

    tk.Label(window, text="username: ayesha     password: 1234",
             font=("Segoe UI", 10), fg=GREY, bg=BG).pack()


def show_portal():
    clear()

    topbar = tk.Frame(window, bg=SURFACE)
    topbar.pack(fill="x")
    tk.Label(topbar, text="  EduCore Portal", font=("Segoe UI", 13, "bold"),
             fg=PURPLE, bg=SURFACE).pack(side="left", pady=10)
    tk.Label(topbar, text=f"  {NAME}  ", font=("Segoe UI", 11),
             fg=GREY, bg=SURFACE).pack(side="right", pady=10)
    tk.Button(topbar, text="Logout", command=show_login, font=("Segoe UI", 10),
              bg=SURFACE, fg=RED, relief="flat", cursor="hand2").pack(side="right", pady=10)

    main = tk.Frame(window, bg=BG)
    main.pack(fill="both", expand=True, padx=16, pady=12)

    left  = tk.Frame(main, bg=BG)
    right = tk.Frame(main, bg=BG)
    left.pack(side="left", fill="both", expand=True, padx=(0, 8))
    right.pack(side="right", fill="both", expand=True, padx=(8, 0))

    info_box = tk.Frame(left, bg=SURFACE, padx=16, pady=14)
    info_box.pack(fill="x", pady=(0, 10))
    tk.Label(info_box, text="Student Info", font=("Segoe UI", 12, "bold"),
             fg=PURPLE, bg=SURFACE).pack(anchor="w", pady=(0, 8))

    for field, value in [("Name", NAME), ("ID", STUDENT_ID), ("Course", COURSE),
                          ("Semester", SEMESTER), ("Email", EMAIL), ("Phone", PHONE)]:
        row = tk.Frame(info_box, bg=SURFACE)
        row.pack(fill="x", pady=1)
        tk.Label(row, text=f"{field}:", font=("Segoe UI", 10), fg=GREY,  bg=SURFACE).pack(side="left", padx=(0,6))
        tk.Label(row, text=value,       font=("Segoe UI", 10), fg=WHITE, bg=SURFACE).pack(side="left")

    stats_row = tk.Frame(left, bg=BG)
    stats_row.pack(fill="x")
    for i, (title, value, color) in enumerate([("Attendance", ATTENDANCE, GREEN),
                                                ("Fee Status", FEE,        GREEN),
                                                ("CGPA",       CGPA,       PURPLE)]):
        card = tk.Frame(stats_row, bg=SURFACE, padx=12, pady=10)
        card.grid(row=0, column=i, padx=4, sticky="ew")
        stats_row.columnconfigure(i, weight=1)
        tk.Label(card, text=title, font=("Segoe UI", 9),        fg=GREY,  bg=SURFACE).pack()
        tk.Label(card, text=value, font=("Segoe UI", 16, "bold"), fg=color, bg=SURFACE).pack()

    grades_box = tk.Frame(right, bg=SURFACE, padx=16, pady=14)
    grades_box.pack(fill="both", expand=True)
    tk.Label(grades_box, text="Subject Grades", font=("Segoe UI", 12, "bold"),
             fg=PURPLE, bg=SURFACE).pack(anchor="w", pady=(0, 10))

    header = tk.Frame(grades_box, bg=PURPLE)
    header.pack(fill="x")
    for col, width in [("Subject", 22), ("Score", 8), ("Grade", 7)]:
        tk.Label(header, text=col, font=("Segoe UI", 10, "bold"), fg="white",
                 bg=PURPLE, width=width, anchor="w", padx=6, pady=5).pack(side="left")

    for i, (subject, score, grade) in enumerate(SUBJECTS):
        row_bg = BG if i % 2 == 0 else SURFACE
        row = tk.Frame(grades_box, bg=row_bg)
        row.pack(fill="x")
        tk.Label(row, text=subject, font=("Segoe UI", 10), fg=WHITE,  bg=row_bg, width=22, anchor="w", padx=6, pady=5).pack(side="left")
        tk.Label(row, text=score,   font=("Segoe UI", 10), fg=GREEN,  bg=row_bg, width=8,  anchor="w", padx=6).pack(side="left")
        tk.Label(row, text=grade,   font=("Segoe UI", 10, "bold"), fg=PURPLE, bg=row_bg, width=7, anchor="w", padx=6).pack(side="left")

    notice = tk.Frame(right, bg="#2a2a1e", padx=12, pady=8)
    notice.pack(fill="x", pady=(10, 0))
    tk.Label(notice, text="📢  Mid-term exams start April 5th. Check your schedule.",
             font=("Segoe UI", 10), fg=YELLOW, bg="#2a2a1e").pack(anchor="w")


show_login()
window.mainloop()