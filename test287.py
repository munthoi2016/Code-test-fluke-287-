#fluke287
import serial
import time

def read_ampe_value():
    try:
        # Mở kết nối với cổng COM, điều chỉnh 'COM1' thành cổng COM thích hợp
        ser = serial.Serial('COM3', baudrate=115200, timeout=1)
        print("Connected to Fluke 287")
        
        while True:
            # Gửi lệnh đọc giá trị dòng điện Ampe đến đồng hồ Fluke 287
            ser.write(('QM' + '\r').encode('utf-8'))
            
            # Đọc dữ liệu trả về từ đồng hồ Fluke 287
            response = ser.readline().decode("utf-8").strip()
            
            # In giá trị dòng điện Ampe đọc được
            print("Current Value:", response)
            
            # Chờ 1 giây trước khi đọc giá trị mới
            time.sleep(0.1)
            
    except serial.SerialException as e:
        print("Error:", e)

if __name__ == "__main__":
    read_ampe_value()
