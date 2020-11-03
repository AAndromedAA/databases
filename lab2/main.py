from router import Router

router = Router()
while True:
    try:
        command = input("Enter command: ")
        if command != "exit":
            router.execute(command)
        else:
            break
    except Exception as ex:
        print(ex)
