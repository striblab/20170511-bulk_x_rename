import glob, os

for filename in glob.iglob(os.path.join('/Users/hargaja/Dropbox/jhargarten.github.io/STRIBLAB/_archive/startribune_dataviz/20141228-mfcu/components/sass', '*.scss.css')):
    os.rename(filename, filename[:-4] + '.scss')