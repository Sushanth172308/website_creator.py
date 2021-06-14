'''file = open('simple_data.txt', 'r')
#print(file.read())
# to print each line
#print(file.readline())
#print(file.readline())


#for line in file.readlines():
#    print(line)

lines = file.readlines()
print(lines)

file = open('new.txt', 'a')
file.write(' sushanth2')
file.close()
'''
'''
# copying file
file = open('simple_data.txt', 'r')
data = file.read()
file.close()

file = open('new.txt', 'w')
file.write(data)
file.close()
print('successfully written')

'''
file = open('new.txt', 'r')
lines = file.readlines()
print(lines)

ln = 0
i = 0

for line in lines:
    if 'sushanth' in line:
        i = ln
    ln += 1

lines[i] = 'VRC' + lines[i]
file.close()

file = open('new.txt', 'w')
file.writelines(lines)
file.close()
print('successfully written')

'''
file = open('new.txt', 'r')
lines = file.readlines()
#print(lines)
ln = 0  # lines
i = 0    # index

for line in lines:
    if 'hobby' in line:
        print(ln)
        i = ln
    ln += 1
print(lines[i])
lines[i] = 'imp:'+lines[i]
#print(ln)

file.close()

file = open('new.txt', 'w')
file.writelines(lines)
file.close
print('successfully written')

'''