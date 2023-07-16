from controller import Menu


def run_program():
    menu = Menu(root_name='buy/rent')
    menu.start()
    print('=' * 50)
    print('Output', menu.output)


if __name__ == '__main__':
    run_program()
