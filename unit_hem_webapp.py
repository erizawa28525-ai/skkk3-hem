import streamlit as st
import json
import os
from datetime import datetime

# Configure page settings
st.set_page_config(
    page_title="Unit HEM SK Kubang Kerian 3",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# File path for persistent data
DATA_FILE = "hem_data.json"

# Define default data to initialize the application
DEFAULT_DATA = {
    "slider": [
        {
            "id": 1,
            "title": "Selamat Datang ke Portal HEM SK Kubang Kerian 3",
            "desc": "Membina Sahsiah, Memperkasa Disiplin, dan Menjaga Kebajikan Murid.",
            "type": "image",
            "url": "https://images.unsplash.com/photo-1546410531-bb4caa6b424d?auto=format&fit=crop&q=80&w=1200",
            "active": True
        },
        {
            "id": 2,
            "title": "Aktiviti Kokurikulum & Sahsiah Unggul",
            "desc": "Rangkuman penglibatan aktif murid-murid dalam membina ketahanan diri.",
            "type": "video",
            "url": "https://assets.mixkit.co/videos/preview/mixkit-children-playing-with-toys-at-school-41551-large.mp4",
            "active": True
        },
        {
            "id": 3,
            "title": "Kempen Sayangi Sekolah Kita",
            "desc": "Sama-sama menjaga kebersihan dan keceriaan demi persekitaran kondusif.",
            "type": "image",
            "url": "https://images.unsplash.com/photo-1577896851231-70ef18881754?auto=format&fit=crop&q=80&w=1200",
            "active": True
        }
    ],
    "announcements": [
        {
            "id": "1",
            "title": "Mesyuarat Agung PIBG Kali Ke-34",
            "date": "2026-09-15",
            "content": "Semua ibu bapa dan penjaga murid SK Kubang Kerian 3 dijemput hadir ke Mesyuarat Agung PIBG kali ke-34. Kehadiran tuan/puan amat penting bagi membincangkan kebajikan dan perancangan akademik anak-anak.",
            "media_type": "image",
            "media_url": "https://images.unsplash.com/photo-1511578314322-379afb476865?auto=format&fit=crop&q=80&w=800",
            "priority": "Penting"
        },
        {
            "id": "2",
            "title": "Program Kesihatan & Pemeriksaan Gigi",
            "date": "2026-09-10",
            "content": "Unit Hal Ehwal Murid (HEM) dengan kerjasama Klinik Pergigian Kubang Kerian akan mengadakan pemeriksaan kesihatan pergigian dan fizikal bagi murid-murid Tahun 1 hingga Tahun 6 secara berperingkat.",
            "media_type": "none",
            "media_url": "",
            "priority": "Normal"
        }
    ]
}

# Function to load data
def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return DEFAULT_DATA
    else:
        # Write default data
        save_data(DEFAULT_DATA)
        return DEFAULT_DATA

# Function to save data
def save_data(data):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        st.error(f"Gagal menyimpan data: {e}")
        return False

# Load data into session state
if 'hem_data' not in st.session_state:
    st.session_state.hem_data = load_data()

# Custom Styling (CSS) for Emerald Green & Gold / Modern Look
st.markdown("""
<style>
    /* Main Theme colors */
    :root {
        --primary-color: #064e3b; /* Emerald */
        --secondary-color: #d97706; /* Gold */
        --background-color: #f9fafb;
    }
    
    .main-header {
        background: linear-gradient(135deg, #064e3b 0%, #022c22 100%);
        padding: 2.5rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border-bottom: 5px solid #d97706;
    }
    
    .main-header h1 {
        font-family: 'Inter', sans-serif;
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        color: #fef08a; /* Soft Gold */
    }
    
    .main-header p {
        font-size: 1.1rem;
        opacity: 0.9;
        font-weight: 400;
        letter-spacing: 1px;
    }
    
    .section-title {
        color: #064e3b;
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        border-left: 5px solid #d97706;
        padding-left: 12px;
    }
    
    .vision-mission-card {
        background-color: #f0fdf4;
        border: 1px solid #bbf7d0;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .announcement-card {
        background-color: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border-top: 4px solid #064e3b;
        transition: transform 0.2s;
    }
    
    .announcement-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.1);
    }
    
    .priority-badge-important {
        background-color: #fee2e2;
        color: #991b1b;
        font-weight: 700;
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        font-size: 0.8rem;
        display: inline-block;
        margin-bottom: 0.5rem;
        border: 1px solid #fecaca;
    }
    
    .priority-badge-normal {
        background-color: #e0f2fe;
        color: #0369a1;
        font-weight: 700;
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        font-size: 0.8rem;
        display: inline-block;
        margin-bottom: 0.5rem;
        border: 1px solid #bae6fd;
    }
    
    .footer {
        text-align: center;
        padding: 2rem;
        margin-top: 3rem;
        color: #6b7280;
        font-size: 0.9rem;
        border-top: 1px solid #e5e7eb;
    }
</style>
""", unsafe_allow_html=True)

# Main Web App Layout
# Header Section
st.markdown("""
    <div class="main-header">
        <h1>PORTAL UNIT HAL EHWAL MURID (HEM)</h1>
        <p>SEKOLAH KEBANGSAAN KUBANG KERIAN 3, KELANTAN</p>
    </div>
""", unsafe_allow_html=True)

# ----------------- SIDEBAR: ADMIN LOGIN & CONTROLS -----------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2991/2991112.png", width=70) # Modern School Placeholder Icon
    st.markdown("### **Akses Pentadbir (Admin)**")
    
    # Session state for tracking admin login status
    if 'is_admin' not in st.session_state:
        st.session_state.is_admin = False
        
    if not st.session_state.is_admin:
        admin_password = st.text_input("Sila masukkan Kata Laluan Admin:", type="password")
        if st.button("Log Masuk 🔑", use_container_width=True):
            if admin_password == "adminhem3":
                st.session_state.is_admin = True
                st.success("Log masuk berjaya!")
                st.rerun()
            else:
                st.error("Kata laluan salah! Sila cuba lagi.")
    else:
        st.markdown("<span style='color:green; font-weight:bold;'>✓ Mod Admin Aktif</span>", unsafe_allow_html=True)
        if st.button("Log Keluar 🔒", use_container_width=True):
            st.session_state.is_admin = False
            st.success("Log keluar berjaya.")
            st.rerun()
            
    st.markdown("---")
    st.markdown("""
    **Slogan HEM:**
    *“Disiplin Terpuji, Kebajikan Terjaga, Murid Cemerlang.”*
    """)

# ----------------- MAIN LAYOUT -----------------
col_main, col_side = st.columns([7, 3])

with col_main:
    # ----------------- MULTIMEDIA SLIDER (MAX 5) -----------------
    active_slides = [s for s in st.session_state.hem_data["slider"] if s.get("active", True)][:5]
    
    if active_slides:
        # Build Swiper.js Slider inside an Iframe to support features like Autoplay, Loop & responsive video display
        slides_html = ""
        for s in active_slides:
            media_content = ""
            if s["type"] == "image":
                media_content = f'<img src="{s["url"]}" class="slider-media">'
            elif s["type"] == "video":
                media_content = f'''
                <video class="slider-media" autoplay loop muted playsinline>
                    <source src="{s["url"]}" type="video/mp4">
                    Browser anda tidak menyokong tag video HTML5.
                </video>
                '''
            
            # Slide template with gradient text overlay
            slides_html += f'''
            <div class="swiper-slide">
                {media_content}
                <div class="slider-overlay">
                    <h3>{s["title"]}</h3>
                    <p>{s["desc"]}</p>
                </div>
            </div>
            '''
            
        swiper_component = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <!-- Swiper CSS -->
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
            <style>
                html, body {{
                    margin: 0;
                    padding: 0;
                    width: 100%;
                    height: 100%;
                    background-color: transparent;
                    font-family: 'Inter', sans-serif;
                }}
                .swiper {{
                    width: 100%;
                    height: 380px;
                    border-radius: 16px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.15);
                    overflow: hidden;
                    position: relative;
                }}
                .swiper-slide {{
                    position: relative;
                    width: 100%;
                    height: 100%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    background-color: #000;
                }}
                .slider-media {{
                    width: 100%;
                    height: 100%;
                    object-fit: cover;
                }}
                .slider-overlay {{
                    position: absolute;
                    bottom: 0;
                    left: 0;
                    right: 0;
                    background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.4) 60%, rgba(0,0,0,0) 100%);
                    color: white;
                    padding: 40px 25px 25px 25px;
                    text-align: left;
                    z-index: 10;
                }}
                .slider-overlay h3 {{
                    margin: 0 0 8px 0;
                    font-size: 20px;
                    font-weight: 700;
                    color: #fef08a;
                    text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
                }}
                .slider-overlay p {{
                    margin: 0;
                    font-size: 14px;
                    color: #f3f4f6;
                    font-weight: 300;
                    text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
                }}
                /* Customize Swiper Buttons */
                .swiper-button-next, .swiper-button-prev {{
                    color: #d97706 !important;
                    background: rgba(255,255,255,0.2);
                    width: 40px;
                    height: 40px;
                    border-radius: 50%;
                    backdrop-filter: blur(4px);
                }}
                .swiper-button-next::after, .swiper-button-prev::after {{
                    font-size: 16px !important;
                    font-weight: bold;
                }}
                .swiper-pagination-bullet-active {{
                    background: #d97706 !important;
                }}
            </style>
        </head>
        <body>
            <div class="swiper mySwiper">
                <div class="swiper-wrapper">
                    {slides_html}
                </div>
                <!-- Navigation -->
                <div class="swiper-button-next"></div>
                <div class="swiper-button-prev"></div>
                <!-- Pagination -->
                <div class="swiper-pagination"></div>
            </div>

            <!-- Swiper JS -->
            <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
            <script>
                const swiper = new Swiper('.mySwiper', {{
                    loop: true,
                    spaceBetween: 0,
                    effect: 'fade',
                    fadeEffect: {{
                        crossFade: true
                    }},
                    autoplay: {{
                        delay: 6000,
                        disableOnInteraction: false,
                    }},
                    pagination: {{
                        el: '.swiper-pagination',
                        clickable: true,
                    }},
                    navigation: {{
                        nextEl: '.swiper-button-next',
                        prevEl: '.swiper-button-prev',
                    }},
                }});
            </script>
        </body>
        </html>
        '''
        st.components.v1.html(swiper_component, height=400)
    else:
        st.info("Tiada slider aktif untuk dipaparkan. Sila tambah atau aktifkan slider di panel admin.")

    # ----------------- ANNOUNCEMENTS SECTION -----------------
    st.markdown('<div class="section-title">📢 Pengumuman & Berita Terkini</div>', unsafe_allow_html=True)
    
    announcements = st.session_state.hem_data.get("announcements", [])
    
    if announcements:
        # Sort announcements by date (latest first)
        try:
            sorted_announcements = sorted(announcements, key=lambda x: x.get('date', ''), reverse=True)
        except Exception:
            sorted_announcements = announcements
            
        for ann in sorted_announcements:
            badge_class = "priority-badge-important" if ann.get("priority") == "Penting" else "priority-badge-normal"
            badge_label = ann.get("priority", "Normal").upper()
            
            # Format Date nicely
            raw_date = ann.get("date", "")
            try:
                date_obj = datetime.strptime(raw_date, "%Y-%m-%d")
                formatted_date = date_obj.strftime("%d %b %Y")
            except Exception:
                formatted_date = raw_date
                
            st.markdown(f'''
            <div class="announcement-card">
                <span class="{badge_class}">{badge_label}</span>
                <span style="float: right; color: #6b7280; font-size: 0.85rem;">📅 {formatted_date}</span>
                <h3 style="margin-top: 0.5rem; margin-bottom: 0.8rem; color: #064e3b; font-weight: 700; font-size: 1.3rem;">{ann["title"]}</h3>
                <p style="color: #4b5563; font-size: 1rem; line-height: 1.6; margin-bottom: 1rem;">{ann["content"]}</p>
            </div>
            ''', unsafe_allow_html=True)
            
            # Optional image/video display for announcements
            media_type = ann.get("media_type", "none")
            media_url = ann.get("media_url", "")
            
            if media_type != "none" and media_url:
                if media_type == "image":
                    st.image(media_url, use_container_width=True, caption=ann["title"])
                elif media_type == "video":
                    st.video(media_url, autoplay=True, loop=True, muted=True)
                    
            st.markdown("<br>", unsafe_allow_html=True)
    else:
        st.info("Tiada sebarang pengumuman buat masa ini.")

with col_side:
    # ----------------- SIDEBAR INFO: VISION, MISSION, CONTACT -----------------
    st.markdown('<div class="section-title">📌 Info Unit HEM</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="vision-mission-card">
        <h4 style="color: #064e3b; margin-top: 0; font-weight: 700; border-bottom: 2px solid #bbf7d0; padding-bottom: 4px;">🎯 VISI</h4>
        <p style="font-size: 0.95rem; line-height: 1.5; color: #1e293b; margin-bottom: 1rem;">
            Mewujudkan persekitaran sekolah yang selamat, kondusif, and melahirkan murid SK Kubang Kerian 3 yang berdisiplin, berakhlak mulia serta cemerlang dari segi rohani dan jasmani.
        </p>
        <h4 style="color: #064e3b; margin-top: 0; font-weight: 700; border-bottom: 2px solid #bbf7d0; padding-bottom: 4px;">🚀 MISI</h4>
        <ul style="font-size: 0.95rem; line-height: 1.5; color: #1e293b; padding-left: 1.2rem; margin: 0;">
            <li>Memantapkan pengurusan kebajikan dan keselamatan murid secara adil dan saksama.</li>
            <li>Memupuk kesedaran sivik, kepimpinan, dan pembinaan sahsiah terpuji secara berterusan.</li>
            <li>Menjalinkan kerjasama erat antara pihak sekolah, ibu bapa, dan komuniti luar.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #fffbeb; border: 1px solid #fef3c7; border-radius: 12px; padding: 1.2rem; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
        <h4 style="color: #d97706; margin-top: 0; font-weight: 700; margin-bottom: 8px;">📞 Hubungi Kami</h4>
        <p style="font-size: 0.85rem; color: #4b5563; margin: 4px 0;"><strong>Alamat:</strong> SK Kubang Kerian 3, Jalan Raja Perempuan Zainab II, 16150 Kota Bharu, Kelantan.</p>
        <p style="font-size: 0.85rem; color: #4b5563; margin: 4px 0;"><strong>Emel:</strong> skkk3.hem@gmail.com</p>
        <p style="font-size: 0.85rem; color: #4b5563; margin: 4px 0;"><strong>Sesi Sekolah:</strong> Pagi (7:30 PG - 1:00 PTG)</p>
    </div>
    """, unsafe_allow_html=True)

# ----------------- ADMIN WORKFLOWS (IF LOGGED IN) -----------------
if st.session_state.is_admin:
    st.markdown("<hr style='border: 2px solid #d97706;'>", unsafe_allow_html=True)
    st.markdown("## ⚙️ PANEL KAWALAN PENTADBIR (ADMIN CONTROL)")
    
    tab_slider, tab_ann = st.tabs(["🖼️ Urus Slider (Maksimum 5)", "📢 Urus Pengumuman"])
    
    # --- TAB 1: MANAGE SLIDER ---
    with tab_slider:
        st.subheader("Urusan Multimedia Slider")
        st.info("Anda boleh menetapkan maksimum 5 slider aktif. Pastikan URL gambar atau video adalah URL terus (direct URL) yang sah.")
        
        sliders = st.session_state.hem_data.get("slider", [])
        
        # Edit existing slides
        for i, s in enumerate(sliders):
            with st.expander(f"Slider {i+1}: {s.get('title', 'Tiada Tajuk')}"):
                col_s1, col_s2 = st.columns([2, 1])
                with col_s1:
                    s["title"] = st.text_input(f"Tajuk Slider {i+1}", s.get("title", ""), key=f"title_s_{i}")
                    s["desc"] = st.text_area(f"Keterangan Slider {i+1}", s.get("desc", ""), key=f"desc_s_{i}", height=70)
                with col_s2:
                    s["type"] = st.selectbox(f"Jenis Media {i+1}", ["image", "video"], index=0 if s.get("type", "image") == "image" else 1, key=f"type_s_{i}")
                    s["active"] = st.checkbox("Aktifkan Slider Ini", s.get("active", True), key=f"active_s_{i}")
                
                s["url"] = st.text_input(f"URL Media Slider {i+1}", s.get("url", ""), key=f"url_s_{i}")
                
                # Dynamic Preview
                if s["url"]:
                    st.markdown("**Pratonton Slider:**")
                    if s["type"] == "image":
                        st.image(s["url"], width=250)
                    else:
                        st.video(s["url"])
                        
                if st.button(f"Hapus Slider {i+1}", key=f"del_s_{i}"):
                    sliders.pop(i)
                    st.session_state.hem_data["slider"] = sliders
                    save_data(st.session_state.hem_data)
                    st.success("Slider berjaya dihapuskan!")
                    st.rerun()
                    
        st.markdown("---")
        # Add new slide (if less than 5)
        if len(sliders) < 5:
            st.markdown("### **Tambah Slider Baharu**")
            with st.form("add_slide_form"):
                new_title = st.text_input("Tajuk Slider")
                new_desc = st.text_area("Keterangan Slider", height=70)
                col_f1, col_f2 = st.columns(2)
                with col_f1:
                    new_type = st.selectbox("Jenis Media", ["image", "video"])
                with col_f2:
                    new_url = st.text_input("URL Media (Direct URL)")
                
                submitted = st.form_submit_button("Tambah Slider ➕")
                if submitted:
                    if not new_title or not new_url:
                        st.error("Tajuk dan URL Media wajib diisi!")
                    else:
                        new_slide = {
                            "id": len(sliders) + 1,
                            "title": new_title,
                            "desc": new_desc,
                            "type": new_type,
                            "url": new_url,
                            "active": True
                        }
                        sliders.append(new_slide)
                        st.session_state.hem_data["slider"] = sliders
                        save_data(st.session_state.hem_data)
                        st.success("Slider baharu berjaya ditambah!")
                        st.rerun()
        else:
            st.warning("Maksimum 5 slider telah dicapai. Sila hapus slider sedia ada untuk menambah slider yang baharu.")

    # --- TAB 2: MANAGE ANNOUNCEMENTS ---
    with tab_ann:
        st.subheader("Urusan Pengumuman")
        
        # Add new announcement
        st.markdown("### **Tambah Pengumuman Baharu**")
        with st.form("add_announcement_form"):
            ann_title = st.text_input("Tajuk Pengumuman")
            ann_content = st.text_area("Kandungan Pengumuman", height=120)
            
            col_a1, col_a2, col_a3 = st.columns(3)
            with col_a1:
                ann_date = st.date_input("Tarikh Pengumuman", datetime.now()).strftime("%Y-%m-%d")
            with col_a2:
                ann_priority = st.selectbox("Keutamaan", ["Normal", "Penting"])
            with col_a3:
                ann_media_type = st.selectbox("Jenis Media Lampiran", ["none", "image", "video"])
                
            ann_media_url = st.text_input("URL Media Lampiran (Jika Ada)")
            
            submitted_ann = st.form_submit_button("Terbitkan Pengumuman 🚀")
            if submitted_ann:
                if not ann_title or not ann_content:
                    st.error("Tajuk dan Kandungan Pengumuman wajib diisi!")
                else:
                    new_ann = {
                        "id": str(datetime.now().timestamp()),
                        "title": ann_title,
                        "date": ann_date,
                        "content": ann_content,
                        "media_type": ann_media_type,
                        "media_url": ann_media_url,
                        "priority": ann_priority
                    }
                    if "announcements" not in st.session_state.hem_data:
                        st.session_state.hem_data["announcements"] = []
                    st.session_state.hem_data["announcements"].append(new_ann)
                    save_data(st.session_state.hem_data)
                    st.success("Pengumuman berjaya diterbitkan!")
                    st.rerun()
                    
        st.markdown("---")
        # List and delete announcements
        st.markdown("### **Senarai & Hapus Pengumuman Sedia Ada**")
        ann_list = st.session_state.hem_data.get("announcements", [])
        
        if ann_list:
            for idx, ann in enumerate(ann_list):
                col_d1, col_d2 = st.columns([5, 1])
                with col_d1:
                    st.markdown(f"**{ann.get('title')}** (Tarikh: {ann.get('date')} | Keutamaan: {ann.get('priority')})")
                with col_d2:
                    if st.button("Hapus 🗑️", key=f"del_ann_{idx}"):
                        ann_list.pop(idx)
                        st.session_state.hem_data["announcements"] = ann_list
                        save_data(st.session_state.hem_data)
                        st.success("Pengumuman berjaya dihapus!")
                        st.rerun()
        else:
            st.info("Tiada pengumuman sedia ada untuk diuruskan.")

# Footer section
st.markdown("""
    <div class="footer">
        <p>© 2026 Unit Hal Ehwal Murid, SK Kubang Kerian 3. Semua Hak Cipta Terpelihara.</p>
        <p>Dibangunkan dengan ❤️ menggunakan Streamlit & Swiper.js.</p>
    </div>
""", unsafe_allow_html=True)
