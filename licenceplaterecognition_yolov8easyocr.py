# -*- coding: utf-8 -*-
"""LicencePlateRecognition-YOLOV8EasyOCR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ekkL3eA95dH1Eqltu5qwQ2zr7ZCFhaTk
"""

!git clone https://github.com/HamidrezaMohammadi-Novgorod/LicencePlateRecognition

cd /content/LicencePlateRecognition

pip install -r requirements.txt

!python predictWithOCR.py model='/content/LicencePlateRecognition/best.pt' source='/content/LicencePlateRecognition/demo.mp4'