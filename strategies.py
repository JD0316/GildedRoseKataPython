from gilded_rose import Item

class ItemStrategy:
    def update_quality(self, item: Item):
        raise NotImplementedError


class NormalItemStrategy(ItemStrategy):
    def update_quality(self, item: Item):
        item.sell_in -= 1
        
        if item.quality > 0:
            item.quality -= 1

        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1
        
        item.quality = max(0, min(50, item.quality))


class ConjuredItemStrategy(ItemStrategy):
    def update_quality(self, item: Item):
        item.sell_in -= 1
        
        if item.quality > 0:
            item.quality -= 2

        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 2
        
        item.quality = max(0, min(50, item.quality))


class AgedBrieStrategy(ItemStrategy):
    def update_quality(self, item: Item):
        item.sell_in -= 1
        
        if item.quality < 50:
            item.quality += 1
        
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1
        
        item.quality = max(0, min(50, item.quality))


class BackstagePassesStrategy(ItemStrategy):
    def update_quality(self, item: Item):
        item.sell_in -= 1

        if item.sell_in < 0:
            item.quality = 0
        else:
            if item.quality < 50:
                item.quality += 1
            if item.sell_in < 10 and item.quality < 50:
                item.quality += 1
            if item.sell_in < 5 and item.quality < 50:
                item.quality += 1
        
        item.quality = max(0, min(50, item.quality))


class SulfurasStrategy(ItemStrategy):
    def update_quality(self, item: Item):
        # do nothing, because "Sulfuras" never changes
        pass
