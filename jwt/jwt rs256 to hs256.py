import jwt

public = open('F:\Script\jwt\public.key', 'r').read()
payload = {"user": "admin"}
print(jwt.encode(payload, key=public, algorithm='HS256'))
