import unittest
import sys
import os

# Add project root directory to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # Import the Flask app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_status(self):
        response = self.app.get('/api/status')
        self.assertEqual(response.status_code, 200)
        self.assertIn("API is running", response.json["message"])

if __name__ == "__main__":
    unittest.main()
