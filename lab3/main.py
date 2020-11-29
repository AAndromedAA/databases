from router import Router

router = Router()
while True:
    try:
        command = input("Enter command: ")
        router.execute(command)
        if command == "exit":
            break
    except Exception as ex:
        print(ex)
