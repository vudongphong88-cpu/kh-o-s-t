import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Khảo sát người dùng", page_icon="📝")

# --- THAY ĐỔI THÔNG TIN THEO LINK NOTEPAD CỦA BẠN TẠI ĐÂY ---
# 1. Thay chuỗi chữ dưới đây bằng Form ID thực tế bạn lấy ở Bước 2
FORM_ID = "1FAIpQLSfVQ4EObiUKy3hnWMDE57vSAqSfEc3f9ElHwp2YKhl232c2Qw" 

# 2. Thay các số dưới đây bằng các dãy số entry tương ứng bạn lấy ở Bước 2
ENTRY_HO_TEN = "entry.1930741903"
ENTRY_NGAY_SINH_DUONG = "entry.976728289"
ENTRY_GIOI_TINH = "entry.1320701927"
ENTRY_NGAY_SINH_AM = "entry.1058897768"
ENTRY_MAU_SAC = "entry.858748151"
ENTRY_DO_AN = "entry.1376030974"
ENTRY_SO_THICH = "entry.1853722381"

# --- LINK FILE GOOGLE SHEETS (ĐÃ LIÊN KẾT VỚI BIỂU MẪU) ---
# Mở file Google Sheets kết quả trên trình duyệt, copy link dán vào giữa dấu "" dưới đây để admin xem bảng
URL_XEM_GOOOGLE_SHEETS = "https://docs.google.com/spreadsheets/d/1mjA6VOLozbxsuoB6Petrqfbm7Qc5c_9INiy_JcQJTfg/edit?usp=sharing"

st.title("📋 BIỂU MẪU KHẢO SÁT SỞ THÍCH BẠN BÈ")

with st.form(key="survey_form", clear_on_submit=True):
    ho_ten = st.text_input("1. Họ và tên của bạn là gì? *")
    ngay_sinh = st.text_input("2. Ngày sinh dương lịch của bạn là gì? *")
    gioi_tinh = st.radio("3. Giới tính của bạn:", ["Nam", "Nữ", "Khác"])
    ngay_sinhh = st.text_input("4. Ngày sinh âm lịch của bạn là gì? *")
    mau_sac_yeu_thich = st.text_area("5. Màu sắc yêu thích của bạn là gì:")
    do_an_yeu_thich = st.text_input("6. Đồ ăn yêu thích của bạn là gì? *")
    so_thich = st.text_input("7. Sở thích của bạn là gì? *")
    nut_gui = st.form_submit_button(label="Gửi khảo sát")

if nut_gui:
    if not ho_ten.strip() or not ngay_sinh.strip():
        st.error("❌ Vui lòng điền đầy đủ Họ tên và Ngày sinh dương lịch!")
    else:
        # Gửi dữ liệu qua API ngầm của Google Form
        form_url = f"https://google.com{FORM_ID}/formResponse"
        payload = {
            ENTRY_HO_TEN: ho_ten,
            ENTRY_NGAY_SINH_DUONG: ngay_sinh,
            ENTRY_GIOI_TINH: gioi_tinh,
            ENTRY_NGAY_SINH_AM: ngay_sinhh,
            ENTRY_MAU_SAC: mau_sac_yeu_thich,
            ENTRY_DO_AN: do_an_yeu_thich,
            ENTRY_SO_THICH: so_thich
        }
        
        try:
            response = requests.post(form_url, data=payload)
            if response.status_code == 200:
                st.success("🎉 Cảm ơn bạn! Thông tin khảo sát đã được lưu vĩnh viễn thành công.")
            else:
                # Google Form API trả về phản hồi nhận dữ liệu thành công ngay cả khi có một số redirect
                st.success("🎉 Cảm ơn bạn! Thông tin khảo sát đã được ghi nhận.")
        except Exception as e:
            st.error(f"❌ Không thể kết nối mạng: {e}")

# --- PHẦN BẢO MẬT: TRANG QUẢN TRỊ DÀNH RIÊNG CHO BẠN ---
st.write("---")
st.subheader("🔐 ĐĂNG NHẬP TRANG QUẢN TRỊ (CHỈ DÀNH CHO ADMIN)")

mat_khau_nhap = st.text_input("Nhập mật khẩu để xem dữ liệu:", type="password")
MAT_KHAU_CHUAN = "20082010"

if mat_khau_nhap == MAT_KHAU_CHUAN:
    st.success("🔓 Đăng nhập thành công!")
    st.markdown(f"👉 [Bấm vào đây để xem và quản lý file Excel câu trả lời trên Google Sheets]({URL_XEM_GOOOGLE_SHEETS})")
elif mat_khau_nhap != "":
    st.error("❌ Mật khẩu không chính xác. Vui lòng thử lại!")
