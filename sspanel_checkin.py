import os
import requests

def sc_send(send_key, title, body):
    url = f'https://sctapi.ftqq.com/{send_key}.send'
    data = {'text': title, 'desp': body}
    
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        result = response.text
    else:
        result = f"方糖酱推送错误 - Status code: {response.status_code}"
    
    return result

def main():
    user_info = os.environ['USER_INFO']
    send_key = os.environ['SEND_KEY'] if "SEND_KEY" in os.environ else ""
    base_url, email, password = user_info.split("|")
    login_url = base_url + '/auth/login'
    checkin_url = base_url + '/user/checkin'

    with requests.sessions.Session() as session:
        post_data = {"email": email, "passwd": password, "code": ""}
        session.post(login_url, post_data)
        res = session.post(checkin_url)
    # message = str(res.json())
    message = res.content.decode('unicode_escape')
    print(message)
    if send_key:
#    if ('您获得了' not in message) and send_key:
        ret = sc_send(send_key, "SSPanel报名结果", message)
        print(ret)
if __name__ == "__main__":
    main()
