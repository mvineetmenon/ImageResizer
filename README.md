ImageResizer
============

General Description
-------------------

Python script for resizing an image depeding upon the aspect ratio user provides

API
---
	
Implements a `class ImageResizer` which accepts the filename and opens the file.

After the class is instanciated, another method `resizeImage(ratio)` can be invoked for resizing/cropping the image with maximum possible width or height as applicable for the given ratio. Ratio is given as float. eg. 16:10 as (16.0/10.0).

By default, the module when invoked directly by python interpreter, takes the filename from command line argument and the ratio as 16:10.
### API Example ###

    im = ImageResizer("/usr/local/vineet/Picture/pic1.jpg")
    im.resizeImage(1280.0/800.0)




