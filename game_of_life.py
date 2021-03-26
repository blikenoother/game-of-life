from cmd import Cmd
import copy

class GameOfLife(Cmd):

	def __init__(self, grid):
		self.grid = grid
		self.generation = 0

	def display(self):
		print(f'Generation-{self.generation}')
		for row in self.grid:
			print(''.join([str(x) for x in row]).replace('0', '.').replace('1', '*'))

	def next_gen(self):
		next_gen_grid = copy.copy(self.grid)

		grid_len = len(self.grid)
		for i in range(0, grid_len):
			row_len = len(self.grid[i])
			for j in range(0, row_len):
				total = self.grid[i][(j-1)%row_len] + self.grid[i][(j+1)%row_len] + self.grid[(i-1)%grid_len][j] + self.grid[(i+1)%grid_len][j] + self.grid[(i-1)%grid_len][(j-1)%row_len] + self.grid[(i-1)%grid_len][(j+1)%row_len] + self.grid[(i+1)%grid_len][(j-1)%row_len] + self.grid[(i+1)%grid_len][(j+1)%row_len]

				if self.grid[i][j] == 1:
					if total < 2 or total > 3:
						next_gen_grid[i][j] = 0
				elif total == 3:
					next_gen_grid[i][j] = 1
				else:
					next_gen_grid[i][j] = self.grid[i][j]

		self.generation += 1
		self.grid = next_gen_grid

class PromptInput(Cmd):
	game_name = "GAME OF LIFE"
	prompt = f"""({game_name} -> 'default' or 'grid 5 10')$ """

	def do_default(self, params):
		grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ],
				[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
		self.game_of_life = GameOfLife(grid)
		self.game_of_life.display()
		self.prompt = f"({self.game_name} -> 'next_gen')$ "

	def do_grid(self, params):
		grid = []
		grid_len, row_len = int(params.split(' ')[0]), int(params.split(' ')[1])
		i = 0
		while i != grid_len:
			row = str(input(f'Enter row-{i} (Only 0 or 1) -> '))
			row = [int(x) for x in row]
			if len(row) != row_len:
				print(f'length must be: {row_len}')
				continue
			grid.append(row)
			i += 1
		self.game_of_life = GameOfLife(grid)
		self.game_of_life.display()
		self.prompt = f"({self.game_name} -> 'next_gen')$ "

	def do_next_gen(self, params):
		self.game_of_life.next_gen()
		self.game_of_life.display()

	def do_exit(self, inp):
		return True

def main():
	PromptInput().cmdloop()

if __name__ == "__main__":
	main()

