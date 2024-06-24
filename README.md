Runs Bad Apple using an ESP32 and an LCD, forked from SpaceWasTaken's Repo and improved.

# Quick Explain
This runs on an ESP32, all frames are stored in PROGMEM.
This should theoretically work on an Arduino as well, but I ran into a lot of issues:
* Frames are duplicated
* Garbled data shown on the LCD
* Not enough storage (PROGMEM on Arduino is just 32KB, we need around ~520KB of space for all frames)
## 2 different variations
* `main.py` is to create the version with I2C, much slower than running the LCD directly in the simulator ([diagram](https://github.com/GangsterFox/Bad-Apple-On-ESP32-LCD/blob/main/diagram.json))
* `mainNoI2C.py` is to create the version without I2C, runs much faster on the simulator ([diagram](https://github.com/GangsterFox/Bad-Apple-On-ESP32-LCD/blob/main/diagramNoI2C.json))

# Running on the simulator
Make sure you have:
* PlatformIO installed
* Wokwi VSCode Extension (running it online will usually kill the build)
* Choose what you want to use:
    * If you want to use I2C, continue the guide as written below
    * If you don't want to use I2C: 
        * delete the current diagram
      * rename `diagramNoI2C.json` to `diagram.json` 
      * run `mainNoI2C.py` to get the correct .ino file. From here, follow step 3 below.

Once you have all of that:

1. Edit main.py with how many frames you'd like
    * currently it's set to start from frame 1 and end on frame 1898 (all frames)
2. Run main.py
    * this will create `output.ino` in `src` after converting all png's into binary
3. Run `pio run` in terminal
    * this will install the ESP32 base
4. Press `F1`, run Wokwi Simulator and done!


## [Demo I2C](https://wokwi.com/projects/401565888569363457)
