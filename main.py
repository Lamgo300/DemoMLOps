from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import numpy as np


# Khởi tạo API
app = FastAPI(title="API Dự Đoán Sinh Viên")

# THÊM ĐOẠN NÀY ĐỂ CẤP QUYỀN CORS TỪ BÊN TRONG CODE PYTHON
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Hoặc thay dấu * bằng "https://lamgo300.github.io" cho chắc chắn 100%
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"], # <--- SỬA CHỖ NÀY: Khai báo rõ ràng các phương thức
    allow_headers=["Content-Type", "Authorization", "Accept"], # <--- SỬA CHỖ NÀY: Khai báo rõ các header
)

# Load mô hình (Đảm bảo file model.pkl nằm cùng thư mục)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Định nghĩa cấu trúc dữ liệu đầu vào
class StudentData(BaseModel):
    diem_giua_ky: float
    so_buoi_vang: int
    diem_tb_tich_luy: float

@app.get("/")
def read_root():
    return {"message": "Hệ thống API Dự đoán đang hoạt động!"}

@app.post("/predict")
def predict_student(data: StudentData):
    # Biến đổi dữ liệu đầu vào thành mảng numpy
    input_data = np.array([[data.diem_giua_ky, data.so_buoi_vang, data.diem_tb_tich_luy]])
    
    # Dự đoán
    prediction = model.predict(input_data)
    
    # Trả về kết quả
    result = "Đậu" if prediction[0] == 1 else "Rớt"
    return {"ket_qua": result}
