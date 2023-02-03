def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i]+=1
        else:
            inventory[i] = 1    
    return inventory
def displayinventory(oye):
    print("Inventory :")
    for i, j in oye.items():
        print(j,i)
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayinventory(inv)