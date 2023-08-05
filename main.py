from controller import Menu
from model.languageModels import ClassifierModel


def run_program():
    # English,  Arabic,     Persian,    Urdu,   Chinese,        Russian,    Hindi
    # en        ar          fa          ur      zh-CN/zh-TW     ru          hi
    default_language = "fa"
    menu = Menu(root_name='buy/rent', default_language=default_language)
    menu.start()
    print('=' * 50)
    print('Output:', menu.output)


if __name__ == '__main__':
    run_program()

