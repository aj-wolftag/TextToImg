import os, io
from google.cloud import vision
from saveIntoJson import parseData
import json
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS']= r'numberpltdetect-a8d863127b3b.json'
client = vision.ImageAnnotatorClient()

path = "imgs/test-plate-img.jpeg"


with io.open(path,'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)
response = client.text_detection(image=image)
texts = response.text_annotations
df = pd.DataFrame(columns=['locale','description'])

for text in texts:
    df = df.append(
        dict(
            locale = text.locale,
            description = text.description
        ),
        ignore_index = True
    )
    
print('Texts:')
print(df)
parseData(df)

if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
