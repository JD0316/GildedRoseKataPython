# -*- coding: utf-8 -*-

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            # 确保 Sulfuras 质量和 SellIn 永远不变
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            # 计算质量下降速度（Conjured 降 2，普通降 1）
            degrade = 2 if item.name.startswith("Conjured") else 1

            # 处理普通物品 & 特殊物品的质量变化
            if item.name == "Aged Brie":
                if item.quality < 50:
                    item.quality += 1
            elif "Backstage passes" in item.name:
                if item.sell_in > 10:
                    item.quality += 1
                elif item.sell_in > 5:
                    item.quality += 2
                elif item.sell_in > 0:
                    item.quality += 3
                else:
                    item.quality = 0  # 演唱会结束，质量归 0
            else:
                if item.quality > 0:
                    item.quality -= degrade  # 正常下降，Conjured 下降 2

            # 减少 SellIn
            item.sell_in -= 1

            # 过期后影响质量变化
            if item.sell_in < 0:
                if item.name == "Aged Brie":
                    if item.quality < 50:
                        item.quality += 1
                elif "Backstage passes" in item.name:
                    item.quality = 0
                else:
                    if item.quality > 0:
                        item.quality -= degrade  # 过期后下降 2，Conjured 下降 4

            # 确保质量在 0 - 50 之间
            item.quality = max(0, min(50, item.quality))
