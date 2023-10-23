instructions = """Please read general instructions carefully:\n
           1.The game is played on a 3*3 grid 
                           
                     1 | 2 | 3
                    ---|---|---
                     4 | 5 | 6
                    ---|---|---  
                     7 | 8 | 9
                    
           2.Choose your symbol(X or O)
           3.Choose number to place a symbol(1-9)
           4.The player who get 3 of his/her marks in a row (up, down, across, or diagonally) is the winner."""

grid = []

for i in range(9):
  grid.append(' ')

def print_board(grid):
  board = f"""

   {grid[0]} | {grid[1]} | {grid[2]}
  ---|---|---
   {grid[3]} | {grid[4]} | {grid[5]}
  ---|---|---
   {grid[6]} | {grid[7]} | {grid[8]}

  """
  print(board)

index_list = []
def take_input(player_name):
  while True:
    spot = int(input(f'{player_name}: '))
    spot -= 1
    if 0 <= spot < 10:
      if spot in index_list:
        print('This spot is already occupied.')
        continue
      index_list.append(spot)  
      return spot
    print('Please Enter number between 1-9')

def result_calculation(grid, player1, player2):
  if grid[0] == grid[1] == grid[2] == 'X' or grid[1] == grid[4] == grid[7] == 'X' or grid[0] == grid[4] == grid[8] == 'X' or grid[2] == grid[5] == grid[8] == 'X' or grid[3] == grid[4] == grid[5] == 'X' or grid[2] == grid[4] == grid[6] == 'X' or grid[6] == grid[7] == grid[8] == 'X' or grid[0] == grid[3] == grid[6] == 'X' :
    print(f'Hurrah!!!{player1} won the match.!!')
    quit('Thank you both for joining')
  elif grid[0] == grid[1] == grid[2] == 'O' or grid[1] == grid[4] == grid[7] == 'O' or grid[0] == grid[4] == grid[8] == 'O' or grid[2] == grid[5] == grid[8] == 'O' or grid[3] == grid[4] == grid[5] == 'O' or grid[2] == grid[4] == grid[6] == 'O' or grid[6] == grid[7] == grid[8] == 'O' or grid[0] == grid[3] == grid[6] == 'O' :
    print(f'Hurrah!!!{player2} won the match.!!')
    quit('Thank you both for joining')
  else:
    return

def main():
  print("                   Welcome to tic tac toe game.!!             ")
  player1 = input("Enter player 1 name: ")
  player2 = input("Enter player 2 name: ")
  print(f"\nWelcome {player1} and {player2}!!!")
  print(instructions)
  print(f"{player1}'s symbol is - X")
  print(f"{player2}'s symbol is - O")
  input("\nEnter any key to start the game: ")
  print_board(grid)
  for i in range(0,9):
    if i%2 == 0:
      index = take_input(player1)
      grid[index] = 'X'
    else:
      index = take_input(player2)
      grid[index] = 'O'

    print_board(grid)
    result_calculation(grid, player1, player2)
    
    print("This is a tie..!! Nobody won. Play Again.")
main()
