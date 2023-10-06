import requests


ngrok_url = "http://127.0.0.1:5000"


def test_post_request(json_file):
    response = requests.post(f"{ngrok_url}/api/post_input", json=json_file)
    if response.status_code == 200:
        print(f'status_code: 200, Test was Successful! {response.json()}')
    elif response.status_code == 400:
        print('status_code: 400, Test failed! Bad request, Node not found.')
    elif response.status_code == 404:
        print('status_code: 404, Test failed! Not found.')
    else:
        print(f'status_code: {response.status_code}, Test failed!')


def test_get_request(params):
    response = requests.get(f"{ngrok_url}/api/get_node", params=params)
    if response.status_code == 200:
        print(f'status_code: 200, Test was Successful! {response.json()}')
    elif response.status_code == 400:
        print(f'status_code: 400, Test failed! {response.json()}')
    elif response.status_code == 404:
        print('status_code: 404, Test failed! Not found.')
    else:
        print(f'status_code: {response.status_code}, Test failed!')


# Test case 1: Valid input
params_valid = {'node_name': 'buy/rent', 'language': 'en'}
test_get_request(params_valid)

# Test case 2: Invalid node_name
params_invalid_node = {'node_name': 'nonexistent_node', 'language': 'en'}
test_get_request(params_invalid_node)

# Test case 4: Missing language (using default)
params_missing_node = {'node_name': 'buy/rent'}
test_get_request(params_missing_node)


json_valid_file = {'node_name': 'buy/rent', 'language': 'en', 'user_input': '0'}
test_post_request(json_valid_file)
