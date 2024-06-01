# Ushbu hash funksiya 2 qadamdan iborat:
#   Kiritlgan matnning har bir harfini mos tub songa almashtiradi va barcha sonlarni qo'shib yuboradi
#   Yuqoridagi yig'indini 10 ga bo'ladi va qoldiqni qaytaradi

# Masalan bad so'zi uchun hash qiymatini hisoblaymiz:
#   Tub sonlar a=2, b=3, c=5, d=7, e=11, f=13, g=17, h=19 va hokazo bo'lsa, bad so'zi 3+2+7=12 bo'ladi
#   bad = 3+2+7=12 va 12%10=2

import string

alphabet = list(string.ascii_lowercase) # Pythondagi tayyor lotin alifbosi
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101) # 26 ta tub son


def hashfun3(text):
    sum=0
    for t in text.lower():
        sum += primes[alphabet.index(t)]
    return sum%10


print(hashfun3('apple'))
print(hashfun3('darslik'))
print(hashfun3('Dorixona'))
print(hashfun3('mohirdev'))
