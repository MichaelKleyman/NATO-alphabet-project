import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter : row.code for (index, row) in data.iterrows()}

user_input = input("Enter a word: ").upper()
list = [dict[letter] for letter in user_input]
print(list)

