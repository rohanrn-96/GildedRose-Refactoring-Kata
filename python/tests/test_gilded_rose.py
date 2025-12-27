import pytest

from python.gilded_rose import GildedRose, Item


def test_normal_item_degrades_by_one_each_day():
    items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].sell_in == 9
    assert items[0].quality == 19

def test_normal_item_degrades_twice_as_fast_after_expiry():
    items = [Item(name="Elixir of the Mongoose", sell_in=0, quality=10)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].sell_in == -1
    assert items[0].quality == 8

def test_quality_never_goes_below_zero():
    items = [Item(name="Elixir of the Mongoose", sell_in=0, quality=0)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].quality == 0

def test_aged_brie_increases_in_quality():
    items = [Item(name="Aged Brie", sell_in=5, quality=10)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].sell_in == 4
    assert items[0].quality == 11

def test_aged_brie_increases_faster_after_expiry():
    items = [Item(name="Aged Brie", sell_in=0, quality=10)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].sell_in == -1
    assert items[0].quality == 12

def test_quality_never_exceeds_fifty():
    items = [Item(name="Aged Brie", sell_in=5, quality=50)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].quality == 50

def test_sulfuras_never_changes():
    items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].sell_in == 0
    assert items[0].quality == 80

def test_backstage_pass_increases_by_one_when_sell_in_above_10():
    items = [
        Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=15,
            quality=20,
        )
    ]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].sell_in == 14
    assert items[0].quality == 21

def test_backstage_pass_increases_by_two_when_10_days_or_less():
    items = [
        Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=10,
            quality=20,
        )
    ]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].sell_in == 9
    assert items[0].quality == 22

def test_backstage_pass_increases_by_three_when_5_days_or_less():
    items = [
        Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=5,
            quality=20,
        )
    ]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].sell_in == 4
    assert items[0].quality == 23

def test_backstage_pass_drops_to_zero_after_concert():
    items = [
        Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=0,
            quality=20,
        )
    ]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].sell_in == -1
    assert items[0].quality == 0

def test_backstage_pass_quality_never_exceeds_fifty():
    items = [
        Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=5,
            quality=50,
        )
    ]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].quality == 50

