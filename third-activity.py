file1 = open('the_essay.txt' , 'r')
file2 = open('the_essay_UPDATED.txt' , 'w')

for line in file1.readLines():
    if not (line.startsWith('Coding')):
        print(line)
        file2.write(line)

file1.close()
file2.close()
