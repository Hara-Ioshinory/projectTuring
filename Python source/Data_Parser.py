import os, numpy
import cv2 as cv

cashed_frames = {}

def dhash(image, hashSize=16):
    resized = cv.resize(image, (hashSize + 1, hashSize))
    diff = resized[:, 1:] > resized[:, :-1]
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])


def init_data():
    directory = "source"
    for tag in os.listdir(directory):
        cashed_frames[tag] = []
    for tag in cashed_frames.keys():
        for vid in os.listdir(f"source/{tag}"):
            print(tag, vid)
            # Коэф сжатия
            camp_ratio = 4
            video_stream = cv.VideoCapture(f"source/{tag}/{vid}")
            # Расчёт параметров
            h = int(video_stream.get(3) / camp_ratio)
            w = int(video_stream.get(4) / camp_ratio)
            offset = int((h - w) / 2)
            while True:
                isTrue, frame = video_stream.read()
                # обеспечивание, обрезка и сжатие
                try:
                    image = cv.cvtColor(cv.resize(frame, (h, w)), cv.COLOR_BGR2GRAY)[0:int(h), offset:int(h) - offset]
                    # обеспечивем контраст для изображения
                    image = cv.createCLAHE(clipLimit=3., tileGridSize=(8, 8)).apply(image)
                    cashed_frames[tag].append([image, dhash(image)])
                except:
                    video_stream.release()
                    print("Выборка завершена")
                    break
    for tag in cashed_frames.keys():
        print(f"{tag}:{len(cashed_frames[tag])}")

def gen_data_update(updated_dikt, update_procent):
    print("loh")

init_data()
