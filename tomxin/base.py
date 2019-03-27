import requests

'''
向后端云推送运行状态
'''
def update_status(error_code):
    object_id = "eJuxAAAM"
    put_url = 'https://api2.bmob.cn/1/classes/project_status/' + object_id
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0",
        "X-Bmob-Application-Id": "",
        "X-Bmob-REST-API-Key": "",
        "Content-Type": "application/json"
    }
    params = {
        "error_code": error_code
    }
    requests.put(put_url, json=params, headers=headers)


if __name__ == '__main__':
    update_status("","正常运行")
