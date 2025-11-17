def add_item(item, item_list=None):
    if item_list is None:
        item_list = []
    item_list.append(item)
    return item_list
print(add_item(1))
print(add_item(2))
