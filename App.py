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


char_delay = 0.07


delays = [
    1.8,  
    1.3,  
    1.5,  
    0.1,  
    0.8,  
    1.5,  
    1.2,  
    1.0,  
]

def print_lyrics():
    for i, line in enumerate(lines):
        for char in line:
            print(char, end='', flush=True)
            time.sleep(char_delay)
        time.sleep(delays[i])
        print("") 
        print("coded by Arka")
print_lyrics()
