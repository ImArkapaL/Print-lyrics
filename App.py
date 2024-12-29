import time

lines = [
    "Ever since I was a kid, I been legit",
    "If I was you, I would cut up my wrist",
    "XO tatted all over her body, yeah"
    "She just wanna roll and I don't mind it, yeah"
    "Ever since I was a jit, I been legit"
    "You should let her go, she wanna be it"
    "Double-O tatted on her body, yeah"
    "It don't matter what they say, I'm timeless, yeah"
]

# Example delays for each line (in seconds)
delays = []  # Adjust the delays as needed

def print_lyrics():
    for i, (line, char_delay) in enumerate(zip(lines, delays)):
        for char in line:
            print(char, end='', flush=True)  # Print character without newline
            time.sleep(char_delay)  # Delay for each character
        time.sleep(delays[i])  # Delay after each line
        print("")  # Print a newline after each line

print_lyrics()
