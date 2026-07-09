from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 1. Bổ sung thư viện CORS
from pydantic import BaseModel
import pickle
import numpy as np

# Khởi tạo API
app = FastAPI(title="API Dự Đoán Sinh Viên")

# 2. CẤU HÌNH CORS - ĐÂY LÀ ĐOẠN CODE SẼ CHỮA DỨT ĐIỂM LỖI CỦA BẠN
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Dấu * cho phép mọi trang web gọi vào (kể cả Localhost)
    allow_credentials=True,
    allow_methods=["*"],  # Cho phép các method như POST, GET...
    allow_headers=["*"],
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
