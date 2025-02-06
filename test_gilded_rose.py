import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):

    def test_normal_item_quality_decreases(self):
        items = [Item("normal item", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 9)

    def test_aged_brie_quality_increases(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 11)

    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80)

    def test_conjured_quality_decreases_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 8)

if __name__ == "__main__":
    unittest.main()
