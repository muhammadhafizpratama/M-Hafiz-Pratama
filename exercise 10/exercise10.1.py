from pathlib import Path

path = Path('C:/Users/LENOVO/nexen/exercise 10/learning_python.txt')
contents = path.read_text()

print(contents)

for line in contents.splitlines():
    print(line)