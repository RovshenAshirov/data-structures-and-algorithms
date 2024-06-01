# Ushbu hash funksiya matnning birinchi harfining alifboda joylashuvini qiymat sifatida qaytaradi.
# Ya'ni: a=0 b=1, c=2, d=3, e=4, va hokazo.

import string

alphabet = list(string.ascii_lowercase) # Pythondagi tayyor lotin alifbosi


def hashfun2(text):
    """Kiritilgan matnning birinchi harfini indeks sifatida qaytaradi"""
    return alphabet.index(text[0].lower())


print(hashfun2('apple'))
print(hashfun2('darslik'))
print(hashfun2('Dorixona'))
print(hashfun2('sariqdev'))
