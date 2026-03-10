import subprocess
import sys


def clamp(value, min, max):
    if value < min:
        return min
    if value > max:
        return max
    return value


def clamp01(value):
    return clamp(value, 0.0, 1.0)


class Time:
    def __init__(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute

    def floating(self) -> float:
        return float(self.hour) + float(self.minute) / 60.0

    def progress(self, start, end) -> float:
        startf: float = start.floating()
        endf: float = end.floating()
        if endf < startf:
            endf = 24.0 - endf

        range = endf - startf

        return clamp01((self.floating() - startf) / range)


NIGHT_START = Time(0, 0)
DAWN_START = Time(6, 0)
DAY_START = Time(12, 0)
SUNSET_START = Time(18, 0)


IMAGE_PREFIX = "/home/lukydrum/Pictures/Cyberbiker/cyberbiker_"
IMAGES = {
    NIGHT_START: "night.png",
    DAWN_START: "dawn.png",
    DAY_START: "day.png",
    SUNSET_START: "sunset.png",
}
TMP_IMAGE = "/tmp/daytime_wallpaper.png"


class ImageCombination:
    def __init__(self, first_img: str, second_img: str, progress: float) -> None:
        self.first_img = first_img
        self.second_img = second_img
        self.progress = progress

    def apply_wallpaper(self):
        second_perc = int(self.progress * 100)
        first_perc = 100 - second_perc

        command = f"composite -blend {first_perc}x{second_perc} {self.first_img} {self.second_img} {TMP_IMAGE}"
        print(f"Running: {command}")

        subprocess.run(command.split(" "))
        subprocess.run(["swww", "img", TMP_IMAGE])


def get_image_combination(time: Time) -> ImageCombination:
    first = None
    second = None

    timef = time.floating()
    if timef >= NIGHT_START.floating() and timef < DAWN_START.floating():
        first = NIGHT_START
        second = DAWN_START
    elif timef >= DAWN_START.floating() and timef < DAY_START.floating():
        first = DAWN_START
        second = DAY_START
    elif timef >= DAY_START.floating() and timef < SUNSET_START.floating():
        first = DAY_START
        second = SUNSET_START
    else:
        first = SUNSET_START
        second = NIGHT_START

    progress = time.progress(first, second)
    return ImageCombination(
        IMAGE_PREFIX + IMAGES[first], IMAGE_PREFIX + IMAGES[second], progress
    )


if __name__ == "__main__":
    # Read and parse the time from args
    try:
        time = sys.argv[1]
        split = time.split(":")
        (hour, minute) = (int(split[0]), int(split[1]))
    except IndexError:
        print(
            "The time argument is missing or invalidly formatted. It must be in format H:M."
        )
        exit(1)

    time = Time(hour, minute)
    combination = get_image_combination(time)
    combination.apply_wallpaper()
