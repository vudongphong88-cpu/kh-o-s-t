import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Khảo sát người dùng", page_icon="📝")

# --- 1. THÔNG TIN ĐÃ ĐƯỢC LÀM SẠCH TUYỆT ĐỐI ---
RAW_ID = "1FAIpQLSfVQ4EObiUKy3hnWMDE57vSAqSfEc3f9ElHwp2YKhl232c2Qw"
# Lệnh loại bỏ hoàn toàn các ký tự lạ, dấu cách hoặc gạch chéo nếu lỡ tay copy thừa
FORM_ID = RAW_ID.strip().replace("/", "")

ENTRY_HO_TEN = "entry.1930741903"
ENTRY_NGAY_SINH_DUONG = "entry.976728289"
ENTRY_GIOI_TINH = "entry.1320701927"
ENTRY_NGAY_SINH_AM = "entry.1058897768"
ENTRY_MAU_SAC = "entry.858748151"
ENTRY_DO_AN = "entry.1376030974"
ENTRY_SO_THICH = "entry.1853722381"

URL_XEM_GOOOGLE_SHEETS = "https://google.com"

# --- 2. GIAO DIỆN FORM KHẢO SÁT ---
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
        # Sử dụng đường dẫn tĩnh hoàn toàn, tách biệt 100% không cho dính chữ
        form_url = "https://google.com" + str(FORM_ID) + "/formResponse"
        
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
            st.success("🎉 Cảm ơn bạn! Thông tin khảo sát đã được gửi đi thành công.")
        except Exception as e:
            st.error(f"❌ Lỗi mạng hệ thống: {e}")

# --- 3. TRANG QUẢN TRỊ ADMIN ---
st.write("---")
st.subheader("🔐 ĐĂNG NHẬP TRANG QUẢN TRỊ (CHỈ DÀNH CHO ADMIN)")

mat_khau_nhap = st.text_input("Nhập mật khẩu để xem dữ liệu:", type="password")
MAT_KHAU_CHUAN = "20082010"

if mat_khau_nhap == MAT_KHAU_CHUAN:
    st.success("🔓 Đăng nhập thành công!")
    st.markdown(f"👉 [Bấm vào đây để xem file Excel câu trả lời trên Google Sheets]({URL_XEM_GOOOGLE_SHEETS})")
elif mat_khau_nhap != "":
    st.error("❌ Mật khẩu không chính xác. Vui lòng thử lại!")

