from view import View
import model

inp_requests = dict({"goods": ["Enter name", "Enter price", "Enter discount", "Enter guarantee",
                               "Enter category ID"],
                     "customer": ["Enter surname", "Enter name", "Enter father name"],
                     "phone": ["Enter phone number", "Enter customer ID"],
                     "email": ["Enter email", "Enter customer ID"],
                     "order": ["Enter date", "Enter goods ID", "Enter customer ID", "Enter confirming method"],
                     "category": ["Enter category name", "Enter parent category ID"]})


def validate(option, item):
    if option == "goods":
        return True if (item[0].isalnum() and item[1].isdigit() and item[2].isdigit() and item[3].isdigit() and
                        item[4].isdigit()) else False
    if option == "customer":
        return True if (item[0].isalpha() and item[1].isalpha() and item[2].isalpha()) else False
    if option == "phone":
        return True if item[1].isdigit() else False
    if option == "email":
        return True if item[1].isdigit() else False
    if option == "order":
        return True if (item[1].isdigit() and item[2].isdigit() and (item[3] == 'phone' or item[3] == 'email'))\
            else False
    if option == "category":
        return True if item[1].isdigit() else False


class Controller:
    def __init__(self):
        self.view = View()
        self.mod = model.Model()

    def insert_item(self, option):
        global inp_requests
        item = list()
        for request in inp_requests[option]:
            item.append(input(request+": "))
        if option == "goods":
            if validate(option, item):
                self.view.insert_goods(item)
            else:
                raise Exception("Incorrect type of entered values")
        if option == "customer":
            if validate(option, item):
                self.view.insert_customer(item)
            else:
                raise Exception("Incorrect type of entered values")
        if option == "phone":
            if validate(option, item):
                self.view.insert_phone(item)
            else:
                raise Exception("Incorrect type of entered values")
        if option == "email":
            if validate(option, item):
                self.view.insert_email(item)
            else:
                raise Exception("Incorrect type of entered values")
        if option == "order":
            if validate(option, item):
                self.view.insert_order(item)
            else:
                raise Exception("Incorrect type of entered values")
        if option == "category":
            if validate(option, item):
                self.view.insert_category(item)
            else:
                raise Exception("Incorrect type of entered values")

    def update_item(self, option, item_pk):
        if not item_pk.isdecimal():
            raise Exception("\'{}\' is not a decimal id".format(item_pk))
        global inp_requests
        item = list()
        for request in inp_requests[option]:
            item.append(input(request+" (Enter empty row to skip): "))
        new_item = list()
        if option == "goods":
            curr_item = self.mod.read_goods_by_pk(int(item_pk))
            new_item.append(curr_item[0][0])
            for i in range(1, 6):
                if item[i-1] != "":
                    new_item.append(item[i-1])
                else:
                    new_item.append(curr_item[0][i])
            if validate(option, new_item):
                self.view.update_goods(new_item)
            else:
                raise Exception("Incorrect type of entered values")
        if option == "customer":
            curr_item = self.mod.read_customer_by_pk(int(item_pk))
            new_item.append(curr_item[0][0])
            for i in range(1, 4):
                if item[i-1] != "":
                    new_item.append(item[i-1])
                else:
                    new_item.append(curr_item[0][i])
            if validate(option, new_item):
                self.view.update_customer(new_item)
            else:
                raise Exception("Incorrect type of entered values")
        if option == "phone":
            curr_item = self.mod.read_phone_by_pk(item_pk)
            new_item.append(curr_item[0][0])
            for i in range(1, 3):
                if item[i-1] != "":
                    new_item.append(item[i-1])
                else:
                    new_item.append(curr_item[0][i-1])
            if validate(option, new_item):
                self.view.update_phone(new_item)
            else:
                raise Exception("Incorrect type of entered values")
        if option == "email":
            curr_item = self.mod.read_email_by_pk(item_pk)
            new_item.append(curr_item[0][0])
            for i in range(1, 3):
                if item[i-1] != "":
                    new_item.append(item[i-1])
                else:
                    new_item.append(curr_item[0][i-1])
            if validate(option, new_item):
                self.view.update_email(new_item)
            else:
                raise Exception("Incorrect type of entered values")
        if option == "order":
            curr_item = self.mod.read_order_by_pk(int(item_pk))
            new_item.append(curr_item[0][0])
            for i in range(1, 5):
                if item[i-1] != "":
                    new_item.append(item[i-1])
                else:
                    new_item.append(curr_item[0][i])
            if validate(option, new_item):
                self.view.update_order(new_item)
            else:
                raise Exception("Incorrect type of entered values")
        if option == "category":
            curr_item = self.mod.read_category_by_pk(int(item_pk))
            new_item.append(curr_item[0][0])
            for i in range(1, 3):
                if item[i-1] != "":
                    new_item.append(item[i-1])
                else:
                    new_item.append(curr_item[0][i])
            if validate(option, new_item):
                self.view.update_category(new_item)
            else:
                raise Exception("Incorrect type of entered values")

    def delete_items(self, option, item_start_pk, item_end_pk=0):
        if not item_start_pk.isdecimal() or not str(item_end_pk).isdecimal():
            raise Exception("\'{}\' or \'{}\' is not a decimal id".format(item_start_pk, item_end_pk))
        if item_end_pk == 0:
            item_end_pk = item_start_pk
        if option == "goods":
            self.view.delete_goods(item_start_pk, item_end_pk)
        if option == "customer":
            self.view.delete_customers(item_start_pk, item_end_pk)
        if option == "category":
            self.view.delete_categories(item_start_pk, item_end_pk)
        if option == "order":
            self.view.delete_orders(item_start_pk, item_end_pk)
        if option == "phone":
            self.view.delete_phone(item_start_pk)
        if option == "email":
            self.view.delete_email(item_start_pk)

    def generate_items(self, option, items_number):
        if not items_number.isdecimal():
            raise Exception("\'{}\' is not a decimal".format(items_number))
        if option == "goods":
            self.view.generate_goods(items_number)
        if option == "customer":
            self.view.generate_customers(items_number)
        if option == "category":
            self.view.generate_categories(items_number)
        if option == "order":
            self.view.generate_orders(items_number)
        if option == "phone":
            self.view.generate_phones(items_number)
        if option == "email":
            self.view.generate_emails(items_number)

    def find_items(self, subcommand):
        query = subcommand.split('?')
        self.view.find_items(query)
