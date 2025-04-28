import os

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
from typing import Tuple
#

#
#
# pic_size: Tuple[int, int] = (360, 100)
# point_chance = 5
# line_number: Tuple[int, int] = (2, 6),
#
# # 创建图像,设置尺寸及颜色
# image = Image.new("RGB", (360, 100), (255, 255, 255))
# # 设置图像字体
# font = ImageFont.truetype('../SourceHanSansCN.otf', 36)
#
# draw = ImageDraw.Draw(image)
#
# for t in range(4):
#     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
#
# for _ in range(int(pic_size[0] * pic_size[1] * point_chance / 100)):
#     # 随机点或小线段
#     if random.random() > 0.3:
#         draw.point(
#             (random.randint(0, pic_size[0]), random.randint(0, pic_size[1])),
#             fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#         )
#     else:
#         x = random.randint(0, pic_size[0])
#         y = random.randint(0, pic_size[1])
#         draw.line(
#             [(x, y), (x + random.randint(1, 3), y + random.randint(1, 3))],
#             fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
#             width=2
#         )
#
# image = image.filter(ImageFilter.GaussianBlur(2))
# image.save('test2.jpg')

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

class CaptchaGenerator(object):
    def __init__(self,
                 font_path: str = "../SourceHanSansCN.otf",
                 font_size: int = 36,
                 text_num: int = 4,
                 pic_size: Tuple[int, int] = (240, 100),
                 bg_color: Tuple[int, int, int] = (255, 255, 255),
                 text_color: Tuple[int, int, int] = (random.randint(0, 100), random.randint(0, 100),
                                                     random.randint(100, 255)),
                 line_color: Tuple[int, int, int] = (random.randint(100, 255), random.randint(0, 100),
                                                     random.randint(0, 100)),
                 draw_line: bool = True,
                 line_number: Tuple[int, int] = (2, 6),  # 更多干扰线
                 draw_points: bool = True,
                 point_chance: int = 5,  # 更多噪点

                 ):
        self.font = None
        self.text = None
        self.font_path = font_path
        self.font_size = font_size
        self.text_num = text_num
        self.pic_size = pic_size
        self.bg_color = bg_color
        self.text_color = text_color
        self.line_color = line_color
        self.draw_line = draw_line
        self.line_number = line_number
        self.draw_points = draw_points
        self.point_chance = point_chance

    def generate(self)-> Tuple[Image.Image, ImageDraw]:
        # 创建图像,设置尺寸及图片背景颜色
        image = Image.new("RGB", self.pic_size, self.bg_color)
        # 设置图像字体
        self.font = ImageFont.truetype(self.font_path, self.font_size)
        # 轻度高斯模糊增加识别难度
        image = image.filter(ImageFilter.GaussianBlur(radius=2))

        draw = ImageDraw.Draw(image)
        return image,draw


    def generate_text(self,draw:ImageDraw.Draw):
        text:str = ""
        for i in range(self.text_num):
            charText = rndChar()
            text += charText
            draw.text((60 * i + 10, 10), charText, font=self.font, fill=rndColor2())
        self.text = text

    def draw_noise(self,draw:ImageDraw.Draw):
        for _ in range(int(self.pic_size[0] * self.pic_size[1] * self.point_chance / 100)):
            # 随机点或小线段
            if random.random() > 0.3:
                draw.point(
                    (random.randint(0, self.pic_size[0]), random.randint(0, self.pic_size[1])),
                    fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                )
            else:
                x = random.randint(0, self.pic_size[0])
                y = random.randint(0, self.pic_size[1])
                draw.line(
                    [(x, y), (x + random.randint(1, 3), y + random.randint(1, 3))],
                    fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                    width=2
                )


if __name__ == "__main__":

    for i in range(100):
        captchaGenerator = CaptchaGenerator()
        image,draw = captchaGenerator.generate()
        captchaGenerator.generate_text(draw)
        captchaGenerator.draw_noise(draw)
        image.save(f"captcha_{i:03d}.png")
        with open(os.path.join("captcha_log.txt"), "a") as f:
            f.write(f"captcha_{i:03d}.png : {captchaGenerator.text}\n")


