import gmpy2 as gp
import binascii
e = 17
p = 473398607161
q = 4511491
# c = 69380371057914246192606760686152233225659503366319332065009
n = p*q
phi = (p-1) * (q-1)
d = gp.invert(e, phi)
# m = pow(c, d, n)
# print(binascii.unhexlify(hex(m)[2:]))
print(d)
d_hex = hex(d)
print(d_hex)