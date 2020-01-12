from PIL import Image

from imageai.Detection import ObjectDetection
from datetime import datetime
import os

print( datetime.now(), "\n\n\n" )

#import tensorflow as tf
#tf.compat.v1.Session()
#self.sess = tf.compat.v1.Session()

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "models/resnet50_coco_best_v2.0.1.h5"))

#detector.setModelTypeAsYOLOv3()
#detector.setModelPath( os.path.join(execution_path , "models/yolo.h5"))

#detector.setModelTypeAsTinyYOLOv3()
#detector.setModelPath("models/yolo-tiny.h5")

detector.loadModel()

#custom = detector.CustomObjects(person=True, dog=True, bird=True, cat=True, horse=True, sheep=True, cow=True, elephant=True, bear=True, zebra=True, giraffe=True)

input_dir = "/home/AI/"
output_dir = "/home/AI/"

for filename in os.listdir( input_dir ):
    if filename.endswith(".JPG") or filename.endswith(".jpg"):
        print(filename)

#        detections = detector.detectCustomObjectsFromImage( custom_objects=custom,
        detections = detector.detectObjectsFromImage(
#                input_image = os.path.join( execution_path, input_dir + filename ),
#                output_image_path = os.path.join( execution_path, output_dir + filename.split(".jpg")[0] + ".png" ),
                input_image = os.path.join( input_dir + filename ),
                output_image_path = os.path.join( output_dir + filename.split(".")[0] + ".png" ),
               # percentage output
#                display_percentage_probability=False,
               # object name output
#                display_object_name=False,
                minimum_percentage_probability=26,
                )

       # Workaround if 'jpg' is not supported
        Image.open( output_dir + filename.split(".")[0]+".png" ).convert('RGB').save( output_dir + filename ,'JPEG')
        os.remove( output_dir + filename.split(".")[0]+".png" )

        print("\n", input_dir + filename, ":")
        for eachObject in detections:
            print(eachObject["name"] , " : " , eachObject["percentage_probability"] )

print( "\n\n", datetime.now() )
