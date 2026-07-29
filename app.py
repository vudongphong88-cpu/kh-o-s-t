import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Khảo sát bạn bè", page_icon="📝")
DATA_FILE = "ket_qua_khao_sat.xlsx"

def luu_du_lieu(data_moi):
    if os.path.exists(DATA_FILE):
        df_cu = pd.read_excel(DATA_FILE)
        df_moi = pd.concat([df_cu, pd.DataFrame([data_moi])], ignore_index=True)
    else:
        df_moi = pd.DataFrame([data_moi])
    df_moi.to_excel(DATA_FILE, index=False)

st.title("📋 BIỂU MẪU KHẢO SÁT SỞ THÍCH BẠN BÈ")

with st.form(key="survey_form", clear_on_submit=True):
    ho_ten = st.text_input("1. Họ và tên của bạn là gì? *")
    gioi_tinh = st.radio("2. Giới tính của bạn:", ["Nam", "Nữ", "Khác"])
    ngay_sinh = st.text_input("3. Ngày sinh theo lịch dương của bạn là ngày nào? *")
    ngay_sinhh = st.text_input("4. Ngày sinh theo lịch âm của bạn là ngày nào? *")
    do_an_yeu_thich = st.text_input("5. Đồ ăn yêu thích của bạn là gì? *")
    so_thich = st.text_input("6. Sở thích của bạn là gì? *")
    mau_sac = st.text_input("7. Màu sắc yêu thích của bạn là gì? *")
    nut_gui = st.form_submit_button(label="Gửi khảo sát")

if nut_gui:
    if not ho_ten.strip() or not email.strip():
        st.error("❌ Vui lòng điền đầy đủ Họ tên và Email!")
    else:
        thong_tin_nguoi_dung = {
            "Họ và tên": ho_ten, "Giới tính": gioi_tinh, "Ngày sinh dương lịch": ngay_sinh, "Ngày sinh âm lịch": ngay_sinhh, "Đồ ăn yêu thích": do_an_yeu_thich, "Sở thích": so_thich
        }
        luu_du_lieu(thong_tin_nguoi_dung)
        st.success("🎉 Cảm ơn bạn! Thông tin khảo sát đã được lưu vào file Excel thành công.")
# --- PHẦN BẢO MẬT: TRANG QUẢN TRỊ DÀNH RIÊNG CHO BẠN ---
st.write("---")
st.subheader("🔐 ĐĂNG NHẬP TRANG QUẢN TRỊ (CHỈ DÀNH CHO ADMIN)")

# Tạo ô nhập mật khẩu
mat_khau_nhap = st.text_input("Nhập mật khẩu để xem dữ liệu:", type="password")

# BẠN CÓ THỂ ĐỔI MẬT KHẨU TẠI ĐÂY (Thay chữ 'phong123' bằng mật khẩu bạn muốn)
MAT_KHAU_CHUAN = "2010"

# Nếu nhập đúng mật khẩu mới hiển thị bảng dữ liệu và nút tải file
if mat_khau_nhap == MAT_KHAU_CHUAN:
    st.success("🔓 Đăng nhập thành công!")
    st.subheader("📊 DANH SÁCH KẾT QUẢ KHẢO SÁT")
    
    if os.path.exists(DATA_FILE):
        df_ket_qua = pd.read_excel(DATA_FILE)
        st.dataframe(df_ket_qua) # Hiện bảng dữ liệu
        
        # Nút tải file Excel
        with open(DATA_FILE, "rb") as file:
            st.download_button(
                label="📥 Tải file Excel kết quả về máy",
                data=file,
                file_name="ket_qua_khao_sat_moi_nhat.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.info("Hiện tại chưa có ai điền khảo sát trên hệ thống Cloud.")
elif mat_khau_nhap != "":
    st.error("❌ Mật khẩu không chính xác. Vui lòng thử lại!")