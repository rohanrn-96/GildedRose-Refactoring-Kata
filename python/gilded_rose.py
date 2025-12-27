# -*- coding: utf-8 -*-

class GildedRose(object):
    AGED_BRIE = "Aged Brie"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == self.SULFURAS:
                continue

            if item.name != self.AGED_BRIE and item.name != self.BACKSTAGE:
                if item.quality > 0:
                    self._decrease_quality(item)
            else:
                if item.quality < 50:
                    self._increase_quality(item)
                    if item.name == self.BACKSTAGE:
                        self._update_backstage_pass(item)
            item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                self._handle_expired_item(item)

    def _increase_quality(self, item, amount=1):
        item.quality = min(50, item.quality + amount)

    def _decrease_quality(self, item, amount=1):
        item.quality = max(0, item.quality - amount)

    def _update_backstage_pass(self, item):
        if item.sell_in < 11 and item.quality < 50:
            self._increase_quality(item)
        if item.sell_in < 6 and item.quality < 50:
            self._increase_quality(item)

    def _handle_expired_item(self, item):
        if item.name == self.AGED_BRIE and item.quality < 50:
            self._increase_quality(item)
        elif item.name == self.BACKSTAGE:
            item.quality = 0
        else:
            if item.quality > 0:
                self._decrease_quality(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
