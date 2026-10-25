import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_returns_text(self):
        self.assertIn('emotionPredictions', emotion_detector('I am glad this happened'))

if __name__ == "__main__":
    unittest.main()