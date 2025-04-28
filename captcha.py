import os
import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from typing import Tuple


class CaptchaGenerator:
    def __init__(
        self,
        font_path: str = "SourceHanSansCN.otf",
        text_num: int = 4,
        pic_size: Tuple[int, int] = (360, 100),  # 稍大尺寸
        bg_color: Tuple[int, int, int] = (255, 255, 255),
        text_color: Tuple[int, int, int] = (random.randint(0, 100), random.randint(0, 100), random.randint(100, 255)),
        line_color: Tuple[int, int, int] = (random.randint(100, 255), random.randint(0, 100), random.randint(0, 100)),
        draw_line: bool = True,
        line_number: Tuple[int, int] = (2, 6),  # 更多干扰线
        draw_points: bool = True,
        point_chance: int = 5,  # 更多噪点
    ):
        """初始化验证码生成器（每次随机字体颜色）"""
        self.font_path = font_path
        self.text_num = text_num
        self.pic_size = pic_size
        self.bg_color = bg_color
        self.text_color = text_color
        self.line_color = line_color
        self.draw_line = draw_line
        self.line_number = line_number
        self.draw_points = draw_points
        self.point_chance = point_chance

        self.font = ImageFont.truetype(self.font_path, 30)  # 更大字体
        self.text = self._generate_text()

    def _generate_text(self) -> str:
        """生成随机文本（避免易混淆字符）"""
        # 移除容易混淆的字符：0O, 1lI, 9g
        chars = string.ascii_uppercase.replace("O", "").replace("I", "") + \
                string.digits.replace("0", "").replace("1", "").replace("9", "")
        return "".join(random.choices(chars, k=self.text_num))

    def _draw_lines(self, draw: ImageDraw.Draw) -> None:
        """绘制曲线干扰线"""
        for _ in range(random.randint(*self.line_number)):
            # 使用贝塞尔曲线更自然
            start = (random.randint(0, self.pic_size[0]//4), random.randint(0, self.pic_size[1]))
            control = (random.randint(self.pic_size[0]//4, 3*self.pic_size[0]//4), random.randint(0, self.pic_size[1]))
            end = (random.randint(3*self.pic_size[0]//4, self.pic_size[0]), random.randint(0, self.pic_size[1]))
            draw.line([start, control, end], fill=self.line_color, width=1, joint="curve")

    def _draw_noise(self, draw: ImageDraw.Draw) -> None:
        """绘制随机噪点（包括小线段）"""
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
                    [(x, y), (x+random.randint(1, 3), y+random.randint(1, 3))],
                    fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                    width=1
                )

    def generate(self) -> Tuple[Image.Image, str]:
        """生成验证码图像和文本"""
        image = Image.new("RGB", self.pic_size, self.bg_color)
        draw = ImageDraw.Draw(image)

        # 绘制文本（每个字符随机位置）
        x_offset = 10
        for char in self.text:
            bbox = draw.textbbox((0, 0), char, font=self.font)
            text_height = bbox[3] - bbox[1]
            y_offset = random.randint(5, self.pic_size[1] - text_height - 5)
            angle = random.randint(-15, 15)  # 随机旋转角度
            
            # 单独绘制每个字符（带旋转）
            char_img = Image.new("RGBA", (bbox[2]+10, bbox[3]+10), (0, 0, 0, 0))
            char_draw = ImageDraw.Draw(char_img)
            char_draw.text((5, 5), char, font=self.font, fill=self.text_color)
            char_img = char_img.rotate(angle, expand=1, resample=Image.BICUBIC)
            
            # 粘贴到主图像
            image.paste(char_img, (x_offset, y_offset), char_img)
            x_offset += char_img.width + random.randint(0, 5)

        # 添加干扰元素
        if self.draw_line:
            self._draw_lines(draw)
        if self.draw_points:
            self._draw_noise(draw)

        # 轻度高斯模糊增加识别难度
        image = image.filter(ImageFilter.GaussianBlur(radius=0.8))
        return image, self.text


def generate_100_captchas(output_dir: str = "captchas"):
    """批量生成100个验证码"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(os.path.join(output_dir, "captcha_log.txt"), "w") as f:
        for i in range(1, 101):
            # 每10个验证码更换一次颜色主题
            if i % 10 == 1:
                color_theme = random.choice([
                    ("blue", "red"),    # 蓝字红干扰线
                    ("green", "purple"), # 绿字紫干扰线
                    ("darkred", "gray"), # 深红字灰干扰线
                    ("black", "orange")  # 黑字橙干扰线
                ])
            
            # 根据主题设置颜色
            if color_theme[0] == "blue":
                text_color = (random.randint(0, 50), random.randint(0, 50), random.randint(150, 255))
            elif color_theme[0] == "green":
                text_color = (random.randint(0, 50), random.randint(150, 255), random.randint(0, 50))
            elif color_theme[0] == "darkred":
                text_color = (random.randint(100, 150), random.randint(0, 50), random.randint(0, 50))
            else:  # black
                text_color = (random.randint(0, 50), random.randint(0, 50), random.randint(0, 50))
            
            if color_theme[1] == "red":
                line_color = (random.randint(150, 255), random.randint(0, 50), random.randint(0, 50))
            elif color_theme[1] == "purple":
                line_color = (random.randint(150, 200), random.randint(0, 50), random.randint(150, 200))
            elif color_theme[1] == "gray":
                line_color = (random.randint(100, 150), random.randint(100, 150), random.randint(100, 150))
            else:  # orange
                line_color = (random.randint(200, 255), random.randint(100, 150), random.randint(0, 50))
            
            # 生成验证码
            generator = CaptchaGenerator(
                text_color=text_color,
                line_color=line_color,
                point_chance=random.randint(3, 7)  # 随机噪点密度
            )
            image, text = generator.generate()
            
            # 保存图片和记录文本
            image.save(os.path.join(output_dir, f"captcha_{i:03d}.png"))
            f.write(f"captcha_{i:03d}.png : {text}\n")
            
            # 进度显示
            if i % 10 == 0:
                print(f"已生成 {i}/100 个验证码")

    print(f"\n验证码生成完成！保存目录: {output_dir}")
    print(f"验证码文本记录在: {os.path.join(output_dir, 'captcha_log.txt')}")


if __name__ == "__main__":
    generate_100_captchas()