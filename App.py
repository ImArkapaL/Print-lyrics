import time

lines = [
    "Ever since I was a kid, I been legit",
    "If I was you, I would cut up my wrist",
    "XO tatted all over her body, yeah",
    "She just wanna roll and I don't mind it, yeah",
    "Ever since I was a jit, I been legit",
    "You should let her go, she wanna be it",
    "Double-O tatted on her body, yeah",
    "It don't matter what they say, I'm timeless, yeah",
]

# Character delay (in seconds)
char_delay = 0.07  # Adjust this for how fast characters appear

# Delays for each line based on the song's timing (in seconds)
delays = [
    1.8,  # Delay after the first line
    1.3,  # Delay after the second line
    1.5,  # Delay after the third line
    0.1,  # Delay after the fourth line
    0.8,  # Delay after the fifth line
    1.5,  # Delay after the sixth line
    1.2,  # Delay after the seventh line
    1.0,  # Delay after the eighth line
]

def print_lyrics():
    for i, line in enumerate(lines):
        for char in line:
            print(char, end='', flush=True)  # Print character without newline
            time.sleep(char_delay)  # Delay for each character
        time.sleep(delays[i])  # Delay after each line
        print("")  # Print a newline after each line

print_lyrics()
