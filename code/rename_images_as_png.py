import os
from PIL import Image

path = 'C:\IDF\personal\monkeys_dataset\jpg_images'
name_of_file = 0
for subdir, dirs, files in os.walk(path):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if (filepath.endswith(".JPEG") or filepath.endswith(".jpg")):
            outputfile = os.path.join(subdir,"image%d" % name_of_file) + ".jpg"
            name_of_file += 1
            im = Image.open(filepath)
            try:
                im.save(outputfile)
            except:
                print("error")