from model import NodeTypes


class Scanner:
    def __init__(self):
        self.scanner = input

    def scan(self, input_type, ret):
        input_query = self.scanner()
        # print(f'input_type={input_type}, input_query={input_query}')
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
            response = input_query
        return response


def instruction_help():
    print('-' * 100)
    print('TYPES of QUESTIONS:')
    print('\t - Option:\t The answer must be a number of desired answer option.')
    print('\t - Scroll:\t The answer must be a number between specified minimum and maximum.')
    print('\t - Input:\t The answer is a prompt.')
    print('-' * 100)
