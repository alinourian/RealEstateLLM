from model import *
from view import Scanner


class Menu:
    def __init__(self, root_name):
        self.root_name = root_name
        self.output = {}  # node_name: answer_value
        self.scanner = Scanner()
        self.quit_ = 'q'
        self.back = 'back'
        self.translator = Translator()

    def create_node(self, node_info, default_language):
        node_type = node_info['type']
        if node_type == NodeTypes.OPTION.value:
            node = OptionNode(
                name=node_info['name'],
                question=node_info['question-' + default_language],
                options=node_info['valid_response-' + default_language],
                valid_responses=node_info['valid_response'],
                parent=node_info['parent'],
                children=node_info['children'],
                scanner=self.scanner,
                printer=print
            )
        elif node_type == NodeTypes.SCROLL.value:
            node = ScrollNode(
                name=node_info['name'],
                question=node_info['question-' + default_language],
                options=node_info['valid_response-' + default_language],
                valid_responses=node_info['valid_response'],
                parent=node_info['parent'],
                children=node_info['children'],
                scanner=self.scanner,
                printer=print
            )
        else:
            node = InputNode(
                name=node_info['name'],
                question=node_info['question-' + default_language],
                options=node_info['valid_response-' + default_language],
                valid_responses=node_info['valid_response'],
                parent=node_info['parent'],
                children=node_info['children'],
                scanner=self.scanner,
                printer=print
            )
        return node

    def get_node_by_api(self, node_name, default_language="en"):
        node_info = menus.get(node_name, None)
        if node_info is None:
            response = {
                'status': -1,
                'error': 'Bad request, node not found',
            }
        elif not self.translator.valid_languages.__contains__(default_language):
            response = {
                'status': -2,
                'error': 'Bad request, language is not valid!',
            }
        else:
            node = self.create_node(node_info, default_language)
            response = {
                'status': 0,
                'type': node.node_type,
                'question': node.question,
                'options': node.options,
            }
        return response

    def analysis_input_by_api(self, node_name, user_input, default_language="en"):
        node_info = menus.get(node_name, None)
        if node_info is None:
            response = {
                'status': -1,
                'error': 'Bad request, node not found',
            }
        elif not self.translator.valid_languages.__contains__(default_language):
            response = {
                'status': -2,
                'error': 'Bad request, language is not valid!',
            }
        else:
            node = self.create_node(node_info, default_language)

            if node.node_type == NodeTypes.OPTION.value or node.node_type == NodeTypes.SCROLL.value:
                try:
                    user_input = int(user_input)
                except ValueError:
                    response = {
                        'status': -3,
                        'error': 'Bad request, input value type must be integer but got str'
                    }
                    return response

            if node.node_type == NodeTypes.INPUT.value and default_language != "en":
                user_input = self.translator.translate_text(user_input, tgt_language=default_language)

            true_response, next_node_name, model_response = node.execute(user_input)

            if true_response:
                self.output[node.name] = model_response
                if next_node_name is None:
                    next_node_name = 'END_TREE'
                response_to_user = f'Alright, you have chosen {model_response}'
            else:
                if node.node_type == NodeTypes.OPTION.value:
                    response_to_user = 'Sorry, the option you chose is not a valid option.' \
                                       '(this message only shows up when you are using cli and' \
                                       ' you choose non available option)'
                elif node.node_type == NodeTypes.SCROLL.value:
                    response_to_user = 'Sorry, your answer is not in the valid range. ' \
                                       '(this message only shows up when you are using cli and' \
                                       ' you entered wrong number outside the valid range)'
                else:
                    response_to_user = 'Sorry, I did not completely understand what you want.'

            response = {
                'status': 0,
                'response': response_to_user,
                'next_node_name': next_node_name,
                'is_valid': true_response,
            }
        return response

    def start(self, default_language="en"):
        node_info = menus[self.root_name]
        node = self.create_node(node_info, default_language)
        while True:
            print('=' * 100)
            node.show()
            input_query = self.scanner.scan(node.node_type, ret=[self.quit_, self.back])
            if input_query == self.quit_:
                break
            elif input_query == self.back:
                node_parent_name = node.parent
                node_info = menus.get(node_parent_name, None)
                if node_info is not None:
                    node = self.create_node(node_info, default_language)
                    continue
                else:
                    break
            else:
                if node.node_type == NodeTypes.INPUT.value and default_language != "en":
                    input_query = self.translator.translate_text(input_query, tgt_language=default_language)
                true_response, next_node_name, response = node.execute(input_query)
                print()
                print(f'log: true_response={true_response}, next_node_name={next_node_name}, response={response}')
                if true_response:
                    self.output[node.name] = response
                    if next_node_name is None:
                        break
                    node_info = menus[next_node_name]
                    node = self.create_node(node_info, default_language)
                else:
                    print("wrong response! Try again pls.")
