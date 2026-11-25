"""Small Morse-code exercise; keep the original compact output convention."""
from pathlib import Path

def translate(text):
    alphabet = dict(line.split() for line in Path(__file__).with_name('morse_alpha.txt').read_text(encoding='utf-8').splitlines() if line.strip())
    return ''.join('/' if letter == ' ' else alphabet.get(letter.upper(), '') for letter in text)

def main():
    print(translate(input()))

if __name__ == '__main__':
    main()
