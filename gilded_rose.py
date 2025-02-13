# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class ItemStrategy(ABC):
    def __init__(self, item):
        self.item = item

    @abstractmethod
    def update_quality(self):
        pass
        
class NormalItemStrategy(ItemStrategy):
    def update_quality(self):
        if self.item.quality > 0:
            self.item.quality -= 1
        self.item.sell_in -= 1
        if self.item.sell_in < 0 and self.item.quality > 0:
            self.item.quality -= 1

class AgedBrieStrategy(ItemStrategy):
    def update_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1
        self.item.sell_in -= 1

class SulfurasStrategy(ItemStrategy):
    def update_quality(self):
        pass  

class BackstagePassStrategy(ItemStrategy):
    def update_quality(self):
        if self.item.sell_in > 10:
            self.item.quality += 1
        elif self.item.sell_in > 5:
            self.item.quality += 2
        elif self.item.sell_in > 0:
            self.item.quality += 3
        else:
            self.item.quality = 0
        self.item.sell_in -= 1


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            strategy = self.get_strategy(item)
            strategy.update_quality()

    def get_strategy(self, item):
        if item.name == "Aged Brie":
            return AgedBrieStrategy(item)
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasStrategy(item)
        elif "Backstage passes" in item.name:
            return BackstagePassStrategy(item)
        elif "Conjured" in item.name:
            return ConjuredItemStrategy(item)
        else:
            return NormalItemStrategy(item)



"""class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1"""
