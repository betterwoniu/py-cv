import os

import fitz


class Pdf2img:
    def __init__(self,path):
        self.path = path

    def run(self):
        print('开始识别图像 pdf_path: %s ' % (self.path))
        pdf = fitz.open(self.path)

        for page_num in range(len(pdf)):
            page = pdf.load_page(page_num)
            image_list = page.get_images(full=True)
            print(enumerate(image_list))
            for img_index, img_info in enumerate(image_list,start=1):
                print( img_info[0])
                print('img_info: %s ' % (img_index))
                xref = img_info[0]  # 图片的交叉引用编号
                base_image = pdf.extract_image(xref)
                image_data = base_image["image"]  # 图片二进制数据

                # 保存图片（根据图片格式自动选择扩展名）
                image_ext = base_image["ext"]
                image_path = os.path.join('../../data/', f"page{page_num + 1}_img{img_index + 1}.{image_ext}")

                with open(image_path, "wb") as img_file:
                    img_file.write(image_data)
                print(f"保存图片: {image_path}")

        pdf.close()



if __name__ == "__main__":
   Pdf2img('../../data/批量@李晴@诚信视野下的科研管理优化@青年与社会.pdf').run()