import unittest

# Function to test
def is_palindrome(word):
    """Check if a word is a palindrome, ignoring non-alphanumeric characters and case."""
    clean_word = ''.join(c.lower() for c in word if c.isalnum())
    return clean_word == clean_word[::-1]

# Unit Test
class TestPalindromeFunction(unittest.TestCase):

    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("madam"))

    def test_case_insensitivity(self):
        self.assertTrue(is_palindrome("MadAm"))

    def test_with_spaces(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_with_non_alphanumeric(self):
        self.assertTrue(is_palindrome("No 'x' in Nixon!"))

    def test_not_a_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

# Manual output for demonstration
def manual_test_cases():
    print("Running manual test cases:")
    test_cases = [
        ("madam", True),
        ("MadAm", True),
        ("A man a plan a canal Panama", True),
        ("No 'x' in Nixon!", True),
        ("hello", False),
    ]

    for word, expected in test_cases:
        result = is_palindrome(word)
        print(f"Input: '{word}' | Expected: {expected} | Result: {result} | {'Pass' if result == expected else 'Fail'}")

if __name__ == "__main__":
    # Run manual test cases
    manual_test_cases()

    # Run tests using unittest
    print("\nRunning tests using unittest...\n")
    unittest.main(verbosity=2)
