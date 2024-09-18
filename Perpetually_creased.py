import random
import textwrap
"""This program generates a different poem at each run by randomly deleting
and joining certain lines but keeping the first and last line the same every time"""

# List of lines for the poem

text = [
    "My plants are dying. It’s not a metaphor; it’s a fact",
    "I see the plants every morning by the side of my bed",
    "I see the plants withering, slowly",
    "I close my eyes; let the familiar darkness swallow me",
    "The clocks ticking, alarms blaring",
    "I know I’ve set alarms, every ten minutes for an hour",
    "Tick tock tick tock tick",
    "I hear the time mocking me",
    "I slept too long",
    "How long has it been? 10 hours? 12?",
    "I should get up",
    "Work has to be done, studies waiting",
    "I hear the time mocking me",
    "Tick tock tick tock",
    "I try the bulb again, it’s a futile fight",
    "For the hundredth time, the switch does nothing right",
    "It’s not new",
    "Remember? My plants are dying",
    "I look into the mirror",
    "My eyes are puffy and swarthy",
    "My forehead, a firework of spots on a beige sky",
    "It’s no surprise",
    "You know, my plants are dying",
    "I get ready, 13 minutes exactly, always",
    "Hair pulled back as usual, creased but ok",
    "I wait for the bus",
    "The same guy with a navy cap keeps me company",
    "I steal a quick glimpse, my heartbeats doubling their rate for seconds. I count-",
    "1 2 3 4",
    "5. The bus arrives",
    "I’m running late for work",
    "I return home, greeted by the same old place",
    "The sneakers go to the designated corner, the jacket on the couch",
    "I move to the kitchen sink and let my mind slouch",
    "This could be the last day of my life",
    "I splash cold water on my face",
    "The next day will be exactly the same",
    "My plants are dying. It’s not a metaphor; it’s a fact"
]

# Define the fixed start and end lines
start_line = "My plants are dying. It’s not a metaphor; it’s a fact."
end_line = "My plants are dying and it’s not a metaphor; it’s a fact."

# Ensure the start and end lines are included
poem_lines = [start_line]

# Remove the start and end lines from the original list for random selection
filtered_text = [line for line in text if line not in [start_line, end_line]]

# Randomly select lines from the remaining lines
while len(poem_lines) < 9:
    poem_lines.append(random.choice(filtered_text))
    filtered_text = [line for line in filtered_text if line not in poem_lines]

# Add the end line
poem_lines.append(end_line)

# Print the generated poem with a title
print("\nPerpetually Creased\n")
poem_text = ". ... ".join(poem_lines) + "."
formatted_poem = textwrap.fill(poem_text, 80)
print(formatted_poem)
