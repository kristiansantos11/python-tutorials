class Product:
    def __init__(self, name, description, price, ratings):
        self.name = name
        self.description = description
        self.price = price
        self.ratings = ratings

    def average(self):
        return sum(self.ratings)/len(self.ratings)

p1 = Product("Apple", "An apple a day keeps a doctor away!", 0.15, [4,2,5,5,5])
p2 = Product("Lemon", "More VITAMIN C!!", 0.25, [1,2,5,5,3])

print("PRODUCT 1:")
print("Product name: "+ p1.name)
print("Product description: " + p1.description)
print("Product price: " + str(p1.price))
print("Product average ratings: " + str(p1.average()))

print("\nPRODUCT 2:")
print("Product name: " + p2.name)
print("Product desc: " + p2.description)
print("Product price: " + str(p2.price))
print("Product average ratings: " + str(p2.average()))
