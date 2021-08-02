import unittest
import uuid

from uuid_generator import app


def bytes_to_str(b):
    return ''.join(chr(x) for x in (b))


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.app.test_client()

    def test_uuid_generator(self):
        resp = self.client.get("/")
        assert uuid.UUID(bytes_to_str(resp.data))
