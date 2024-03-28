import random

players = ["John", "Clark", "Eddie", "Alex", "Dan", "Niru", "Albert", 
           "Bill", "Kwong", "Max", "Leo", "Ray", "George"]

team_1 = []
team_2 = []

while True:
  try:
      players_attending = int(input("Number of players: "))
      if 2 <= players_attending <= len(players):
          break
      print(f"Please enter a number between 2 and {len(players)}.")
  except ValueError:
      print("Please enter a valid integer.")

team_size = players_attending / 2
    
while len(team_1) < team_size:

  selected_player = random.choice(players)
  team_1.append(selected_player)
  players.remove(selected_player)
  
  second_selected_player = random.choice(players)
  team_2.append(second_selected_player)
  players.remove(second_selected_player)

print(f"Team 1: {', '.join(team_1)}")
print(f"Team 2: {', '.join(team_2)}")