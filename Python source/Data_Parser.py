import os, random
import cv2 as cv

cashed_frames, camp_ratio, directory = {}, 4, "source"


def dhash(image):
    resized = cv.resize(image, (17, 16))
    diff = resized[:, 1:] > resized[:, :-1]
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])


def init_data():
    for key in cashed_frames.keys():
        for vid in os.listdir(f"{directory}/{key}"):
            # Коэф сжатия
            video_stream = cv.VideoCapture(f"{directory}/{key}/{vid}")
            # Расчёт параметров
            h = int(video_stream.get(3) / camp_ratio)
            while True:
                frame = video_stream.read()[1]
                # обеспечивание, обрезка и сжатие
                try:
                    image = cv.cvtColor(cv.resize(frame, (h, h)), cv.COLOR_BGR2GRAY)
                    # обеспечивем контраст для изображения
                    image = cv.createCLAHE(clipLimit=3., tileGridSize=(8, 8)).apply(image)
                    cashed_frames[key].append([image, dhash(image)])
                except():
                    video_stream.release()
                    break


def gen_data_update(updated_dict, update_procent):

    result = updated_dict

    for key in updated_dict.keys():
        rcs = (result[key][x][1] for x in range(len(result[key])-1))
        for line in range(int(len(updated_dict[key]) * update_procent)):
            i = random.randint(0, len(result[key]) - 1)

            while True:
                ri = random.randint(0, len(cashed_frames[key]) - 1)
                rc = cashed_frames[key][ri][1]
                if rc not in rcs:
                    result[key][i] = cashed_frames[key][ri]
                    break

    return result


init_data()
gen_data_update(cashed_frames, 0.2)
