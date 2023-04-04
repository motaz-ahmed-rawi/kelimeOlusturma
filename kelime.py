import urllib.request
import random

# İnternetten Türkçe kelime listesi alınır
url = 'https://raw.githubusercontent.com/bilalozdemir/tr-word-list/master/files/words_meanings_big.txt'
response = urllib.request.urlopen(url)
long_txt = response.read().decode()

# Kelime listesi daha hızlı bir arama için küme haline dönüştürülür
turkish_words = set(long_txt.split())

# Rastgele harfler oluşturulur
letters = random.sample('abcçdefgğhıijklmnoöprsştuüvyz', 6)

# Rastgele oluşturulan harfler yazdırılır
print("Random harfler: ", " ".join(letters))

# Harfleri içeren kelimeler kontrol edilir ve yazdırılır
for word in turkish_words:
    if all(letter in letters for letter in word) and all(word.count(letter) <= letters.count(letter) for letter in set(word)):
        print(word)
