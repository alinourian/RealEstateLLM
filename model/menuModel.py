from enum import Enum
from model.languageModels import get_model_response


class NodeTypes(Enum):
    OPTION = 'option'
    SCROLL = 'scroll'
    INPUT = 'input'


class Node:
    def __init__(
            self,
            name: str,
            node_type: str,
            question: str,
            valid_responses: dict,
            parent,
            children: list,
            scanner,
            printer=print
    ):
        self.name = name
        self.node_type = node_type
        self.question = question
        self.valid_responses = valid_responses
        self.parent = parent
        self.children = self.add_children(children)
        self.scanner = scanner
        self.printer = printer

    def add_children(self, children_list):
        assert len(children_list) == len(self.valid_responses)
        children = {}
        for i in range(len(children_list)):
            children[i] = children_list[i]
        return children

    def show(self):
        pass

    def execute(self, response):
        if self.is_valid_response(response):
            next_node_name = self.children.get(response, None)
            return True, next_node_name, response
        else:
            return False, None, response

    def is_valid_response(self, response):
        return self.valid_responses.__contains__(response)


class OptionNode(Node):
    def __init__(
            self,
            name,
            question,
            valid_responses,
            parent,
            children,
            scanner=input,
            printer=print
    ):
        super(OptionNode, self).__init__(
            name,
            NodeTypes.OPTION.value,
            question,
            valid_responses,
            parent,
            children,
            scanner,
            printer
        )

    def show(self):
        self.printer(self.question)
        for i, option in self.valid_responses.items():
            self.printer(f'{i}. {option}')
        self.printer('Option Answer: ')


class ScrollNode(Node):
    def __init__(
            self,
            name,
            question,
            valid_responses,
            parent,
            children,
            scanner=input,
            printer=print
    ):
        super(ScrollNode, self).__init__(
            name,
            NodeTypes.SCROLL.value,
            question,
            valid_responses,
            parent,
            children,
            scanner,
            printer
        )
        self.min_value = valid_responses[0]
        self.argmax = max(valid_responses.keys())
        self.max_value = valid_responses[self.argmax]

    def add_children(self, children_list):
        assert len(children_list) + 1 == len(self.valid_responses)
        children = {}
        for i in range(len(children_list)):
            children[i] = children_list[i]
        return children

    def show(self):
        self.printer(self.question)
        self.printer(self.valid_responses)
        self.printer(f'Scroll Answer (min={self.min_value}, max={self.max_value}): ')

    def execute(self, response):
        if self.is_valid_response(response):
            n = len(self.valid_responses) - 1
            for i in range(n):
                if response <= self.valid_responses[i + 1]:
                    next_node_name = self.children.get(i, None)
                    return True, next_node_name, response
        return False, None, response

    def is_valid_response(self, response):
        if isinstance(response, int):
            return self.valid_responses[0] <= response <= self.valid_responses[self.argmax]
        return False


class InputNode(Node):
    def __init__(
            self,
            name,
            question,
            valid_responses,
            parent,
            children,
            scanner=input,
            printer=print
    ):
        super(InputNode, self).__init__(
            name,
            NodeTypes.INPUT.value,
            question,
            valid_responses,
            parent,
            children,
            scanner,
            printer
        )

    def show(self):
        self.printer(self.question)
        self.printer(self.valid_responses)
        self.printer('Input Answer: ')

    def execute(self, response):
        model_name = self.name.split("__")[-1]
        idx_pred, response_pred = get_model_response(prompt=response, model_name=model_name)
        if self.is_valid_response(idx_pred):
            next_node_name = self.children.get(idx_pred, None)
            return True, next_node_name, response_pred
        else:
            return False, None, response_pred

