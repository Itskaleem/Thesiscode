import configparser
import argparse
import cv2
from utils import video_and_image_generator


ap = argparse.ArgumentParser(description='This script helps to record the video from the webcam. given different parameters')
ap.add_argument("CameraName", type=str,help="CameraName is needed: 1) kaleemCam 2) kaleemCam2 3) kaleemCam3 4) kaleemCam4")
config = configparser.ConfigParser()

try:
    config.read('config.ini')
except configparser.Error as e:
    print(f"Error reading configuration file: {e}")


# Access Global parameters
recording_time = int(config.get('GLOBAL', 'seconds'))
Root_folder = config.get('GLOBAL', 'Root_path')
video_types = config.get('GLOBAL','video_types').split(',')
args = vars(ap.parse_args())
Camera_type = args['CameraName']


match Camera_type:
    case 'KaleemCam':
        # Open the webcam
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error: Could not open webcam.")
            exit()
    
        # Get the default width and height of the frames
        frame_width = 1280
        frame_height = 720

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

        # Get the default fps of the camera
        fps = cap.get(cv2.CAP_PROP_FPS)
        # Define the codec and create a VideoWriter object to save the video
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        images_folder = config.get(Camera_type,'image_folder_path')
        videos_folder = config.get(Camera_type,'video_folder_path')
        
        
        print(recording_time,Root_folder,Camera_type,frame_width,frame_height,fps,images_folder,videos_folder)

        video_and_image_generator(Root_folder,cap,fourcc,frame_width,frame_height,fps,images_folder,videos_folder,recording_time,video_types)
        

    case 'FullHDCam':
        cap = cv2.VideoCapture(2)

        if not cap.isOpened():
            print("Error: Could not open webcam.")
            exit()

        # Get the default width and height of the frames

        frame_width = 1920
        frame_height = 1080

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

        fps = cap.get(cv2.CAP_PROP_FPS)
     
        # Define the codec and create a VideoWriter object to save the video
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        images_folder = config.get(Camera_type,'image_folder_path')
        videos_folder = config.get(Camera_type,'video_folder_path')
          
        print(recording_time,Root_folder,Camera_type,frame_width,frame_height,fps,images_folder,videos_folder)

        video_and_image_generator(Root_folder,cap,fourcc,frame_width,frame_height,fps,images_folder,videos_folder,recording_time,video_types)
        
    
    case 'HDCam': 
        cap = cv2.VideoCapture(1)

        if not cap.isOpened():
            print("Error: Could not open webcam.")
            exit()
        
        print(f'ORIGINAL WIDTH AND HEIGHT AND FPS {cap.get(3)} {cap.get(4)} {cap.get(cv2.CAP_PROP_FPS)}')

        

        # Check if the resolution was set successfully
        actual_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        actual_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        # Get the default fps of the camera
        fps = cap.get(cv2.CAP_PROP_FPS)

        # Define the codec and create a VideoWriter object to save the video
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        images_folder = config.get(Camera_type,'image_folder_path')
        videos_folder = config.get(Camera_type,'video_folder_path')
          
        print(recording_time,Root_folder,Camera_type,actual_width,actual_height,fps,images_folder,videos_folder)

        video_and_image_generator(Root_folder,cap,fourcc,actual_width,actual_height,fps,images_folder,videos_folder,recording_time,video_types)





