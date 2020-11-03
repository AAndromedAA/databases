from controller import Controller

commands = dict({"post/goods": "goods", "post/customers": "customer", "post/phones": "phone",
                 "post/emails": "email", "post/orders": "order", "post/categories": "category",
                 "update/goods/": "goods", "update/customers/": "customer", "update/phones/": "phone",
                 "update/emails/": "email", "update/categories/": "category", "update/orders/": "order",
                 "delete/goods/": "goods", "delete/customers/": "customer", "delete/phones/": "phone",
                 "delete/emails/": "email", "delete/categories/": "category", "delete/orders/": "order",
                 "random/goods/": "goods", "random/customers/": "customer", "random/phones/": "phone",
                 "random/emails/": "email", "random/categories/": "category", "random/orders/": "order",
                 })


class Router:
    def __init__(self):
        self.controller = Controller()

    def execute(self, command):
        global commands
        if command.split('/')[0] == "post":
            self.controller.insert_item(commands[command])
        elif command.split('/')[0] == "update":
            command_parts = command.split('/')
            if len(command_parts) == 3:
                self.controller.update_item(commands[command_parts[0]+'/'+command_parts[1]+'/'], command_parts[2])
            else:
                raise Exception("Unknown command \'{}\'".format(command))
        elif command.split('/')[0] == "delete":
            command_parts = command.split('/')
            if len(command_parts) == 4:
                self.controller.delete_items(commands[command_parts[0] + '/' + command_parts[1] + '/'], command_parts[2],
                                             command_parts[3])
            elif len(command_parts) == 3:
                self.controller.delete_items(commands[command_parts[0] + '/' + command_parts[1] + '/'], command_parts[2])
            else:
                raise Exception("Unknown command \'{}\'".format(command))
        elif command.split('/')[0] == "random":
            command_parts = command.split('/')
            if len(command_parts) == 3:
                self.controller.generate_items(commands[command_parts[0] + '/' + command_parts[1] + '/'],
                                               command_parts[2])
            else:
                raise Exception("Unknown command \'{}\'".format(command))
        elif command.split('/')[0] == "find":
            if len(command.split('/')) == 2:
                command = command.lstrip("find/")
                self.controller.find_items(command)
            else:
                raise Exception("Unknown command \'{}\'".format(command))
        else:
            raise Exception("Unknown command \'{}\'".format(command))
