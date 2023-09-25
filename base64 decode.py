import base64

encoded_str = input()
decoded_str = base64.b64decode(encoded_str).decode('utf-8')
print(decoded_str)
