import unittest
from utils.text_preprocessing import (
    preprocess_text,
)

class TestPreprocessText(unittest.TestCase):
    def test_basic_text(
        self,
    ):
        text = "The quick brown fox jumps over the lazy dog."
        expected_result = "quick brown fox jump lazy dog"
        self.assertEqual(
            preprocess_text(text),
            expected_result,
        )

    def test_empty_string(
        self,
    ):
        text = ""
        expected_result = ""
        self.assertEqual(
            preprocess_text(text),
            expected_result,
        )

    def test_numbers(
        self,
    ):
        text = "123 4567 890"
        expected_result = "123 4567 890"
        self.assertEqual(
            preprocess_text(text),
            expected_result,
        )

    def test_punctuation(
        self,
    ):
        text = "Hello!!! Can you hear me?"
        expected_result = "hello hear"
        self.assertEqual(
            preprocess_text(text),
            expected_result,
        )

    def test_mixed_content(
        self,
    ):
        text = "Python is great. I love coding in Python 3.8!"
        expected_result = "python great love coding python"
        self.assertEqual(
            preprocess_text(text),
            expected_result,
        )

    def test_stopwords_removal(
        self,
    ):
        text = "This is a simple test case to check stopwords removal."
        expected_result = "simple test case check stopwords removal"
        self.assertEqual(
            preprocess_text(text),
            expected_result,
        )

    def test_lemmatization(
        self,
    ):
        text = "The leaves on the trees are falling down."
        expected_result = "leaf tree falling"
        self.assertEqual(
            preprocess_text(text),
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
