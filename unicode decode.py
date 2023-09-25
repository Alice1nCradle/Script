text = input()
decoded_text = bytes(text, 'utf-8').decode('unicode_escape')
print(decoded_text)
