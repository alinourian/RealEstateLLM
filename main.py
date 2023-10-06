from controller import Menu
from argparse import ArgumentParser
from model.languageModels import ClassifierModel
from view.menuView import instruction_help
from flask import Flask, jsonify, request
from pyngrok import ngrok


app = Flask(__name__)
menu = Menu(root_name='buy/rent')


@app.route('/api/get_node', methods=['GET'])
def get_node():
    node_name = request.args.get('node_name', None)
    default_language = request.args.get('language', 'en')

    response = menu.get_node_by_api(node_name, default_language)
    print(response)

    if response['status'] != 0:
        return jsonify(response), 400
    return jsonify(response)


@app.route('/api/post_input', methods=['POST'])
def post_input():
    data = request.json

    node_name = data.get('node_name', None)
    user_input = data.get('user_input', None)
    default_language = data.get('default_language', 'en')

    response = menu.analysis_input_by_api(node_name, user_input, default_language)

    if response['status'] != 0:
        return jsonify(response), 400
    return jsonify(response)


def run_program(default_language="en"):
    instruction_help()
    # English,  Arabic,     Persian,    Urdu,   Chinese,        Russian,    Hindi
    # en        ar          fa          ur      zh-CN/zh-TW     ru          hi
    menu.start(default_language=default_language)
    print('=' * 100)
    print('Output:', menu.output)


if __name__ == '__main__':
    # run_program()

    # Set up ngrok tunnel
    public_url = ngrok.connect(5000)
    print(' * ngrok tunnel "{}" -> "http://127.0.0.1:5000"'.format(public_url))
    app.run(debug=True)
