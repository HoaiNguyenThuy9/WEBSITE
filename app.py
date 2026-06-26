import streamlit as st

# --- CẤU HÌNH TRANG ---
st.set_page_config(
    page_title="NORTHFRAME | Premium Visualization",
    page_icon="✨",
    layout="wide",
)

# --- GOOGLE FONTS & CUSTOM CSS ---
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Montserrat:wght@300;400;600&display=swap" rel="stylesheet">
<style>
    /* Tổng thể */
    .main {
        background-color: #FDFDFD;
    }
    
    /* Typography */
    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
        color: #1A1A1A;
    }
    
    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        font-weight: 700 !important;
        letter-spacing: 1px;
    }

    /* Tiêu đề Studio lớn ở trang chủ */
    .hero-title {
        font-size: 4.5rem;
        font-weight: 700;
        text-align: center;
        margin-top: 2rem;
        margin-bottom: 0px;
        color: #0F172A;
    }
    
    .hero-subtitle {
        font-family: 'Montserrat', sans-serif;
        font-size: 1rem;
        text-transform: uppercase;
        letter-spacing: 5px;
        text-align: center;
        color: #94A3B8;
        margin-bottom: 3rem;
    }

    /* Hiệu ứng Glassmorphism cho Card */
    .luxury-card {
        background: rgba(255, 255, 255, 0.8);
        border: 1px solid rgba(200, 200, 200, 0.3);
        padding: 2rem;
        border-radius: 0px; /* Vuông vức thường sang trọng hơn */
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        transition: transform 0.3s ease;
    }
    
    .luxury-card:hover {
        transform: translateY(-5px);
        border-color: #C5A059; /* Màu Gold accent */
    }

    /* Button sang trọng */
    .stButton>button {
        background-color: #0F172A;
        color: white;
        border-radius: 0px;
        padding: 0.75rem 2.5rem;
        border: none;
        font-family: 'Montserrat', sans-serif;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #C5A059;
        color: white;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0F172A;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1634712282287-14ed57b9cc89?w=500", use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>NORTHFRAME</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 0.8rem; opacity: 0.7;'>ARCHITECTURAL VISUALIZATION</p>", unsafe_allow_html=True)
    st.write("---")
    page = st.radio("CHỌN TRANG", ["TRANG CHỦ", "PORTFOLIO", "DỊCH VỤ", "LIÊN HỆ"])
    st.write("---")
    st.caption("© 2026 NORTHFRAME STUDIO")

# --- TRANG CHỦ ---
if page == "TRANG CHỦ":
    st.markdown('<p class="hero-title">NORTHFRAME</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Furniture Photography & AI Visualization</p>', unsafe_allow_html=True)
    
    # Hero Image - Sử dụng ảnh có chiều sâu
    st.image("https://images.unsplash.com/photo-1600210491892-03d54c0aaf87?w=1200&q=80", use_container_width=True)
    
    st.write("##")
    
    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        st.markdown("### Sự Giao Thoa Giữa Nghệ Thuật & Công Nghệ")
        st.write("""
        Tại **NORTHFRAME**, chúng tôi không chỉ chụp ảnh hay vẽ 3D. Chúng tôi kiến tạo những trải nghiệm thị giác đỉnh cao 
        bằng cách kết hợp kỹ thuật nhiếp ảnh truyền thống với sức mạnh đột phá của trí tuệ nhân tạo (AI).
        
        Sứ mệnh của chúng tôi là biến những bản thiết kế nội thất thô cứng thành những tác phẩm nghệ thuật có hồn, 
        giúp khách hàng của bạn 'cảm' được không gian ngay từ cái nhìn đầu tiên.
        """)
        st.button("Khám phá dự án")
        
    with col2:
        st.image("https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=800", use_container_width=True)

# --- PORTFOLIO ---
elif page == "PORTFOLIO":
    st.markdown("<h1 style='text-align: center;'>Featured Projects</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Tuyển tập những dự án tiêu biểu mang dấu ấn nghệ thuật.</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Grid Portfolio kiểu tạp chí kiến trúc
    cols = st.columns(2)
    projects = [
        {"title": "The Penthouse AI", "type": "AI Visualization", "img": "https://images.unsplash.com/photo-1616594039964-ae9021a400a0?w=800"},
        {"title": "Organic Living", "type": "Photography", "img": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=800"},
        {"title": "Minimalist Loft", "type": "CGI & AI", "img": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=800"},
        {"title": "The Classic Edit", "type": "Photography", "img": "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=800"}
    ]
    
    for i, p in enumerate(projects):
        with cols[i % 2]:
            st.image(p['img'], use_container_width=True)
            st.markdown(f"<h4 style='margin-bottom:0;'>{p['title']}</h4>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: #C5A059; font-size: 0.9rem; text-transform: uppercase;'>{p['type']}</p>", unsafe_allow_html=True)
            st.write("##")

# --- DỊCH VỤ ---
elif page == "DỊCH VỤ":
    st.markdown("<h1 style='text-align: center;'>Our Expertise</h1>", unsafe_allow_html=True)
    st.write("##")
    
    c1, c2, c3 = st.columns(3)
    
    services = [
        {"icon": "📸", "name": "Furniture Photography", "desc": "Chụp ảnh sản phẩm nội thất chuyên nghiệp cho Catalog và Website."},
        {"icon": "🤖", "name": "AI Interior Visualization", "desc": "Sử dụng AI để dựng phối cảnh không gian từ bản vẽ tay hoặc mặt bằng thô."},
        {"icon": "🏠", "name": "3D Architectural Render", "desc": "Diễn họa kiến trúc 3D với độ chi tiết và vật liệu chân thực 100%."}
    ]
    
    for i, s in enumerate([c1, c2, c3]):
        with s:
            st.markdown(f"""
            <div class="luxury-card">
                <h2 style='font-size: 3rem;'>{services[i]['icon']}</h2>
                <h3>{services[i]['name']}</h3>
                <p style='font-size: 0.9rem; color: #555;'>{services[i]['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

    st.write("---")
    st.markdown("<h3 style='text-align: center;'>Ước tính ngân sách dự án</h3>", unsafe_allow_html=True)
    
    col_calc1, col_calc2 = st.columns([2, 1])
    with col_calc1:
        m2 = st.slider("Diện tích mặt bằng (m2)", 20, 1000, 100)
    with col_calc2:
        package = st.selectbox("Gói dịch vụ", ["Standard (AI)", "Premium (Photo + AI)", "Luxury (CGI + AI)"])
    
    price_map = {"Standard (AI)": 50000, "Premium (Photo + AI)": 150000, "Luxury (CGI + AI)": 300000}
    total = m2 * price_map[package]
    
    st.markdown(f"<h2 style='text-align: center; color: #C5A059;'>Tạm tính: {total:,.0f} VNĐ</h2>", unsafe_allow_html=True)

# --- LIÊN HỆ ---
elif page == "LIÊN HỆ":
    st.markdown("<h1 style='text-align: center;'>Let's Create Together</h1>", unsafe_allow_html=True)
    
    col_f1, col_f2 = st.columns([1, 1], gap="large")
    
    with col_f1:
        st.markdown("### Gửi lời nhắn")
        with st.form("luxury_form"):
            st.text_input("Tên của bạn")
            st.text_input("Số điện thoại / Zalo")
            st.selectbox("Dịch vụ quan tâm", ["Nhiếp ảnh nội thất", "AI Visualization", "Tư vấn tổng thể"])
            st.text_area("Mô tả sơ lược về dự án")
            st.form_submit_button("GỬI YÊU CẦU")
            
    with col_f2:
        st.markdown("### Thông tin liên hệ")
        st.write("📍 **Studio:** 123 Luxury Road, District 2, HCMC")
        st.write("📧 **Email:** studio@northframe.vn")
        st.write("📞 **Hotline:** 0901.234.567")
        st.write("---")
        # Bản đồ tối giản đen trắng
        st.map(data=[{"lat": 10.7876, "lon": 106.7048}])
