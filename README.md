# Bulk Extension Renamer

by [Frey Hargarten](http://github.com/jeffhargarten)

Changes files in selected folder from one extension to another. Requires [Python3](https://www.python.org/download/releases/3.0/).


To configure targets:
```bash
for filename in glob.iglob(os.path.join('FULL PATH HERE', '*.OLDEXTENSION')):
    os.rename(filename, filename[:-4] + '.NEWEXTENSION')
```


To run the application:
```bash
$ python bulk_x_rename.py <url>      
```