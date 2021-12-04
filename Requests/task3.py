from pprint import pprint
import requests

def get_qwestions(fromdate, todate, tag):
        url = "https://api.stackexchange.com/2.3/questions"
        headers = ""
        params = {'fromdate' : fromdate,
                  'todate' : todate,
                  'min' : fromdate,
                  'max' : todate,
                  'tagged' : tag,
                  'order' : 'desc',
                  'sort' : 'activity',
                  'site' : 'stackoverflow'}
        response = requests.get(url, headers=headers, params=params)
        return response.json()


if __name__ == '__main__':
    pprint(get_qwestions('2021-12-02', '2021-12-04', 'Python'))