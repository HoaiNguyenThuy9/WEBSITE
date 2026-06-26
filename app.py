import streamlit as st

# --- CẤU HÌNH TRANG ---
st.set_page_config(
    page_title="LUMEN Studio | Thiết Kế Nội Thất",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SỬ DỤNG CSS ĐỂ CUSTOM GIAO DIỆN (Tối giản & Sang trọng) ---
st.markdown("""
<style>
    /* Chỉnh font và màu sắc chủ đạo */
    .main .block-container {
        padding-top: 2rem;
    }
    h1, h2, h3 {
        font-family: 'Playfair Display', serif;
        color: #2C3E50;
    }
    .studio-title {
        font-size: 3rem;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 0px;
        text-align: center;
    }
    .studio-subtitle {
        font-size: 1.2rem;
        font-style: italic;
        color: #7F8C8D;
        text-align: center;
        margin-bottom: 2rem;
    }
    .project-card {
        border-radius: 5px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        padding: 15px;
        background-color: #ffffff;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- THANH ĐIỀU HƯỚNG (SIDEBAR) ---
st.sidebar.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=500", use_container_width=True)
st.sidebar.title("LUMEN STUDIO")
st.sidebar.write("Khơi nguồn không gian sống đương đại.")
st.sidebar.markdown("---")

# Chọn trang
page = st.sidebar.radio(
    "DANH MỤC",
    ["Trang Chủ", "Bộ Sưu Tập (Portfolio)", "Dịch Vụ & Báo Giá", "Liên Hệ"]
)

# Thêm thông tin chân trang ở Sidebar
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 LUMEN Studio. All rights reserved.")

# --- NỘI DUNG TỪNG TRANG ---

# 1. TRANG CHỦ
if page == "Trang Chủ":
    st.markdown('<p class="studio-title">LUMEN STUDIO</p>', unsafe_allow_html=True)
    st.markdown('<p class="studio-subtitle">Architecture & Interior Design</p>', unsafe_allow_html=True)
    
    # Banner chính
    st.image("https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=1200", 
             caption="Không gian tối giản, nâng tầm trải nghiệm sống.", use_container_width=True)
    
    st.markdown("---")
    
    # Giới thiệu ngắn
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Về Chúng Tôi")
        st.write("""
        Tại **LUMEN Studio**, chúng tôi tin rằng mỗi ngôi nhà là một câu chuyện độc bản của gia chủ. 
        Không chỉ dừng lại ở việc sắp xếp nội thất, chúng tôi kiến tạo những không gian sống cân bằng 
        giữa **công năng tối ưu** và **thẩm mĩ tinh tế**. 
        
        Với phong cách chủ đạo là Hiện đại (Modern), Tối giản (Minimalism) và Đông Dương (Indochine), 
        LUMEN cam kết mang lại sự hài lòng tuyệt đối trong từng đường nét chi tiết.
        """)
    with col2:
        st.subheader("Triết Lý Thiết Kế")
        st.info("“Chi tiết làm nên sự hoàn hảo, nhưng sự hoàn hảo không phải là chi tiết.” – Leonardo da Vinci")
        st.write("Chúng tôi chú trọng vào vật liệu tự nhiên, ánh sáng tự nhiên và luồng giao thông thông thoáng để tạo ra cảm giác bình yên nhất khi bạn trở về nhà.")

# 2. BỘ SƯU TẬP (PORTFOLIO)
elif page == "Bộ Sưu Tập (Portfolio)":
    st.title("Dự Án Nổi Bật")
    st.write("Khám phá các công trình thiết kế và thi công trọn gói bởi LUMEN.")
    
    tab1, tab2, tab3 = st.tabs(["Phòng Khách", "Phòng Ngủ", "Nhà Bếp & Phòng Ăn"])
    
    with tab1:
        st.subheader("Biệt thự Thảo Điền - Phong cách Eco-Minimalism")
        col_a, col_b = st.columns(2)
        with col_a:
            st.image("https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=600")
        with col_b:
            st.image("https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=600")
        st.caption("Dự án sử dụng tông màu trung tính, gỗ sồi tự nhiên và hệ kính lớn đón sáng.")

    with tab2:
        st.subheader("Căn hộ Penthouse Landmark 81 - Luxury Modern")
        col_a, col_b = st.columns(2)
        with col_a:
            st.image("https://images.unsplash.com/photo-1616594039964-ae9021a400a0?w=600")
        with col_b:
            st.image("https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=600")
        st.caption("Không gian phòng ngủ ấm cúng, sang trọng với chất liệu da và nỉ cao cấp.")

    with tab3:
        st.subheader("Nhà phố Bình Dương - Japandi Style")
        col_a, col_b = st.columns(2)
        with col_a:
            st.image("https://images.unsplash.com/photo-1556911220-e15b29be8c8f?w=600")
        with col_b:
            st.image("https://images.unsplash.com/photo-1556912172-45b7abe8b7e1?w=600")
        st.caption("Sự kết hợp hoàn hảo giữa nét tinh tế Nhật Bản và sự tiện nghi Bắc Âu cho căn bếp.")

# 3. DỊCH VỤ & BÁO GIÁ
elif page == "Dịch Vụ & Báo Giá":
    st.title("Dịch Vụ Của Chúng Tôi")
    st.write("Chúng tôi cung cấp giải pháp toàn diện từ ý tưởng đến thực tế.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="project-card">
            <h3>1. Thiết Kế 3D</h3>
            <p>Khảo sát hiện trạng, lên mặt bằng công năng và phối cảnh 3D trực quan, chi tiết vật liệu.</p>
            <p><b>Chi phí:</b> từ 180.000 VNĐ / m²</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="project-card">
            <h3>2. Thi Công Trọn Gói</h3>
            <p>Sản xuất đồ gỗ tại xưởng riêng, quản lý và giám sát thi công hoàn thiện chìa khóa trao tay.</p>
            <p><b>Chi phí:</b> Theo dự toán chi tiết</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="project-card">
            <h3>3. Cải Tạo Nội Thất</h3>
            <p>Làm mới không gian cũ, tối ưu hóa công năng mà không ảnh hưởng đến kết cấu cốt lõi.</p>
            <p><b>Chi phí:</b> Khảo sát và báo giá riêng</p>
        </div>
        """, unsafe_allow_html=True)

    # Dự toán nhanh cho khách hàng
    st.markdown("---")
    st.subheader("🧮 Dự Toán Chi Phí Thiết Kế Nhanh")
    
    area = st.number_input("Nhập diện tích căn hộ của bạn (m²):", min_value=10, max_value=500, value=70, step=5)
    style = st.selectbox("Chọn phong cách thiết kế:", ["Hiện Đại (Modern)", "Tối Giản (Minimalism)", "Tân Cổ Điển (Classic Luxury)"])
    
    # Định giá theo phong cách
    price_per_m2 = 180000 if style != "Tân Cổ Điển (Classic Luxury)" else 250000
    total_cost = area * price_per_m2
    
    st.metric(label=f"Chi phí thiết kế tạm tính ({style})", value=f"{total_cost:,.0f} VNĐ")
    st.caption("*Lưu ý: Báo giá mang tính chất tham khảo sơ bộ, chi phí thực tế phụ thuộc vào yêu cầu chi tiết.")

# 4. LIÊN HỆ
elif page == "Liên Hệ":
    st.title("Kết Nối Với LUMEN")
    st.write("Hãy để lại thông tin, kiến trúc sư của chúng tôi sẽ liên hệ tư vấn miễn phí trong vòng 24h.")
    
    left_col, right_col = st.columns(2)
    
    with left_col:
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Họ và tên *")
            phone = st.text_input("Số điện thoại *")
            email = st.text_input("Email")
            note = st.text_area("Yêu cầu tư vấn (Ví dụ: Thiết kế căn hộ 2 PN, thi công nhà phố...)")
            
            submitted = st.form_submit_submit_button("Gửi Yêu Cầu")
            if submitted:
                if name and phone:
                    st.success(f"Cảm ơn {name}! LUMEN đã tiếp nhận thông tin và sẽ gọi cho bạn sớm nhất.")
                else:
                    st.error("Vui lòng điền đầy đủ Họ tên và Số điện thoại.")
                    
    with right_col:
        st.subheader("Thông Tin Văn Phòng")
        st.markdown("""
        * 📍 **Văn phòng chính:** Đường Đại Lộ Bình Dương, Thủ Dầu Một, Bình Dương
        * 🏢 **Chi nhánh:** Quận 2, TP. Hồ Chí Minh
        * 📞 **Hotline:** 090X.XXX.XXX
        * ✉️ **Email:** contact@lumenstudio.vn
        * ⏰ **Giờ làm việc:** Thứ 2 - Thứ 7 (8:00 - 18:00)
        """)
        # Bản đồ minh họa (Tọa độ giả định khu vực trung tâm)
        st.map(data=[{"lat": 10.9805, "lon": 106.6642}])
