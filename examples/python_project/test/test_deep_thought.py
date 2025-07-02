import unittest
from examples.python_project.deep_thought import deep_thought


class TestDeepThought(unittest.TestCase):
    """
    Ensure the deep_thought function provides the correct anwser regardless the input question.
    """
    def test_empty_argument(self):
        self.assertEqual(deep_thought(),42)

    def test_ultimate_question(self):
        ultimate_question = "What is the Ultimate Answer to Life, The Universe, and Everything?"

        self.assertEqual(deep_thought(ultimate_question),42)

if __name__ == "__main__":
    unittest.main(verbosity=2)
