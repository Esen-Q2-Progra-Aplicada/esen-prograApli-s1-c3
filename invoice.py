class Product:
    def __init__(self, id, name, cost, discount):
        self.id = id
        self.name = name
        self.cost = cost
        self.discount = discount

    def getTotalAmount(self):
        return self.cost - self.discount

    def __repr__(self):
        return (
            f"Product(id:{self.id}, name:{self.name}, "
            + f"cost:{self.cost}, discount:{self.discount})"
        )


class ProductSiman(Product):
    def __init__(self, id, name, cost, discount, brand, ref):
        super().__init__(id, name, cost, discount)
        self.brand = brand
        self.ref = ref
        self.tax = 0.5

    def getTotalAmount(self):
        return (self.cost - self.discount) + self.tax

    def __repr__(self):
        return (
            f"ProductSiman(id:{self.id}, name:{self.name}, "
            + f"cost:{self.cost}, discount:{self.discount}, "
            + f"brand:{self.brand}, ref:{self.ref})"
        )


class Invoice:
    def __init__(self):
        self.productList = []

    def addProduct(self, product):
        if isinstance(product, Product):
            self.productList.append(product)

    def getProductList(self):
        return self.productList

    def getTotal(self):
        total = 0
        for item in self.productList:
            total += item.getTotalAmount()
        output = f"${total}"
        return output


invoice = Invoice()
invoice.addProduct(Product(1, "refri", 600.0, 0.0))
invoice.addProduct(Product(2, "tele", 400.0, 0.0))
invoice.addProduct(ProductSiman(3, "lavadora", 529.0, 100.0, "mabe", "103139154"))
invoice.addProduct(ProductSiman(4, "batidora", 99.0, 0.0, "cuisinart", "102703224"))
print(invoice.getProductList())
print(invoice.getTotal())
