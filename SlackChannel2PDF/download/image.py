import urllib
import os
from subprocess import call

def download_image(user_id, image_url):
    IMAGES_DIR = 'images'

    if not os.path.exists(IMAGES_DIR):
        os.mkdir(IMAGES_DIR)
    image_path = '{}/{}.jpg'.format(IMAGES_DIR, user_id)
    urllib.urlretrieve(image_url, image_path)
    call(['convert', image_path, image_path + '.eps'])    
