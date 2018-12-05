import os
import glob
from PIL import Image

files = glob.glob('/Users/matsudo/pyenv/syusenkou/base_collect_imgs/*')

for f in files:
    img = Image.open(f)
    img_resize = img.resize((32,32),Image.ANTIALIAS)
    ftitle, fext = os.path.splitext(f)
    img_resize.save(ftitle + '_half' + fext)
