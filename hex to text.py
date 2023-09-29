import binascii

hex_string = input()
text = str(binascii.unhexlify(hex_string), 'utf-8')
print(text)  # 输出 'Hello World'
