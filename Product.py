class Product:

    __name: str
    __dscription: str
    __price: float

    def __init__(self, name, description, price):
        self.__name = name
        self.__description = description
        self.__price = price

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_description(self) -> str:
        return self.__description

    def set_description(self, description: str):
        self.__description = description

    def get_price(self) -> float:
        return self.__price

    def set_price(self, price):
        self.__price = price

    def print(self):
        print("Name: " + self.__name)
        print("Description: " + self.__description)
        print("Price: " + str(self.__price))



def show_menu() -> int:
    option = -1

    while(option < 0 or option > 4):
        print()
        print(40*'*')
        option = int(input("""What do you want to do?
                       1 - Add a new product
                       2 - Search for a product
                       3 - Edit a product
                       4 - Delete a product
                       0 - Finish 
                       """))
    return option

def add_new_product() -> Product:
    print("Let's add a new product!")
    name = input("Tell me its name: ")
    description = input("Now a brief description: ")
    price = float(input("And its price: "))

    p = Product(name, description, price)
    return p


def search_product(products_list, key) -> Product:
    for p in products_list:
        if (p.get_name() == key):
            return p

    print("There is no product named " + key)
    return None

def  update_product(products_list):
    key = input("What is the name of the product you want to update? ")
    p = search_product(products_list, key)

    if (p != None):
        print("Let's update it then!")
        print("Current name: " + p.get_name())
        name = input("New name: ")
        p.set_name(name)
        print()
        print("Current description: " + p.get_description())
        description = input("New description: ")
        p.set_description(description)
        print()
        print("Current price: " + str(p.get_price()))
        price = input("New price: ")
        p.set_price(price)
        print("Product successfully updated!")
    else :
        print("Product not found!")

def delete_product(products_list):



option = -1
products_list = list()

while(option != 0):
    option = show_menu()

    if(option == 1):
        products_list.append(add_new_product())
    elif(option == 2):
        key = input("What is the name of the product you want to search for? ")
        p = search_product(products_list, key)
        if(p != None):
            p.print()
    elif(option == 3):
        update_product(products_list)
    elif(option == 4):
        delete_product(products_list)
    elif (option > 4 or option < 0):
        print("Invalid option! Try again!")