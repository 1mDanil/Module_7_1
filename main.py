from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'



class Shop():
    __file_name = 'products.txt'
    def __init__(self, __file_name = 'products.txt'):
        self.__file_name = __file_name



    def get_products(self):
        a = open(Shop.__file_name, 'r+')
        info = a.read()
        a.close()
        return info

    def add(self, *products):
        info = self.get_products()
        for prod in products:
            if str(prod) in info:
                print(f'Продукт {prod.name} уже есть в магазине')
            else:
                with open(Shop.__file_name, 'a') as file:
                    file.writelines(str(prod) + '\n')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())