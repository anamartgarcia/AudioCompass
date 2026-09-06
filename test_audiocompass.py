# test_audiocompass.py
"""
Tests for AudioCompass module.
"""

import unittest
from audiocompass import AudioCompass

class TestAudioCompass(unittest.TestCase):
    """Test cases for AudioCompass class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AudioCompass()
        self.assertIsInstance(instance, AudioCompass)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AudioCompass()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
