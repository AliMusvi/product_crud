from product import Product

def main():
    product = Product("title", "short description", "slug", "permalink",
     True, "sku", 10.0, 19.0, 25.0, 10, 20)
    
    product.add()
    product.Show()
    product.update(slug="gtft")
    product.delet()
    Product.show_all()

    print(type(Product))


if __name__ == "__main__":
    main()