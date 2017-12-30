import pandas as pd
import numpy as np

'''
Creating a list of examples when every example is a list itself, containing the following fields:
[height, width, filename, image_format, xmins, xmaxs, ymins, ymaxs, classes_text, classes]
'''



labels_path = 'C:\IDF\personal\monkeys_dataset\labels\monkeys_labels.csv'
df = pd.read_csv(labels_path)
