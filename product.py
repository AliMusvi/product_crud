import time
from time import gmtime, strftime
import uuid


class Product:
    __products = {}

    def __init__(self, title: str, short_description: str, slug: str, permalink: str,
    isAvailable: bool, sku: str, price: float, regular_price: float, sale_price: float, 
    manage_stock: int, stock_quantity: int):
        self.__product_id = uuid.uuid4().int
        self.__title = title
        self.__short_description = short_description
        self.__slug = slug
        self.__permalink = permalink
        self.__isAvailable = isAvailable
        self.__sku = sku
        self.__price = price
        self.__regular_price = regular_price
        self.__sale_price = sale_price
        self.__manage_stock = manage_stock
        self.__stock_quantity = stock_quantity
        self.__isVisible = True
        self.__date_created_gmt = time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())
        self.__date_modified_gmt : str        
    
    def add(self):
        msg = self.Show()
        if msg != "Not Found":
            return "The product with id : {self.id} is exist."
        self.__products[self.__product_id] = self

        

    def update(self, title = "", short_description = "", slug = "", permalink = "",
    isAvailable: bool  = None, sku = "", price = 0.0, regular_price = 0.0, sale_price = 0.0, 
    manage_stock = 0, stock_quantity = 0):
        
        if title != "": self.__title = title 
        if short_description != "" : self.__short_description = short_description
        if slug != "": self.__slug = slug
        if permalink != "":self.__permalink = permalink
        if isAvailable != None:self.__isAvailable = isAvailable
        if sku != "":self.__sku = sku
        if price != 0.0:self.__price = price
        if regular_price != 0.0:self.__regular_price = regular_price
        if sale_price != 0.0:self.__sale_price = sale_price
        if manage_stock != 0:self.__manage_stock = manage_stock        
        if stock_quantity != 0:self.__stock_quantity = stock_quantity
        self.__date_modified_gmt = time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())

        self.__products[self.__product_id] = self

    def delet(self):
        product = self.find_by_id(id)
        self.__products[id].__isVisible = False

    def Show(self):
        if self.__isVisible == False:
            return "Not Found"
        
        return self.__products.get(id, "Not found")

    @classmethod
    def show_all(cls):
        products = cls.__products.values()
        visible_product = filter(lambda prodct: prodct.__isVisible == True, products)

        return list(visible_product)

    def __repr__(self) -> str:
        rep = str('product {' + '\n' + 'id :' + str(self.__product_id) + '\n' 
        + "title : " + self.__title + '\n'
        + "short_description : " + self.__short_description + '\n'
        + "slug : " + self.__slug + '\n'
        + "permalink : " + self.__permalink + '\n'
        + "isAvailable : " + str(self.__isAvailable) + '\n'
        + "sku : " + self.__sku + '\n'
        + "price : " + str(self.__price) + '\n'
        + "regular price : " + str(self.__regular_price) + '\n'
        + "sale price : " + str(self.__sale_price) + '\n'
        + "manage stock : " + str(self.__manage_stock) + '\n'
        + "stock quantity : " + str(self.__stock_quantity) + '\n'
        + '}')
        return rep
    

