import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Khảo sát người dùng", page_icon="📝")
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
except Exception:
    conn = None

st.title("📋 BIỂU MẪU KHẢO SÁT SỞ THÍCH BẠN BÈ")

# Giao diện Form nhập liệu
with st.form(key="survey_form", clear_on_submit=True):
    ho_ten = st.text_input("1. Họ và tên của bạn là gì? *")
    ngay_sinh = st.text_input("2. Ngày sinh dương lịch của bạn là gì? *")
    gioi_tinh = st.radio("3. Giới tính của bạn:", ["Nam", "Nữ", "Khác"])
    ngay_sinhh = st.text_input("4. Ngày sinh theo âm lịch của bạn là gì? *")
    mau_sac_yeu_thich = st.text_area("5. màu sắc yêu thích của bạn là gì:")
    do_an_yeu_thich = st.text_input("6. Đồ ăn yêu thích của bạn là gì? *")
    so_thich = st.text_input("7. Sở thích của bạn là gì? *")
    nut_gui = st.form_submit_button(label="Gửi khảo sát")

if nut_gui:
    if not ho_ten.strip() or not ngay_sinh.strip():
        st.error("❌ Vui lòng điền đầy đủ Họ tên và Ngày sinh dương lịch!")
    else:
        # Gom dữ liệu người dùng vừa nhập vào một bảng tạm
        data_moi = pd.DataFrame([{
            "Họ và tên": ho_ten,
            "Ngày sinh dương lịch": ngay_sinh,
            "Giới tính": gioi_tinh,
            "Ngày sinh âm lịch": ngay_sinhh,
            "Màu sắc yêu thích": mau_sac_yeu_thich,
            "Đồ ăn yêu thích": do_an_yeu_thich,
            "Sở thích": so_thich
        }])
        
    try:
            # Đọc và cập nhật dữ liệu tự động không cần dán link vào code
            df_cu = conn.read(ttl=0)
            df_cap_nhat = pd.concat([df_cu, data_moi], ignore_index=True)
            conn.update(data=df_cap_nhat)
            st.success("🎉 Cảm ơn bạn! Thông tin khảo sát đã được lưu vĩnh viễn vào Google Sheets.")
        except Exception as e:
            st.error(f"❌ Lỗi kết nối Google Sheets: {e}")


# --- PHẦN BẢO MẬT: TRANG QUẢN TRỊ DÀNH RIÊNG CHO BẠN ---
st.write("---")
st.subheader("🔐 ĐĂNG NHẬP TRANG QUẢN TRỊ (CHỈ DÀNH CHO ADMIN)")

mat_khau_nhap = st.text_input("Nhập mật khẩu để xem dữ liệu:", type="password")
MAT_KHAU_CHUAN = "2010" # Bạn có thể đổi mật khẩu này theo ý muốn

if mat_khau_nhap == MAT_KHAU_CHUAN:
    st.success("🔓 Đăng nhập thành công!")
    st.subheader("📊 DANH SÁCH KẾT QUẢ KHẢO SÁT TRÊN GOOGLE SHEETS")
    try:
        df_hien_thi = conn.read(spreadsheet=URL_GOOGLE_SHEETS, ttl=0)
        st.dataframe(df_hien_thi)
    except Exception:
        st.info("Chưa có dữ liệu hoặc không thể tải bảng trực tiếp. Bạn hãy xem trực tiếp trên ứng dụng Google Sheets nhé.")
elif mat_khau_nhap != "":
    st.error("❌ Mật khẩu không chính xác. Vui lòng thử lại!")
