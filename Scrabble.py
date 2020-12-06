letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letters_lowercase = [i.lower() for i in letters]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

points_per_letter_upper = {key:value for key, value in zip(letters, points)}
points_per_letter_lower = {key:value for key, value in zip(letters_lowercase, points)}

def merge(dict1, dict2):
  dict1.update(dict2)
  return dict1

points_per_letter = merge(points_per_letter_upper, points_per_letter_lower)

points_per_letter[' '] = 0

def score_word(word):
  point_total = 0
  for letter in word:
    point_total = point_total + points_per_letter.get(letter, 0)
  return point_total

player_words_played = {'p1': [], 'p2': [], 'p3': [], 'p4': []}
def update_player_words(player, word):
  player_words_played[player].append(word)

player_points = {}
def update_points():
  for player, words in player_words_played.items():
    points = 0
    for word in words:
      points = points + score_word(word)
    player_points[player] = points

def main():
  player_name = input('player? ')
  word_played = input('word? ')
  update_player_words(player_name, word_played)
  update_points()
  print(player_points)
while True:
  main()