import streamlit as st

# --- CẤU HÌNH TRANG ---
st.set_page_config(
    page_title="NORTHFRAME Studio | Thiết Kế Nội Thất & Hình Ảnh",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="collapsed" # Ẩn sidebar mặc định để giống giao diện web truyền thống
)

# --- GOOGLE FONTS & CUSTOM CSS (Style NADA Design: Tối giản, Chữ thanh mảnh, Tông ấm nhẹ) ---
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<style>
    /* Reset & Cấu trúc nền */
    .main {
        background-color: #FCFBF9; /* Màu nền trắng kem nhẹ của NADA */
    }
    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
        color: #2A2A2A;
    }
    
    /* Thanh Menu Ngang giả lập giống Website */
    .nav-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
        background-color: #FFFFFF;
        border-bottom: 1px solid #EEEEEE;
        margin-bottom: 2rem;
    }
    .nav-logo {
        font-family: 'Playfair Display', serif;
        font-size: 1.6rem;
        font-weight: 600;
        letter-spacing: 2px;
        color: #111111;
    }
    .nav-sub {
        font-size: 0.75rem;
        letter-spacing: 1px;
        color: #777777;
        text-transform: uppercase;
    }

    /* Các Header phân khu */
    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        font-weight: 400;
        text-align: center;
        margin-top: 3rem;
        margin-bottom: 0.5rem;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .section-subtitle {
        font-size: 0.85rem;
        text-align: center;
        color: #888888;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 3rem;
    }

    /* Định dạng Grid Blog & Dự Án */
    .content-box {
        background-color: #FFFFFF;
        border: 1px solid #EFEFEF;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
    }
    .content-box:hover {
        box-shadow: 0 5px 15px rgba(0,0,0,0.02);
        border-color: #D4AF37; /* Điểm xuyết viền vàng nhẹ khi di chuột */
    }
    .content-tag {
        font-size: 0.75rem;
        color: #8E7046;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
    }

    /* Triết lý thiết kế khu vực lớn */
    .philosophy-bg {
        background-color: #F4F1EA;
        padding: 4rem 2rem;
        text-align: center;
        margin: 4rem 0;
    }
    .philosophy-text {
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        font-style: italic;
        max-width: 800px;
        margin: 0 auto;
        color: #4A4A4A;
        line-height: 1.6;
    }

    /* Footer kiểu NADA */
    .footer-container {
        background-color: #1A1A1A;
        color: #FFFFFF;
        padding: 4rem 2rem 2rem 2rem;
        margin-top: 5rem;
    }
    .footer-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        letter-spacing: 2px;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# --- THANH MENU ĐIỀU HƯỚNG CHÍNH ---
# Sử dụng st.sidebar làm bộ chọn trang tinh gọn, ẩn/hiện linh hoạt
with st.sidebar:
    st.markdown("### ĐIỀU HƯỚNG WEBSITE")
    page = st.radio(
        "Chuyển đến khu vực:",
        ["Tổng Quan (Trang Chủ)", "Công Trình & Dự Án", "Ý Tưởng & Blog", "Câu Hỏi Thường Gặp (FAQs)"]
    )
    st.info("💡 Mẹo: Bạn có thể đóng Sidebar này lại bằng dấu 'x' ở góc trên để trải nghiệm giao diện full-width giống như Website thực tế.")

# --- HEADER GIẢ LẬP MENU NGANG TRÊN TRANG ---
st.markdown("""
<div class="nav-bar">
    <div>
        <div class="nav-logo">NORTHFRAME STUDIO</div>
        <div class="nav-sub">Personalized design for all of your spaces</div>
    </div>
    <div style="font-size: 0.85rem; color: #555; font-weight: 500;">
        TRANG CHỦ &nbsp;&nbsp;|&nbsp;&nbsp; CÔNG TRÌNH &nbsp;&nbsp;|&nbsp;&nbsp; DỊCH VỤ &nbsp;&nbsp;|&nbsp;&nbsp; BLOG &nbsp;&nbsp;|&nbsp;&nbsp; LIÊN HỆ
    </div>
</div>
""", unsafe_allow_html=True)


# ====================================================================================================
# PHẦN 1: BANNER CHÍNH & GIỚI THIỆU DỊCH VỤ (Giống kết cấu trang chủ NADA)
# ====================================================================================================
if page == "Tổng Quan (Trang Chủ)":
    
    # Banner ảnh lớn tràn viền kèm lời chào
    st.image("https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=1400&q=80", 
             caption="Tư vấn thiết kế nội thất, đưa ra các phương án và giải pháp phù hợp cho không gian của bạn.", 
             use_container_width=True)
    
    # Khu vực DỊCH VỤ CUNG CẤP
    st.markdown('<p class="section-title">DỊCH VỤ</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Luôn hướng tới chất lượng không gian tốt nhất - Cá nhân hóa với từng khách hàng</p>', unsafe_allow_html=True)
    
    ser_col1, ser_col2, ser_col3 = st.columns(3, gap="large")
    
    with ser_col1:
        st.image("https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=600", use_container_width=True)
        st.markdown("#### 1. TƯ VẤN THIẾT KẾ NỘI THẤT")
        st.write("Tư vấn phương án thiết kế nội thất phù hợp với từng không gian riêng biệt, ưu tiên các mong muốn và trải nghiệm cốt lõi của khách hàng.")
        st.caption("[ Xem thêm dịch vụ ]")
        
    with ser_col2:
        st.image("https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=600", use_container_width=True)
        st.markdown("#### 2. THIẾT KẾ & THI CÔNG TRỌN GÓI")
        st.write("Dịch vụ chìa khóa trao tay: Từ lên phương án ý tưởng, triển khai kỹ thuật, quản lý cải tạo thô, sản xuất đồ gỗ tới lắp đặt hoàn thiện trang trí.")
        st.caption("[ Xem thêm dịch vụ ]")
        
    with ser_col3:
        # Thay bằng thế mạnh độc quyền của NORTHFRAME theo phong cách NADA (Quảng cáo nội thất/Hình ảnh AI)
        st.image("https://images.unsplash.com/photo-1634712282287-14ed57b9cc89?w=600", use_container_width=True)
        st.markdown("#### 3. HÌNH ẢNH & AI VISUALIZATION")
        st.write("Cung cấp dịch vụ phục vụ cho quá trình thương mại, truyền thông nội thất: Chụp ảnh sản phẩm (Furniture Photography) và dựng concept không gian bằng AI nâng cao.")
        st.caption("[ Xem thêm dịch vụ ]")


# ====================================================================================================
# PHẦN 2: CÔNG TRÌNH / PORTFOLIO
# ====================================================================================================
if page in ["Tổng Quan (Trang Chủ)", "Công Trình & Dự Án"]:
    st.markdown('<p class="section-title">CÔNG TRÌNH TIÊU BIỂU</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Các dự án thực tế đã triển khai bàn giao</p>', unsafe_allow_html=True)
    
    p_col1, p_col2 = st.columns(2, gap="medium")
    with p_col1:
        st.image("https://images.unsplash.com/photo-1616594039964-ae9021a400a0?w=800", use_container_width=True)
        st.markdown("<div class='content-tag'>Dự án Nhà phố</div>", unsafe_allow_html=True)
        st.markdown("##### KHÔNG GIAN CĂN HỘ PENTHOUSE LANDMARK - LUXURY MODERN")
        st.write("Sự kết hợp hoàn hảo giữa vật liệu đá tự nhiên, kim loại mạ titan cao cấp và hệ thống chiếu sáng thông minh.")
        st.write("##")
        
    with p_col2:
        st.image("https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=800", use_container_width=True)
        st.markdown("<div class='content-tag'>Dự án Biệt thự</div>", unsafe_allow_html=True)
        st.markdown("##### ECO-MINIMALISM VILLA - THẢO ĐIỀN")
        st.write("Tối giản hóa đường nét kiến trúc, đưa ánh sáng tự nhiên và cây xanh lồng ghép vào từng góc nhỏ sinh hoạt.")
        st.write("##")


# ====================================================================================================
# PHẦN 3: TRIẾT LÝ THIẾT KẾ (Đặc trưng cốt lõi trên trang chủ NADA)
# ====================================================================================================
if page == "Tổng Quan (Trang Chủ)":
    st.markdown("""
    <div class="philosophy-bg">
        <div class="philosophy-text">
            "Thiết kế là tính thẩm mỹ, dựa trên công năng. Nếu thiết kế đẹp nhưng không có chức năng, hoặc không khả thi trong quá trình sử dụng, thì đó không phải là một thiết kế thành công."
        </div>
        <p style="margin-top: 1.5rem; font-size: 0.8rem; letter-spacing: 2px; color: #777;">— NORTHFRAME STUDIO PHILOSOPHY</p>
    </div>
    """, unsafe_allow_html=True)


# ====================================================================================================
# PHẦN 4: Ý TƯỞNG THIẾT KẾ & BLOG (Giống hệt cụm bài viết của NADA)
# ====================================================================================================
if page in ["Tổng Quan (Trang Chủ)", "Ý Tưởng & Blog"]:
    st.markdown('<p class="section-title">Ý TƯỞNG THIẾT KẾ & BLOG</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Chia sẻ kinh nghiệm, xu hướng kiến trúc và giải pháp không gian</p>', unsafe_allow_html=True)
    
    b_col1, b_col2, b_col3 = st.columns(3)
    
    with b_col1:
        st.markdown("""
        <div class="content-box">
            <div class="content-tag">Bản Quyền & Chia Sẻ</div>
            <h4>Ý TƯỞNG THIẾT KẾ - VẤN ĐỀ BẢN QUYỀN VÀ MÂU THUẪN ĐẠO ĐỨC</h4>
            <p style="font-size:0.85rem; color:#666;">Góc nhìn chuyên môn về việc bảo hộ ý tưởng sáng tạo trong ngành nội thất hiện nay...</p>
            <a href="#" style="color:#111; font-size:0.8rem; font-weight:600; text-decoration:none;">[ Đọc bài viết ]</a>
        </div>
        """, unsafe_allow_html=True)
        
    with b_col2:
        st.markdown("""
        <div class="content-box">
            <div class="content-tag">Series Concept</div>
            <h4>KHÔNG GIAN "NHÀ CỦA CHÚNG MÌNH"</h4>
            <p style="font-size:0.85rem; color:#666;">Concept nghiên cứu chuyên sâu về không gian nhà ở tối ưu dành cho các cặp đôi trẻ theo phong cách Japandi...</p>
            <a href="#" style="color:#111; font-size:0.8rem; font-weight:600; text-decoration:none;">[ Đọc bài viết ]</a>
        </div>
        """, unsafe_allow_html=True)
        
    with b_col3:
        st.markdown("""
        <div class="content-box">
            <div class="content-tag">Giải Pháp Ngân Sách</div>
            <h4>MẪU THIẾT KẾ PHÒNG BẾP TỪ 10M2, NGÂN SÁCH DƯỚI 40 TRIỆU</h4>
            <p style="font-size:0.85rem; color:#666;">Bài toán tối ưu hóa công năng tủ bếp, lựa chọn cốt gỗ và phụ kiện thông minh tiết kiệm chi phí...</p>
            <a href="#" style="color:#111; font-size:0.8rem; font-weight:600; text-decoration:none;">[ Đọc bài viết ]</a>
        </div>
        """, unsafe_allow_html=True)


# ====================================================================================================
# PHẦN 5: FREQUENTLY ASKED QUESTIONS (FAQs - Chuẩn 6 câu hỏi hệ thống của NADA)
# ====================================================================================================
if page in ["Tổng Quan (Trang Chủ)", "Câu Hỏi Thường Gặp (FAQs)"]:
    st.markdown('<p class="section-title">FREQUENTLY ASKED QUESTIONS</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Các câu hỏi phổ biến về dịch vụ thiết kế nội thất</p>', unsafe_allow_html=True)
    
    with st.expander("1. Tại sao tôi nên xem xét dịch vụ chìa khóa trao tay?"):
        st.write("""
        Dịch vụ chìa khóa trao tay mang lại cho bạn nhiều lợi ích trong việc hoàn thiện nội thất căn nhà. 
        Các nhà thiết kế sẽ tư vấn và đồng hành cùng bạn từ quá trình hiện thực hóa ý tưởng, lên bản vẽ mô phỏng 3D đến thi công thực tế. 
        Bảng dự toán thi công rõ ràng giúp bạn kiểm soát chặt chẽ ngân sách, tránh phát sinh chi phí ngoài tầm kiểm soát.
        """)
        
    with st.expander("2. Tất cả các ý tưởng trong thiết kế đều thực hiện được ở thực tế?"):
        st.write("""
        Dựa vào lối sinh hoạt hằng ngày và nhu cầu thực tế của gia đình, các chuyên gia sẽ điều chỉnh phương án triển khai tốt nhất. 
        Mọi ý tưởng bay bổng đều cần được cân bằng với cấu trúc kỹ thuật thực tế và tính chất của vật liệu tại xưởng sản xuất.
        """)
        
    with st.expander("3. Tại sao tôi nên chọn nhà thầu xây dựng / xưởng sản xuất từ bạn?"):
        st.write("""
        Khi bản vẽ thiết kế được phê duyệt, chúng tôi cung cấp hồ sơ hoàn chỉnh gồm đánh giá năng lực nhà thầu, dự toán chi tiết từng hạng mục. 
        Bạn không cần mất thời gian tìm kiếm nhãn hiệu, lo lắng chất lượng vật liệu hay xung đột tiến độ phối hợp, tất cả quy về một đầu mối chịu trách nhiệm duy nhất.
        """)
        
    with st.expander("4. Tôi chưa nhận bàn giao căn hộ/nhà thô, tôi có thể bắt đầu thiết kế không?"):
        st.write("""
        Hoàn toàn có thể. Công đoạn lên ý tưởng 3D ban đầu thường chiếm 1/4 tổng thời gian toàn bộ dự án. 
        Triển khai sớm hồ sơ thiết kế trong thời gian chờ nhận bàn giao nhà giúp bạn tiết kiệm tối đa thời gian chờ đợi, sẵn sàng thi công ngay khi nhận khóa.
        """)
        
    with st.expander("5. Tôi không biết chọn phong cách thiết kế nào, tôi nên làm gì?"):
        st.write("""
        Đừng lo lắng, nhiệm vụ của kiến trúc sư là trò chuyện, đặt câu hỏi định hướng để khai phá gu thẩm mỹ ẩn giấu của bạn. 
        Chúng tôi sẽ gửi các bản moodboard ý tưởng trực quan để bạn dễ dàng lựa chọn ra phong cách thuộc về riêng mình.
        """)


# ====================================================================================================
# PHẦN 6: ĐỐI TÁC VÀ FORM ĐĂNG KÝ NHẬN TƯ VẤN TRỰC TIẾP
# ====================================================================================================
if page == "Tổng Quan (Trang Chủ)":
    st.write("##")
    st.markdown('<p class="section-title" style="font-size:1.5rem;">ĐỐI TÁC CHIẾN LƯỢC</p>', unsafe_allow_html=True)
    
    # Hiển thị text/logo đơn giản, tinh tế như dòng đối tác cuối trang NADA
    brand_col1, brand_col2, brand_col3, brand_col4 = st.columns(4)
    with brand_col1: st.markdown("<p style='text-align:center; color:#999; font-weight:500;'>GỖ AN CƯỜNG</p>", unsafe_allow_html=True)
    with brand_col2: st.markdown("<p style='text-align:center; color:#999; font-weight:500;'>SƠN DULUX</p>", unsafe_allow_html=True)
    with brand_col3: st.markdown("<p style='text-align:center; color:#999; font-weight:500;'>PHỤ KIỆN HAFELE</p>", unsafe_allow_html=True)
    with brand_col4: st.markdown("<p style='text-align:center; color:#999; font-weight:500;'>SƠN NIPPON</p>", unsafe_allow_html=True)

    st.write("---")
    
    # Khu vực Form Đăng Ký
    st.markdown('<p class="section-title">ĐĂNG KÝ NHẬN TƯ VẤN THIẾT KẾ</p>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:0.9rem; color:#666;'>Chúng ta sẽ cùng tìm hiểu về: 1. Xu hướng thiết kế | 2. Chi phí cải tạo | 3. Tối ưu ngân sách | 4. Tiến độ thực hiện</p>", unsafe_allow_html=True)
    
    # Căn giữa Form bằng cách dùng col phụ
    _, form_col, _ = st.columns([1, 2, 1])
    with form_col:
        with st.form("nada_contact_form", clear_on_submit=True):
            f_name = st.text_input("Họ và tên của bạn *")
            f_phone = st.text_input("Số điện thoại liên hệ *")
            f_email = st.text_input("Địa chỉ Email")
            f_msg = st.text_area("Diện tích và hiện trạng không gian cần tư vấn...")
            
            submitted = st.form_submit_button("GỬI THÔNG TIN")
            if submitted:
                if f_name and f_phone:
                    st.success("Cảm ơn bạn đã gửi thông tin! Đội ngũ Kiến trúc sư NORTHFRAME sẽ liên hệ lại ngay trong vòng 24h làm việc.")
                else:
                    st.error("Vui lòng điền đầy đủ các thông tin bắt buộc (*)")


# ====================================================================================================
# PHẦN 7: FOOTER TOÀN TRANG (Thông tin doanh nghiệp)
# ====================================================================================================
st.markdown("""
<div class="footer-container">
    <div style="max-width: 1200px; margin: 0 auto;">
        <div class="row" style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 2rem;">
            <div style="flex: 1; min-width: 280px;">
                <div class="footer-title">NORTHFRAME STUDIO</div>
                <p style="opacity: 0.7; font-size: 0.85rem; line-height: 1.6;">
                    Đơn vị tư vấn giải pháp thiết kế kiến trúc, nội thất toàn diện, kết hợp nền tảng công nghệ xử lý hình ảnh AI đột phá nhằm tối ưu hóa trải nghiệm thị giác cho từng không gian sống biệt lập.
                </p>
            </div>
            <div style="flex: 1; min-width: 250px;">
                <h5 style="color: #D4AF37; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 1rem;">Thông tin liên hệ</h5>
                <p style="opacity: 0.8; font-size: 0.85rem; margin-bottom: 0.5rem;">📍 <b>Địa chỉ:</b> 11A Hồng Hà, Phường 2, Quận Tân Bình, TP. Hồ Chí Minh</p>
                <p style="opacity: 0.8; font-size: 0.85rem; margin-bottom: 0.5rem;">📞 <b>Điện thoại:</b> 0703 900 XXX</p>
                <p style="opacity: 0.8; font-size: 0.85rem; margin-bottom: 0.5rem;">✉️ <b>Email:</b> info@northframestudio.com</p>
            </div>
        </div>
        <hr style="border-color: rgba(255,255,255,0.1); margin: 2rem 0 1rem 0;">
        <p style="text-align: center; font-size: 0.75rem; opacity: 0.5; margin: 0;">© 2026 NORTHFRAME STUDIO. All rights reserved.</p>
    </div>
</div>
""", unsafe_allow_html=True)
