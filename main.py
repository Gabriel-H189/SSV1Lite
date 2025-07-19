import winsound
import random
import time
import datetime
import configparser


random.seed()

# Read config file
parser = configparser.ConfigParser()
parser.read("ss_config.ini")

config = parser.sections()

timer = int(parser[config[0]]["scaring_time"])
min_time = int(parser[config[0]]["min_time"])
max_time = int(parser[config[0]]["max_time"])
sound = parser[config[0]]["default_sound"]

# Play sound in a loop waiting for a random number of seconds until timer equals 0
seagulls = 0
while timer > 0:
    winsound.PlaySound(sound + ".wav", winsound.SND_ASYNC)
    pause = random.randint(min_time, max_time)
    timer -= pause
    seagulls += 1
    print("Approximately", seagulls, "seagull(s) were scared on", datetime.datetime.now())
    if timer == 0:
        break
    time.sleep(pause)

print("Done!")
print("Approximately", seagulls, "seagull(s) were scared on", datetime.datetime.now())
