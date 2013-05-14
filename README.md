ImageResizer
============

General Description
-------------------

Python script for resizing an image depeding upon the aspect ratio user provides. The resizing is from center i.e. the center of both the images will be same.

Dependency
----------

###Necessary Libraries###
* Python
* Python Imaging Library (PIL)
	can be installed with command `sudo apt-get install python-imaging`. Please consult local documentation for specific instruction.

###Recommended Funtionality###
* PIL preview feature
	on linux machine, `sudo ln -s /usr/bin/eog /usr/bin/xv`. PIL uses a program called xv for previewing. In ubuntu installation, this behavior can be altered and instead of xv, the default image viewer `eog` can be used by creating a symlink.

API
---
	
Implements a `class ImageResizer` which accepts the filename and opens the file.

After the class is instanciated, another method `resizeImage(ratio)` can be invoked for resizing/cropping the image with maximum possible width or height as applicable for the given ratio. Ratio is given as float. eg. 16:10 as (16.0/10.0).

By default, the module when invoked directly by python interpreter, takes the filename from command line argument and the ratio as 16:10.
### API Example ###

    im = ImageResizer("/usr/local/vineet/Picture/pic1.jpg")
    im.resizeImage(1280.0/800.0)



Example
-------

[[/example/lena.jpg|frame|alt=Original Image]]
[[/example/0.8/lena-489x612.jpg|frame|alt=Resized with ratio 0.8]]
[[/example/1/lena-612x612.jpg|frame|alt=Resized with ratio 1]]
[[/example/1.6/lena-979x612.jpg|frame|alt=Resized with ratio 1.6]]

