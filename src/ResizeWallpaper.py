from PIL import Image, ImageDraw
import sys

class ImageResizer:
	def __init__(self, path):
		self.filename = path.rpartition("/")[-1].rsplit(".")[0]
		self.extension = path.rpartition("/")[-1].rsplit(".")[1]
		print self.filename, self.extension
		self.im = Image.open(path)
		self.imagesize = self.im.size
		self.imageratio = (self.imagesize[0] + 0.0)/(self.imagesize[1] + 0.0)

	def resizeImage(self, ratio):
		print "Original Size of image", self.imagesize
		if self.imageratio == ratio:
			print "Ratio Perfect, ", self.imageratio 
		elif(self.imageratio > ratio):
			#length if larger than required, length needs to be cropped
			lengthact = ratio * self.imagesize[1]
			print "Length larger ",lengthact
			extralength = self.imagesize[0] - lengthact
			print extralength	
			bbox = (int(extralength/2),0,int(self.imagesize[0]-extralength/2), self.imagesize[1])
			print bbox
			self._preview_pic(bbox)

		elif(self.imageratio < ratio):
			#width larger than required, need to be cropped
			widthact = 1/ratio * self.imagesize[0]
			print "Width larger ",widthact
			extrawidth = self.imagesize[1] - widthact
			print extrawidth
			bbox = (0,int(extrawidth/2),self.imagesize[0],int(self.imagesize[1]-extrawidth/2))
			print bbox
			self._preview_pic(bbox)

		userinput = raw_input("Do you want to confirm to this cropping? Y or N ")
		if(userinput == "Y"or userinput == 'y'):
			newim = self.im.crop(bbox)
			newim.save(self.filename+"-"+str(newim.size[0])+'x'+str(newim.size[1])+"."+ self.extension)
			newim.show()
		elif(userinput == "N"or userinput=='n'):
			print "You selected N, Exiting"
			return
	
	def _preview_pic(self, bbox):
		draw = ImageDraw.Draw(self.im)
		#Top
		draw.line((bbox[0], bbox[1], bbox[2], bbox[1]),fill="black")
		#Bottom
		draw.line((bbox[0], bbox[3], bbox[2], bbox[3]),fill="black")
		#Right
		draw.line((bbox[0], bbox[1], bbox[0], bbox[3]),fill="black")
		#Left
		draw.line((bbox[2], bbox[1], bbox[2], bbox[3]),fill="black")
		
		self.im.show()
			

if(__name__ == "__main__"):
	if len(sys.argv) < 3 :
		print "Need more arguments!\n Usage:", sys.argv[0], "<image path> <ratio>"
	else:
		ImageResizer(sys.argv[1]).resizeImage(eval(sys.argv[2]))
