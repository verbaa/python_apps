import random
def generator (count_char=4):
    arr = ['a', 'b', 'c', 'd', 'e', 'k', 'l', 'm', '1', '2', '3', '4', '5']
    passw = []
    for i in range(count_char):
        passw.append(random.choice(arr))
    return "".join(passw)

print(generator())
print(generator(8))
input()
