from category import Category
from customer import Customer
from email import Email
from phone import Phone
from goods import Goods
from base import Base
from order import Order
from base import Base, Session, engine

import psycopg2
import query_parser

def iterator(mes):
    for i in range(10):
        mes += "chr(trunc(65+random()*25)::int) || "
    return mes


class Model:
    # ========== ctor ==========
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = Session()
        self.conn = psycopg2.connect("dbname='shop' user='postgres' host='localhost' password='3497279088'")
        self.curs = self.conn.cursor()

    # ========== Goods table ==========
    def read_goods_by_pk(self, goods_pk):
        return self.session.query(Goods).filter(Goods.goods_id == goods_pk).one()

    def insert_goods(self, goods):
        self.session.add(Goods(goods[0], goods[1], goods[2], goods[3], goods[4], self.session.query(Category)
                               .filter(Category.category_id == goods[4]).one()))
        self.session.commit()

    def update_goods(self, goods):
        self.session.query(Goods).filter(Goods.goods_id == goods[0]) \
            .update({'name': goods[1], 'price': goods[2], 'discount': goods[3], 'guarantee': goods[4],
                     'category_id': goods[5]})
        self.session.commit()

    def delete_goods(self, goods_start_id, goods_end_id):
        self.session.query(Goods).filter(Goods.goods_id >= goods_start_id).filter(Goods.goods_id <= goods_end_id)\
            .delete()
        self.session.commit()

    def generate_goods(self, goods_counter):
        message = "SELECT "
        for i in range(2):
            message = iterator(message)
        message += 'chr(trunc(65+random()*25)::int), trunc(10000+random()*999999)::int, random()*30, 24, ' \
                   '(SELECT category_id FROM "Category" order by random() limit 1) from generate_series(1, {})' \
            .format(goods_counter)
        self.curs.execute('INSERT INTO "Goods" (name, price, discount, guarantee, category_id) {}'.format(message))
        self.conn.commit()

    # ========== Customers table ==========
    def read_customer_by_pk(self, customer_pk):
        return self.session.query(Customer).filter(Customer.customer_id == customer_pk).one()

    def insert_customer(self, customer):
        self.session.add(Customer(customer[0], customer[1], customer[2]))
        self.session.commit()

    def update_customer(self, customer):
        self.session.query(Customer).filter(Customer.customer_id == customer[0]) \
            .update({'surname': customer[1], 'name': customer[2], 'father_name': customer[3]})
        self.session.commit()

    def delete_customer(self, customer_start_id, customer_end_id):
        self.session.query(Customer).filter(Customer.customer_id >= customer_start_id) \
                            .filter(Customer.customer_id <= customer_end_id).delete()
        self.session.commit()

    def generate_customers(self, customers_number):
        message = "SELECT "
        message = iterator(message)
        message += "chr(trunc(65+random()*25)::int) as surname, "
        message = iterator(message)
        message += "chr(trunc(65+random()*25)::int) as name, "
        message = iterator(message)
        message += "chr(trunc(65+random()*25)::int) as father_name "
        self.curs.execute('INSERT INTO "Customer" (surname, name, father_name, favourites) {},'
                          'random_favourites() from generate_series(1, {})'
                          .format(message, customers_number))
        self.conn.commit()

    # ========== Phone table ==========
    def read_phone_by_pk(self, phone_pk):
        return self.session.query(Phone).filter(Phone.phone == phone_pk).one()

    def insert_phone(self, phone):
        self.session.add(Phone(phone[0], phone[1], self.session.query(Customer)
                               .filter(Customer.customer_id == phone[1]).one()))
        self.session.commit()

    def update_phone(self, phone):
        self.session.query(Phone).filter(Phone.phone == phone[0]) \
            .update({'phone': phone[1], 'customer_id': phone[2]})
        self.session.commit()

    def delete_phone(self, phone):
        self.session.query(Phone).filter(Phone.phone.ilike(phone)).delete()
        self.session.commit()

    def generate_phone(self, phone_counter):
        self.curs.execute('INSERT INTO "Phone" SELECT ' + "'+'" + ' || text(trunc(100000000+random()*999999999)::int), '
                                                                  '(SELECT customer_id FROM "Customer" order by random() limit 1) FROM generate_series(1, {})'.
                          format(phone_counter))
        self.conn.commit()

    # ========== Email table ==========
    def read_email_by_pk(self, email_pk):
        return self.session.query(Email).filter(Email.email == email_pk).one()

    def insert_email(self, email):
        self.session.add(Email(email[0], email[1], self.session.query(Customer)
                               .filter(Customer.customer_id == email[1]).one()))
        self.session.commit()

    def update_email(self, email):
        self.session.query(Email).filter(Email.email == email[0]) \
            .update({'email': email[1], 'customer_id': email[2]})
        self.session.commit()

    def delete_email(self, email):
        self.session.query(Email).filter(Email.email == email).delete()
        self.session.commit()

    def generate_emails(self, emails_counter):
        message = "SELECT "
        for i in range(2):
            message = iterator(message)
        message += "'@gmail.com'"
        self.curs.execute('INSERT INTO "Email" {}, (SELECT customer_id FROM "Customer" '
                          'order by random() limit 1) FROM generate_series(1, {})'.
                          format(message, emails_counter))
        self.conn.commit()

    # ========== Category table ==========
    def read_category_by_pk(self, category_pk):
        return self.session.query(Category).filter(Category.category_id == category_pk).one()

    def insert_category(self, category):
        if category[1] != '':
            self.session.add(Category(category[0], category[1]))
        else:
            self.session.add(Category(category[0]))
        self.session.commit()

    def update_category(self, category):
        self.session.query(Category).filter(Category.category_id == category[0]) \
            .update({'name': category[1], 'parent_category_id': category[2]})
        self.session.commit()

    def delete_category(self, category_start_id, category_end_id):
        self.session.query(Category).filter(Category.category_id >= category_start_id) \
                            .filter(Category.category_id <= category_end_id).delete()
        self.session.commit()

    def generate_categories(self, categories_counter):
        message = "SELECT "
        for i in range(2):
            message = iterator(message)
        message += "chr(trunc(65+random()*25)::int), null"
        self.curs.execute('INSERT INTO "Category" (name, parent_category_id) {} FROM generate_series(1, {})'
                          .format(message, categories_counter))
        self.conn.commit()

    # ========== Order table ==========
    def read_order_by_pk(self, order_pk):
        return self.session.query(Order).filter(Order.order_id == order_pk).one()

    def insert_order(self, order):
        self.session.add(Order(order[0], order[1], order[2], order[3], self.session.query(Goods)
                               .filter(Goods.goods_id == order[1]).one(), self.session.query(Customer)
                               .filter(Customer.customer_id == order[2]).one()))
        self.session.commit()

    def update_order(self, order):
        self.session.query(Order).filter(Order.order_id == order[0]) \
            .update({'date': order[1], 'goods_id': order[2], 'customer_id': order[3], 'confirming_method': order[4]})
        self.session.commit()

    def delete_order(self, order_start_id, order_end_id):
        self.session.query(Order).filter(Order.order_id >= order_start_id).filter(Order.order_id <= order_end_id)\
            .delete()
        self.session.commit()

    def generate_orders(self, orders_number):
        message = "SELECT timestamp '2008-01-10 20:00:00' + " \
                  "random() * (timestamp '2020-12-31 23:00:00' - timestamp '2008-01-10 20:00:00'), " \
                  '(SELECT goods_id FROM "Goods" order by random() limit 1), ' \
                  '(SELECT customer_id FROM "Customer" order by random() limit 1), ' + "'phone'"
        self.curs.execute('INSERT INTO "Order" '
                          '(date, goods_id, customer_id, confirming_method) {} from generate_series(1, {})'
                          .format(message, orders_number))
        self.conn.commit()

    # ========== Find ==========
    def find_entities(self, query):
        pass
        try:
            message = "SELECT * FROM \"{}\" WHERE ".format(query[0])
            message += query_parser.QueryParser.parse_query(query)
            message = message.rstrip("and ")
            self.curs.execute(message)
            return self.curs.fetchall()
        except Exception as ex:
            raise ex
        finally:
            self.conn.rollback()
