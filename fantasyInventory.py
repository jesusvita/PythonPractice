stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

#displays a dictionay
def displayInventory(inventory):
    print("Inventory: ")
    itemTotal = 0
    for k, v in inventory.items():
        print(k + ' : ' + str(v))
        itemTotal = itemTotal + int(v)
    print("Total number of items: " + str(itemTotal))

#takes in a dictionary and adds a list of items to it as keys with default of 0
def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0 )
        inventory[i] = inventory[i] + 1
    return inventory

#remove a number of items or the item completely
def removeFromInventory(inventory, item, numberRemoved):
    x = inventory[item]
    if numberRemoved >= x:
        del inventory[item]
    else:
        inventory[item] =  inventory[item] - numberRemoved
    print('You now have ' + str(x) + ' ' + item + '(s)')
    return inventory


stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)
stuff = removeFromInventory(stuff, 'rope', 1)
displayInventory(stuff)
