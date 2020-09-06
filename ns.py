# Then multires based on neural-style-pt...
# Example based on: https://github.com/ProGamerGov/neural-style-pt/blob/master/examples/scripts/starry_stanford.sh

#Set everything up

from pathlib import Path
import sys
import os

CONTENT_IMAGE=str(sys.argv[1])
STYLE_IMAGE=str(sys.argv[2])
CONTENT_WEIGHT=str(sys.argv[3])
STYLE_WEIGHT=str(sys.argv[4])
STYLE_SCALE=str(sys.argv[5])
ORIGINAL_COLORS=(sys.argv[6])
multipleimages=False
colorTransfer=False

content=Path(CONTENT_IMAGE).stem
style=Path(STYLE_IMAGE).stem
cw=str(CONTENT_WEIGHT)
sw=str(STYLE_WEIGHT)
scale=str(STYLE_SCALE)
oc=str(ORIGINAL_COLORS)

if ',' in STYLE_IMAGE:
    multipleimages=True
	
if ORIGINAL_COLORS == "0" and multipleimages == False:
	colorTransfer=True	

if multipleimages == False:
	OUT_DIR="MyDrive/neuralstyle/"+content+"_"+style+"_"+cw+"_"+sw+"_"+scale+"_"+oc
else:
	style=os.path.splitext(STYLE_IMAGE)
	stylelist=style[0].split(",")
	laststyle=str(stylelist[-1])
	OUT_DIR="MyDrive/neuralstyle/"+content+"_"+laststyle+"_"+cw+"_"+sw+"_"+scale+"_"+oc
			
os.makedirs(OUT_DIR, exist_ok=True)

os.system("python3 neural_style.py -content_image " + CONTENT_IMAGE + " -style_image " + STYLE_IMAGE + " -style_scale " + STYLE_SCALE + " -print_iter 1000 -save_iter 0 -num_iterations 1000 -content_weight " + CONTENT_WEIGHT + " -style_weight " + STYLE_WEIGHT + " -image_size 256 -content_layers relu1_1,relu2_1,relu3_1,relu4_1,relu5_1 -style_layers relu1_1,relu2_1,relu3_1,relu4_1,relu5_1 -output_image " + OUT_DIR +"/X0.png -tv_weight 0.00001 -gpu 0 -model_file MyDrive/models/vgg19-d01eb7cb.pth -backend cudnn -cudnn_autotune")

PREV=OUT_DIR+"/X0.png"

if colorTransfer == True:
    os.system("python3 linear-color-transfer.py --target_image " + PREV + " --source_image " + STYLE_IMAGE + " --mode chol --output_image " + OUT_DIR + "/histstyleX0.png")
    PREV=OUT_DIR+"/histstyleX0.png"

os.system("python3 neural_style.py -content_image " + CONTENT_IMAGE + " -style_image " + STYLE_IMAGE + " -init image -init_image " + PREV + " -style_scale " + STYLE_SCALE + " -print_iter 1000 -save_iter 0 -num_iterations 1000 -content_weight " + CONTENT_WEIGHT + " -style_weight " + STYLE_WEIGHT + " -image_size 512 -model_file MyDrive/models/nyud-fcn32s-color-heavy.pth -content_layers relu1_1,relu2_1,relu3_1,relu4_1,relu5_1 -style_layers relu1_1,relu2_1,relu3_1,relu4_1,relu5_1 -output_image " + OUT_DIR +"/X1.png -tv_weight 0.00001 -gpu 0 -backend cudnn -cudnn_autotune")

PREV=OUT_DIR+"/X1.png"

if colorTransfer == True:
    os.system("python3 linear-color-transfer.py --target_image " + PREV + " --source_image " + STYLE_IMAGE + " --mode chol --output_image " + OUT_DIR + "/histstyleX1.png")
    PREV=OUT_DIR+"/histstyleX1.png"

os.system("python3 neural_style.py -content_image " + CONTENT_IMAGE + " -style_image " + STYLE_IMAGE + " -init image -init_image " + PREV + " -style_scale " + STYLE_SCALE + " -print_iter 1500 -save_iter 0 -num_iterations 1500 -content_weight " + CONTENT_WEIGHT + " -style_weight " + STYLE_WEIGHT + " -image_size 1024 -model_file MyDrive/models/nyud-fcn32s-color-heavy.pth -content_layers relu1_1,relu2_1,relu3_1,relu4_1,relu5_1 -style_layers relu1_1,relu2_1,relu3_1,relu4_1,relu5_1 -output_image " + OUT_DIR +"/X2.png -tv_weight 0.00001 -gpu 0 -backend cudnn -cudnn_autotune")

PREV=OUT_DIR+"/X2.png"

STYLE_WEIGHT=int(float(STYLE_WEIGHT))/10
CONTENT_WEIGHT=int(float(CONTENT_WEIGHT))/5

STYLE_WEIGHT=str(STYLE_WEIGHT)
CONTENT_WEIGHT=str(CONTENT_WEIGHT)

if colorTransfer == True:
    os.system("python3 linear-color-transfer.py --target_image " + PREV + " --source_image " + STYLE_IMAGE + " --mode chol --output_image " + OUT_DIR + "/histstyleX2.png")
    PREV=OUT_DIR+"/histstyleX2.png"

os.system("python3 neural_style.py -content_image " + CONTENT_IMAGE + " -style_image " + STYLE_IMAGE + " -init image -init_image " + PREV + " -style_scale " + STYLE_SCALE + " -print_iter 1200 -save_iter 0 -num_iterations 1200 -content_weight " + CONTENT_WEIGHT + " -style_weight " + STYLE_WEIGHT + " -image_size 1800 -model_file MyDrive/models/nyud-fcn32s-color-heavy.pth -output_image " + OUT_DIR +"/X3.png -tv_weight 0.00001 -gpu 0 -backend cudnn")

PREV=OUT_DIR+"/X3.png"

if colorTransfer == True:
    os.system("python3 linear-color-transfer.py --target_image " + PREV + " --source_image " + STYLE_IMAGE + " --mode chol --output_image " + OUT_DIR + "/" + content+"_"+style+"_"+"histstyleX3.png")
    PREV=OUT_DIR+"/histstyleX3.png"