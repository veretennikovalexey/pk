from collections import Counter
import unittest

def canMake(secret, guess):
    return Counter(secret) >= Counter(guess)

def check_word(secret, guess):
    return 'Ок' if canMake(secret.lower(), guess.lower()) else 'Слово не состоит из букв загаданного слова'

class TestWordChecker(unittest.TestCase):
    def test_sample_1(self):
        """Test the first sample case from the problem"""
        self.assertEqual(check_word('программирование', 'грамм'), 'Ок')
        
    def test_sample_2(self):
        """Test the second sample case from the problem"""
        self.assertEqual(check_word('программирование', 'программист'), 
                       'Слово не состоит из букв загаданного слова')
        
    def test_case_insensitive(self):
        """Test that the function works regardless of letter case"""
        self.assertEqual(check_word('ПРОГРАММИРОВАНИЕ', 'грамм'), 'Ок')
        self.assertEqual(check_word('программирование', 'ГРАММ'), 'Ок')
        
    def test_empty_strings(self):
        """Test with empty strings"""
        self.assertEqual(check_word('программирование', ''), 'Ок')
        
    def test_same_word(self):
        """Test when both words are the same"""
        self.assertEqual(check_word('программирование', 'программирование'), 'Ок')

if __name__ == '__main__':
    # If running as a script, use input() for interactive mode
    secret = input()
    guess = input()
    print(check_word(secret, guess))
    
# To run tests, run with -m unittest flag:
# python -m unittest 2.py