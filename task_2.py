import requests as reqs
import os, sys

class YaUploader:
    def __init__(self, token: str):
        self.host = 'https://cloud-api.yandex.net:443'
        self.token = token        

    def upload(self, file_path: str):
        file_name = os.path.basename(file_path)

        upload_link = self._get_upload_link(file_name)
        if not upload_link:
            return 1337

        headers = {'Accept' : 'application/json'}
        with open(file_path, 'rb') as f:
            resp = reqs.put(upload_link, data=f, headers=headers, timeout=5)

        return resp.status_code

    def _get_upload_link(self, path):
        uri = self.host + f'/v1/disk/resources/upload?path={path}&overwrite=true'
        headers = {'Accept' : 'application/json', 'Authorization' : token}
        resp = reqs.get(uri, headers=headers, timeout=5)

        return resp.json().get('href', '')


if __name__ == '__main__':
    path_to_file = input('Введите абсолютный путь к файлу:\n')

    if not os.path.isfile(path_to_file):
        print(f'[ОШИБКА] Файл не существует! ({path_to_file})')
        sys.exit()

    token = input('Ваш токен авторизации:\n')
    uploader = YaUploader(token)

    try:
        result = uploader.upload(path_to_file)
        if result == 201:
            print("[ИНФО] Файл успешно загружен!")
        elif result == 1337:
            print("[ОШИБКА] Произошла ошибка при формированнии ссылки для загрузки файла. Проверьте правильность токена авторизации.")
        else:
            print(f"[ОШИБКА] Произшла ошибка при загрузке файла. Код ошибки - {result}")

    except reqs.exceptions.ReadTimeout:
        print("[ОШИБКА] Нет связи с сервером, проверьте подключение к интернету")
