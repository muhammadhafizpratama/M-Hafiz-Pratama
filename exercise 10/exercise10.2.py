from pathlib import Path

path = Path(r'C:\Users\LENOVO\nexen\exercise 10\learning_python.txt')
contents = path.read_text()

for line in contents.splitlines():
    line = line.replace('Python', 'C')
    print(line)