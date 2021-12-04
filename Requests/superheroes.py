import requests

def get_intellect(token, hero_name):
    url = f'https://superheroapi.com/api/{token}/search/{hero_name}'
    response = requests.get(url)
    id = response.json()["results"][0]['id']
    url_int = f'https://superheroapi.com/api/{token}/{id}/powerstats'
    response2 = requests.get(url_int)
    return response2.json()['intelligence']
    # или
    # return response.json()["results"][0]['powerstats']['intelligence']

if __name__ == '__main__':
    token = "2619421814940190"
    heros_list = ["Hulk", "Captain America", "Thanos"]
    intelligence_dict = {}
    for hero in heros_list:
        intelligence_dict[hero] = get_intellect(token, hero)
    print(intelligence_dict)
    print(f'Самый умный - {max(intelligence_dict)}')