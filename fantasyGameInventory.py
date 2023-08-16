from typing import Any, List

def displayInventory(inventory:dict) -> None:
    print('Inventory:')
    item_count = 0

    for key,value in inventory.items():
        print(f'{str(value)} {key}')
        item_count += value
    
    print(f'Total number of items: {item_count}')

    return None

def addToInventory(inventory:dict, loot:List[Any]) -> dict:
    new_inventory = dict()

    for obj in loot:
        new_inventory[obj] = inventory.get(obj, 0)
        
    for obj in loot:
        new_inventory.setdefault(obj, 0)
        new_inventory[obj] += 1
    
    '''
    for obj in loot:
        new_inventory.setdefault(obj, 0)
        new_inventory[obj] += 1
    '''
    
    return new_inventory

if __name__ == '__main__':
    inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    displayInventory(inventory)
    displayInventory(addToInventory(inventory, dragonLoot))