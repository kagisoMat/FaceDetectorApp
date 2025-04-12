import unittest
from unittest.mock import patch
import cv2
import numpy as np
from tkinter import filedialog
from image_detector import detect_faces_in_image  # Import your function here

class TestFaceDetectionToolkit(unittest.TestCase):

    @patch.object(filedialog, 'askopenfilename', return_value="test_image.jpg")  # 1st decorator
    @patch('cv2.destroyAllWindows')                                               # 2nd
    @patch('cv2.waitKey')                                                         # 3rd
    @patch('cv2.imread')                                                          # 4th
    @patch('cv2.imshow')                                                          # 5th
    def test_face_detection_image(self, mock_imshow, mock_imread, mock_wait, mock_destroy, mock_filedialog):
        # Create a mock image
        mock_image = np.zeros((100, 100, 3), dtype=np.uint8)
        mock_imread.return_value = mock_image
        mock_wait.return_value = 0

        file_path = filedialog.askopenfilename()
        detect_faces_in_image(file_path)

        mock_imshow.assert_called_with("Detected Faces", mock_image)
        mock_wait.assert_called_with(0)
        mock_destroy.assert_called()

if __name__ == '__main__':
    unittest.main()
