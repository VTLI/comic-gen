import os
import cv2
import re

source_path = 'YOUR\COMICS\SOURCE\PATH'
resize_save_location = 'YOUR:\\SAVE\\LOCATION\\FOR\\RESIZED\\OUTPUT'
target_image_height = 400


for root, dirs, files in os.walk(source_path, topdown=True):
    for filename in files:
        if filename.endswith('.jpg') or filename.endswith('.JPG') or filename.endswith('.jpeg') or filename.endswith(
                '.JPEG'):
            file_path = os.path.join(root, filename)
            save_path = os.path.join(
                resize_save_location,
                root[-70:].replace(" ", "_").replace("\\", "_").replace(":", "_")
                + filename[:-4] + '_resize_' + str(target_image_height) + '.jpg'
            )

            # cleaned_save_path = re.sub(r'[^\x00-\x7f]', r'', save_path)
            if '／' in file_path:
                new_filename = file_path.replace("／", "_")
                if not os.path.isfile(new_filename):
                    os.renames(file_path, new_filename)
                save_path.replace("／", "_")
                print('Renamed: %s' % new_filename)
                file_path = new_filename

            if os.path.isfile(save_path):
                print('Already resized: ' + save_path)
                continue

            print('Resize: ' + file_path)

            try:
                orig_img = cv2.imread(file_path)

                height, width, depth = orig_img.shape
                imgScale = target_image_height / height
                newX, newY = orig_img.shape[1] * imgScale, orig_img.shape[0] * imgScale

                new_img = cv2.resize(orig_img, (int(newX), int(newY)))
                cv2.imwrite(save_path, new_img)
                print('Save: ' + save_path)
            except Exception as e:
                print('Excluded: %s' % file_path)
                print(str(e))
