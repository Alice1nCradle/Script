import gmpy2 as gp
import binascii
e = 17
p = 447685307
q = 2037
c = 704796792
n = p*q
phi = (p-1) * (q-1)
d = gp.invert(e, phi)
m = pow(c, d, n)
print(m)
print(binascii.unhexlify(hex(m)[2:]))
print(d)
d_hex = hex(d)
print(d_hex)