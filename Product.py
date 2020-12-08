import csv

class Category:
    __id: int
    __name: str

    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int):
        self.__id = id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def print(self):
        print(str(self.__id) + ": " + self.__name)


def add_categories(categories_set):
    # Reading input categories filename
    #file = input('Enter file name (Expects a csv file, using  comma as separator): ')
    file = 'categories.csv'
    # Extracting categories from file
    with open(file, newline='') as csvfile:
        reader = list(csv.reader(csvfile, delimiter=","))
        reader.pop(0)  # removing row name

    cont = 1
    # Insert categories into list
    for row in reader:
        cat = Category(cont, row[0])
        categories_list.append(cat)
        cont += 1


def print_categories(categories_list):
    print("Categories:")
    for cat in categories_list:
        cat.print()

class SubCategory:
    __id: int
    __name: str
    __father: Category

    def __init__(self, id, name, father):
        self.__id = id
        self.__name = name
        self.__father = father

    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int):
        self.__id = id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_father(self) -> str:
        return self.__father

    def set_father(self, father: Category):
        self.__father = father

    def print(self):
        print(str(self.__id) + ": " + self.__name + " -> " + self.__father.get_name())

def print_subcategories(subcategories_list):
    print("Subcategories")
    for sub in subcategories_list:
        sub.print()


class Product:
    __name: str
    __description: str
    __price: float
    __weight: float
    __length: float
    __width: float
    __height: float
    __categories: list
    __subcategories: list


    def __init__(self, name):
        self.__name = name
        self.__categories = list()
        self.__subcategories = list()

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_description(self) -> str:
        return self.__description

    def set_description(self, description: str):
        while(len(description) < 20):
            description = input("Description too short! Minimum of 20 characters needed: ")
        self.__description = description

    def get_price(self) -> float:
        return self.__price

    def set_price(self, price):
        while(price <= 0):
            price = float(input("Price should be greater than 0! Enter again please: "))
        self.__price = price

    def get_weight(self) -> float:
        return self.__weight

    def set_weight(self, weight):
        while(weight <= 0):
            weight = float(input("Weight should be greater than 0! Enter again please: "))
        self.__weight = weight

    def get_length(self) -> float:
        return self.__length

    def set_length(self, length):
        while (length <= 0):
            length = float(input("Length should be greater than 0! Enter again please: "))
        self.__length = length

    def get_width(self) -> float:
        return self.__width

    def set_width(self, width):
        while (width <= 0):
            width = float(input("Width should be greater than 0! Enter again please: "))
        self.__width = width

    def get_height(self) -> float:
        return self.__height

    def set_height(self, height):
        while (height <= 0):
            height = float(input("Height should be greater than 0! Enter again please: "))
        self.__height = height

    def get_categories(self) -> list:
        return self.__categories

    def get_subcategories(self) -> list:
        return self.__subcategories

    def add_category(self, cat):
        self.__categories.append(cat)

    def clear_categories(self):
        self.__categories = list()

    def clear_subcategories(self):
        self.__subcategories = list()

    def add_subcategory(self, sub):
        self.__subcategories.append(sub)


    def print(self):
        print("Name: " + self.__name)
        print("Description: " + self.__description)
        print("Price: " + str(self.__price))
        print("Weight: " + str(self.__weight))
        print("Length: " + str(self.__length))
        print("Width: " + str(self.__width))
        print("Height: " + str(self.__height))
        print_categories(self.__categories)
        print_subcategories(self.__subcategories)

def show_menu() -> int:
    option = -1

    while option < 0 or option > 5:
        print()
        print(40 * '*')
        option = int(input("""What do you want to do?
                       1 - Add a new product
                       2 - Search for a product
                       3 - Edit a product
                       4 - Delete a product
                       5 - Create new subcategory
                       0 - Finish 
                       """))
    return option

def search_category(id, categories_list) -> Category:
    for cat in categories_list:
        if cat.get_id() == id:
            return cat
    print("Category not found!")
    return None

def search_subcategory(id, subcategories_list) -> SubCategory:
    for sub in subcategories_list:
        if sub.get_id() == id:
            return sub
    print("Subcategory not found!")
    return None

def add_new_product(categories_list, subcategories_list) -> Product:
    print("Let's add a new product!")
    name = input("Tell me its name: ")
    description = input("Now a brief description: ")
    price = float(input("And its price: "))
    weight = float(input("Its weight (g):"))
    length = float(input("Its length (cm):"))
    width = float(input("Its width (cm):"))
    height = float(input("Its height (cm):"))

    p = Product(name)
    p.set_description(description)
    p.set_price(price)
    p.set_weight(weight)
    p.set_length(length)
    p.set_width(width)
    p.set_height(height)

    print("Now, please choose which categories it should be included in: ")

    print_categories(categories_list)
    cat = 1

    while(cat != 0):
        cat = int(input("Category ID (0 to end): "))
        if(cat > 0):
            c = search_category(cat, categories_list)
            if c is not None:
                p.add_category(c)

    print("Now, please choose which subcategories it should be included in: ")

    print_subcategories(subcategories_list)
    sub = 1

    while (sub != 0):
        sub = int(input("Subcategory ID (0 to end): "))
        if (sub > 0):
            s = search_subcategory(sub, subcategories_list)
            if s is not None:
                p.add_subcategory(s)

    return p


def search_product(products_list, key) -> Product:
    for p in products_list:
        if p.get_name() == key:
            return p

    print("There is no product named " + key)
    return None


def update_product(products_list):
    key = input("What is the name of the product you want to update? ")
    p = search_product(products_list, key)

    if p is None:
        print("Product not found!")
    else:
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
        price = float(input("New price: "))
        p.set_price(price)
        print()
        print("Current weight: " + str(p.get_weight()))
        weight = float(input("New weight: "))
        p.set_weight(weight)
        print()
        print("Current length: " + str(p.get_length()))
        length = float(input("New length: "))
        p.set_length(length)
        print()
        print("Current width: " + str(p.get_width()))
        width = float(input("New width: "))
        p.set_width(width)
        print()
        print("Current height: " + str(p.get_height()))
        height = float(input("New height: "))
        p.set_height(height)

        print("Current Categories: ")
        print_categories(p.get_categories())
        p.clear_categories()

        print("Now, please choose which categories it should be included in: ")

        print_categories(categories_list)
        cat = 1

        while (cat != 0):
            cat = int(input("Category ID (0 to end): "))
            if (cat > 0):
                c = search_category(cat, categories_list)
                if c is not None:
                    p.add_category(c)

        print("Current Subcategories: ")
        print_subcategories(p.get_subcategories())
        p.clear_subcategories()

        print("Now, please choose which subcategories it should be included in: ")

        print_subcategories(subcategories_list)
        sub = 1

        while (sub != 0):
            sub = int(input("Subcategory ID (0 to end): "))
            if (sub > 0):
                s = search_subcategory(sub, subcategories_list)
                if s is not None:
                    p.add_subcategory(s)

        print("Product successfully updated!")


def delete_product(products_list):
    key = input("What is the name of the product you want to delete? ")
    p = search_product(products_list, key)

    if p is None:
        print("Product not found!")

    else:
        products_list.remove(p)

def create_subcategory(categories_list, subcategories_list):
    print("Let's create a new subcategory:")
    name = input("Subcategories name: ")
    print("Now, tell me the id of the father category of this new one: ")
    print_categories(categories_list)
    father_id = int(input())
    father = None

    for cat in categories_list:
        if cat.get_id() == father_id:
            print(cat.get_name())
            father = cat
            id = len(subcategories_list) + 1
            sub = SubCategory(id, name, father)
            subcategories_list.append(sub)
            return

option = -1
products_list = list()
categories_list = list()
subcategories_list = list()

add_categories(categories_list)
print_categories(categories_list)

while option != 0:
    option = show_menu()

    if option == 1:
        products_list.append(add_new_product(categories_list, subcategories_list))
    elif option == 2:
        key = input("What is the name of the product you want to search for? ")
        p = search_product(products_list, key)
        if p is not None:
            p.print()
    elif option == 3:
        update_product(products_list)
    elif option == 4:
        delete_product(products_list)
    elif option == 5:
        create_subcategory(categories_list, subcategories_list)
        print_subcategories(subcategories_list)
    elif option > 5 or option < 0:
        print("Invalid option! Try again!")
