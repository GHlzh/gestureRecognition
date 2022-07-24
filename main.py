import cv2
from mediapipe import solutions
import mediapipe as mp
import time
import gesture_judgment
cap = cv2.VideoCapture(0)  # 设置摄像头 0是默认的摄像头 如果你有多个摄像头的话呢，可以设置1,2,3....
# while True:  # 进入无限循环
#     ret, frame = cap.read()  # 将摄像头拍到的图像作为frame值
#     cv2.imshow('frame', frame)  # 将frame的值显示出来 有两个参数 前一个是窗口名字，后面是值
#     if cv2.waitKey(1) == ord('a'):  # 判断退出的条件 当按下'Q'键的时候呢，就退出
#         break
# cap.release()  # 常规操作
# cv2.DestroyAllWindows()
mpHands = mp.solutions.hands  # 获取手部对象
hands = mpHands.Hands(min_detection_confidence=0.7)
mpDraw = solutions.drawing_utils  # 描绘线条的对象，定义线的粗、颜色等
junction = mpDraw.DrawingSpec(circle_radius=3, color=(123, 214, 63))
connectingLine = mpDraw.DrawingSpec(thickness=3, color=(244, 233, 42))
previousTime = 0
currentTime = 0
string_flag = ""
while True:
    success, img = cap.read()  # success的值为T和F，反应是否读到图像
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # imgRGB = cv2.flip(imgRGB, 1)
    results = hands.process(imgRGB)  # 返回一个“multi_hand_landmarks”字段，其中包含每个检测到的手上的手部标志。
    # img.shape[]第一个元素是高度，第二个元素是宽度，第三个元素是通道数，RGB格式通道数为3
    # RGB格式下每一个像素点有3个值，shape是一个3维数组
    imgHeight = img.shape[0]
    imgWidth = img.shape[1]
    positionList = []  # 坐标列表
    if results.multi_hand_landmarks:  # 检测/跟踪的手，其中每个手被表示为21层的手的地标列表以及每个界标由收集x，y和z。 x和y分别 [0.0, 1.0]通过图像的宽度和高度进行归一化
        for handLms in results.multi_hand_landmarks:
            # handLms:一个“multi_hand_landmarks”字段
            # mpHands.HAND_CONNECTIONS:连接线(设为none则没有连接线)
            # mpDraw.DrawingSpec(circle_radius=3, color=(123, 214, 63)):连接点半径,颜色
            # mpDraw.DrawingSpec(thickness=3, color=(244, 233, 42)):连接线的粗细，颜色
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS, junction, connectingLine)
            string_flag = "None"
            for i, lm in enumerate(handLms.landmark):
                x_position = int(lm.x * imgWidth)
                y_position = int(lm.y * imgHeight)
                nowPosition = []
                nowPosition.append(x_position)
                nowPosition.append(y_position)
                # if x_position == None :
                #     nowPosition.append(-1)
                # else:
                #     nowPosition.append(x_position)
                # if y_position == None :
                #     nowPosition.append(-1)
                # else:
                #     nowPosition.append(y_position)
                positionList.append(nowPosition)
                # print(i, x_position, y_position)
                # cv2.putText可以在图像上置文本
                # 参数1是对象，参数2是文本值，参数3是位置，参数4是文本字体样式，参数5是大小，参数6是颜色，参数7是粗细
                cv2.putText(img, str(i), (x_position-25, y_position+5), cv2.FONT_HERSHEY_SIMPLEX,
                            0.4, (0, 0, 255), 2)
                # # 大拇指加粗
                # if i == 4:
                #     # lineType： 圆边界的类型。
                #     # shift：中心坐标和半径值中的小数位数
                #     cv2.circle(img, (x_position, y_position), 10, (0, 0, 255), cv2.FILLED)

                # cv2.putText(img, str(i), (x_position - 25, y_position + 5), cv2.FONT_HERSHEY_SIMPLEX,
                #             0.4, (0, 0, 255), 2)
            # print(positionList)
            # string_flag = gesture_judgment.is_one(positionList)
            cv2.putText(img, string_flag, (30, 50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 56, 75))
    # 计算FPS
    # currentTime = time.time()
    # fps = 1/(currentTime-previousTime)
    # previousTime = currentTime
    # # 打印FPS
    # cv2.putText(img, f"FPS:{int(fps)}", (30, 50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0))
    # cTime = time.time()
    # fps = 1 / (cTime - pTime)
    # pTime = cTime
    # cv2.putText(img, str(int(fps)), (25, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) == 27:
        break
cap.release()  # 常规操作
# cv2.DestroyAllWindows()
