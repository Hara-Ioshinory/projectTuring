import os, cv2, datetime, csv, random


#загружаем модель
camp_ratio, directory = 10, "source"
event_count = False


def alarm_activate(alarm_type, new_activate):
    global event_count
    if 0.5 > new_activate and event_count:
        event_count = False
        print(f'Конец события: {alarm_type}, в {datetime.datetime.now()}')
        with open('logs.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Конец события', alarm_type, datetime.datetime.now()])
    elif 0.5 <= new_activate and not event_count:
        event_count = True
        print(f'Начало событие: {alarm_type}, в {datetime.datetime.now()}')
        with open('logs.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Начало события', alarm_type, datetime.datetime.now()])


for key in os.listdir(f"{directory}"):

    for vid in os.listdir(f"{directory}/{key}"):
        video_stream = cv2.VideoCapture(f"{directory}/{key}/{vid}")
        h, w = int(video_stream.get(3) / camp_ratio),  int(video_stream.get(4) / camp_ratio)
        while True:
            frame = video_stream.read()[1]
            try:
                image = cv2.cvtColor(cv2.resize(frame, (h, h)), cv2.COLOR_BGR2GRAY)
                image = cv2.createCLAHE(clipLimit=3., tileGridSize=(8, 8)).apply(image)

                cv2.imshow('Прямой вывод', cv2.resize(frame, (h*2, w*2)))
                cv2.imshow('Ввод в сеть', image)

                # Загоняем фрейм под модель
                # alarm_activate('Люди на пути', out[peoples])
                # alarm_activate('Рабочие на пути', out[workers])
                # alarm_activate('Техника на пути', out[machines])

                if cv2.waitKey(1) == ord('q'):
                    break
            except:
                video_stream.release()
                video_stream.release()
                break
