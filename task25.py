from itertools import count

card_pub = 2959251
door_pub = 4542595
modulus = 20201227

exponent = next(filter(lambda x: pow(7, x, modulus) == card_pub, count()))
print(pow(door_pub, exponent, modulus))
