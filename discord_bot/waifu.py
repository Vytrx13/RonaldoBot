import requests


def getWaifu(tag):
    url = 'https://api.waifu.im/search'

    params = {
        'included_tags': [tag],
        'height': '>=2000'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        # Process the response data as needed
    else:
        print('Request failed with status code:', response.status_code)

    
    return data['images'][0]['url']



# url = 'https://api.waifu.im/search'
# params = {
#     'included_tags': ['maid'],
#     'height': '>=2000'
# }

# response = requests.get(url, params=params)

# if response.status_code == 200:
#     data = response.json()
#     # Process the response data as needed
# else:
#     print('Request failed with status code:', response.status_code)
    
# print(data['images'][0]['url'])

getWaifu("waifu")