import numpy as np
# Nguy cơ cháy rừng
A = np.array([[3,1,0,0,1], [2,1,2,3,0], [2,2,2,0,0], [2,2,1,1,2]])
# Nguy cơ lũ quét
B = np.array([[0,0,1,0,2], [1,1,2,2,2], [2,1,2,1,1], [1,1,2,0,0]])
# Nguy cơ sạt lở núi
C = np.array([[0,1,1,1,1], [2,2,2,2,2], [1,0,0,1,1], [1,0,0,2,2]])
# Nguy cơ bệnh dịch
D = np.array([[5,0,0,3,1], [1,1,1,2,2], [0,1,2,1,1], [0,0,1,1,0]])
# Nguy cơ lộ bí mật
E = np.array([[0,0,0,0,0], [1,1,1,0,0], [0,0,0,0,0], [5,0,3,0,0]])

def dong_quan(nguy_co):
    tong_nguy_co = sum(nguy_co)
    an_toan = (tong_nguy_co <= 5).astype(int)
    return  an_toan, tong_nguy_co

kich_ban = {
    'a. Chiến dịch ngắn hạn (chỉ xét lộ bí mật)': [E],
    'b. Tập luyện thời bình (không xét lộ bí mật và bệnh dịch)': [A, B, C],
    'c. Mùa khô (không lũ, không sạt nhưng có cháy và bệnh)': [A, C, D],
    'd. Mùa mưa (có lũ, sạt, bệnh nhưng không cháy)': [B, C, D],
    'e. 8 tháng (xét toàn bộ nguy cơ)': [A, B, C, D, E],
}

for ten, nguy_co in kich_ban.items():
    an_toan, tong_nguy_co = dong_quan(nguy_co)
    print(f"\n{ten}")
    print("Tổng nguy cơ:")
    print(tong_nguy_co)
    print("Mặt nạ an toàn (1=an toàn, 0=nguy hiểm):")
    print(an_toan)