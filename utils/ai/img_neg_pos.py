from PIL import Image, ImageOps
from imageai.Detection import ObjectDetection
from datetime import datetime
import os

#import tensorflow as tf
#tf.compat.v1.Session()
#self.sess = tf.compat.v1.Session()

def negative(img):
    original = Image.open(img).convert('RGB')
    inverted_image = ImageOps.invert(original)
    inverted_image.save(img)


def search_animal(detector, col, infile, outfile):
    custom = detector.CustomObjects(person=True, dog=True, bird=True, cat=True, horse=True, sheep=True, cow=True, elephant=True, bear=True, zebra=True, giraffe=True)

    detections = detector.detectCustomObjectsFromImage( custom_objects=custom,
#    detections = detector.detectObjectsFromImage(
        input_image = infile,
        output_image_path = outfile,
       # percentage output
#        display_percentage_probability=False,
       # object name output
#        display_object_name=False,
        minimum_percentage_probability=18,
        )

#    print (detections)
    if len(detections) != 0:
      with open(log_file, "a") as f:
        f.write( "  " + col + ":\n" )
        for obj in detections:
          f.write( "    " + str(obj["name"]) + " : " + str(obj["percentage_probability"]) + " : " + str(obj["box_points"]) + "\n" )

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
        search_animal( detector, "POSITIVE", input_dir + filename, output_dir + filename.split(".jpg")[0] + ".png" )

       # Workaround if 'jpg' is not supported
        Image.open( output_dir + filename.split(".jpg")[0]+".png" ).convert('RGB').save( output_dir + filename ,'JPEG')

       # INVERT IMAGE
        negative( output_dir + filename )
       # NEGATIVE DETECT
        search_animal( detector, "NEGATIVE", output_dir + filename, output_dir + filename.split(".jpg")[0] + ".png" )

       # Workaround if 'jpg' is not supported
        Image.open( output_dir + filename.split(".jpg")[0]+".png" ).convert('RGB').save( output_dir + filename ,'JPEG')
       # Cleanup .png
        os.remove( output_dir + filename.split(".jpg")[0]+".png" )

       # INVERT IMAGE TO ORIGINAL
        negative( output_dir + filename )

d_time = datetime.now().strftime("%Y/%m/%d %H:%M:%s")
with open(log_file, "a") as f:
  f.write( d_time + "\n\n" )

