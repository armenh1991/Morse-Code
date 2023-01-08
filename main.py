from morse_letters import letter_list

user_word = input("Write your word: ").lower()

# Convert user_word to morse code.

converted_word = ''

for letter in user_word:
    new_word = letter_list[letter]
    converted_word += new_word + ' '


print(f"Your word converted to morse code is: {converted_word}")










