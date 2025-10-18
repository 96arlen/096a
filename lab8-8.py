class MediaFile:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def play(self):
        return f"Идёт воспроизведение {self.name}"


class AudioFile(MediaFile):
    def play(self):
        return f"Аудио '{self.name}' играет {self.time} мин"


class VideoFile(MediaFile):
    def play(self):
        return f"Видео '{self.name}' с картинкой {self.time} мин"


class Podcast(MediaFile):
    def play(self):
        return f"Подкаст '{self.name}' эпизод {self.time} мин"



files = [
    AudioFile("Песня", 4),
    VideoFile("Фильм", 120),
    Podcast("Интервью", 60)
]

for f in files:
    print(f.play())
