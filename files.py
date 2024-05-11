file = open('test.csv', 'r')
count = 0
for content in file.readlines():
    print(content)
    count += 1

file.close()

print('using with statement')
with open('test.csv', 'r') as file:
    for content in file.readlines():
        print(content)
