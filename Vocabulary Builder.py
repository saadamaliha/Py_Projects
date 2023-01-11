"""
This program is a vocabulary learning tool that helps users practice and memorize advanced English words and their meanings. It uses a list of tuples, called vocab, that contains a set of 50 advanced English words and their corresponding meanings. The program imports the random module, which is used to randomly select a word and its definition from the vocab list.

The program then enters into an infinite loop (while True) in which it randomly selects a word and its definition from
the vocab list. The definition is then printed to the console for the user to see.
The user is then prompted to guess the word, and their response is stored in the variable guess.

The program then checks the value of guess using an if-elif-else statement:

If the user's guess is equal to the string 'quit', the program exits the while loop and the program ends.
If the user's guess is equal to the word, the program prints "Correct!" to the console.
If the user's guess is neither 'quit' nor correct, the program prints "Incorrect, the correct word is "
followed by the correct word.

After the above process, the program restarts the loop again and continues until the user types 'quit' for it to exit.
"""
import random

# creating a list of words and definitions as a tuple
vocab = [
    ("cryptic", "hidden"),
    ("currency", "widespread acceptance, 2. money"),
    ("decorous", "good and correct (used of behavior)"),
    ("denunciation", "act of speaking out against"),
    ("derailed", "thrown off course"),
    ("derivative", "unoriginal"),
    ("despotic", "acting like a tyrant"),
    ("detritus", "rubbish"),
    ("diaphanous", "very thin and transparent"),
    ("dictum", "often-used saying"),
    ("dilettante", "person who dabbles in the arts"),
    ("disdained", "showed contempt for"),
    ("dispassionate", "unbiased; fair"),
    ("dowager", "an elderly woman of elevated social status"),
    ("dubious", "doubtful"),
    ("egalitarian", "equal; believer in equality"),
    ("elicit", "draw out (used mainly for information or feelings)"),
    ("elliptical", "1. shaped like an ellipse, 2. indirect"),
    ("epitomizes", "acts as a typical example of"),
    ("equivocate", "speak ambiguously/vaguely"),
    ("evasiveness", "trying to avoid something"),
    ("explicitly", "very clear; nothing hidden"),
    ("foraging", "searching for food"),
    ("hypothetical", "based on guesswork; not proven"),
    ("iconoclast", "person who goes against accepted authority"),
    ("idiosyncratic", "quirky; unique to an individual"),
    ("imponderable", "cannot be understood"),
    ("indecorous", "not well-behaved; lacking in dignity"),
    ("indigence", "extreme poverty"),
    ("inept", "clumsy"),
    ("inherent", "inbuilt; genetic"),
    ("intricate", "complicated"),
    ("irrefutable", "cannot be proved wrong"),
    ("jingoism", "using words to stir up exaggerated patriotism"),
    ("jubilant", "joyful"),
    ("judicious", "fair and equal"),
    ("lament", "express regret over something"),
    ("loquacious", "talkative; using too many words"),
    ("mendicancy", "begging"),
    ("metaphorical", "not literal; figurative"),
    ("milieu", "environment; surroundings"),
    ("mitigated", "made less severe"),
    ("nascent", "just begun; in an early stage of development"),
    ("nostalgia", "longing for the past"),
    ("obtrusive", "easily seen"),
    ("orthographical", "concerned with writing and spelling"),
    ("ossified", "become fixed and rigid"),
    ("ostentatious", "showy"),
    ("palpable", "can be felt"),
    ("pastoral", "1. concerned with the countryside, 2. concerned with the care a pastor gives to someone"),
    ("pedestrian", "1. boring (adj), 2. person who walks (n)"),
    ("perfidy", "treachery; betrayal"),
    ("profligacy", "wasteful")
]

while True:
    # randomly selecting a word and its definition
    word, definition = random.choice(vocab)
    print("Definition: " + definition)

    # prompting the user to guess the word
    guess = input("Guess the word: ")

    if guess == 'quit':
        break
    elif guess == word:
        print("Correct!")
    else:
        print("Incorrect, the correct word is " + word)
