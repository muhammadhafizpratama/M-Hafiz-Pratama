car = 'koenigsegg'
print(car == 'koenigsegg')
print(car == 'ferrari')

car = 'ferrari'
car = car.lower()
print(car == 'ferrari')

num = 10
print(num == 10)
print(num < 5)
print(num > 5)
print(num <= 10)
print(num >= 10)

num = 10 and num <= 20
print(num == 8)
print(num ==15)
num = 10 and num == 15
print(num == 10)
print(num == 13)
print()

list = [ 'grape', 'banana', 'apple']
print('grape' in list)
print('cherry' in list)