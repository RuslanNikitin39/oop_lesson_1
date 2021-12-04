from pprint import pprint
import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_up_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, file_path: str, filename):
        href = self._get_up_link(file_path=file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }


if __name__ == '__main__':
    # path_to_file = "Netology"
    path_to_file = input(f'Input path to file: ')
    token = input(f'Input token: ')
    # filename = "test.txt"
    filename = input(f'Input filename: ')
    uploader = YaUploader(token)
    result = uploader.upload(f'{path_to_file}/{filename}', filename)