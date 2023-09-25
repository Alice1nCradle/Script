import base64

original_str = input().encode()
decode_str = base64.b64encode(original_str)
print(decode_str)
