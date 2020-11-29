from model import Model
import time


class View:
    def __init__(self):
        self.model = Model()

    def insert_goods(self, item):
        self.model.insert_goods(item)
        print("Done! {} was inserted!".format(item))

    def insert_customer(self, item):
        self.model.insert_customer(item)
        print("Done! {} was inserted!".format(item))

    def insert_phone(self, item):
        self.model.insert_phone(item)
        print("Done! {} was inserted!".format(item))

    def insert_email(self, item):
        self.model.insert_email(item)
        print("Done! {} was inserted!".format(item))

    def insert_order(self, item):
        self.model.insert_order(item)
        print("Done! {} was inserted!".format(item))

    def insert_category(self, item):
        self.model.insert_category(item)
        print("Done! {} was inserted!".format(item))

    def update_goods(self, item):
        self.model.update_goods(item)
        print("Goods with ID {} was successfully updated\n{}".format(item[0], item))

    def update_category(self, item):
        self.model.update_category(item)
        print("Goods with ID {} was successfully updated\n{}".format(item[0], item))

    def update_customer(self, item):
        self.model.update_customer(item)
        print("Customer with ID {} was successfully updated\n{}".format(item[0], item))

    def update_order(self, item):
        self.model.update_order(item)
        print("Order with ID {} was successfully updated\n{}".format(item[0], item))

    def update_phone(self, item):
        self.model.update_phone(item)
        print("Phone {} was successfully updated\n{}".format(item[0], item))

    def update_email(self, item):
        self.model.update_email(item)
        print("Email {} was successfully updated\n{}".format(item[0], item))

    def delete_phone(self, item_pk):
        self.model.delete_phone(item_pk)
        print("Phone {} was successfully deleted".format(item_pk))

    def delete_email(self, item_pk):
        self.model.delete_email(item_pk)
        print("Email {} was successfully deleted".format(item_pk))

    def delete_customers(self, item_start_pk, item_end_pk):
        self.model.delete_customer(item_start_pk, item_end_pk)
        print("All customers in ID range [{}, {}] was successfully deleted".format(item_start_pk, item_end_pk))

    def delete_goods(self, item_start_pk, item_end_pk):
        self.model.delete_goods(item_start_pk, item_end_pk)
        print("All goods in ID range [{}, {}] was successfully deleted".format(item_start_pk, item_end_pk))

    def delete_orders(self, item_start_pk, item_end_pk):
        self.model.delete_order(item_start_pk, item_end_pk)
        print("All orders in ID range [{}, {}] was successfully deleted".format(item_start_pk, item_end_pk))

    def delete_categories(self, item_start_pk, item_end_pk):
        self.model.delete_category(item_start_pk, item_end_pk)
        print("All categories in ID range [{}, {}] was successfully deleted".format(item_start_pk, item_end_pk))

    def generate_goods(self, items_counter):
        self.model.generate_goods(items_counter)
        print("{} random goods was successfully generated".format(items_counter))

    def generate_customers(self, items_counter):
        self.model.generate_customers(items_counter)
        print("{} random customers was successfully generated".format(items_counter))

    def generate_categories(self, items_counter):
        self.model.generate_categories(items_counter)
        print("{} random categories was successfully generated".format(items_counter))

    def generate_orders(self, items_counter):
        self.model.generate_orders(items_counter)
        print("{} random orders was successfully generated".format(items_counter))

    def generate_phones(self, items_counter):
        self.model.generate_phone(items_counter)
        print("{} random phones was successfully generated".format(items_counter))

    def generate_emails(self, items_counter):
        self.model.generate_emails(items_counter)
        print("{} random phones was successfully generated".format(items_counter))

    def find_items(self, tables):
        time_before = time.time()
        items = self.model.find_entities(tables)
        time_after = time.time()
        for item in items:
            print(item)
        print("Operation time --- {} ms.".format((time_after-time_before)*1000))
