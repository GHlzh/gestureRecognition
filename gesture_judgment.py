import time
import numpy as np


def find_angle(x1, y1, x2, y2, x3, y3):
    if x2 - x1 == 0 and x3 - x2 == 0:
        angle = 180
        # print("a1 a2 a3平行")
    elif x2 - x1 == 0:
        angle = np.arctan((y3 - y2) / (float(x3 - x2))) * 180 / np.pi + 90 + 0.5
        # print("a1 a2平行 ")
    elif x3 - x2 == 0:
        angle = np.arctan((y2 - y1) / (float(x2 - x1))) * 180 / np.pi + 90 + 0.5
        # print("a2 a3平行")
    else:
        # 求出斜率
        k1 = (y2 - y1) / (float(x2 - x1))
        k2 = (y3 - y2) / (float(x3 - x2))

        # 方向向量
        x = np.array([1, k1])
        y = np.array([1, k2])
        # 模长
        lx = np.sqrt(x.dot(x))
        ly = np.sqrt(y.dot(y))
        # 根据向量之间求其夹角并四舍五入
        angle = (np.arccos(x.dot(y) / (float(lx * ly))) * 180 / np.pi) + 0.5
    if angle == angle:
        angle = int(angle)
    else:
        angle = -2
    if 0 <= angle < 90:
        angle = 180 - angle
    return angle


def find_distance(x1, y1, x2, y2):
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    # 四舍五入
    distance = int(distance + 0.5)
    return distance


def thumbs_up(position_list):
    point1x = position_list[1][0]
    point1y = position_list[1][1]
    point2x = position_list[2][0]
    point2y = position_list[2][1]
    point3x = position_list[3][0]
    point3y = position_list[3][1]
    point4x = position_list[4][0]
    point4y = position_list[4][1]
    flag = False
    angle1 = find_angle(point1x, point1y, point2x, point2y, point3x, point3y)
    angle2 = find_angle(point2x, point2y, point3x, point3y, point4x, point4y)
    if angle1 > 170 and angle2 > 150:
        flag = True
    # print("angle1,2,3:", angle1)
    # print("angle2,3,4:", angle2)
    # print()
    return flag


def index_finger_up(position_list):
    point5x = position_list[5][0]
    point5y = position_list[5][1]
    point6x = position_list[6][0]
    point6y = position_list[6][1]
    point7x = position_list[7][0]
    point7y = position_list[7][1]
    point8x = position_list[8][0]
    point8y = position_list[8][1]
    # deviation1 = 300
    # deviation2 = 150
    flag = False
    # left1 = (point5y - point6y)*(point5x - point7x)
    # right1 = (point5y - point7y)*(point5x-point6x)
    # left2 = (point6y-point8y)*(point6x - point7x)
    # right2 = (point6y - point7y)*(point6x-point8x)
    # if abs(left1 - right1) <= deviation1 and abs(left2 - right2) <= deviation2:
    #     string_flag = "1"
    #     距离
    #     distance5to6 = int(((point5x - point6x) ** 2 + (point5y - point6y) ** 2) ** 0.5 + 0.5)
    #     distance6to7 = int(((point6x - point7x) ** 2 + (point6y - point7y) ** 2) ** 0.5 + 0.5)
    #     distance7to8 = int(((point7x - point8x) ** 2 + (point7y - point8y) ** 2) ** 0.5 + 0.5)
    #     if distance5to6 > 45 and distance6to7 > 30 and distance7to8 > 20:
    #         string_flag = "1"
    #     # print("5 to 6:", int(((point5x - point6x) ** 2 + (point5y - point6y) ** 2) ** 0.5 + 0.5))
    #     # print("6 to 7:", int(((point6x - point7x) ** 2 + (point6y - point7y) ** 2) ** 0.5 + 0.5))
    #     # print("7 to 8:", int(((point7x - point8x) ** 2 + (point7y - point8y) ** 2) ** 0.5 + 0.5))
    #     # print()
    # print("5", point5x, point5y)
    # print("6", point6x, point6y)
    # print("7", point7x, point7y)
    # print("8", point8x, point8y)
    # print(abs(left1 - right1))
    # print(abs(left2 - right2))
    # # time.sleep(2)
    angle1 = find_angle(point5x, point5y, point6x, point6y, point7x, point7y)
    angle2 = find_angle(point6x, point6y, point7x, point7y, point8x, point8y)
    if angle1 > 170 and angle2 > 170:
        flag = True
    print("angle5,6,7:", angle1)
    print("angle6,7,8:", angle2)
    print()
    return flag


def middle_finger_up(position_list):
    point9x = position_list[9][0]
    point9y = position_list[9][1]
    point10x = position_list[10][0]
    point10y = position_list[10][1]
    point11x = position_list[11][0]
    point11y = position_list[11][1]
    point12x = position_list[12][0]
    point12y = position_list[12][1]
    flag = False
    angle1 = find_angle(point9x, point9y, point10x, point10y, point11x, point11y)
    angle2 = find_angle(point10x, point10y, point11x, point11y, point12x, point12y)
    if angle1 > 165 and angle2 > 165:
        flag = True
    print("angle9,10,11:", angle1)
    print("angle10,11,12:", angle2)
    print()
    return flag


def ring_finger_up(position_list):
    point13x = position_list[13][0]
    point13y = position_list[13][1]
    point14x = position_list[14][0]
    point14y = position_list[14][1]
    point15x = position_list[15][0]
    point15y = position_list[15][1]
    point16x = position_list[16][0]
    point16y = position_list[16][1]
    flag = False
    angle1 = find_angle(point13x, point13y, point14x, point14y, point15x, point15y)
    angle2 = find_angle(point14x, point14y, point15x, point15y, point16x, point16y)
    if angle1 > 170 and angle2 > 170:
        flag = True
    print("angle13,14,15:", angle1)
    print("angle14,15,16:", angle2)
    print()
    return flag


def little_finger_up(position_list):
    point17x = position_list[17][0]
    point17y = position_list[17][1]
    point18x = position_list[18][0]
    point18y = position_list[18][1]
    point19x = position_list[19][0]
    point19y = position_list[19][1]
    point20x = position_list[20][0]
    point20y = position_list[20][1]
    flag = False
    angle1 = find_angle(point17x, point17y, point18x, point18y, point19x, point19y)
    angle2 = find_angle(point18x, point18y, point19x, point19y, point20x, point20y)
    if angle1 > 170 and angle2 > 170:
        flag = True
    print("angle17,18,19:", angle1)
    print("angle18,19,20:", angle2)
    print()
    return flag




