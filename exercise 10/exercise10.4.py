from pathlib import Path

name = input("What's your name? ")
path = Path(r'C:\Users\LENOVO\nexen\exercise 10\guest.txt')
path.write_text(name)