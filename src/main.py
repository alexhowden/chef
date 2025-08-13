import tkinter as tk
from tkinter import ttk

FONT = ("Courier New", 35)

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

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

class DifficultyPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		label = ttk.Label(self, text="Select Your Difficulty", font=FONT)
		label.grid(row=0, column=4, padx=10, pady=10)

		diff1 = ttk.Button(self, text="3x2", command = lambda : controller.show_frame(MultDiff1))
		diff1.grid(row=1, column=1, padx=10, pady=10)

		diff2 = ttk.Button(self, text="4x2", command = lambda : controller.show_frame(MultDiff2))
		diff2.grid(row=2, column=1, padx=10, pady=10)

		diff3 = ttk.Button(self, text="3x3", command = lambda : controller.show_frame(MultDiff3))
		diff3.grid(row=3, column=1, padx=10, pady=10)

		diff4 = ttk.Button(self, text="4x3", command = lambda : controller.show_frame(MultDiff4))
		diff4.grid(row=4, column=1, padx=10, pady=10)

# 3x2 multiplication
class MultDiff1(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		label = ttk.Label(self, text="3x2 Multiplication", font=FONT)
		label.grid(row=0, column=4, padx=10, pady=10)

		back = ttk.Button(self, text="<", command = lambda : controller.show_frame(DifficultyPage))
		back.grid(row=0, column=1, padx=10, pady=10)

# 4x2 multiplication
class MultDiff2(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		label = ttk.Label(self, text="4x2 Multiplication", font=FONT)
		label.grid(row=0, column=4, padx=10, pady=10)

		back = ttk.Button(self, text="<", command = lambda : controller.show_frame(DifficultyPage))
		back.grid(row=0, column=1, padx=10, pady=10)

# 3x3 multiplication
class MultDiff3(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		label = ttk.Label(self, text="3x3 Multiplication", font=FONT)
		label.grid(row=0, column=4, padx=0, pady=10)

		back = ttk.Button(self, text="<", width=0, command = lambda : controller.show_frame(DifficultyPage))
		back.grid(row=0, column=1, padx=10, pady=10)

# 4x3 multiplication
class MultDiff4(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		label = ttk.Label(self, text="4x3 Multiplication", font=FONT)
		label.grid(row=0, column=4, padx=10, pady=10)

		back = ttk.Button(self, text="<", command = lambda : controller.show_frame(DifficultyPage))
		back.grid(row=0, column=1, padx=10, pady=10)


if __name__ == "__main__":
	app = App()
	app.mainloop()
