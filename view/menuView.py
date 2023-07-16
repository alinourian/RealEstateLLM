from model import NodeTypes


class Scanner:
    def __init__(self):
        self.scanner = input

    def scan(self, input_type, ret):
        input_query = self.scanner()
        print(f'input_type={input_type}, input_query={input_query}')
        if ret.__contains__(input_query):
            return input_query
        if input_type == NodeTypes.OPTION.value:
            try:
                response = int(input_query)
            except ValueError:
                response = "invalid input"
        elif input_type == NodeTypes.SCROLL.value:
            try:
                response = int(input_query)
            except ValueError:
                response = "invalid input"
        else:                           # string input
            response = self.get_string_label(input_query)
        return response

    def get_string_label(self, command):
        return len(command)
