from collections import Counter

def canMake( secret, guess ):
    return Counter(secret) >= Counter(guess)

secret = input().lower()
guess = input().lower()

print( 'Ок' if canMake(secret, guess) else 'Слово не состоит из букв загаданного слова' )