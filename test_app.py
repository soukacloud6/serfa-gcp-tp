import unittest

from app import create_app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("test")
        self.client = self.app.test_client

    def tearDown(self):
        """Hook executed after each test"""
        pass

    def test_get_base_url_200(self):
        """Given a web user,
        when he hits /api with a get request,
        then the response should have a status code of 200
        and it should show that the API is up"""
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)
        if res.text is not None:
            self.assertEqual(res.text, "Hello, World!")
        else:
            self.fail("Response is not expected")

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main() 