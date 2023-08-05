from model import *
from view import Scanner


class Menu:
    def __init__(self, root_name, default_language="en"):
        self.root_name = root_name
        self.output = {}   # node_name: answer_value
        self.scanner = Scanner()
        self.quit_ = 'q'
        self.back = 'back'
        self.default_language = default_language
        self.translator = Translator(default_language=default_language)

    def create_node(self, node_info):
        node_type = node_info['type']
        if node_type == NodeTypes.OPTION.value:
            node = OptionNode(
                name=node_info['name'],
                question=node_info['question-' + self.default_language],
                valid_responses=node_info['valid_response'],
                parent=node_info['parent'],
                children=node_info['children'],
                scanner=self.scanner,
                printer=print
            )
        elif node_type == NodeTypes.SCROLL.value:
            node = ScrollNode(
                name=node_info['name'],
                question=node_info['question-' + self.default_language],
                valid_responses=node_info['valid_response'],
                parent=node_info['parent'],
                children=node_info['children'],
                scanner=self.scanner,
                printer=print
            )
        else:
            node = InputNode(
                name=node_info['name'],
                question=node_info['question-' + self.default_language],
                valid_responses=node_info['valid_response'],
                parent=node_info['parent'],
                children=node_info['children'],
                scanner=self.scanner,
                printer=print
            )
        return node

    def start(self):
        node_info = menus[self.root_name]
        node = self.create_node(node_info)
        while True:
            print('=' * 50)
            node.show()
            input_query = self.scanner.scan(node.node_type, ret=[self.quit_, self.back])
            if input_query == self.quit_:
                break
            elif input_query == self.back:
                node_parent_name = node.parent
                node_info = menus.get(node_parent_name, None)
                if node_info is not None:
                    node = self.create_node(node_info)
                    continue
                else:
                    break
            else:
                if node.node_type == NodeTypes.INPUT.value and self.default_language != "en":
                    input_query = self.translator.translate_text(input_query)
                true_response, next_node_name, response = node.execute(input_query)
                print(f'true_response={true_response}, next_node_name={next_node_name}, response={response}')
                if true_response:
                    self.output[node.name] = response
                    if next_node_name is None:
                        break
                    node_info = menus[next_node_name]
                    node = self.create_node(node_info)
                else:
                    print("wrong response! Try again pls.")
