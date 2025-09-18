from class_3.twttr.twttr import remove_vowels


def test_main():
    assert remove_vowels("Twitter") == "Twttr"
    assert remove_vowels("CS50") == "CS50"
    assert remove_vowels("AEIOUaeiou") == ""
    assert remove_vowels("Python") == "Pythn"
    assert remove_vowels("12345") == "12345"
    assert remove_vowels("") == ""
