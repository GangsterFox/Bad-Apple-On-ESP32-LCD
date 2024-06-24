Runs Bad Apple using an ESP32 and an I2C LCD, forked from SpaceWasTaken's Repo and improved.

# Quick Explain
This runs on an ESP32, all frames are stored in PROGMEM.
This should theoretically work on an Arduino as well, but I ran into a lot of issues:
* Frames are duplicated
* Garbled data shown on the LCD
* Not enough storage (PROGMEM on Arduino is just 32KB, we need around ~520KB of space for all frames)

# Running on the simulator
Make sure you have:
* PlatformIO installed
* Wokwi VSCode Extension (running it online will usually kill the build)

Once you have all of that:

1. Edit main.py with how many frames you'd like
    * currently it's set to start from frame 1 and end on frame 1898 (all frames)
2. Run main.py
    * this will create `output.ino` in `src` after converting all png's into binary
3. Run `pio run` in terminal
    * this will install the ESP32 base
4. Press `F1`, run Wokwi Simulator and done!


## [Demo](https://wokwi.com/projects/401565888569363457)