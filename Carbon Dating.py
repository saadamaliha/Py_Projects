import math

# Constants
half_life = 5730 # years
initial_C14 = 100 # percent

# Sample data
sample_C14 = float(input("Percentage of C-14 in your sample: ")) # percent
sample_C12 = float(input("Percentage of C-12 in your sample: ")) # percent

# Calculate the age of the sample
age = (math.log(sample_C12/sample_C14) + math.log(initial_C14/100))/(math.log(2)/half_life)

print("The age of the fossil is: ", age, "years.")
