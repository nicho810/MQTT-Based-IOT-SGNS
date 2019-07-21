import serial
import time
import mqtt_pub

ser = serial.Serial("/dev/ttyUSB0", 9600)

recFlag = 0


def closeSerial():
    if ser != None:
        ser.close()


def readSerial():
    # 获得接收缓冲区字符
    count = ser.inWaiting()
    if count != 0:
        # 读取内容并回显
        recv = ser.read(count)
        recv = str(recv)[2:-5]
        print("Received: " + recv)
        # 清空接收缓冲区
        ser.flushInput()
        # 必要的软件延时
        time.sleep(0.2)
        return recv
    # 清空接收缓冲区
    ser.flushInput()
    # 必要的软件延时
    time.sleep(0.2)
    return 0


def readSerial_0():
    # 获得接收缓冲区字符
    count = ser.inWaiting()
    if count != 0:
        # 读取内容并回显
        recv = ser.read(count)
        recv = str(recv)[2:-5]
        print("Received: " + recv)
    # 清空接收缓冲区
    ser.flushInput()
    # 必要的软件延时
    time.sleep(0.2)
    return 0


if __name__ == '__main__':
    try:
        while (True):
            serial_Data = readSerial()
            if (serial_Data != 0):
                mqtt_pub.pub_data(serial_Data)
                print("pub finished.")
            time.sleep(1)
    except KeyboardInterrupt:
        closeSerial()

