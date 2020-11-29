from view import View
import model

inp_requests = dict({"goods": ["Enter name", "Enter price", "Enter discount", "Enter guarantee",
                               "Enter category ID"],
                     "customer": ["Enter surname", "Enter name", "Enter father name", "Enter favourites"],
                     "phone": ["Enter phone number", "Enter customer ID"],
                     "email": ["Enter email", "Enter customer ID"],
                     "order": ["Enter date", "Enter goods ID", "Enter customer ID", "Enter confirming method"],
                     "category": ["Enter category name", "Enter parent category ID"]})


def validate(option, item):
    if option == "goods":
        return True if (item[1].isdigit() and item[2].isdigit() and item[3].isdigit() and
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
        return True if item[1].isdigit() or item[1] == '' else False


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
            item[len(item) - 1] = item[len(item) - 1].split(",")
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

    def fill_entity(self, curr_entity, item, new_entity, attributes):
        i = 0
        new_entity.append(getattr(curr_entity, attributes[0]))
        for j in range(1, len(attributes)):
            if item[i] == '':
                new_entity.append(getattr(curr_entity, attributes[j]))
            else:
                new_entity.append(item[i])
            i += 1
        return new_entity

    goods_attrs = ['goods_id', 'name', 'price', 'discount', 'guarantee', 'category_id']
    customer_attrs = ['customer_id', 'surname', 'name', 'father_name', 'favourites']
    phone_attrs = ['phone', 'customer_id']
    email_attrs = ['email', 'customer_id']
    category_attrs = ['category_id', 'name', 'parent_category_id']
    order_attrs = ['order_id', 'date', 'goods_id', 'customer_id', 'confirming_method']

    def update_item(self, option, item_pk):
        global inp_requests
        item = list()
        for request in inp_requests[option]:
            item.append(input(request+" (Enter empty row to skip): "))
        new_item = list()
        if option == "goods":
            curr_item = self.mod.read_goods_by_pk(int(item_pk))
            self.view.update_goods(self.fill_entity(curr_item, item, new_item, self.goods_attrs))
        if option == "customer":
            if item[len(item) - 1] != '':
                item[len(item) - 1] = item[len(item) - 1].split(',')
            curr_item = self.mod.read_customer_by_pk(int(item_pk))
            self.view.update_customer(self.fill_entity(curr_item, item, new_item, self.customer_attrs))
        if option == "phone":
            curr_item = self.mod.read_phone_by_pk(item_pk)
            i = 0
            new_item.append(getattr(curr_item, self.phone_attrs[0]))
            for attr in self.phone_attrs:
                if item[i] == '':
                    new_item.append(getattr(curr_item, attr))
                else:
                    new_item.append(item[i])
                i += 1
            self.view.update_phone(new_item)
        if option == "email":
            curr_item = self.mod.read_email_by_pk(item_pk)
            i = 0
            new_item.append(getattr(curr_item, self.email_attrs[0]))
            for attr in self.email_attrs:
                if item[i] == '':
                    new_item.append(getattr(curr_item, attr))
                else:
                    new_item.append(item[i])
                i += 1
            self.view.update_email(new_item)
        if option == "order":
            curr_item = self.mod.read_order_by_pk(int(item_pk))
            self.view.update_order(self.fill_entity(curr_item, item, new_item, self.order_attrs))
        if option == "category":
            curr_item = self.mod.read_category_by_pk(int(item_pk))
            self.view.update_category(self.fill_entity(curr_item, item, new_item, self.category_attrs))

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
