import unittest
from backpack import BackPack
from items import Items
from room import Room
from troglodyte import Troglodyte
from backpack import BackPack
BackPack = BackPack()
RandomRoom = Room("RandomRoom")
WrongRoom = Room("RandomRoom")
RandomRoom.find_directions(WrongRoom)
FakeCharacter = Troglodyte(BackPack)

RandomItem = Items("RandomItem")
WrongItem = Items("WrongItem")
RandomRoom.item1 = RandomItem


class TestBackPack(unittest.TestCase):
    def test_add_backpack(self):
        List = []
        List.append(RandomItem)
        (BackPack.add(RandomRoom, List))
        self.assertEqual(BackPack.in_backpack(RandomItem.item),RandomItem.item)
    def test_add_backpack_none(self):
        List = []
        List.append(RandomItem)
        (BackPack.add(RandomRoom, List))
        self.assertEqual(BackPack.in_backpack(WrongItem.item), None)



if __name__ == '__main__':
    unittest.main()