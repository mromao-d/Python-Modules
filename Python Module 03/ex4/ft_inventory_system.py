import sys

class SplitError(Exception):
    pass


def treat_args(arg: str, inventory: dict[str, int] = {}):
    

    try:
        kv = arg.split(":")
        if len(kv) != 2:
            raise SplitError(f"Error - invalid parameter '{arg}'")
        item, qty = kv
        if item not in inventory.keys():
            inventory.update({item: int(qty)})
    except ValueError as e:
        print(f"Quantity error for {item}: {e}")



def ft_inventory_system(args: list[str]):
    inventory: dict[str, int] = {}

    items: list[str] = list(item.split(':')[0] for item in args)
    print(f"items are: {items}")
    redudant_items: set[str] = {item for item in items if items.count(item) > 1}

    for item in redudant_items:
        print(f"Redundant item {item} - discarding")

    for item in args:
        try:
            treat_args(item, inventory)
        except (SplitError, ValueError) as e:
            print(e)
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)} items: {sum(list(inventory.values()))}")
    for item, qty in inventory.items():
        min_item = min(inventory.items(), key=lambda x: x[1])
        max_item = max(inventory.items(), key=lambda x: x[1])
        print(f"Item {item} represents {qty/sum(list(inventory.values())) * 100:.1f}%")

    print(f"Item most abundant: {max_item[0]} with quantity {max_item[1]}")
    print(f"Item most abundant: {min_item[0]} with quantity {min_item[1]}")

    inventory.update({'magic_item': 1})

    print(f"Updated inventory: {inventory}")

    # print(redudant_items)

if __name__ == '__main__':
    print("=== Inventory System Analysis ===")
    ft_inventory_system(sys.argv[1:])
    # test: set = set()
    # test.add("abc")
    # test.add("def")
    # test.add("abc")
    # print(list(test))
