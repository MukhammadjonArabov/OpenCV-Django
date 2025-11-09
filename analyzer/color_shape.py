import cv2
import numpy as np
from collections import Counter
COLORS = {
    "Qizil": (0,0,255), "Yashil": (0,255,0), "Ko‘k": (255,0,0),
    "Sariq": (0,255,255), "Binafsha": (128,0,128), "Oq": (255,255,255),
    "Qora": (0,0,0), "Kulrang": (128,128,128)
}
def color_distance(c1, c2):
    return np.linalg.norm(np.array(c1).astype('int') - np.array(c2).astype('int'))
def find_nearest_color(bgr_pixel):
    min_d = float('inf'); name = "Noma'lum"
    for n,c in COLORS.items():
        d = color_distance(bgr_pixel, c)
        if d < min_d:
            min_d = d; name = n
    return name
def analyze_image_colors_shapes(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(image_path)
    result = img.copy()
    # colors
    small = cv2.resize(img, (200,200))
    pixels = small.reshape(-1,3)
    names = [find_nearest_color(tuple(p)) for p in pixels]
    counts = Counter(names)
    colors = [(k, round(v/len(pixels)*100,2)) for k,v in counts.items() if v/len(pixels)*100 >= 0.5]
    # shapes
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(blur, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    shapes = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 500: continue
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
        sides = len(approx)
        if sides == 3: shape = 'UCHBURCHAK'
        elif sides == 4:
            x,y,w,h = cv2.boundingRect(approx)
            aspect = w/float(h)
            shape = 'KVADRAT' if 0.95<=aspect<=1.05 else 'TO\'RTBURCHAK'
        elif sides > 6: shape = 'AYLANA'
        else: shape = f'{sides}-Burchak'
        M = cv2.moments(cnt)
        if M['m00']!=0:
            cx = int(M['m10']/M['m00']); cy = int(M['m01']/M['m00'])
        else:
            cx,cy = 0,0
        shapes.append((shape,cx,cy,area))
        cv2.drawContours(result, [cnt], -1, (0,255,0), 2)
        cv2.putText(result, shape, (max(cx-40,0), max(cy,20)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255),2)
    out = 'analyzed_result.jpg'
    cv2.imwrite(out, result)
    return out, colors, shapes
