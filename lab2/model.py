import psycopg2
import query_parser


def iterator(mes):
    for i in range(10):
        mes += "chr(trunc(65+random()*25)::int) || "
    return mes


class Model:
    # ========== ctor ==========
    def __init__(self):
        self.conn = psycopg2.connect("dbname='lab1' user='postgres' host='localhost' password='3497279088'")
        self.curs = self.conn.cursor()

    # ========== Goods table ==========
    def read_goods_by_pk(self, goods_pk):
        self.curs.execute('SELECT * FROM "Goods" WHERE goods_id = {}'.format(goods_pk))
        return self.curs.fetchall()

    def insert_goods(self, goods):
        try:
            self.curs.execute('INSERT INTO "Goods" (name, price, discount, guarantee, category_id) '
                              'VALUES (\'%s\', %d, %f, %d, %d)' %
                              (goods[0], int(goods[1]), float(goods[2]), int(goods[3]), int(goods[4])))
            self.conn.commit()
        except Exception as ex:
            raise ex
        finally:
            self.conn.rollback()

    def update_goods(self, goods):
        try:
            self.curs.execute('UPDATE "Goods" SET name=\'{}\', price={}, discount={}, guarantee={}, category_id={} '
                              'WHERE goods_id={};'.
                              format(goods[1], int(goods[2]), float(goods[3]), int(goods[4]), int(goods[5]), goods[0]))
            self.conn.commit()
        except Exception as ex:
            raise ex
        finally:
            self.conn.rollback()

    def delete_goods(self, goods_start_id, goods_end_id):
        for table in ["Order", "Goods"]:
            self.curs.execute('DELETE FROM "{}" WHERE goods_id >= {} and goods_id <= {}'
                              .format(table, goods_start_id, goods_end_id))
            self.conn.commit()
        self.conn.rollback()

    def generate_goods(self, goods_counter):
        message = "SELECT "
        for i in range(2):
            message = iterator(message)
        message += 'chr(trunc(65+random()*25)::int), trunc(10000+random()*999999)::int, random()*30, 24, ' \
                   '(SELECT category_id FROM "Category" order by random() limit 1) from generate_series(1, {})'\
            .format(goods_counter)
        self.curs.execute('INSERT INTO "Goods" (name, price, discount, guarantee, category_id) {}'.format(message))
        self.conn.commit()

    # ========== Customers table ==========
    def read_customer_by_pk(self, customer_pk):
        self.curs.execute('SELECT * FROM "Customer" WHERE customer_id = {}'.format(customer_pk))
        return self.curs.fetchall()

    def insert_customer(self, customer):
        try:
            self.curs.execute('INSERT INTO "Customer" (surname, name, father_name) '
                              'VALUES (\'%s\', \'%s\', \'%s\')' % (customer[0], customer[1], customer[2]))
            self.conn.commit()
        except Exception as ex:
            raise ex
        finally:
            self.conn.rollback()

    def update_customer(self, customer):
        try:
            self.curs.execute('UPDATE "Customer" SET surname=\'{}\', name=\'{}\', father_name=\'{}\' '
                              'WHERE customer_id={};'.
                              format(customer[1], customer[2], customer[3], customer[0]))
            self.conn.commit()
        except Exception as ex:
            raise ex
        finally:
            self.conn.rollback()

    def delete_customer(self, customer_start_id, customer_end_id):
        for table in ["Order", "Phone", "Email", "Customer"]:
            self.curs.execute('DELETE FROM "{}" WHERE customer_id >= {} and customer_id <= {}'
                              .format(table, customer_start_id, customer_end_id))
            self.conn.commit()

    def generate_customers(self, customers_number):
        message = "SELECT "
        message = iterator(message)
        message += "chr(trunc(65+random()*25)::int) as surname, "
        message = iterator(message)
        message += "chr(trunc(65+random()*25)::int) as name, "
        message = iterator(message)
        message += "chr(trunc(65+random()*25)::int) as father_name "
        self.curs.execute('INSERT INTO "Customer" (surname, name, father_name) {} from generate_series(1, {})'
                          .format(message, customers_number))
        self.conn.commit()

    # ========== Phone table ==========
    def read_phone_by_pk(self, phone_pk):
        self.curs.execute('SELECT * FROM "Phone" WHERE phone = \'{}\''.format(phone_pk))
        return self.curs.fetchall()

    def insert_phone(self, phone):
        try:
            self.curs.execute('INSERT INTO "Phone" (phone, customer_id) '
                              'VALUES (\'%s\', %d)' % (phone[0], int(phone[1])))
            self.conn.commit()
        except Exception as ex:
            raise ex
        finally:
            self.conn.rollback()

    def update_phone(self, phone):
        try:
            self.curs.execute('UPDATE "Phone" SET phone=\'{}\', customer_id={} '
                              'WHERE phone=\'{}\';'.
                              format(phone[1], int(phone[2]), phone[0]))
            self.conn.commit()
        except Exception as ex:
            raise ex
        finally:
            self.conn.rollback()

    def delete_phone(self, phone):
        self.curs.execute('DELETE FROM "Phone" WHERE phone=\'{}\''.format(phone))
        self.conn.commit()

    def generate_phone(self, phone_counter):
        self.curs.execute('INSERT INTO "Phone" SELECT ' + "'+'" + ' || text(trunc(100000000+random()*999999999)::int), '
                          '(SELECT customer_id FROM "Customer" order by random() limit 1) FROM generate_series(1, {})'.
                                                                  format(phone_counter))
        self.conn.commit()

    # ========== Email table ==========
    def read_email_by_pk(self, email_pk):
        self.curs.execute('SELECT * FROM "Email" WHERE email = \'{}\''.format(email_pk))
        return self.curs.fetchall()

    def insert_email(self, email):
        try:
            self.curs.execute('INSERT INTO "Email" (email, customer_id) '
                              'VALUES (\'%s\', %d);' % (email[0], int(email[1])))
            self.conn.commit()
        except Exception as ex:
            raise ex
        finally:
            self.conn.rollback()

    def update_email(self, email):
        try:
            self.curs.execute('UPDATE "Email" SET email=\'{}\', customer_id={} '
                              'WHERE email=\'{}\';'.
                              format(email[1], int(email[2]), email[0]))
            self.conn.commit()
        except Exception as ex:
            raise ex
        finally:
            self.conn.rollback()

    def delete_email(self, email):
        self.curs.execute('DELETE FROM "Email" WHERE email=\'{}\''.format(email))
        self.conn.commit()

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
        self.curs.execute('SELECT * FROM "Category" WHERE category_id = {}'.format(category_pk))
        return self.curs.fetchall()

    def insert_category(self, category):
        try:
            self.curs.execute('INSERT INTO "Category" (name, parent_category_id) '
                              'VALUES (\'%s\', %d);' % (category[0], int(category[1])))
            self.conn.commit()
        except Exception as ex:
            raise ex
        finally:
            self.conn.rollback()

    def update_category(self, category):
        try:
            self.curs.execute('UPDATE "Category" SET name=\'{}\', parent_category_id={} '
                              'WHERE category_id={};'.
                              format(category[1], int(category[2]), int(category[0])))
            self.conn.commit()
        except Exception as ex:
            raise ex
        finally:
            self.conn.rollback()

    def delete_category(self, category_start_id, category_end_id):
        for table in ["Goods", "Category"]:
            self.curs.execute('DELETE FROM "{}" WHERE category_id >= {} and category_id <= {}'
                              .format(table, category_start_id, category_end_id))
            self.conn.commit()

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
        self.curs.execute('SELECT * FROM "Order" WHERE order_id = {}'.format(order_pk))
        return self.curs.fetchall()

    def insert_order(self, order):
        try:
            self.curs.execute('INSERT INTO "Order" (date, goods_id, customer_id, confirming_method) '
                              'VALUES (\'%s\', %d, %d, \'%s\')'
                              % (order[0], int(order[1]), int(order[2]), order[3]))
            self.conn.commit()
        except Exception as ex:
            raise ex
        finally:
            self.conn.rollback()

    def update_order(self, order):
        try:
            self.curs.execute('UPDATE "Order" SET date=\'{}\', goods_id={}, customer_id={}, confirming_method=\'{}\' '
                              'WHERE order_id={};'.
                              format(order[1], int(order[2]), int(order[3]), order[4], int(order[0])))
            self.conn.commit()
        except Exception as ex:
            raise ex
        finally:
            self.conn.rollback()

    def delete_order(self, order_start_id, order_end_id):
        self.curs.execute('DELETE FROM "Order" WHERE order_id >= {} and order_id <= {}'
                          .format(order_start_id, order_end_id))
        self.conn.commit()

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
