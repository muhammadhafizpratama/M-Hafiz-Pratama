from pathlib import Path

filenames = [r'C:\Users\LENOVO\nexen\exercise 10\dogs.txt', r'C:\Users\LENOVO\nexen\exercise 10\cats.txt']

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        print(f"\nReading {filename}:")
        print(contents)