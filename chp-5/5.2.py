inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
def displayinventory(oye):
    print("Inventory :")
    for i, j in oye.items():
        print(j,i)
displayinventory(inventory)