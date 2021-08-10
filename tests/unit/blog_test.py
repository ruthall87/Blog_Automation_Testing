from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertEqual([], b.post)

    def test_repr(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual(b.__repr())