cat <<-'TEST_CASES' > test.py
#!/usr/bin/env python
import unittest
import app

class TestHello(unittest.TestCase):
    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

if __name__ == '__main__':
    unittest.main()
TEST_CASES
chmod +x test.py

