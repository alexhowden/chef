import tkinter as tk
from tkinter import ttk
from tkinter import *
from random import randrange

BIGFONT = ("Courier New", 35)
REGFONT = ("Helvecta", 22)

class App(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)

		self.geometry("700x500")

		container = ttk.Frame(self)
		container.pack(side="top", fill="both", expand=True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for f in (DifficultyPage, MultDiff1, MultDiff2, MultDiff3, MultDiff4):
			frame = f(container, self)
			self.frames[f] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(DifficultyPage)

		style = ttk.Style(self)

		style.map("TButton", foreground=[('active', 'blue')])

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

class DifficultyPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		label = ttk.Label(self, text="Select Your Difficulty", font=BIGFONT)
		label.grid(row=0, column=4, padx=10, pady=10)

		diffs = [MultDiff1, MultDiff2, MultDiff3, MultDiff4]
		diffs_text = ["3x2", "4x2", "3x3", "4x3"]

		for i in range(len(diffs)):
			ttk.Button(self, text=diffs_text[i], width=0, command = lambda i=i: controller.show_frame(diffs[i])).grid(row=i+1, column=1, padx=5, pady=10)

# 3x2 multiplication
class MultDiff1(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		titlebar = tk.Frame(self)
		titlebar.pack(fill="x", pady=10)

		ttk.Button(titlebar, text="<", width=0, command = lambda : controller.show_frame(DifficultyPage)).pack(side="left", padx=10)
		ttk.Label(titlebar, text="3x2 Multiplication", font=BIGFONT).pack(side="top")

		a, b = generate_problem(3, 2)
		print(f"{a} x {b}")

		problem = Problem(self, a, b)
		problem.pack(fill="both", expand=True, pady=20)

# 4x2 multiplication
class MultDiff2(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		titlebar = tk.Frame(self)
		titlebar.pack(fill="x", pady=10)

		ttk.Button(titlebar, text="<", width=0, command = lambda : controller.show_frame(DifficultyPage)).pack(side="left", padx=10)
		ttk.Label(titlebar, text="4x2 Multiplication", font=BIGFONT).pack(side="top")

		a, b = generate_problem(4, 2)
		print(f"{a} x {b}")

		problem = Problem(self, a, b)
		problem.pack(fill="both", expand=True, pady=20)

# 3x3 multiplication
class MultDiff3(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		titlebar = tk.Frame(self)
		titlebar.pack(fill="x", pady=10)

		ttk.Button(titlebar, text="<", width=0, command = lambda : controller.show_frame(DifficultyPage)).pack(side="left", padx=10)
		ttk.Label(titlebar, text="3x3 Multiplication", font=BIGFONT).pack(side="top")

		a, b = generate_problem(3, 3)
		print(f"{a} x {b}")

		problem = Problem(self, a, b)
		problem.pack(fill="both", expand=True, pady=20)

# 4x3 multiplication
class MultDiff4(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		titlebar = tk.Frame(self)
		titlebar.pack(fill="x", pady=10)

		ttk.Button(titlebar, text="<", width=0, command = lambda : controller.show_frame(DifficultyPage)).pack(side="left", padx=10)
		ttk.Label(titlebar, text="4x3 Multiplication", font=BIGFONT).pack(side="top")

		a, b = generate_problem(4, 3)
		print(f"{a} x {b}")

		problem = Problem(self, a, b)
		problem.pack(fill="both", expand=True, pady=20)

class Problem(tk.Frame):
	def __init__(self, parent, a, b):
		tk.Frame.__init__(self, parent)

		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(2, weight=1)
		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(2, weight=1)

		content = tk.Frame(self)
		content.grid(row=1, column=1)

		num_cols = len(a) + len(b)
		val_cmd = (self.register(validate_entry), '%P')

		tallies = []
		for c in range(num_cols - len(a) - 1, num_cols - 1):
			tally = ttk.Entry(content, font=REGFONT, width=1, validate="key", validatecommand=val_cmd)
			tally.grid(row=0, column=c)
			tallies.append(tally)

		match len(a):
			case 3:
				seq_a = [' ', *a]
			case 4:
				seq_a = [*a]

		seq_b = ['x', ' ', *b]

		for c, val in enumerate(seq_a):
			ttk.Label(content, text=val, font=REGFONT, width=1).grid(row=1, column=c+(num_cols-len(seq_a)))

		for c, val in enumerate(seq_b):
			ttk.Label(content, text=val, font=REGFONT, width=1).grid(row=2, column=c+(num_cols-len(seq_b)))

		entries = []
		for r in range(3, len(b) + 4):
			for c in range(num_cols):
				entry = ttk.Entry(content, font=REGFONT, width=1, validate="key", validatecommand=val_cmd)
				entry.grid(row=r, column=c)
				entries.append(entry)

def validate_entry(I):
	return (I.isdigit() and len(I) == 1) or (I == "")

def generate_problem(a: int, b: int):
	str_a = str(randrange(pow(10, a -1), pow(10, a), 1))
	str_b = str(randrange(pow(10, b - 1), pow(10, b), 1))
	return str_a, str_b

if __name__ == "__main__":
	app = App()
	app.mainloop()

