from PIL import Image, ImageTk

class ImageHandler:
	__img = None
	@staticmethod
	def image(file=None):
		IH = ImageHandler(file)
		return IH

	def __init__(self, img_path):
		self.path = img_path
		try:
			self.__img = Image.open(self.path)
		except :
			self.__img = None

	@property
	def img(self):
		return self.__img

	@property
	def imgTk(self):
		return ImageTk.PhotoImage(self.__img)
	
	def display(self):
		self.__img.show()



# x = ImageHandler("../logo.png")