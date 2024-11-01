import streamlit as st
import base64
from PIL import Image
import pandas as pd

def add_logo_and_name():
    # Add profile picture styling
    st.sidebar.markdown(
        """
        <style>
        .sidebar-img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 80%;
            border-radius: 50%;
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    # Load and display profile picture using st.image
    try:
        image = Image.open("foto/photo_2024-10-26_09-25-53.jpg")
        st.sidebar.image(image, use_column_width=True, caption="")
    except Exception as e:
        st.sidebar.error(f"Error loading image: {str(e)}")
        st.sidebar.warning("Please check if the image path is correct")
    
    # Add name and title in sidebar
    st.sidebar.markdown("<h1 style='text-align: center; color: #1E88E5;'>Irfan Triadi Saputra</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='text-align: center; font-size: 1.2em;'>Back-End AI Developer</p>", unsafe_allow_html=True)
    
    # Add social links
    st.sidebar.markdown("---")
    st.sidebar.markdown("<h3 style='text-align: center;'>Connect With Me</h3>", unsafe_allow_html=True)
    social_links = {
        "LinkedIn": "https://www.linkedin.com/in/irfan-triadi-saputra/",
        "GitHub": "https://github.com/Irfantriadis",
        "Instagram": "@irfantriadis_",
        "Email": "irfants1710@gmail.com"
    }
    
    for platform, link in social_links.items():
        if platform in ["LinkedIn", "GitHub"]:
            st.sidebar.markdown(f"<p style='text-align: center;'><a href='{link}'>{platform}</a></p>", unsafe_allow_html=True)
        else:
            st.sidebar.markdown(f"<p style='text-align: center;'>{platform}: {link}</p>", unsafe_allow_html=True)

def main():
    # Set page config
    st.set_page_config(
        page_title="Irfan Triadi Saputra - Portfolio",
        page_icon="👨‍💻",
        layout="wide"
    )

    # Add sidebar content
    add_logo_and_name()

    # Custom CSS
    st.markdown("""
    <style>
    .big-font {
        font-size:50px !important;
        font-weight: bold;
    }
    .medium-font {
        font-size:30px !important;
        font-weight: bold;
    }
    .small-font {
        font-size:20px !important;
    }
    .highlight {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .main-content {
        padding-left: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Main content area
    with st.container():
        # About Me Section
        st.markdown("## 👨‍💼 About Me")
        st.markdown("""
        Irfan Triadi Saputra,
        lulus tahun 2024 dari program Studi Teknik Informatika, Politeknik Harapan Bersama dengan IPK 3.89. 
        Memiliki pengalaman sebagai Ketua Study Club Forum Riset Teknologi Informasi (FORTI) dengan achievement 75% target program kerja tercapai.
        Berpengalaman dalam pengembangan web, AI, dan machine learning dengan berbagai proyek yang telah dikembangkan.
        """)

        # Contact Information in main area
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 📞 Contact Information")
            st.write("📍 Kabupaten Pemalang, Jawa Tengah 52361")
            st.write("📱 +62 823 2428 2477")

        # Skills Section
        st.markdown("## 🛠️ Skills & Competencies")
        
        col1, col2 = st.columns(2)
        
        with col1:
            skills = [
                "Python ⭐⭐⭐⭐⭐",
                "Public Speaking ⭐⭐⭐⭐",
                "Artificial Intelligence ⭐⭐⭐⭐",
                "Machine Learning ⭐⭐⭐⭐"
            ]
            
            for skill in skills:
                st.write(f"- {skill}")
                
        with col2:
            more_skills = [
                "Image Processing ⭐⭐⭐⭐",
                "Data Analysis ⭐⭐⭐⭐",
            ]
            
            for skill in more_skills:
                st.write(f"- {skill}")

        # Work Experience
        st.markdown("## 💼 Professional Experience")
        
        st.markdown("### Back-End AI Developer")
        st.markdown("*PT. Inti Utama Solusindo (Pharos Group) | MSIB Program*")
        st.markdown("- Mengembangkan Forklift Otomatis dengan teknologi Object Detection")
        st.markdown("- Durasi: 6 bulan")

        st.markdown("### Assistant Dosen")
        st.markdown("*Politeknik Harapan Bersama*")
        st.markdown("""
        - Mengajar mata kuliah Pemrograman Sistem Cerdas 1 (Kelas RPL: 1 Kelas)
        - Mengajar mata kuliah Pemrograman Sistem Cerdas 2 (Kelas Reguler: 3 Kelas)
        - Durasi: 1 semester
        """)

        # Projects Section
        st.markdown("## 🚀 Projects")
        
        projects = {
            "SI-Mosque": "Sistem Informasi Keuangan Masjid untuk mewujudkan Good Mosque Governance",
            "Stunting App": "Virtual Assistant, Prediksi dan Klasifikasi Image untuk penanganan stunting",
            "Class Child Education": "Game edukasi pembelajaran untuk anak-anak",
            "BAIKMU: Self Care": "Aplikasi Virtual Assistant Kesehatan Mental"
        }
        
        for project, description in projects.items():
            with st.expander(f"🔍 {project}"):
                st.write(description)

        # Organizational Experience
        st.markdown("## 👥 Organizational Experience")
        
        st.markdown("### Ketua Study Club Forum Riset dan Teknologi Informasi (FORTI)")
        st.markdown("*Agustus 2021 - Mei 2023*")
        st.markdown("""
        - Mengelola dan mengkoordinasi kegiatan riset dan kepenulisan mahasiswa
        - Mencapai 75% target program kerja
        - Membimbing lebih dari 10 Tim dalam kompetisi tingkat nasional
        """)

        st.markdown("### Koordinator Humas INVOFEST")
        st.markdown("*Agustus 2022 - Desember 2022*")
        st.markdown("- Mengelola komunikasi dan persebaran informasi kegiatan internal dan eksternal kampus")

        # Education
        st.markdown("## 📚 Education")
        
        st.markdown("### Politeknik Harapan Bersama (2020-2024)")
        st.markdown("*Sarjana Terapan Teknik Informatika - IPK 3.89*")
        
        with st.expander("🏆 Achievements & Publications"):
            achievements = [
                "Finalis 7 Lomba Kepenulisan National Youth Competition",
                "Peraih Insentif PKM DIKTI VOKASI Tingkat Nasional (2021, 2023)",
                "Juara 3 Lomba Karya Tulis Ilmiah Vocation Of The Champions",
                "Juara 3 Penelitian Insentif BAPPEDA Kabupaten Tegal",
                "Terbaik Kedua Capstone Project Semester 5",
                "Terbaik Ketiga Capstone Project Semester 6",
                "Mahasiswa Terbaik Program Studi Diploma IV Teknik Informatika 2022"
            ]
            
            publications = [
                "Game online multiplayer untuk pembelajaran jarak jauh siswa TK IT Khairunnisa",
                "Aplikasi Question Answer Sebagai Media Pembelajaran Interaktif Untuk Mata Pelajaran Akuntansi",
                "Peningkatan Ketrampilan Digital Enterpreneur Bagi Siswa Siswi SMK",
                "Si-Mosque: Instrumen Pelaporan Keuangan Masjid untuk Mewujudkan Good Mosque Governance",
                "HKI Si-Mosque.com",
                "HKI BaikMu: Self Care Mobile Apps"
            ]
            
            st.markdown("#### 🏆 Achievements:")
            for achievement in achievements:
                st.markdown(f"- {achievement}")
                
            st.markdown("#### 📝 Publications:")
            for publication in publications:
                st.markdown(f"- {publication}")

        st.markdown("### SMA NEGERI 2 PEMALANG (2016-2019)")
        st.markdown("*Jurusan IPS (Ilmu Pengetahuan Sosial)*")
        st.markdown("""
        - Juara Harapan 2 Kompetisi Band Tingkat Keresidenan Pekalongan
        - Koordinator TEKPRAM di PRAMUKA
        """)

if __name__ == "__main__":
    main()
