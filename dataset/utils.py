import cv2
import os
import time
import numpy as np



def video_and_image_generator(Root_folder,cap,fourcc,frame_width,frame_height,fps,images_folder,videos_folder,recording_time,video_types):
    #CHECK IF THE QUALITY IS LOST

    for videotype in video_types:

        out = cv2.VideoWriter(os.path.join(Root_folder,videos_folder,f'video_{videotype}.mp4'), fourcc, fps, (frame_width,frame_height))
        response = input(f'Are you ready Recording {videotype} type video:\n1 for yes \n2 for Abort the program\n')
        # Check if VideoWriter is opened successfully
        if response == '2':
            print('Aborting the program..')
            exit(0)  
        
        if not out.isOpened():
            print("Error: Could not open VideoWriter.")
            exit(1)

        frame_folder = os.path.join(Root_folder,images_folder,f'video_{videotype}')    
        
        if create_destination_image_folder(frame_folder):
            print(f"Successfully created the folder {frame_folder}")
        

        start = time.time()
        end_time = start + recording_time
        
        while True:
            # Capture frame-by-frame
            if time.time() < end_time:
                _ , frame = cap.read()

                # Display the frame with bounding boxes and keypoints
                cv2.imshow('Output video', frame)
                # Write the frame to the output video file
                out.write(frame)

                # Check for key press 'q' to exit the loop
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            elif time.time() >= end_time+2:
                print('Recording is done')
                break 

        # Destroy all OpenCV windows
        cv2.destroyAllWindows()

    # Introduce a short delay (adjust the sleep time as needed)
    # Release the video capture and writer objects
    cap.release()
    out.release()

def create_destination_image_folder(folder_path):

    # Create the folder
    os.makedirs(folder_path, exist_ok=True)

    # Check if the folder has been created
    if os.path.exists(folder_path):
        return True
    else:
        return False
