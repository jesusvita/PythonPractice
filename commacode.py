def printList(aListItem):
    for i in range(len(aListItem)):

        if i == int(len(aListItem)) - 1:
            print('and ' + str(aListItem[i]) + '.')
        else:
            print(str(aListItem[i]) + ', ', end= '')



spam = ['a', 'b', 'c'] * 4
print(spam)
printList(spam)
