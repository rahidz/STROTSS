#Set everything up

from pathlib import Path
import sys
import os

CONTENT_IMAGE=str(sys.argv[1])
STYLE_IMAGE=str(sys.argv[2])

content=Path(CONTENT_IMAGE).stem
style=Path(STYLE_IMAGE).stem

OUT_DIR="MyDrive/strotss/"+content+style
os.makedirs(OUT_DIR, exist_ok=True)

os.system("python3 strotss.py --weight 0.50 --resize_to 1024 --output " + OUT_DIR + "/out50.png " + CONTENT_IMAGE + " " + STYLE_IMAGE)

os.system("python3 strotss.py --weight 0.75 --resize_to 1024 --output " + OUT_DIR + "/out75.png " + CONTENT_IMAGE + " " + STYLE_IMAGE)

os.system("python3 strotss.py --weight 0.85 --resize_to 1024 --output " + OUT_DIR + "/out85.png " + CONTENT_IMAGE + " " + STYLE_IMAGE)

os.system("python3 strotss.py --weight 1.00 --resize_to 1024 --output " + OUT_DIR + "/out100.png " + CONTENT_IMAGE + " " + STYLE_IMAGE)