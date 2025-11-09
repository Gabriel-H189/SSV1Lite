# Seagull Scaring V1 Lite
A minimal seagull scaring program with CLI that has no external dependencies.
Sound effects come separately.

> [!WARNING]
> Seagull Scaring V1 Lite will reach end of support in July 2026. There will be no further updates to the program after this date.

### ⚠ This program will only run on Windows!

The days of having me run around scaring seagulls manually are over! With Seagull Scaring, you can just start the program, choose a time to scare seagulls for, and relax as the seagulls fly away when you want.\
Recommended settings: 2700 seconds (timer), 60 seconds (min time), 300 seconds (max time), seagull (sound).

### About this project
Seagull Scaring was created to stop the biggest problem plaguing my school since I can’t remember when. 
It has been tested to have a 98% success rate against seagulls (or shall I say gulls) of all shapes and sizes! 
Seagull Scaring V1 Lite is a minimal, user-friendly CLI interface for Seagull Scaring 1.4. 
The recommended settings are meant to be used during 1 lunchtime (45 minutes).

### Install instructions
1. Unzip the program folder.  
3. Copy a `media.zip` to the program folder, and run `main.pyw`.

### Config file documentation
In the program directory, there is a file called `ss_config.ini`.

You may edit this file as you desire.

**All settings must go in the [main] section.**

Valid settings: 

`scaring_time (int)`: How long to run the program for.

`min_time (int)`: Minimum time to wait.

`max_time (int)`: Maximum time to wait.

`default_volume (int)`: Default volume from 0-100.

`default_sound (str)`: Seagull sound to use. Valid options: seagull, sad seagull, angry seagull, confused seagull, disgust seagull, robot seagull, alarm seagull, Seagull 2, sea gull.

`autostart (str)`: Enable/disable autostart feature. Valid options: yes/no.

`autostart_delay (int)`: Delay seconds for the autostart feature.
