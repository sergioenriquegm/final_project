import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_joy_emotion(self):
        result_joy = emotion_detector("I am glad this happened")
        self.assertEqual (result_joy, "joy")

    def test_anger_emotion(self):
        result_anger = emotion_detector("I am really mad about this")
        self.assertEqual (result_anger, "anger")

    def test_disgust_emotion(self):
        result_disgust = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual (result_disgust, "disgust")

    def test_sadness_emotion(self):
        result_sadness = emotion_detector("I am so sad about this")
        self.assertEqual (result_sadness, "sadness")

    def test_fear_emotion(self):
        result_fear = emotion_detector("I am really afraid that this will happen")
        self.assertEqual (result_fear, "fear")

if __name__ == '__main__':
    unittest.main()
