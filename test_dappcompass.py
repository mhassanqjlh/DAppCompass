# test_dappcompass.py
"""
Tests for DAppCompass module.
"""

import unittest
from dappcompass import DAppCompass

class TestDAppCompass(unittest.TestCase):
    """Test cases for DAppCompass class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DAppCompass()
        self.assertIsInstance(instance, DAppCompass)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DAppCompass()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
