from items import Items
class BackPack:
    """
    BackPack Class



    ToDo: [X] Instantiate backpack
    ToDo: [X] Add Item
    ToDo: [ ] Remove Item
    ToDo: [ ] List Items
    ToDo: [X] Count items
    ToDo: [ ] in backpack (Search for Item - Student to do)
    ToDo: [X] Sort Items

    """

    def __init__(self, items=None):
        self._backpack = []
        if items is None:
            items = []
        for item in items:
            self._backpack.append(item)
        self.sort()

    # def remove(self, location):
    #     while True:
    #         item_number = input("Enter the item you wish to remove?")
    #         if item_number.isnumeric():
    #             item_number = int(item_number)
    #             if not self._backpack.index(item_number) == Items:
    #                 print("There is no item with that index")
    #                 break
    #             if self._backpack.index(item_number) == Items:
    #                 location.item1 = self._backpack.index(item_number)
    #                 self._backpack.remove(item_number)
    #         if not item_number.isnumeric():
    #             print("please enter a number")
    def remove(self, item):
        self.sort()
        self._backpack.remove(item.item)



    def get_key(self, item):
        return item.item
    def sort(self):
        self._backpack.sort(key=self.get_key)

    def count(self):
        pass

    def list(self):
        if len(self._backpack) == 0:
            print("You have nothing!, You lose!")
        print(" I'm a backpack loaded up with things and knickknacks too.\n"
              "Anything that you might need I've got inside for you.")
        for i in self._backpack:
            print(i.item)

    def add(self, location, items):
        items = items
        for i in items:
            if i is not None:
                print(f"Adding {i.item} to backpack")
                if i.is_collectable:
                    self._backpack.append(i)
                    location.remove_items()
                    self.sort()


    def in_backpack(self, target):
        """
        Complete this method using a binary search
        returns -1 or False if not found
        returns position if found
        :param item:
        :return: -1 | False | integer
        """
        self.sort()

        min_value = 0
        max_value = len(self._backpack)-1
        while min_value <= max_value:
            middle = (min_value + max_value)//2
            midpoint = self._backpack[middle].item
            if midpoint > target:
                max_value = middle - 1
            if midpoint < target:
                min_value = middle + 1
            else:
                return midpoint
        return None



