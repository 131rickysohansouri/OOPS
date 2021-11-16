from item import Item
from phone import phone
from ky import Keyboard

item1 = Keyboard("jscKeyboard", 1000, 3)

item1.apply_discount()

print(item1.price)
phone1 = phone("okayphone",500,5,1)
print(phone1.calctprice())
phone2 = phone("okayphone2",700,5,1)

# Item.instantiate_from_csv()
# print(Item.is_integer(7.0))

# item1 = Item("Phone", 100, 1)
# item1.__repr__()
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(Item.__dict__)
# print(item1.__dict__)
# print(Item.all_items)
