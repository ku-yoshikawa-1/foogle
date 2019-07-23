from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import pprint
from functools import reduce
from operator import add

'''
前処理. 画像をnp.arrayに突っ込んで処理しやすくする
'''
# 元となる画像の読み込み
img = Image.open('test.png')
#オリジナル画像の幅と高さを取得
width, height = img.size
print(width, height)

img_pixels = []
for y in range(height):
  for x in range(width):
    # getpixel((x,y))で左からx番目,上からy番目のピクセルの色を取得し、img_pixelsに追加する
    img_pixels.append(img.getpixel((x,y)))
# あとで計算しやすいようにnumpyのarrayに変換しておく
img_pixels = np.array(img_pixels)


# 列ごとに見てみる
#height = 100
'''
縦方向をチェックする
'''
#line = Image.new('RGB', (1, height))
threshold = 20000
diff_arr = []
length_hash = {}

def add_hash(count, x, start):
  if count in length_hash:
    length_hash[count].append((x, start))
  else:
    length_hash[count] = [(x, start)]

for x in range(width):
  prev_y = None
  line_diff = []
  count = 0
  start = 0
  for y in range(height):
    pix_value = img.getpixel((x,y))
    #line.putpixel((0,y), pix_value[:3])
    if not prev_y:
      prev_y = pix_value
    else:
      #print(list(zip(pix_value, prev_y)))
      dr, dg, db, = list(map(lambda x: x[0]-x[1], zip(pix_value, prev_y)))[:3] # delta-Red, delta-Green, delta-Blue
      color_distance = 2*(dr**2) + 4*(dg**2) + 3*(db**2)
      if color_distance >= threshold:
        add_hash(count, x, start)
        #line_diff.append(((x, start), count))
        count = 0
        start = y
      prev_y = pix_value
    count += 1
  
  add_hash(count, x, start)

### 長さと頻度を可視化 ###
x_axis = []
y_axis = []
for k in length_hash:
  x_axis.append(k)
  y_axis.append(len(length_hash[k]))
plt.scatter(x_axis, y_axis)
plt.show()

### 長さの大きい方から10個プロット
