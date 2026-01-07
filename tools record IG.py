import tkinter as tk
from tkinter import messagebox
import csv
import random
import time
from datetime import datetime
import threading

CSV_FILE = "ig_follow_log.csv"
MIN_DELAY = 0   # 2 menit
MAX_DELAY = 0   # 8 menit

class IGFollowTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("IG Manual Follow Tracker (SAFE)")
        self.root.geometry("520x420")
        self.root.resizable(False, False)

        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        tk.Label(self.root, text="Instagram Manual Follow Tracker",
                 font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self.root, text="Username IG yang baru difollow:").pack()
        self.username_entry = tk.Entry(self.root, width=30)
        self.username_entry.pack(pady=5)

        self.save_btn = tk.Button(self.root, text="Save & Start Timer",
                                  command=self.save_and_timer)
        self.save_btn.pack(pady=8)

        self.timer_label = tk.Label(self.root, text="Timer: -",
                                    font=("Arial", 12), fg="blue")
        self.timer_label.pack(pady=5)

        tk.Label(self.root, text="Follow Log:").pack(pady=5)

        self.listbox = tk.Listbox(self.root, width=65, height=10)
        self.listbox.pack()

    def save_and_timer(self):
        username = self.username_entry.get().strip()
        if not username:
            messagebox.showwarning("Warning", "Username tidak boleh kosong")
            return

        now = datetime.now()
        data = [username,
                now.strftime("%Y-%m-%d"),
                now.strftime("%H:%M:%S"),
                "Followed"]

        with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(data)

        self.listbox.insert(tk.END, f"{data[1]} {data[2]} | {username} | Followed")
        self.username_entry.delete(0, tk.END)

        delay = random.randint(MIN_DELAY, MAX_DELAY)
        threading.Thread(target=self.start_timer, args=(delay,), daemon=True).start()

    def start_timer(self, delay):
        self.save_btn.config(state="disabled")
        for remaining in range(delay, 0, -1):
            mins, secs = divmod(remaining, 60)
            self.timer_label.config(
                text=f"Timer: {mins} menit {secs} detik")
            time.sleep(1)

        self.timer_label.config(text="Timer: Selesai, silakan follow lagi ✅")
        self.save_btn.config(state="normal")

    def load_data(self):
        try:
            with open(CSV_FILE, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    self.listbox.insert(
                        tk.END, f"{row[1]} {row[2]} | {row[0]} | {row[3]}")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    app = IGFollowTracker(root)
    root.mainloop()
