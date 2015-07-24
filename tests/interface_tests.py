import unittest
from meowmeowbeanz import Meowmeowbeanz

def create_test_beanz():
    return Meowmeowbeanz("http://imgur.com/gallery/np9XnzV", "Tron Swanson")


class TestBeanzInterface(unittest.TestCase):

    def test_creations(self):
        testlink = create_test_beanz
        self.assertEqual(testlink.score, 0)

    def test_upvotes(self):
        testlink = create_test_beanz
        testlink.upvote()
        testlink.upvote()
        testlink.downvote()
        testlink.upvote()
        self.assertEqual(testlink.score, 2)




