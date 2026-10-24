import streamlit as st
st.set_page_config(layout="wide")

# Thêm logo trường và logo khoa
col_logo_truong, col_tieu_de, col_logo_khoa = st.columns([1, 3, 1])

with col_logo_truong:
    st.image("logo_truong.png", width=130)

with col_tieu_de:
    st.markdown(
        """
        <div style="text-align: center; padding-top: 25px;">
            <h2>CHUYỂN ĐỔI KHÔNG GIAN MÀU</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_logo_khoa:
    st.image("logo_khoa.png", width=130)

st.divider()

# Phần chuyển đổi không gian màu
chon_khong_gian_mau = st.sidebar.radio(
    "Chuyển đổi không gian màu",
    ("sRGB to XYZ", "XYZ to sRGB")
)

col1, col2 = st.columns(2)
st.set_page_config(
    page_title="Khoa học Màu sắc", layout="wide"
)

st.write("### Chào mừng bạn đến với project Khoa học Màu sắc của mình!")
st.write("# Mình tên là Lê Nguyễn Như Quỳnh")
st.write("# MSSV: 23458012")
