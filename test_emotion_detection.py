import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_joy_emotion(self):
        result_joy = emotion_detector("I am glad this happened")
        desired_emotion_joy = result_joy["dominant_emotion"] 
        self.assertEqual (desired_emotion_joy, "joy")

    def test_anger_emotion(self):
        result_anger = emotion_detector("I am really mad about this")
        desired_emotion_anger = result_anger["dominant_emotion"] 
        self.assertEqual (desired_emotion_anger, "anger")

    def test_disgust_emotion(self):
        result_disgust = emotion_detector("I feel disgusted just hearing about this")
        desired_emotion_disgust = result_disgust["dominant_emotion"] 
        self.assertEqual (desired_emotion_disgust, "disgust")

    def test_sadness_emotion(self):
        result_sadness = emotion_detector("I am so sad about this")
        desired_emotion_sadness = result_sadness["dominant_emotion"] 
        self.assertEqual (desired_emotion_sadness, "sadness")

    def test_fear_emotion(self):
        result_fear = emotion_detector("I am really afraid that this will happen")
        desired_emotion_fear = result_fear["dominant_emotion"] 
        self.assertEqual (desired_emotion_fear, "fear")

if __name__ == '__main__':
    unittest.main()
