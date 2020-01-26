from PIL import Image
from imageai.Detection import ObjectDetection
from PIL import ImageOps # negative
from PIL import ImageEnhance # sharpen
from PIL import ImageDraw # draw boxes

import os
import sys # reading args from termial comand

#from time import sleep # DEVELOPMENT use

from random import randrange # random colors
from datetime import datetime

#import tensorflow as tf
#tf.compat.v1.Session()
#self.sess = tf.compat.v1.Session()

# colors
color = ["lime", "aqua", "magenta", "coral", "cyan", "darkorchid", "fuchsia"]
# random starting color
color_enum = randrange(len(color))
def set_color():
    global color_enum
    try:
        temp = color[color_enum]
    except:
        color_enum = 0
        temp = color[color_enum]
    color_enum += 1
    return temp

# negative image
def negative(img_in, img_out):
    original = Image.open( img_in ).convert('RGB')
    inverted_image = ImageOps.invert(original)
    inverted_image.save( img_out )

# sharpened image
def sharpen(img_in, img_out):
    original = Image.open( img_in ).convert('RGB')
    enhancer = ImageEnhance.Sharpness(original)
    enhancer.enhance(25/4.0).save( img_out)

# draw box + log
def draw_boxes(source, dest, img, boxes):
    mx = 80
   # compacting similar boxes (twice if number of boxes is alot)
    for i in range(0, 2):
      for index1, box in enumerate( boxes ):
        for index2, rect in enumerate( boxes ):
          if index1 != index2:
            if abs(box[0]-rect[0])<=mx and abs(box[1]-rect[1])<=mx and abs(box[2]-rect[2])<=mx and abs(box[3]-rect[3])<=mx:
             # !!! SET MAX BOX SIZE !!!
              box[0] = min(box[0], rect[0])
              box[1] = min(box[1], rect[1])
              box[2] = max(box[2], rect[2])
              box[3] = max(box[3], rect[3])
              boxes.pop(index2)

   # Draw rectangles
    output_img = Image.open(source + img).convert('RGB')
    draw = ImageDraw.Draw( output_img )
    for b in boxes:
        c = set_color()
        print(c)
        draw.rectangle(b, fill=None, outline=c, width=4)
    output_img.save(dest + img)

# search objects from loaded model
def search_animal(detector, col, infile, outfile):
   # Array for 'box_points'
    boxes = []
   # Object Clases for detection
    custom = detector.CustomObjects(person=True, dog=True, bird=True, cat=True, horse=True, sheep=True, cow=True, elephant=True, bear=True, zebra=True, giraffe=True)

    detections = detector.detectCustomObjectsFromImage( custom_objects=custom,
#    detections = detector.detectObjectsFromImage(
        input_image = infile,
        output_image_path = outfile,
       # percentage output
#        display_percentage_probability=False,
       # object name output
#        display_object_name=False,
        minimum_percentage_probability=20,
        )

#    print (detections)

    if len(detections) != 0:
      with open(log_file, "a") as f:
        f.write( "  " + col + ":\n" )
        for obj in detections:
            boxes.append( obj["box_points"] )
            f.write( "    " + str(obj["name"]) + " : " + str(obj["percentage_probability"]) + " : " + str(obj["box_points"]) + "\n" )
   # return 'box_points'
    return boxes


# ===============================================================
if __name__ == '__main__':

   # count the arguments
    arguments = len(sys.argv) - 1
#    print("\nthe script is called with %i arguments" % (arguments))
#    print(sys.argv[1])
#    print()

   # Get working directory (images, temporary files, e.t.c.) from args
    working_dir = sys.argv[1]

    execution_path = os.getcwd() + "/"
    log_file = execution_path + "output.log"
#    log_file = "/home/svabis/web/utils/ai/output.log"

    d_time = datetime.now().strftime("%Y/%m/%d %H:%M:%s")
    with open(log_file, "a") as f:
      f.write( d_time + "\n" )

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "models/resnet50_coco_best_v2.0.1.h5"))

#    detector.setModelTypeAsYOLOv3()
#    detector.setModelPath( os.path.join(execution_path , "models/yolo.h5"))

#    detector.setModelTypeAsTinyYOLOv3()
#    detector.setModelPath("models/yolo-tiny.h5")

    detector.loadModel()

    for filename in os.listdir( working_dir ):
        if filename.endswith(".JPG") or filename.endswith(".jpg"):
            with open(log_file, "a") as f:
              f.write( working_dir + filename + ":\n" )

#            print()

           # ORIGINAL DETECT
            pos_boxes = search_animal( detector, "ORIGINAL", working_dir + filename, working_dir + "temp1.png" )

           # INVERT IMAGE
            negative( working_dir + "temp1.png", working_dir + "temp2_neg_clean.png" )
           # NEGATIVE DETECT
            neg_boxes = search_animal( detector, "NEGATIVE", working_dir + "temp2_neg_clean.png", working_dir + "temp3_neg.png" )

           # SHARPEN IMAGE
            sharpen( working_dir + filename, working_dir + "temp4_sharp_clean.png" )
           # SHARPEN DETECT
            sharp_boxes = search_animal( detector, "SHARPENED", working_dir + "temp4_sharp_clean.png", working_dir + "temp5_sharp.png" )

           # INVERT SHAEPEN IMAGE
            negative( working_dir + "temp5_sharp.png", working_dir + "temp6_sharp_neg.png" )
           # SHARPEN NEGATIVE DETECT
            sharp_neg_boxes = search_animal( detector, "SHARPENED NEGATIVE", working_dir + "temp6_sharp_neg.png", working_dir + "temp6_sharp_neg.png" )

           # CLEANUP
#            os.remove( working_dir + "temp1.png" )
#            os.remove( working_dir + "temp2_neg_clean.png" )
#            os.remove( working_dir + "temp3_neg.png" )
#            os.remove( working_dir + "temp4_sharp_clean.png" )
#            os.remove( working_dir + "temp5_sharp.png" )
#            os.remove( working_dir + "temp6_sharp_neg.png" )

           # DRAW CUSTOM BOXES ON OUTPUT
            boxes = pos_boxes + neg_boxes + sharp_boxes + sharp_neg_boxes
            draw_boxes( working_dir, working_dir, filename, boxes )

#            sleep(10)

    d_time = datetime.now().strftime("%Y/%m/%d %H:%M:%s")
    with open(log_file, "a") as f:
      f.write( d_time + "\n\n\n" )

