f = open('first.txt', 'w')

f.write('Hello, ')
f.write('World\n')

f.writelines(['Hello, ', 'Python'])

f.close()

with open('first.txt', 'r') as f:
    for line in f:
        print(line)