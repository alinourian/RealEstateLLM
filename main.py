from controller import Menu
from argparse import ArgumentParser
from model.languageModels import ClassifierModel


def run_program(default_language="en"):
    # English,  Arabic,     Persian,    Urdu,   Chinese,        Russian,    Hindi
    # en        ar          fa          ur      zh-CN/zh-TW     ru          hi
    menu = Menu(root_name='buy/rent', default_language=default_language)
    menu.start()
    print('=' * 50)
    print('Output:', menu.output)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        "--lang",
        type=str,
        required=False,
        help="define the language (default=en)"
    )
    args = parser.parse_args()
    run_program(args)
