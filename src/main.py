import tkinter as tk
from tkinter import ttk
from random import randrange
import json
import time

FONT_TITLE = ('Courier New', 35)
FONT_CONTENT = ('Courier New', 22)

DIFFICULTIES = [
	(3,2),
	(4,2),
	(3,3),
	(4,3)
]

class App(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)

		self.title('chef')
		self.geometry('800x550')

		container = ttk.Frame(self)
		container.pack(side='top', fill='both', expand=True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for f in (DifficultyPage, StatsPage):
			frame = f(container, self)
			self.frames[f] = frame
			frame.grid(row=0, column=0, sticky='nsew')

		for len_a, len_b in DIFFICULTIES:
			frame = MultiplicationPage(container, self, len_a, len_b)
			self.frames[f'Mult_{len_a}x{len_b}'] = frame
			frame.grid(row=0, column=0, sticky='nsew')

		self.show_frame(DifficultyPage)

		style = ttk.Style(self)
		style.configure('TButton', font=FONT_CONTENT)
		style.map('TButton', foreground=[('active', 'blue')])

	def show_frame(self, cont):
		frame = self.frames[cont]
		if cont == StatsPage:
			frame.refresh()
		frame.tkraise()

class DifficultyPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(2, weight=1)
		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(6, weight=1)

		label = ttk.Label(self, text='Select Your Difficulty', font=FONT_TITLE)
		label.grid(row=0, column=1, padx=10, pady=10)

		for i in range(len(DIFFICULTIES)):
			a, b = DIFFICULTIES[i]
			ttk.Button(self, text=f'{a}x{b}', command = lambda f=f'Mult_{a}x{b}': controller.show_frame(f)).grid(row=i+1, column=1, padx=5, pady=10)

		ttk.Button(self, text='Stats', command = lambda : controller.show_frame(StatsPage)).grid(row=5, column=1, padx=5, pady=10)

class StatsPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		self.controller = controller

		titlebar = tk.Frame(self)
		titlebar.pack(fill='x', pady=25)

		data = self.retrieve()

		ttk.Button(titlebar, text='<', width=0, command = lambda : self.controller.show_frame(DifficultyPage)).pack(side='left', padx=10)
		ttk.Label(titlebar, text=f'Stats for {data['username']}', font=FONT_TITLE).pack(side='top')

		stats = tk.Frame(self)
		stats.pack(fill='both', expand=True, pady=20)

		stats.grid_columnconfigure(0, weight=1)
		stats.grid_columnconfigure(2, weight=1)
		stats.grid_rowconfigure(0, weight=1)
		stats.grid_rowconfigure(2, weight=1)

		self.content = tk.Frame(stats)
		self.content.grid(row=1, column=1, padx=10, pady=10)

	def refresh(self):
		user_data = self.retrieve()

		labels = {}

		label = ttk.Label(self.content, text=f'Balance: {user_data['balance']}', font=FONT_CONTENT)
		label.grid(row=0, column=0, padx=10, pady=10)
		labels['balance'] = label

		row = 1
		for key, value in user_data.items():
			if key.endswith('answered'):
				label = ttk.Label(self.content, text=f'{key[0:3]} Questions Answered: {value}', font=FONT_CONTENT)
				label.grid(row=row, column=0, padx=10, pady=10)
				labels[key] = label
				row += 1

	def retrieve(self):
		try:
			with open('./src/user_data.json', 'r') as f:
				user_data = json.load(f)
		except FileNotFoundError:
			user_data = { "username": "kid", "3x2_answered": 0, "4x2_answered": 0, "3x3_answered": 0, "4x3_answered": 0, "balance": 0 }
		return user_data

class MultiplicationPage(tk.Frame):
	def __init__(self, parent, controller, len_a, len_b):
		tk.Frame.__init__(self, parent)

		titlebar = tk.Frame(self)
		titlebar.pack(fill='x', pady=25)

		ttk.Button(titlebar, text='<', width=0, command = lambda : controller.show_frame(DifficultyPage)).pack(side='left', padx=10)
		ttk.Label(titlebar, text=f'{len_a}x{len_b} Multiplication', font=FONT_TITLE).pack(side='top')

		a, b = generate_problem(len_a, len_b)
		self.problem = Problem(self, a, b)
		self.problem.pack(fill='both', expand=True, pady=20)

	def new_problem(self, len_a, len_b):
		try:
			with open('./src/user_data.json', 'r') as f:
				user_data = json.load(f)
		except FileNotFoundError:
			user_data = { "username": "kid", "3x2_answered": 0, "4x2_answered": 0, "3x3_answered": 0, "4x3_answered": 0, "balance": 0 }

		dim = f'{len_a}x{len_b}'
		user_data[f'{dim}_answered'] += 1
		match dim:
			case '3x2':
				user_data['balance'] += .01
			case '4x2':
				user_data['balance'] += .02
			case '3x3':
				user_data['balance'] += .03
			case '4x3':
				user_data['balance'] += .04

		with open('./src/user_data.json', 'w') as f:
			json.dump(user_data, f)

		self.problem.destroy()
		a, b = generate_problem(len_a, len_b)
		self.problem = Problem(self, a, b)
		self.problem.pack(fill='both', expand=True, pady=20)
		self.problem.update_idletasks()

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
		solution = solve(a, b)
		focus = 0

		tallies = []
		for c in range(num_cols - len(a) - 1, num_cols - 1):
			tally = ttk.Entry(content, font=FONT_CONTENT, width=1, validate='key', validatecommand=val_cmd)
			tally.grid(row=0, column=c)
			tallies.append(tally)

		seq_a = [*a]
		seq_b = ['x', ' ', *b]
		for c, val in enumerate(seq_a):
			ttk.Label(content, text=val, font=FONT_CONTENT, width=1).grid(row=1, column=c+(num_cols-len(seq_a)))
		for c, val in enumerate(seq_b):
			ttk.Label(content, text=val, font=FONT_CONTENT, width=1).grid(row=2, column=c+(num_cols-len(seq_b)))

		entries = []
		checks = []
		for r in range(3, len(b) + 4):
			infocus = focus + 3 == r

			for c in range(num_cols):
				entry = ttk.Entry(content, font=FONT_CONTENT, width=1, validate='key', validatecommand=val_cmd, state='normal' if infocus else 'disabled')
				entry.grid(row=r, column=c)
				entries.append(entry)

			check = tk.Label(content, text='>' if infocus else '', font=FONT_CONTENT, width=1, background='blue' if infocus else content['background'], padx=2)
			check.grid(row=r, column=num_cols)
			check.bind('<Button-1>', lambda event, row=r-3: check_row(event, row)) if infocus else check.unbind('<Button-1>')
			checks.append(check)

		def check_row(event, row):
			nonlocal focus
			for i in range((row + 1) * num_cols - 1, row * num_cols - 1, -1):
				sol_ind = (num_cols * (1 + row * 2) - 1) - i
				user_val = 0 if entries[i].get() == '' else int(entries[i].get())

				if solution[sol_ind] != int(user_val):
					checks[focus].config(background='red')
					return

			checks[focus].config(background='green')
			checks[focus].unbind('<Button-1>')

			[t.delete(0, tk.END) for t in tallies]

			for c in range(num_cols):
				entries[focus * num_cols + c].config(state='disabled')
				if focus != len(b):
					entries[(focus + 1) * num_cols + c].config(state='normal')

			if focus == len(b):
				parent.new_problem(len(a), len(b))
				return

			focus += 1

			checks[focus].config(text='>', background='blue')
			checks[focus].bind('<Button-1>', lambda event, row=focus: check_row(event, row))

def validate_entry(I):
	return (I.isdigit() and len(I) == 1) or (I == '')

def generate_problem(a: int, b: int):
	str_a = str(randrange(pow(10, a -1), pow(10, a), 1))
	str_b = str(randrange(pow(10, b - 1), pow(10, b), 1))
	return str_a, str_b

def solve(a, b):
	num_cols = len(a) + len(b)
	solution = []
	zeros = 0
	for dig_b in b[::-1]:
		for x in range(zeros):
			solution.append(0)
		tally = 0
		for dig_a in a[::-1]:
			prod = int(dig_a) * int(dig_b)
			added = (prod + tally) % 10
			solution.append(added)
			tally = int((prod + tally) / 10)
		solution.append(tally)
		zeros += 1
		while len(solution) % num_cols != 0:
			solution.append(0)

	product = int(a) * int(b)
	product = str(product)
	for c in product[::-1]:
		solution.append(int(c))
	while len(solution) % num_cols != 0:
		solution.append(0)

	return solution

if __name__ == '__main__':
	app = App()
	app.mainloop()

