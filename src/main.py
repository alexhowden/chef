import tkinter as tk
from tkinter import ttk
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

		diff1 = ttk.Button(self, text="3x2", width=0, command = lambda : controller.show_frame(MultDiff1))
		diff1.grid(row=1, column=1, padx=5, pady=10)

		diff2 = ttk.Button(self, text="4x2", width=0, command = lambda : controller.show_frame(MultDiff2))
		diff2.grid(row=2, column=1, padx=5, pady=10)

		diff3 = ttk.Button(self, text="3x3", width=0, command = lambda : controller.show_frame(MultDiff3))
		diff3.grid(row=3, column=1, padx=5, pady=10)

		diff4 = ttk.Button(self, text="4x3", width=0, command = lambda : controller.show_frame(MultDiff4))
		diff4.grid(row=4, column=1, padx=5, pady=10)

# 3x2 multiplication
class MultDiff1(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		titlebar = tk.Frame(self)
		titlebar.pack(fill="x", pady=10)

		back = ttk.Button(titlebar, text="<", width=0, command = lambda : controller.show_frame(DifficultyPage))
		back.pack(side="left", padx=10)

		label = ttk.Label(titlebar, text="3x2 Multiplication", font=BIGFONT)
		label.pack(side="top")

		a, b = generate_problem(3, 2)
		print(f"{a} x {b}")

		problem = tk.Frame(self)
		problem.pack(fill="both", expand=True, pady=20)

		problem.grid_columnconfigure(0, weight=1)
		problem.grid_columnconfigure(2, weight=1)
		problem.grid_rowconfigure(0, weight=1)
		problem.grid_rowconfigure(2, weight=1)

		content = tk.Frame(problem)
		content.grid(row=1, column=1)

		tally1 = ttk.Entry(content, font=REGFONT, width=1)
		tally1.grid(row=0, column=1)
		tally2 = ttk.Entry(content, font=REGFONT, width=1)
		tally2.grid(row=0, column=2)
		tally3 = ttk.Entry(content, font=REGFONT, width=1)
		tally3.grid(row=0, column=3)
		tally4 = ttk.Entry(content, font=REGFONT, width=1)
		tally4.grid(row=0, column=4)

		label_s1 = ttk.Label(content, text=' ', font=REGFONT, width=1, borderwidth=2, relief='solid')
		label_s1.grid(row=1, column=1)

		label_a1 = ttk.Label(content, text=a[0], font=REGFONT, width=1, borderwidth=2, relief='solid')
		label_a1.grid(row=1, column=2)

		label_a2 = ttk.Label(content, text=a[1], font=REGFONT, width=1, borderwidth=2, relief='solid')
		label_a2.grid(row=1, column=3)

		label_a3 = ttk.Label(content, text=a[2], font=REGFONT, width=1, borderwidth=2, relief='solid')
		label_a3.grid(row=1, column=4)

		label_x1 = ttk.Label(content, text='x', font=REGFONT, width=1, borderwidth=2, relief='solid')
		label_x1.grid(row=2, column=1)

		label_s1 = ttk.Label(content, text=' ', font=REGFONT, width=1, borderwidth=2, relief='solid')
		label_s1.grid(row=2, column=2)

		label_b1 = ttk.Label(content, text=b[0], font=REGFONT, width=1, borderwidth=2, relief='solid')
		label_b1.grid(row=2, column=3)

		label_b2 = ttk.Label(content, text=b[1], font=REGFONT, width=1, borderwidth=2, relief='solid')
		label_b2.grid(row=2, column=4)

		entry10 = ttk.Entry(content, font=REGFONT, width=1)
		entry10.grid(row=3, column=0)
		entry11 = ttk.Entry(content, font=REGFONT, width=1)
		entry11.grid(row=3, column=1)
		entry12 = ttk.Entry(content, font=REGFONT, width=1)
		entry12.grid(row=3, column=2)
		entry13 = ttk.Entry(content, font=REGFONT, width=1)
		entry13.grid(row=3, column=3)
		entry14 = ttk.Entry(content, font=REGFONT, width=1)
		entry14.grid(row=3, column=4)

		entry20 = ttk.Entry(content, font=REGFONT, width=1)
		entry20.grid(row=4, column=0)
		entry21 = ttk.Entry(content, font=REGFONT, width=1)
		entry21.grid(row=4, column=1)
		entry22 = ttk.Entry(content, font=REGFONT, width=1)
		entry22.grid(row=4, column=2)
		entry23 = ttk.Entry(content, font=REGFONT, width=1)
		entry23.grid(row=4, column=3)
		entry24 = ttk.Entry(content, font=REGFONT, width=1)
		entry24.grid(row=4, column=4)

		entry30 = ttk.Entry(content, font=REGFONT, width=1)
		entry30.grid(row=5, column=0)
		entry31 = ttk.Entry(content, font=REGFONT, width=1)
		entry31.grid(row=5, column=1)
		entry32 = ttk.Entry(content, font=REGFONT, width=1)
		entry32.grid(row=5, column=2)
		entry33 = ttk.Entry(content, font=REGFONT, width=1)
		entry33.grid(row=5, column=3)
		entry34 = ttk.Entry(content, font=REGFONT, width=1)
		entry34.grid(row=5, column=4)

# 4x2 multiplication
class MultDiff2(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		label = ttk.Label(self, text="4x2 Multiplication", font=BIGFONT)
		label.grid(row=0, column=4, padx=10, pady=10)

		back = ttk.Button(self, text="<", width=0, command = lambda : controller.show_frame(DifficultyPage))
		back.grid(row=0, column=1, padx=10, pady=10)

		a, b = generate_problem(4, 2)
		print(f"{a} x {b}")

# 3x3 multiplication
class MultDiff3(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		label = ttk.Label(self, text="3x3 Multiplication", font=BIGFONT)
		label.grid(row=0, column=4, padx=0, pady=10)

		back = ttk.Button(self, text="<", width=0, command = lambda : controller.show_frame(DifficultyPage))
		back.grid(row=0, column=1, padx=10, pady=10)

		a, b = generate_problem(3, 3)
		print(f"{a} x {b}")

# 4x3 multiplication
class MultDiff4(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		label = ttk.Label(self, text="4x3 Multiplication", font=BIGFONT)
		label.grid(row=0, column=4, padx=10, pady=10)

		back = ttk.Button(self, text="<", width=0, command = lambda : controller.show_frame(DifficultyPage))
		back.grid(row=0, column=1, padx=10, pady=10)

		a, b = generate_problem(4, 3)
		print(f"{a} x {b}")

def generate_problem(a: int, b: int):
	str_a = str(randrange(pow(10, a -1), pow(10, a), 1))
	str_b = str(randrange(pow(10, b - 1), pow(10, b), 1))
	return str_a, str_b

if __name__ == "__main__":
	app = App()
	app.mainloop()
