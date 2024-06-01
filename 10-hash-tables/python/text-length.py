# Ushbu hash funksiya matn qabul qiladi va matn uzunligini qiymat sifatida qaytaradi.

def hashfun1(text):
    """Kiritilgan matn uzunlgini hash sifatida qaytaradi"""
    return len(text)


print(hashfun1('olma'))
print(hashfun1('sariqdev'))
print(hashfun1('algoritmlar'))
