from strategies import (
    ItemStrategy, NormalItemStrategy, ConjuredItemStrategy,
    AgedBrieStrategy, BackstagePassesStrategy, SulfurasStrategy
)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            strategy = self._get_strategy(item)
            strategy.update_quality(item)

    def _get_strategy(self, item: Item) -> ItemStrategy:
        if item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasStrategy()
        elif item.name == "Aged Brie":
            return AgedBrieStrategy()
        elif "Backstage passes" in item.name:
            return BackstagePassesStrategy()
        elif item.name.startswith("Conjured"):
            return ConjuredItemStrategy()
        else:
            return NormalItemStrategy()
