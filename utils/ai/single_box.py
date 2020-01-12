from PIL import Image, ImageOps, ImageDraw
from imageai.Detection import ObjectDetection
from datetime import datetime
import os

#import tensorflow as tf
#tf.compat.v1.Session()
#self.sess = tf.compat.v1.Session()

# colors
color = ["lime", "aqua", "magenta", "coral", "cyan", "darkorchid", "fuchsia"]
color_enum = 0
def set_color():
    global color_enum
    try:
        temp = color[color_enum]
    except:
        color_enum = 0
        temp = color[color_enum]
    color_enum += 1
    return temp

def negative(img):
    original = Image.open(img).convert('RGB')
    inverted_image = ImageOps.invert(original)
    inverted_image.save(img)

def draw_boxes(source, dest, img, pos, neg):
    boxes = pos + neg
    mx = 50
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
        draw.rectangle(b, fill=None, outline=set_color(), width=4)
    output_img.save(dest + img)

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

    print (detections)

    if len(detections) != 0:
      with open(log_file, "a") as f:
        f.write( "  " + col + ":\n" )
        for obj in detections:
            boxes.append( obj["box_points"] )
            f.write( "    " + str(obj["name"]) + " : " + str(obj["percentage_probability"]) + " : " + str(obj["box_points"]) + "\n" )
   # return 'box_points'
    return boxes

execution_path = os.getcwd() + "/"
#input_dir  = execution_path + "galery/"
#output_dir = execution_path + "output/"
input_dir = "/home/AI/"
output_dir = "/home/AI/"
log_file = "/home/svabis/web/utils/ai/output.log"

d_time = datetime.now().strftime("%Y/%m/%d %H:%M:%s")
with open(log_file, "a") as f:
  f.write( d_time + "\n" )

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "models/resnet50_coco_best_v2.0.1.h5"))

#detector.setModelTypeAsYOLOv3()
#detector.setModelPath( os.path.join(execution_path , "models/yolo.h5"))

#detector.setModelTypeAsTinyYOLOv3()
#detector.setModelPath("models/yolo-tiny.h5")

detector.loadModel()

for filename in os.listdir( input_dir ):
    if filename.endswith(".JPG") or filename.endswith(".jpg"):
        with open(log_file, "a") as f:
          f.write( input_dir + filename + ":\n" )

       # ORIGINAL DETECT
        pos_boxes = search_animal( detector, "POSITIVE", input_dir + filename, output_dir + filename.split(".")[0] + "_.png" )

       # INVERT IMAGE
        negative( output_dir + filename.split(".")[0] + "_.png" )

       # NEGATIVE DETECT
        neg_boxes = search_animal( detector, "NEGATIVE", output_dir + filename.split(".")[0] + "_.png", output_dir + filename.split(".")[0] + "_.png" )

       # CLEANUP .png
        os.remove( output_dir + filename.split(".")[0]+"_.png" )

       # OUTPUT IMAGE WITH CUSTOM BOXES
        draw_boxes(input_dir, output_dir, filename, pos_boxes, neg_boxes)

d_time = datetime.now().strftime("%Y/%m/%d %H:%M:%s")
with open(log_file, "a") as f:
  f.write( d_time + "\n\n" )

