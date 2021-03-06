#!/usr/bin/env python
import unittest
import app

class TestHello(unittest.TestCase):
    def setUp(self):
        app.APP.testing = True
        self.app = app.APP.test_client()

    def test_main(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

if __name__ == '__main__':
    unittest.main()

#https://www.jenkins.io/blog/2017/09/25/declarative-1/
#https://medium.com/@Joachim8675309/jenkins-ci-pipeline-with-python-8bf1a0234ec3