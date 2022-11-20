from fer import FER
import matplotlib.pyplot as plt

test_image_one = plt.imread("img/ph.jpg")

emo_detector = FER(mtcnn=True)

captured_emotions = emo_detector.detect_emotions(test_image_one)
plt.imshow(test_image_one)

dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_one)
print(dominant_emotion, emotion_score)