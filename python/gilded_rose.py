# -*- coding: utf-8 -*-

class GildedRose(object):
    AGED_BRIE = "Aged Brie"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
    CONJURED = "Conjured"

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == self.SULFURAS:
                continue

            self._update_item(item)

            item.sell_in -= 1
            if item.sell_in < 0:
                self._handle_expired_item(item)

    def _update_item(self, item):
        if item.name == self.AGED_BRIE:
            self._update_aged_brie(item)
        elif item.name == self.BACKSTAGE:
            self._update_backstage(item)
        elif self.CONJURED in item.name:
            self._update_conjured_item(item)
        else:
            self._update_normal_item(item)

    def _update_aged_brie(self, item):
        self._increase_quality(item)

    def _update_backstage(self, item):
        self._increase_quality(item)
        self._update_backstage_pass(item)

    def _update_normal_item(self, item):
        self._decrease_quality(item)

    def _update_conjured_item(self, item):
        self._decrease_quality(item, amount=2)

    def _increase_quality(self, item, amount=1):
        item.quality = min(50, item.quality + amount)

    def _decrease_quality(self, item, amount=1):
        item.quality = max(0, item.quality - amount)

    def _update_backstage_pass(self, item):
        if item.sell_in < 11:
            self._increase_quality(item)
        if item.sell_in < 6:
            self._increase_quality(item)

    def _handle_expired_item(self, item):
        if item.name == self.AGED_BRIE:
            self._increase_quality(item)
        elif item.name == self.BACKSTAGE:
            item.quality = 0
        elif self.CONJURED in item.name:
            self._decrease_quality(item, amount=2)
        else:
            self._decrease_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
