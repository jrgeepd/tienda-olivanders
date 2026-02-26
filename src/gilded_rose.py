class GildedRose:
    def __init__(self):
        self.inventory = Inventory()

    def updateDate(self):
        self.inventory.updateInventory()

    def addItem(self, item):
        self.inventory.addItem(item)

    def getItems(self):
        return self.inventory.getItems()


class Inventory:
    def __init__(self):
        self.items = []

    def updateInventory(self):
        for item in self.items:
            item.updateQuality()

    def addItem(self, item):
        self.items.append(item)

    def getItems(self):
        return self.items

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class NormalItem(Item):
    def setSell_in(self):
        self.sell_in -= 1

    def setQuality(self, value_change):
        new_quality = self.quality + value_change

        if new_quality > 50:
            self.quality = 50
        elif new_quality >= 0:
            self.quality = new_quality
        else:
            self.quality = 0

        assert 0 <= self.quality <= 50, (
            "quality de %s fuera de rango" % self.__class__.__name__
        )

    def updateQuality(self):
        if self.sell_in > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)

        self.setSell_in()

class ConjuredItem(NormalItem):
    def updateQuality(self):
        if self.sell_in >= 0:
            self.setQuality(-2)
        else:
            self.setQuality(-4)

        self.setSell_in()

class AgedBrie(NormalItem):
    def updateQuality(self):
        if self.sell_in > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)

        self.setSell_in()

class Sulfuras(Item):
    def updateQuality(self):
        assert self.quality == 80, (
            "quality de %s debe ser 80" % self.__class__.__name__
        )

class BackstagePasses(NormalItem):
    def updateQuality(self):
        if self.sell_in > 10:
            self.setQuality(1)
        elif self.sell_in > 5:
            self.setQuality(2)
        elif self.sell_in > 0:
            self.setQuality(3)
        else:
            self.quality = 0

        self.setSell_in()
