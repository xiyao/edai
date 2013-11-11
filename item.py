from scrapy.item import Item, Field

class DmozItem(Item):
    # define the fields for your item here like:
    # name = Field()
    phone = Field()
    link = Field()
    desc = Field()  
    pass
