import pygame
import os
import glob
from convert import U1, U2, U3, U4, D1, D2, D3, D4

print("Converting frames to pixel format...")
os.system("python image.py")
print(f"Converted {len(glob.glob('convImages/*'))} frames \n")

# Dont mind this, it is just for refreshing the file once the code has exectued
try:
    os.remove('src/output.ino')
except:pass
print('Creating .ino file...\n')

# Specify from which to which frame to play
# If data exceeds the limit on the board, either decrease the amount of frames or use a sd card

start, end = 1, 5255

# _______________________arduino script_______________________ #
print("Writing script...\n")
with open('src/output.txt', 'w') as f:
    f.write(f"#include <LiquidCrystal_I2C.h>\n")

    

    for i in range(start, end):
        f.write(f"const byte UA{i+1}[] PROGMEM = " + str("{" + str(U1[i])[1:-1].replace("'", "") + "};\n"))
        f.write(f"const byte UB{i+1}[] PROGMEM = " + str("{" + str(U2[i])[1:-1].replace("'", "") + "};\n"))
        f.write(f"const byte UC{i+1}[] PROGMEM = " + str("{" + str(U3[i])[1:-1].replace("'", "") + "};\n"))
        f.write(f"const byte UD{i+1}[] PROGMEM = " + str("{" + str(U4[i])[1:-1].replace("'", "") + "};\n"))

        f.write(f"const byte BA{i+1}[] PROGMEM = " + str("{" + str(D1[i])[1:-1].replace("'", "") + "};\n"))
        f.write(f"const byte BB{i+1}[] PROGMEM = " + str("{" + str(D2[i])[1:-1].replace("'", "") + "};\n"))
        f.write(f"const byte BC{i+1}[] PROGMEM = " + str("{" + str(D3[i])[1:-1].replace("'", "") + "};\n"))
        f.write(f"const byte BD{i+1}[] PROGMEM = " + str("{" + str(D4[i])[1:-1].replace("'", "") + "};\n"))
        

    f.write("const uint8_t* const frames[][8] PROGMEM = {\n")
    lists = [(U1, "UA"), (U2, "UB"), (U3, "UC"), (U4, "UD"), (D1, "BA"), (D2, "BB"), (D3, "BC"), (D4, "BD")]
    for i in range(start, end):
        set_items = []  # Items in the current set
        for list, prefix in lists:
            if i < len(list):
                set_items.append(f"{prefix}{i+1}")
        f.write("  {" + ", ".join(set_items) + "},\n")  # Write the entire set at once
    f.write("};\n")
    f.write("LiquidCrystal_I2C lcd(0x27, 16, 2);\n")
    f.write("const int totalFrames = sizeof(frames) / sizeof(frames[0]);\n\n")
    
    f.write("void setup() {\n")
    f.write("  // Initialize the LCD\n")
    f.write("  lcd.init();\n\n")
    f.write("  // Start displaying frames from the first frame\n")
    f.write("  int currentFrame = 0;\n")
    f.write("  createAndDisplayCharacters(currentFrame);\n")
    f.write("}\n\n")
    
    f.write("void createAndDisplayCharacters(int frame) {\n")
    f.write("  for (int i = 0; i < 8; i++) {\n")
    f.write("    uint8_t data[8];\n")
    f.write("    for (int j = 0; j < 8; j++) {\n")
    f.write("      data[j] = pgm_read_byte(&(frames[frame][i][j]));\n")
    f.write("    }\n")
    f.write("    lcd.createChar(i, data);  // Store the character in the LCD's memory\n\n")
    f.write("    // Display the character\n")
    f.write("    if (i < 4) {\n")
    f.write("      lcd.setCursor(i, 0);\n")
    f.write("    } else {\n")
    f.write("      lcd.setCursor(i - 4, 1);\n")
    f.write("    }\n")
    f.write("    lcd.write((uint8_t)i);\n")
    f.write("  }\n")
    f.write("}\n\n")
    
    f.write("void loop() {\n")
    f.write("  static int currentFrame = 0;\n")
    f.write("  createAndDisplayCharacters(currentFrame);\n\n")
    f.write("  // Increment the frame counter and reset if it exceeds the total frames\n")
    f.write("  currentFrame = (currentFrame + 1) % totalFrames;\n\n")
    f.write("  // Add a delay to control the frame rate\n")
    f.write("  delay(80);\n")
    f.write("}\n")
# _____________________________________________________________#
print('Done\n')

os.rename('src/output.txt', os.path.splitext('src/output.txt')[0] + '.ino')
