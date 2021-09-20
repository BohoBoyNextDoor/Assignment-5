OLD_POINT_STRUCTURE = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in old_point_structure:

            if char in old_point_structure[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints



def initial_prompt():
   print("Let's play some Scrabble!\n")
   user_input = input("Please enter a word to be scored <3 :")
   return user_input

def simple_scorer(word):
    score = 0

    for char in word.lower():
        score += 1

    return score

def vowel_bonus_scorer(word):
    vowels = 'aeiou'
    score = 0

    for char in word.lower():
        point = 3 if char in vowels else 1
        score += point

    return score

def scrabble_scorer(word):
    score = 0

    for char in word.lower():
        if char in new_point_structure:
            score += new_point_structure[char]

    return score

scoring_algorithms = ()

def scorer_prompt():
    score_prompt = 'Which scoring alogorithm should we use this time?'
    user_selection = 3
    while user_selection > 2:
        for index, algorithm in enumerate(scoring_algorithms):
            print(f'{index} - {algorithm["name"]}: {algorithm["description"]}')

        user_selection = int(input('Enter 0, 1, or 2:'))

    selected_score_algorithm_dict = scoring_algorithms[user_selection]

    return selected_score_algorithm_dict

def transform(provided_dict):
    new_dict = {}

    for (key, value) in provided_dict.items():
        for letter in value:
            new_dict[letter.lower()] = key

    return new_dict

new_point_structure = transform(old_point_structure)

simple_scorer_dict = {
    'name': 'Simple',
    'description': 'This scoring structure grades each letter as worth one point.',
    'score_function': simple_scorer


}

vowel_bonus_scorer_dict = {
    'name': 'Bonus Vowels',
    'description': 'This paradigm priotizes vowels, with vowels being worth 3 points whilst consonants are worth 1',
    'score_function': vowel_bonus_scorer
}

old_scrabble_scorer_dict = {
    'name': 'Scrabble',
    'description': 'Traditional typical usual rules; nothing fancy here',
    'score_function': scrabble_scorer
}


scoring_algorithms = (
    simple_scorer_dict,
    vowel_bonus_scorer_dict,
    old_scrabble_scorer_dict
)

def run_program():
    word = initial_prompt()
    selected_score_algorithm_dict = scorer_prompt()

    score = selected_score_algorithm_dict['score_function'](word)

    print(
        f'''
Perfect! The entered word was "{word}", and you chose to use the "{selected_score_algorithm_dict["name"]}" 
scoring algorithm which grades by {selected_score_algorithm_dict["description"]}.
Therefor, your word is worth {score} points! Thanks so much for playing! <3'''
    )
