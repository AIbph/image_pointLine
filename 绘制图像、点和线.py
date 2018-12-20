#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('gb18030')
from PIL import Image
from pylab import *

'''
    plot(x,y) # 默认为蓝色实线
    plot(x,y,'r*') # 红色星状标记
    plot(x,y,'go-') # 带有圆圈标记的绿线
    plot(x,y,'ks:') # 带有正方形标记的黑色虚线

    用PyLab库绘图的基本颜色格式命令
            'b' 蓝色
            'g' 绿色
            'r' 红色
            'c' 青色
            'm' 品红
            'y' 黄色
            'k' 黑色
            'w' 白色
            
    用PyLab库绘图的基本线型格式命令
            '-' 实线
            '--' 虚线
            ':' 点线
            
    用PyLab库绘图的基本绘制标记格式命令
            '.' 点
            'o' 圆圈
            's' 正方形
            '*' 星形
            '+' 加号
            'x' 叉号
                
'''

if __name__ == '__main__':
    # 读取图像到数组中
    im = array(Image.open("./img/test.jpg"))

    # 绘制图像
    imshow(im)

    # 一些点
    x = [100, 150, 200, 250]
    y = [150, 180, 200, 240]

    # 使用红色星状标记绘制点
    plot(x, y, 'rx')

    # 绘制连接前两个点的线
    plot(x[:], y[:], 'g')

    # 添加标题
    title('Plotting: "test.jpg"')

    # 是否隐藏坐标轴
    axis('off')

    # 显示绘制的图像
    show()

