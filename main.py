import tkinter as tk
from tkinter import ttk, messagebox

# ── Data ──────────────────────────────────────────────────────────────────────
USERS = {
    "teacher": {"pass": "1234", "role": "teacher", "name": "Dr. Ayesha Khan"},
    "student": {"pass": "1234", "role": "student", "name": "Ali Hassan"},
}

STUDENTS = ["Ali Hassan", "Sara Malik", "Usman Tariq", "Hina Baig"]
SUBJECTS  = ["HCI", "OOP", "DBMS", "Networks"]

MARKS = {
    "Ali Hassan":  {"HCI": 85, "OOP": 78, "DBMS": 90, "Networks": 72},
    "Sara Malik":  {"HCI": 70, "OOP": 65, "DBMS": 74, "Networks": 68},
    "Usman Tariq": {"HCI": 91, "OOP": 88, "DBMS": 85, "Networks": 93},
    "Hina Baig":   {"HCI": 60, "OOP": 55, "DBMS": 62, "Networks": 58},
}

NOTIFS = [
    "📢  Mid-Term exams scheduled for next week.",
    "✅  HCI project submissions are now open.",
    "⚠️  Last date to register electives is 25 May.",
    "📌  Campus closed on 23 March – Public Holiday.",
]

def grade(m):
    for mn, g in [(90,"A+"),(80,"A"),(70,"B+"),(60,"B"),(50,"C"),(0,"F")]:
        if m >= mn: return g

def gpa(marks):
    t = {"A+":4.0,"A":4.0,"B+":3.5,"B":3.0,"C":2.0,"F":0.0}
    v = [t[grade(m)] for m in marks.values()]
    return round(sum(v)/len(v), 2)

# ── Colors / Fonts ────────────────────────────────────────────────────────────
BG, SIDE, ACC = "#F0F4F8", "#1E3A5F", "#2E86AB"
W, TD, MU     = "#FFFFFF", "#1A1A2E", "#7F8C9A"
FB, FN        = ("Segoe UI",11,"bold"), ("Segoe UI",11)
FH            = ("Segoe UI",15,"bold")

# ── App ───────────────────────────────────────────────────────────────────────
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("UniPortal")
        self.geometry("860x560")
        self.resizable(False, False)
        self.login_screen()

    def clear(self):
        for w in self.winfo_children(): w.destroy()

    # LOGIN
    def login_screen(self):
        self.clear(); self.configure(bg=SIDE); self.geometry("380x420")
        tk.Label(self, text="🎓 UniPortal", font=("Segoe UI",22,"bold"), bg=SIDE, fg=W).pack(pady=(50,4))
        tk.Label(self, text="University Portal System", font=FN, bg=SIDE, fg="#A0BCD8").pack(pady=(0,28))

        box = tk.Frame(self, bg=W, padx=28, pady=28); box.pack(padx=36, fill="x")
        tk.Label(box, text="Username", font=FB, bg=W, fg=TD).pack(anchor="w")
        self.eu = ttk.Entry(box, font=FN); self.eu.pack(fill="x", pady=(2,10))
        tk.Label(box, text="Password", font=FB, bg=W, fg=TD).pack(anchor="w")
        self.ep = ttk.Entry(box, font=FN, show="●"); self.ep.pack(fill="x", pady=(2,18))
        tk.Button(box, text="Login", font=FB, bg=ACC, fg=W, relief="flat",
                  cursor="hand2", pady=7, command=self.login).pack(fill="x")
        tk.Label(self, text="Hint: teacher/1234  or  student/1234",
                 font=("Segoe UI",9), bg=SIDE, fg="#7FA8C8").pack(pady=14)

    def login(self):
        u, p = self.eu.get().strip(), self.ep.get().strip()
        if u in USERS and USERS[u]["pass"] == p:
            self.user = USERS[u]; self.user["uname"] = u
            self.geometry("860x560"); self.configure(bg=BG)
            self.main_screen()
        else:
            messagebox.showerror("Error", "Wrong username or password.")

    # MAIN SHELL
    def main_screen(self):
        self.clear()
        top = tk.Frame(self, bg=ACC, height=46); top.pack(fill="x"); top.pack_propagate(False)
        tk.Label(top, text="🎓  UniPortal", font=FB, bg=ACC, fg=W).pack(side="left", padx=16, pady=10)
        tk.Label(top, text=self.user["name"], font=FN, bg=ACC, fg="#D0EAF8").pack(side="right", padx=8)
        tk.Button(top, text="Logout", font=("Segoe UI",9), bg=SIDE, fg=W, relief="flat",
                  cursor="hand2", padx=8, command=self.login_screen).pack(side="right", padx=6, pady=8)

        body = tk.Frame(self, bg=BG); body.pack(fill="both", expand=True)
        self.sb = tk.Frame(body, bg=SIDE, width=170); self.sb.pack(side="left", fill="y"); self.sb.pack_propagate(False)
        self.pane = tk.Frame(body, bg=BG); self.pane.pack(side="left", fill="both", expand=True)

        if self.user["role"] == "teacher":
            self.sbtn("📤  Upload Marks",  lambda: self.show("upload"))
            self.sbtn("📋  View All Marks", lambda: self.show("view"))
            self.sbtn("🔔  Notifications",  lambda: self.show("notif"))
            self.show("upload")
        else:
            self.sbtn("📊  My Results",     lambda: self.show("results"))
            self.sbtn("🔔  Notifications",  lambda: self.show("notif"))
            self.show("results")

    def sbtn(self, txt, cmd):
        tk.Button(self.sb, text=txt, font=("Segoe UI",10), bg=SIDE, fg=W,
                  activebackground=ACC, relief="flat", anchor="w",
                  padx=14, pady=9, cursor="hand2", command=cmd).pack(fill="x", pady=1)

    def show(self, view):
        for w in self.pane.winfo_children(): w.destroy()
        {"upload": self.upload, "view": self.view_marks,
         "results": self.results, "notif": self.notifications}[view]()

    # ── TEACHER: UPLOAD ───────────────────────────────────────────────────────
    def upload(self):
        tk.Label(self.pane, text="Upload Marks", font=FH, bg=BG, fg=TD).pack(anchor="w", padx=20, pady=(18,2))

        top = tk.Frame(self.pane, bg=BG); top.pack(anchor="w", padx=20, pady=8)
        tk.Label(top, text="Subject:", font=FB, bg=BG, fg=TD).grid(row=0, column=0, padx=(0,6))
        self.subj_var = tk.StringVar(value=SUBJECTS[0])
        ttk.Combobox(top, textvariable=self.subj_var, values=SUBJECTS,
                     state="readonly", width=16, font=FN).grid(row=0, column=1, padx=(0,12))
        tk.Button(top, text="Load", font=FB, bg=ACC, fg=W, relief="flat",
                  cursor="hand2", padx=10, command=self.load_table).grid(row=0, column=2)

        self.tbl = tk.Frame(self.pane, bg=BG); self.tbl.pack(fill="x", padx=20)
        self.load_table()

    def load_table(self):
        for w in self.tbl.winfo_children(): w.destroy()
        subj = self.subj_var.get()

        hdr = tk.Frame(self.tbl, bg=ACC); hdr.pack(fill="x")
        for t, wd in [("Student",28),("Current",16),("New Marks",14),("Grade",8)]:
            tk.Label(hdr, text=t, font=FB, bg=ACC, fg=W, width=wd, anchor="w").pack(side="left", padx=8, pady=5)

        self.entries = {}
        for i, stu in enumerate(STUDENTS):
            cur = MARKS[stu].get(subj, 0)
            bg = W if i % 2 == 0 else "#EBF4FA"
            row = tk.Frame(self.tbl, bg=bg); row.pack(fill="x", pady=1)
            tk.Label(row, text=stu,      font=FN, bg=bg, fg=TD, width=28, anchor="w").pack(side="left", padx=8, pady=6)
            tk.Label(row, text=str(cur), font=FN, bg=bg, fg=MU, width=16, anchor="w").pack(side="left")
            e = ttk.Entry(row, width=10, font=FN); e.insert(0, str(cur)); e.pack(side="left", padx=6)
            gl = tk.Label(row, text=grade(cur), font=FB, bg=bg, fg=ACC, width=8); gl.pack(side="left")
            self.entries[stu] = (e, gl)

        tk.Button(self.tbl, text="💾  Save Marks", font=FB, bg="#27AE60", fg=W,
                  relief="flat", cursor="hand2", padx=14, pady=5,
                  command=lambda: self.save(subj)).pack(pady=12, anchor="w")

    def save(self, subj):
        bad = []
        for stu, (e, gl) in self.entries.items():
            v = e.get().strip()
            if v.isdigit() and 0 <= int(v) <= 100:
                MARKS[stu][subj] = int(v); gl.config(text=grade(int(v)))
            else:
                bad.append(stu)
        if bad: messagebox.showwarning("Invalid", f"Check marks for: {', '.join(bad)}")
        else:   messagebox.showinfo("Saved ✅", f"{subj} marks saved!")

    # ── TEACHER: VIEW ALL ─────────────────────────────────────────────────────
    def view_marks(self):
        tk.Label(self.pane, text="All Student Marks", font=FH, bg=BG, fg=TD).pack(anchor="w", padx=20, pady=(18,10))
        cols = ["Student"] + SUBJECTS + ["GPA"]
        tree = ttk.Treeview(self.pane, columns=cols, show="headings", height=12)
        for c in cols:
            tree.heading(c, text=c)
            tree.column(c, width=90 if c != "Student" else 150, anchor="center")
        for stu in STUDENTS:
            tree.insert("", "end", values=[stu] + [MARKS[stu].get(s,"—") for s in SUBJECTS] + [gpa(MARKS[stu])])
        tree.pack(fill="x", padx=20)

    # ── STUDENT: RESULTS ──────────────────────────────────────────────────────
    def results(self):
        name = self.user["name"]
        tk.Label(self.pane, text="My Results", font=FH, bg=BG, fg=TD).pack(anchor="w", padx=20, pady=(18,2))
        tk.Label(self.pane, text=f"Student: {name}", font=FN, bg=BG, fg=MU).pack(anchor="w", padx=20)

        marks = MARKS.get(name, {})
        hdr = tk.Frame(self.pane, bg=ACC); hdr.pack(fill="x", padx=20, pady=(12,0))
        for t, w in [("Subject",26),("Marks",14),("Grade",10),("Status",12)]:
            tk.Label(hdr, text=t, font=FB, bg=ACC, fg=W, width=w, anchor="w").pack(side="left", padx=8, pady=5)

        for i, (s, m) in enumerate(marks.items()):
            bg = W if i % 2 == 0 else "#EBF4FA"
            ok = "Pass" if m >= 60 else "Fail"
            fc = "#27AE60" if ok == "Pass" else "#E74C3C"
            row = tk.Frame(self.pane, bg=bg); row.pack(fill="x", padx=20, pady=1)
            tk.Label(row, text=s,        font=FN, bg=bg, fg=TD, width=26, anchor="w").pack(side="left", padx=8, pady=7)
            tk.Label(row, text=str(m),   font=FB, bg=bg, fg=TD, width=14, anchor="w").pack(side="left")
            tk.Label(row, text=grade(m), font=FB, bg=bg, fg=ACC,width=10, anchor="w").pack(side="left")
            tk.Label(row, text=ok,       font=FB, bg=bg, fg=fc, width=12, anchor="w").pack(side="left")

        foot = tk.Frame(self.pane, bg=W); foot.pack(fill="x", padx=20, pady=8)
        tk.Label(foot, text=f"  Semester GPA:  {gpa(marks)} / 4.00",
                 font=FH, bg=W, fg=ACC).pack(anchor="w", padx=10, pady=8)

    # ── NOTIFICATIONS ─────────────────────────────────────────────────────────
    def notifications(self):
        tk.Label(self.pane, text="🔔  Notifications", font=FH, bg=BG, fg=TD).pack(anchor="w", padx=20, pady=(18,8))
        for msg in NOTIFS:
            f = tk.Frame(self.pane, bg=W); f.pack(fill="x", padx=20, pady=4)
            tk.Frame(f, bg=ACC, width=4).pack(side="left", fill="y")
            tk.Label(f, text=msg, font=FN, bg=W, fg=TD, anchor="w", padx=12, pady=10).pack(side="left")


App().mainloop()
