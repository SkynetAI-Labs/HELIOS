
import unittest

from router import route_task


class TestHeliosRouter(unittest.TestCase):

    def test_cipher(self):
        self.assertEqual(
            route_task("Analyse Solana wallets"),
            "CIPHER"
        )

    def test_oscar(self):
        self.assertEqual(
            route_task("Deploy Docker containers"),
            "OSCAR"
        )

    def test_gtm(self):
        self.assertEqual(
            route_task("Find sales prospects"),
            "GTM"
        )

    def test_nova(self):
        self.assertEqual(
            route_task("Research cybersecurity"),
            "NOVA"
        )

    def test_default(self):
        self.assertEqual(
            route_task("Help me with something"),
            "NOVA"
        )


if __name__ == "__main__":
    unittest.main()
