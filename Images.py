# 黑白、模糊、细节、边缘
from PIL import Image
from PIL import ImageFilter

wuxi = Image.open('wuxi.jpg')  # 打开图像
black_white = wuxi.convert('L')  # 转化成黑白
blur = wuxi.filter(ImageFilter.BLUR)  # 模糊
detail = wuxi.filter(ImageFilter.DETAIL)  # 细节
edges = wuxi.filter(ImageFilter.FIND_EDGES)  # 边缘

black_white.show()
blur.show()
detail.show()
edges.show()

# 调整尺寸
from PIL import Image

wuxi = Image.open('wuxi.jpg')
square_wuxi = wuxi.resize((250, 250))
flip_wuxi = wuxi.transpose(Image.FLIP_LEFT_RIGHT)
spin_wuxi = wuxi.transpose(Image.ROTATE_270)
# wuxi.show()
# square_wuxi.show()
# flip_wuxi.show()
spin_wuxi.show()

# 修改图片RGB通道
from PIL import Image

wuxi = Image.open('wuxi.jpg')
moi = Image.open('moi.jpg')
r1, g1, b1 = wuxi.split()
r2, g2, b2 = moi.split()

new_img = Image.merge('RGB', (b1, g2, r1))  
# 尺寸一样的图片可以进行各个通道数据的混合
new_img.show()
# r.show()

# 叠加两张图片
from PIL import Image

wuxi = Image.open('wuxi.jpg')
moi = Image.open('moi.jpg')

area = (0, 0, 189, 264)
wuxi.paste(moi, area)

wuxi.show()

# 裁剪图片
from PIL import Image

img = Image.open('wuxi.jpg')
print(img.size)   # 打印图片尺寸信息
print(img.format) # 打印图片格式信息
area = (100, 100, 300, 375)
cropped_img = img.crop(area)

# img.show()
cropped_img.show()
