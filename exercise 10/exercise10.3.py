from pathlib import Path

path = Path(r'C:\Users\LENOVO\nexen\exercise 10\learning_python.txt')
for line in path.read_text().splitlines():
    print(line)