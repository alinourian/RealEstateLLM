buy_rent = {
    'name': 'buy/rent',
    'type': 'option',
    'question': 'Do you want to buy or rent?',
    'valid_response': {0: 'rent', 1: 'buy'},
    'parent': '',
    'children': ['rent__budget', 'buy__budget-buy']
}

rent__budget = {
    'name': 'rent__budget',
    'type': 'scroll',
    'question': 'How much money do you have per month?',
    'valid_response': {0: 1000, 1: 5000},
    'parent': 'buy/rent',
    'children': ['time']
}

buy__budget = {
    'name': 'buy__budget',
    'type': 'scroll',
    'question': 'How much money do you have?',
    'valid_response': {0: 50000, 1: 500000},
    'parent': 'buy/rent',
    'children': ['ready/off-plane']
}

time = {
    'name': 'time',
    'type': 'input',
    'question': 'How long are you looking to rent the property for?',
    'valid_response': {0: 'less than 6 month', 1: '6 month', 2: '1 year'},
    'parent': 'rent__budget',
    'children': ['rent__property-type', 'rent__property-type', 'rent__property-type']
}

ready_off_plan = {
    'name': 'ready/off-plane',
    'type': 'option',
    'question': 'Do you want it ready or off-plan?',
    'valid_response': {0: 'ready', 1: 'off-plan'},
    'parent': 'buy__budget',
    'children': ['buy__property-type', 'buy__property-type']
}

rent__property_type = {
    'name': 'rent__property-type',
    'type': 'option',
    'question': 'What kind of property type do you want?',
    'valid_response': {0: 'Apartment', 1: 'vila'},
    'parent': 'time',
    'children': ['rent__square-root', 'rent__square-root']
}

buy__property_type = {
    'name': 'buy__property-type',
    'type': 'option',
    'question': 'What kind of property type do you want?',
    'valid_response': {0: 'Apartment', 1: 'vila'},
    'parent': 'ready/off-plane',
    'children': ['buy__square-root', 'buy__square-root']
}

rent__square = {
    'name': 'rent__square-root',
    'type': 'scroll',
    'question': 'What is the square footage of the house you are interested in?',
    'valid_response': {0: 30, 1: 300},
    'parent': 'rent__property-type',
    'children': ['rent__room']
}

buy__square = {
    'name': 'buy__square-root',
    'type': 'scroll',
    'question': 'What is the square footage of the house you are interested in?',
    'valid_response': {0: 30, 1: 300},
    'parent': 'buy__property-type',
    'children': ['buy__room']
}

rent__room = {
    'name': 'rent__room',
    'type': 'option',
    'question': 'How many bedrooms do you want?',
    'valid_response': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5},
    'parent': 'rent__square-root',
    'children': [None] * 5
}

buy__room = {
    'name': 'buy__room',
    'type': 'input',
    'question': 'How many bedrooms do you want?',
    'valid_response': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5},
    'parent': 'buy__square-root',
    'children': [None] * 5
}

menus = {
    buy_rent['name']: buy_rent,
    buy__budget['name']: buy__budget,
    rent__budget['name']: rent__budget,
    time['name']: time,
    ready_off_plan['name']: ready_off_plan,
    rent__property_type['name']: rent__property_type,
    buy__property_type['name']: buy__property_type,
    rent__square['name']: rent__square,
    buy__square['name']: buy__square,
    rent__room['name']: rent__room,
    buy__room['name']: buy__room
}
