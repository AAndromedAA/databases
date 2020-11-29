class QueryParser:
    @staticmethod
    def parse_query(query):
        message = ""
        if len(query) != 1:
            subquery = query[1].split('&')
            for param in subquery:
                params = param.split('=')
                if params[0] == "name" or params[0] == "surname" or params[0] == "father_name" or params[0] == "phone" \
                        or params[0] == "email" or params[0] == "confirming_method":
                    message += "\"{}\".{} LIKE \'%{}%\' and ".format(query[0], params[0], params[1])
                elif params[0] == "category_id" or params[0] == "parent_category_id" or params[0] == "order_id"\
                        or params[0] == "customer_id" or params[0] == "goods_id" or params[0] == "discount"\
                        or params[0] == "guarantee" or params[0] == "price":
                    range_ = params[1].split('_to_')
                    message += "\"{}\".{} BETWEEN {} and {} and ".format(query[0], params[0], range_[0], range_[1])
                elif params[0] == "date":
                    time_range = params[1].split('_to_')
                    message += "\"{}\".{} BETWEEN timestamp \'{}\' and timestamp \'{}\' and ".\
                        format(query[0], params[0], time_range[0], time_range[1])
        return message
