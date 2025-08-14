from random import randrange

def test():
	valid = False
	while not valid:
		nums = input("Enter your equation (ex: 1024x48): ")

		try:
			a, b = nums.split("x")
			if int(a) and int(b):
				valid = True
		except ValueError:
			pass

	print(f"""

	{a.rjust(len(b) + 2)}
	x {b.rjust(max(0, len(a) - len(b) - 1))}
	{"–" * max(len(a), len(b) + 2)}

	""")

	int_a = int(a)
	int_b = int(b)

	solved = False
	while not solved:
		next_a = int_a % 10
		next_b = int_b % 10

		calc = next_a * next_b
		print(f"calc: {calc}")

		correct = False
		while not correct:
			try:
				val = input(f"{next_a} x {next_b}: ")
				correct = int(val) == calc
			except ValueError:
				pass

		int_a = int(int_a / 10)
		if int_a == 0:
			int_b = int(int_b / 10)
			int_a = int(a)

			if int_b == 0:
				solved = True

	print("solved!")

def generate_problem(a: int, b: int):
	return randrange(pow(10, a - 1), pow(10, a), 1), randrange(pow(10, b - 1), pow(10, b), 1)

# print(generate_problem(4, 3))





def solve(a, b):
	num_cols = len(a) + len(b)
	solution = []
	zeros = 0
	for dig_b in b[::-1]:
		for x in range(zeros):
			solution.append(0)
		tally = 0
		for dig_a in a[::-1]:
			print(dig_b, dig_a)
			prod = int(dig_a) * int(dig_b)
			added = (prod + tally) % 10
			solution.append(added)
			tally = int((prod + tally) / 10)
			print("prod: ", prod)
			print("tally: ", tally)
			print("added: ", added)
		solution.append(tally)
		zeros += 1
		while len(solution) % num_cols != 0:
			solution.append(0)

	print(solution)

solve("409", "72")
