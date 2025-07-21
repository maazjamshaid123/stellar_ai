import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from PIL import Image
import requests
from streamlit_option_menu import option_menu
import base64
import os
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="Stellar AI - Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
    }
    .css-1d391kg {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
    }
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border: none;
        border-radius: 25px;
        color: white;
        padding: 10px 30px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
    }
    .metric-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    .project-card {
        background: rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(15px);
        transition: all 0.3s ease;
    }
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(102, 126, 234, 0.2);
    }
    .expertise-item {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(102, 126, 234, 0.3);
        margin: 10px 0;
    }
    .hero-section {
        text-align: center;
        padding: 80px 0;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border-radius: 30px;
        margin: 20px 0;
    }
    .section-title {
        color: #667eea;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 0 0 20px rgba(102, 126, 234, 0.5);
    }
    .section-subtitle {
        color: #a8b2d1;
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 50px;
    }
</style>
""", unsafe_allow_html=True)

# Custom CSS for modern nav bar
st.markdown("""
<style>
    .st-emotion-cache-1avcm0n { /* Option menu container */
        background: rgba(20, 22, 34, 0.85) !important;
        border-radius: 18px !important;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
        backdrop-filter: blur(12px);
        margin: 24px 0 32px 0 !important;
        padding: 0.5rem 2rem !important;
        border: 1px solid rgba(255,255,255,0.08);
    }
    .st-emotion-cache-1avcm0n .nav-link {
        color: #3a4266 !important;
        font-size: 1.1rem !important;
        font-weight: 500 !important;
        border-radius: 12px !important;
        margin: 0 0.5rem !important;
        padding: 0.7rem 1.6rem !important;
        transition: background 0.2s, color 0.2s, box-shadow 0.2s;
    }
    .st-emotion-cache-1avcm0n .nav-link:hover {
        background: rgba(102, 126, 234, 0.12) !important;
        color: #667eea !important;
        box-shadow: 0 2px 8px 0 rgba(102, 126, 234, 0.08);
    }
    .st-emotion-cache-1avcm0n .nav-link-selected {
        background: linear-gradient(90deg, #667eea 0%, #60a5fa 100%) !important;
        color: #fff !important;
        font-weight: 700 !important;
        box-shadow: 0 4px 16px 0 rgba(102, 126, 234, 0.15);
        border-radius: 14px !important;
    }
    .st-emotion-cache-1avcm0n .nav-icon {
        color: #3a4266 !important;
        font-size: 1.3rem !important;
        margin-right: 0.5rem !important;
    }
</style>
""", unsafe_allow_html=True)

# Navigation
selected = option_menu(
    menu_title=None,
    options=["Home", "About", "Projects", "Expertise", "Contact"],
    icons=["house", "person", "folder", "cpu", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background": "none"},
        "icon": {"color": "#3a4266", "font-size": "20px"},
        "nav-link": {
            "font-size": "1.1rem",
            "font-weight": "500",
            "color": "#3a4266",
            "border-radius": "12px",
            "margin": "0 0.5rem",
            "padding": "0.7rem 1.6rem",
        },
        "nav-link-selected": {
            "background": "linear-gradient(90deg, #667eea 0%, #60a5fa 100%)",
            "color": "#fff",
            "font-weight": "700",
            "border-radius": "14px",
        },
    }
)

# Home Page
if selected == "Home":
    # Rocket Animation
    st.markdown("""
    <div id="rocket-container">
        <div id="rocket" class="rocket-fly">🚀</div>
    </div>
    
    <style>
        @keyframes rocketFly {
            0% {
                transform: translateX(0) translateY(0) rotate(30deg) scale(1);
                opacity: 0;
            }
            10% {
                opacity: 1;
            }
            50% {
                transform: translateX(50vw) translateY(-50vh) rotate(30deg) scale(1.2);
                opacity: 1;
            }
            90% {
                opacity: 1;
            }
            100% {
                transform: translateX(100vw) translateY(-100vh) rotate(30deg) scale(0.8);
                opacity: 0;
            }
        }
        
        @keyframes rocketPulse {
            0%, 100% {
                text-shadow: 0 0 5px #667eea, 0 0 10px #667eea, 0 0 15px #667eea;
            }
            50% {
                text-shadow: 0 0 10px #60a5fa, 0 0 20px #60a5fa, 0 0 30px #60a5fa;
            }
        }
        
        #rocket-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100vh;
            pointer-events: none;
            z-index: 1000;
        }
        
        #rocket {
            position: absolute;
            font-size: 3rem;
            bottom: 0;
            left: 0;
            animation: rocketFly 4s ease-in-out forwards, rocketPulse 0.5s infinite alternate;
            filter: drop-shadow(0 0 10px rgba(102, 126, 234, 0.7));
        }
        
        .rocket-fly {
            animation-delay: 0.5s;
        }
    </style>
    
    <script>
        // Trigger rocket animation on page load
        setTimeout(function() {
            var rocket = document.getElementById('rocket');
            if (rocket) {
                rocket.style.animationPlayState = 'running';
            }
        }, 100);
    </script>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="hero-section">
        <h1 style="color: #ffffff; font-size: 4rem; margin-bottom: 20px; text-shadow: 0 0 30px rgba(102, 126, 234, 0.8);">
            🚀 Stellar AI
        </h1>
        <p style="color: #a8b2d1; font-size: 1.5rem; margin-bottom: 30px;">
            Pioneering the Future of Artificial Intelligence Applications
        </p>
        <p style="color: #8892b0; font-size: 1.1rem; max-width: 800px; margin: 0 auto;">
            Stellar AI delivers innovative solutions across the entire spectrum of artificial intelligence. From computer vision and natural language processing to automation, predictive analytics, and generative AI, we build, deploy, and scale all types of AI applications for businesses and individuals worldwide.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #667eea; font-size: 2rem; margin-bottom: 10px;">40+</h3>
            <p style="color: #a8b2d1;">Projects Completed</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #667eea; font-size: 2rem; margin-bottom: 10px;">10+</h3>
            <p style="color: #a8b2d1;">AI Models</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #667eea; font-size: 2rem; margin-bottom: 10px;">99.9%</h3>
            <p style="color: #a8b2d1;">Uptime</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #667eea; font-size: 2rem; margin-bottom: 10px;">10+</h3>
            <p style="color: #a8b2d1;">Countries Served</p>
        </div>
        """, unsafe_allow_html=True)

# About Page
elif selected == "About":
    st.markdown('<h1 class="section-title">About Stellar AI</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.05); border-radius: 20px; padding: 30px; border: 1px solid rgba(255,255,255,0.1);">
            <h3 style="color: #667eea; margin-bottom: 20px;">Our Mission</h3>
            <p style="color: #a8b2d1; line-height: 1.8;">
                At Stellar AI, we're driven by the belief that artificial intelligence can solve the world's most 
                complex challenges. Our team of experts combines deep technical knowledge with innovative thinking 
                to create solutions that push the boundaries of what's possible.
            </p>
            <p style="color: #a8b2d1; line-height: 1.8;">
                From advanced trading algorithms to cutting-edge machine learning models, we're building the 
                future of technology, one breakthrough at a time.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.05); border-radius: 20px; padding: 30px; border: 1px solid rgba(255,255,255,0.1);">
            <h3 style="color: #667eea; margin-bottom: 20px;">Core Values</h3>
            <ul style="color: #a8b2d1; line-height: 2;">
                <li><strong>Innovation:</strong> Constantly pushing technological boundaries</li>
                <li><strong>Excellence:</strong> Delivering world-class solutions</li>
                <li><strong>Reliability:</strong> Building systems you can trust</li>
                <li><strong>Transparency:</strong> Clear communication and honest partnerships</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # --- Meet the Team Section ---
    st.markdown('<h2 style="color: #667eea; margin-top: 48px; margin-bottom: 32px; text-align: center;">Meet the Team</h2>', unsafe_allow_html=True)
    team_col1, team_col2 = st.columns(2)
    with team_col1:
        maaz_img = Image.open("Maaz.png")
        maaz_buf = BytesIO()
        maaz_img.save(maaz_buf, format="PNG")
        maaz_b64 = base64.b64encode(maaz_buf.getvalue()).decode()
        st.markdown("""
        <div style='text-align: center;'>
            <img src='data:image/png;base64,""" + maaz_b64 + """' width='180' style='border-radius: 12px;'/><br/>
            <h4 style="color: #667eea; margin-bottom: 8px;">Maaz</h4>
            <p style="color: #a8b2d1; margin-bottom: 4px; font-size: 1.05rem;">Head of Machine Learning Department</p>
            <span style="background: rgba(102, 126, 234, 0.15); color: #667eea; padding: 6px 16px; border-radius: 12px; font-size: 0.95rem;">7+ Years Experience</span>
            <p style='color: #a8b2d1; margin-top: 14px; font-size: 0.98rem;'>A visionary in AI and data science, Maaz leads Stellar AI's machine learning initiatives with a focus on innovation, reliability, and real-world impact. He has architected and delivered dozens of advanced AI solutions across industries, specializing in deep learning, NLP, and predictive analytics. Maaz is known for his hands-on leadership, technical depth, and commitment to client success.</p>
        </div>
        """, unsafe_allow_html=True)
    with team_col2:
        zaid_img = Image.open("Zaid.png")
        zaid_buf = BytesIO()
        zaid_img.save(zaid_buf, format="PNG")
        zaid_b64 = base64.b64encode(zaid_buf.getvalue()).decode()
        st.markdown("""
        <div style='text-align: center;'>
            <img src='data:image/png;base64,""" + zaid_b64 + """' width='180' style='border-radius: 12px;'/><br/>
            <h4 style="color: #667eea; margin-bottom: 8px;">Zaid</h4>
            <p style="color: #a8b2d1; margin-bottom: 4px; font-size: 1.05rem;">Head of Web Design</p>
            <span style="background: rgba(102, 126, 234, 0.15); color: #667eea; padding: 6px 16px; border-radius: 12px; font-size: 0.95rem;">7+ Years Experience</span>
            <p style='color: #a8b2d1; margin-top: 14px; font-size: 0.98rem;'>Zaid is the creative force behind Stellar AI's modern, user-centric web experiences. With a keen eye for design and usability, he transforms complex ideas into beautiful, intuitive interfaces. Zaid's expertise spans UI/UX, responsive design, and frontend engineering, ensuring every project not only works flawlessly but looks stunning across all platforms.</p>
        </div>
        """, unsafe_allow_html=True)

    # --- Testimonials Section ---
    st.markdown("""
    <div style="text-align: center; margin: 56px 0 48px 0;">
        <h2 style="color: #667eea; font-size: 2.5rem; font-weight: 700; margin-bottom: 16px; 
                   background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
                   background-clip: text;">
            What Our Clients Say
        </h2>
        <div style="width: 80px; height: 4px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    margin: 0 auto; border-radius: 2px;"></div>
    </div>
    """, unsafe_allow_html=True)
    
    testimonials = [
        "Absolutely exceeded expectations. The AI solution was delivered on time and works flawlessly!",
        "Professional, responsive, and highly skilled. Will definitely work with them again.",
        "Stellar AI turned our ideas into reality. The automation saved us countless hours.",
        "Modern design, robust backend, and great communication throughout the project.",
        "Outstanding work! The machine learning model accuracy was beyond what we hoped for.",
        "Fast delivery, excellent communication, and results that truly made a difference to our business.",
        "The team understood our complex requirements and delivered exactly what we needed.",
        "Impressive technical skills combined with great project management. Highly recommended!"
    ]
    
    # First row of testimonials
    test_cols = st.columns(4, gap="medium")
    
    for i, review in enumerate(testimonials[:4]):
        with test_cols[i]:
            # Stars
            st.markdown("⭐⭐⭐⭐⭐", unsafe_allow_html=True)
            
            # Review in a styled container
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.1); border-radius: 16px; padding: 20px; margin: 10px 0; border: 1px solid rgba(102,126,234,0.2); text-align: center;">
                <p style="color: #e8e8e8; font-style: italic; margin-bottom: 0;">"{review}"</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Second row of testimonials
    test_cols2 = st.columns(4, gap="medium")
    
    for i, review in enumerate(testimonials[4:]):
        with test_cols2[i]:
            # Stars
            st.markdown("⭐⭐⭐⭐⭐", unsafe_allow_html=True)
            
            # Review in a styled container
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.1); border-radius: 16px; padding: 20px; margin: 10px 0; border: 1px solid rgba(102,126,234,0.2); text-align: center;">
                <p style="color: #e8e8e8; font-style: italic; margin-bottom: 0;">"{review}"</p>
            </div>
            """, unsafe_allow_html=True)

# Projects Page
elif selected == "Projects":
    st.markdown('<h1 class="section-title">Our Projects</h1>', unsafe_allow_html=True)
    
    # Project data
    projects = [
        {
            "name": "MT5 AI Trading Bot with Multi-API Integration",
            "description": "Developed a robust AI-powered trading bot for MetaTrader 5 (MT5) that integrates with Databento and FinancialModelingPrep APIs. The system fetches real-time and historical market data, processes COT reports, and uses advanced machine learning (PyCaret, custom models) to generate and execute trading signals. Includes full deployment, error handling, and Telegram alerting.",
            "tech": ["Python", "MetaTrader5", "Databento API", "FinancialModelingPrep API", "PyCaret", "Pandas", "Telegram Bot API", "Linux Deployment"],
            "status": "Completed",
            "performance": "Production-ready",
            "location": "United States"
        },
        {
            "name": "Horse Race Outcome Prediction Engine",
            "description": "Developed a machine learning engine to predict horse race outcomes using historical race cards, runner performance, and contextual features (class, going, distance, prize money). The system cleans and structures raw data, engineers smart features, and trains/tests multiple models (XGBoost, ensemble stacks) to deliver the most accurate winner predictions with probability scores. Delivered as a deployable engine and web app with full documentation.",
            "tech": ["Python", "XGBoost", "scikit-learn", "Pandas", "Feature Engineering", "Data Preprocessing", "Web App"],
            "status": "Completed",
            "performance": "Production-ready",
            "location": "United Kingdom"
        },
        {
            "name": "United States Stock Market Trading Signal Automation",
            "description": "Reviewed, optimized, and deployed a professional Python-based trading signal system that analyzes United States stock market data using APIs (TwelveData, Finnhub), filters tickers under $10 based on liquidity, volume, price movement, and financial fundamentals, and sends real-time alerts to Telegram channels for both general and high-quality opportunities.",
            "tech": ["Python", "TwelveData API", "Finnhub API", "Pandas", "Telegram Bot API", "Linux VPS", "CyberPanel", "Systemd", "Automation"],
            "status": "Completed",
            "performance": "Production-ready",
            "location": "United States"
        },
        {
            "name": "Bitcoin Rate Prediction AI",
            "description": "Developed a machine learning application to analyze historical Bitcoin price data and discover advanced algorithmic trading rules. The system leverages deep learning and feature engineering to generate predictive models and suggest optimal trading strategies, outperforming manual approaches.",
            "tech": ["Python", "LSTM", "scikit-learn", "Pandas", "Feature Engineering", "API Integration", "Windows Deployment"],
            "status": "Completed",
            "performance": "Production-ready",
            "location": "Poland"
        },
        {
            "name": "Conversational Art Analysis Web App",
            "description": "Developed a full-stack conversational AI web application for a client, enabling users to upload artworks and interact with an assistant (GPT-4 Vision, CLIP, OmniArt) for artist attribution, style analysis, symbolism, and visual element breakdown. The app leverages cloud-based AI APIs and advanced prompt engineering for deep art insights.",
            "tech": ["Next.js", "Tailwind CSS", "Vercel", "OpenAI GPT-4 Vision", "Replicate API", "Hugging Face", "LangChain.js", "Cloudinary/S3", "WikiArt API", "Rijksmuseum API"],
            "status": "Completed",
            "performance": "Production-ready",
            "location": "United States"
        },
        {
            "name": "AI-Powered Lottery Prediction Application",
            "description": "Developed a deep learning and machine learning application to predict Florida Pick 3, Pick 4, and Pick 5 lottery games. The system leverages historical draw data, advanced sequence models (LSTM, TFT), and feature engineering to generate optimized number sets with the highest predictive confidence.",
            "tech": ["Python", "LSTM", "TFT", "Pandas", "Feature Engineering", "Data Preprocessing", "Windows Deployment"],
            "status": "Completed",
            "performance": "91%+ Accuracy (Pick 3/4), 85%+ (Pick 5)",
            "location": "United States"
        },
        {
            "name": "Automated Employee Signature Extraction",
            "description": "Developed a deep learning and image processing system to automatically detect and extract handwritten signatures from scanned ID cards and documents, outputting high-quality PNGs with transparent backgrounds.",
            "tech": ["Python", "YOLOv8", "OpenCV", "Tesseract OCR", "Custom Dataset Labeling", "Image Processing", "Windows Deployment"],
            "status": "Completed",
            "performance": "90%+ Accuracy",
            "location": "Portugal"
        },
        {
            "name": "Lender Matchmaking AI Engine",
            "description": "Developed a robust AI/ML engine for a fintech client to intelligently match borrowers with the most relevant loan products using credit profiles, application data, and historical trends.",
            "tech": ["Python", "scikit-learn", "TensorFlow", "Pandas", "Docker", "REST APIs", "Feature Engineering"],
            "status": "Completed",
            "performance": "98.9%",
            "location": "Japan"
        },
        {
            "name": "Automated Sports Prediction System",
            "description": "Built a robust Python system for a United States client to automate sports score predictions for NBA, NFL, and college games. The solution scrapes real-time stats, injuries, and expert picks, applies layered logic for predictions, and auto-updates daily. Delivered with intuitive dashboard, detailed analytics, and manual override capabilities.",
            "tech": ["Python", "Pandas", "Scikit-learn", "BeautifulSoup", "Dash/Streamlit", "Cron"],
            "status": "Completed",
            "performance": "98.7%",
            "location": "United States"
        },
        {
            "name": "Python Stock Charts OCR & Automation Script",
            "description": "Developed an end-to-end OCR and computer vision pipeline to extract and analyze financial chart data from PNG images, automate scoring, and generate CSV reports with Dropbox integration.",
            "tech": ["Python", "OpenCV", "Tesseract OCR", "Pandas", "Dropbox API", "Windows Automation"],
            "status": "Completed",
            "performance": "99.5%",
            "location": "Mexico"
        },
        {
            "name": "AI/ML Backend for Social Meetup Platform",
            "description": "Developed the full AI/ML backend for a social meetup app, including recommendation systems, NLP, predictive analytics, and fraud detection, collaborating with a cross-functional team.",
            "tech": ["Python", "FastAPI", "TensorFlow Recommenders", "scikit-learn", "XGBoost", "Prophet", "spaCy", "BERT", "Hugging Face", "Docker", "MySQL", "AWS"],
            "status": "Completed",
            "performance": "97.5%",
            "location": "Austria"
        },
        {
            "name": "Portable AI Toolkit (LLM-Powered Desktop & USB Application)",
            "description": "Deployment of a local LLM-based AI toolkit featuring GPT, DeepL, DALL·E, and more, accessible via a beautiful offline menu for both desktop and USB use.",
            "tech": ["Python", "Tkinter", "PyInstaller", "OpenAI GPT", "DeepL API", "DALL·E API", "HTML/JS", "SQLite", "USB Deployment"],
            "status": "Completed",
            "performance": "98.2%",
            "location": "France"
        },
        {
            "name": "AI-Powered Invoicing Automation",
            "description": "End-to-end automation system integrating ChannelDoc WMS, AI agents, and Moneybird invoicing.",
            "tech": ["Python", "LangChain", "REST APIs", "Pandas", "Docker"],
            "status": "Production",
            "performance": "95.8%",
            "location": "Netherlands"
        },
        {
            "name": "FortifAI Fraud Detection System",
            "description": "Developed an advanced fraud detection web application using CatBoost machine learning, real-time transaction simulation, and interactive risk analysis. Features include voice-based OTP verification via Twilio, risk factor breakdown, historical data analysis, and a modern Streamlit dashboard. Enables financial institutions to proactively detect and block high-risk transactions with explainable AI.",
            "tech": ["Python", "Streamlit", "CatBoost", "scikit-learn", "Twilio API", "Pandas", "Matplotlib", "Seaborn"],
            "status": "Completed",
            "performance": "$900 Budget",
            "location": "United States"
        }
    ]
    
    # Display projects in a grid
    cols = st.columns(2, gap="large")
    for i, project in enumerate(projects):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="project-card" style="
                padding: 25px; 
                margin-bottom: 40px; 
                background: rgba(255,255,255,0.05); 
                border-radius: 16px; 
                border: 1px solid rgba(102,126,234,0.2);
                backdrop-filter: blur(10px);
            ">
                <h3 style="color: #667eea; margin-bottom: 15px;">{project['name']}</h3>
                <p style="color: #a8b2d1; margin-bottom: 15px; line-height: 1.6;">{project['description']}</p>
                <div style="margin-bottom: 15px;">
                    <span style="background: rgba(102, 126, 234, 0.2); color: #667eea; padding: 5px 10px; border-radius: 15px; font-size: 0.8rem; margin-right: 5px;">{project['status']}</span>
                    <span style="background: rgba(118, 75, 162, 0.2); color: #764ba2; padding: 5px 10px; border-radius: 15px; font-size: 0.8rem; margin-right: 5px;">{project['performance']} Reliability</span>
                    <span style="background: rgba(255, 193, 7, 0.2); color: #FFC107; padding: 5px 10px; border-radius: 15px; font-size: 0.8rem;">{project['location']}</span>
                </div>
                <div style="display: flex; flex-wrap: wrap; gap: 10px 20px; margin-top: 18px; margin-bottom: 0;">
                    {''.join([f'<span style="background: rgba(255,255,255,0.1); color: #ffffff; padding: 3px 8px; border-radius: 10px; font-size: 0.7rem; margin-bottom: 12px;">{tech}</span>' for tech in project['tech']])}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Featured case study for the MT5 AI Trading Bot with Multi-API Integration project
    st.markdown("""
    <div style="background: rgba(255,255,255,0.05); border-radius: 20px; padding: 30px; border: 1px solid rgba(255,255,255,0.1); margin-top: 40px;">
        <h2 style="color: #667eea; margin-bottom: 20px; text-align: center;">Featured Project: MT5 AI Trading Bot with Multi-API Integration</h2>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 30px;">
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Client: Private Trader</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Built a professional trading automation system for MT5, integrating Databento for historical and real-time trades, and FinancialModelingPrep for COT reports. The bot uses advanced ML (PyCaret, custom feature engineering) to enhance signal quality, supports multiple timeframes, and sends actionable alerts via Telegram. Delivered with full deployment on Linux, documentation, and post-delivery support.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Key Features:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Real-time and historical data fetching from Databento and FMP APIs</li>
                    <li>MT5 integration for live trading and backtesting</li>
                    <li>COT report processing and macro feature extraction</li>
                    <li>Machine learning model training and prediction (PyCaret, custom logic)</li>
                    <li>Telegram alerting for trade signals and system status</li>
                    <li>Robust error handling and background operation</li>
                    <li>Full deployment and documentation</li>
                </ul>
            </div>
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Technical Implementation</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Developed with Python, MetaTrader5, Databento API, FinancialModelingPrep API, PyCaret, Pandas, and Telegram Bot API for robust data processing, ML, and alerting. Deployed on Linux for reliable background operation.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Business Impact:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Enabled automated, data-driven trading on MT5</li>
                    <li>Improved signal quality with multi-source data and ML</li>
                    <li>Reduced manual intervention and increased trading opportunities</li>
                </ul>
                <div style="margin-top: 20px;">
                    <span style="background: rgba(76, 175, 80, 0.2); color: #4CAF50; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; font-weight: bold;">Project Value: $1,200</span>
                    <span style="background: rgba(102, 126, 234, 0.2); color: #667eea; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">Timeline: 2 weeks</span>
                    <span style="background: rgba(255, 193, 7, 0.2); color: #FFC107; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">United States</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Featured case study for the Horse Race Outcome Prediction Engine project
    st.markdown("""
    <div style="background: rgba(255,255,255,0.05); border-radius: 20px; padding: 30px; border: 1px solid rgba(255,255,255,0.1); margin-top: 40px;">
        <h2 style="color: #667eea; margin-bottom: 20px; text-align: center;">Featured Project: Horse Race Outcome Prediction Engine</h2>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 30px;">
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Client: Sports Analytics Enthusiast</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Built a robust machine learning system to predict horse race winners based on historical and contextual data. The solution cleans and structures large CSV datasets, engineers features for form, class, going, distance, and prize money, and tests multiple models to maximize predictive accuracy. Outputs include the most likely winner and probability scores for each runner. Delivered as a web app with full documentation and post-delivery support.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Key Features:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Data cleaning and structuring for large, messy race datasets</li>
                    <li>Feature engineering for form, class, going, distance, and prize money</li>
                    <li>Model training, validation, and selection (XGBoost, ensemble stacks)</li>
                    <li>Probability scoring and winner prediction</li>
                    <li>Web app interface for easy use and future race uploads</li>
                    <li>Full documentation and two rounds of post-delivery support</li>
                </ul>
            </div>
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Technical Implementation</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Developed with Python, XGBoost, scikit-learn, and Pandas for robust feature engineering and prediction. Delivered as a web app with full documentation and support.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Business Impact:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Enabled data-driven horse race predictions for enthusiasts and analysts</li>
                    <li>Improved accuracy over manual or heuristic approaches</li>
                    <li>Scalable to new races and datasets</li>
                </ul>
                <div style="margin-top: 20px;">
                    <span style="background: rgba(76, 175, 80, 0.2); color: #4CAF50; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; font-weight: bold;">Project Value: $1,000</span>
                    <span style="background: rgba(102, 126, 234, 0.2); color: #667eea; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">Timeline: 12–15 days</span>
                    <span style="background: rgba(255, 193, 7, 0.2); color: #FFC107; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">United Kingdom</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Featured case study for the United States Stock Market Trading Signal Automation project
    st.markdown("""
    <div style="background: rgba(255,255,255,0.05); border-radius: 20px; padding: 30px; border: 1px solid rgba(255,255,255,0.1); margin-top: 40px;">
        <h2 style="color: #667eea; margin-bottom: 20px; text-align: center;">Featured Project: United States Stock Market Trading Signal Automation</h2>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 30px;">
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Client: Private Trader</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Combined and refactored 11+ Python scripts into a single, clean, and optimized trading signal system. The solution scans all United States tickers under $10, applies multi-layered filters (liquidity, volume, price movement, cash/debt, margin), and sends entry, liquidity boost, and exit alerts to two Telegram channels. Deployed and tested on Linux VPS with full automation and error handling.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Key Features:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Real-time data analysis from TwelveData and Finnhub APIs</li>
                    <li>Multi-stage filtering for liquidity, technicals, and fundamentals</li>
                    <li>Dual Telegram channel alerting (general and high-quality signals)</li>
                    <li>Automated entry, liquidity boost (+25%), and exit (-15%, -25%) alerts</li>
                    <li>Reliable Linux background operation (systemd)</li>
                    <li>Full deployment, testing, and documentation for future updates</li>
                </ul>
            </div>
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Technical Implementation</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Developed with Python, Pandas, TwelveData and Finnhub APIs, and Telegram Bot API for robust data processing and alerting. Deployed on a Linux VPS (CyberPanel) with systemd for reliable background operation.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Business Impact:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Enabled automated, real-time trading signal delivery</li>
                    <li>Improved reliability and maintainability of trading infrastructure</li>
                    <li>Reduced manual monitoring and increased actionable opportunities</li>
                </ul>
                <div style="margin-top: 20px;">
                    <span style="background: rgba(76, 175, 80, 0.2); color: #4CAF50; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; font-weight: bold;">Project Value: $1,500</span>
                    <span style="background: rgba(102, 126, 234, 0.2); color: #667eea; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">Timeline: 2 weeks</span>
                    <span style="background: rgba(255, 193, 7, 0.2); color: #FFC107; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">United States</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Featured case study for the Bitcoin Rate Prediction AI project
    st.markdown("""
    <div style="background: rgba(255,255,255,0.05); border-radius: 20px; padding: 30px; border: 1px solid rgba(255,255,255,0.1); margin-top: 40px;">
        <h2 style="color: #667eea; margin-bottom: 20px; text-align: center;">Featured Project: Bitcoin Rate Prediction AI</h2>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 30px;">
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Client: Crypto Trader</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Built a machine learning application to analyze historical Bitcoin price data and discover advanced algorithmic trading rules. The system leverages deep learning and feature engineering to generate predictive models and suggest optimal trading strategies, outperforming manual approaches.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Key Features:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Deep learning-based time series prediction (LSTM, scikit-learn)</li>
                    <li>Feature engineering and pattern discovery</li>
                    <li>API integration for real-time Bitcoin rates</li>
                    <li>Automated strategy suggestion and backtesting</li>
                    <li>Local Windows deployment, full documentation</li>
                </ul>
            </div>
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Technical Implementation</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Developed with Python, LSTM, scikit-learn, and Pandas for robust time series modeling and prediction. Integrated with Bitcoin price APIs and delivered as a local Windows app with full documentation and support.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Business Impact:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Enabled data-driven trading decisions</li>
                    <li>Improved prediction accuracy over manual strategies</li>
                    <li>Scalable to other cryptocurrencies and markets</li>
                </ul>
                <div style="margin-top: 20px;">
                    <span style="background: rgba(76, 175, 80, 0.2); color: #4CAF50; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; font-weight: bold;">Project Value: $1,000</span>
                    <span style="background: rgba(102, 126, 234, 0.2); color: #667eea; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">Timeline: 2 weeks</span>
                    <span style="background: rgba(255, 193, 7, 0.2); color: #FFC107; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">Poland</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Featured case study for the Conversational Art Analysis Web App project
    st.markdown("""
    <div style="background: rgba(255,255,255,0.05); border-radius: 20px; padding: 30px; border: 1px solid rgba(255,255,255,0.1); margin-top: 40px;">
        <h2 style="color: #667eea; margin-bottom: 20px; text-align: center;">Featured Project: Conversational Art Analysis Web App</h2>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 30px;">
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Client: ArtTech Startup</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Built a modern web application that allows users to upload artwork images and chat with an AI assistant for in-depth analysis. The system orchestrates multiple vision and language models (GPT-4 Vision, CLIP, OmniArt) to provide artist attribution, style/period detection, symbolism, and esoteric meaning. Integrated public art APIs for metadata enrichment and deployed the solution on Vercel with secure API key management.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Key Features:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Drag-and-drop or click-to-upload image interface (Next.js, Tailwind)</li>
                    <li>Real-time chat with AI assistant (Vercel AI chat components)</li>
                    <li>Vision model orchestration (GPT-4 Vision, CLIP/BLIP, OmniArt)</li>
                    <li>Prompt engineering for art context, allegory, and references</li>
                    <li>Metadata retrieval from WikiArt, Rijksmuseum, and public APIs</li>
                    <li>Inline and citation-based result rendering</li>
                    <li>Cloudinary/S3 image storage, secure API key management</li>
                    <li>Mobile-optimized, with copy/export and retry flows</li>
                    <li>Full documentation and developer onboarding</li>
                </ul>
            </div>
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Technical Implementation</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Developed with Next.js, Tailwind CSS, OpenAI GPT-4 Vision, Replicate API, Hugging Face, and LangChain.js for robust orchestration and analysis. Deployed on Vercel with secure API key management and cloud image storage.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Business Impact:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Enabled scalable, interactive art analysis for end users</li>
                    <li>Reduced manual research for art professionals and enthusiasts</li>
                    <li>Provided a foundation for future AI-powered art tools</li>
                </ul>
                <div style="margin-top: 20px;">
                    <span style="background: rgba(76, 175, 80, 0.2); color: #4CAF50; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; font-weight: bold;">Project Value: $2,500</span>
                    <span style="background: rgba(102, 126, 234, 0.2); color: #667eea; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">Timeline: 2 weeks</span>
                    <span style="background: rgba(255, 193, 7, 0.2); color: #FFC107; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">United States</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Featured case study for the AI-Powered Lottery Prediction Application project
    st.markdown("""
    <div style="background: rgba(255,255,255,0.05); border-radius: 20px; padding: 30px; border: 1px solid rgba(255,255,255,0.1); margin-top: 40px;">
        <h2 style="color: #667eea; margin-bottom: 20px; text-align: center;">Featured Project: AI-Powered Lottery Prediction Application</h2>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 30px;">
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Client: Private User</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Built a production-ready desktop application to automate lottery number prediction for Florida Pick 3, Pick 4, and Pick 5 games. Combined deep learning (LSTM, TFT) with advanced feature engineering and time-series analysis to deliver top-N predictions and confidence scores. The app supports daily data updates and retraining, and is fully documented for user operation.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Key Features:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Deep learning-based sequence prediction (LSTM, TFT)</li>
                    <li>Feature extraction and engineering from historical draw data</li>
                    <li>Top-N number set suggestions for each game</li>
                    <li>Confidence scoring and positional analysis</li>
                    <li>Batch data import and retraining support</li>
                    <li>Local Windows deployment with easy-to-use interface</li>
                    <li>Full documentation and remote support</li>
                </ul>
            </div>
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Technical Implementation</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Developed with Python, LSTM, TFT, and Pandas for robust sequence modeling and prediction. Automated data preprocessing and feature engineering for optimal results. Delivered as a local Windows app with full documentation and support.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Business Impact:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Reduced guesswork for lottery players</li>
                    <li>Improved prediction accuracy over random guessing and prior models</li>
                    <li>Enabled ongoing model improvement as new data is added</li>
                </ul>
                <div style="margin-top: 20px;">
                    <span style="background: rgba(76, 175, 80, 0.2); color: #4CAF50; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; font-weight: bold;">Project Value: $1,000</span>
                    <span style="background: rgba(102, 126, 234, 0.2); color: #667eea; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">Timeline: 15 days</span>
                    <span style="background: rgba(255, 193, 7, 0.2); color: #FFC107; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">United States</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Featured case study for the Automated Employee Signature Extraction project
    st.markdown("""
    <div style="background: rgba(255,255,255,0.05); border-radius: 20px; padding: 30px; border: 1px solid rgba(255,255,255,0.1); margin-top: 40px;">
        <h2 style="color: #667eea; margin-bottom: 20px; text-align: center;">Featured Project: Automated Employee Signature Extraction</h2>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 30px;">
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Client: Internal HR Automation</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Built a production-ready web application to automate the extraction of employee signatures from scanned ID cards and A4 documents. Combined a custom-trained YOLOv8 deep learning model with advanced image processing to deliver clean, transparent-background signature images, named and organized for easy HR integration.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Key Features:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Deep learning-based signature detection (YOLOv8, custom dataset)</li>
                    <li>Image preprocessing pipeline for noise reduction and background removal</li>
                    <li>Transparent PNG output, named to match source documents</li>
                    <li>Batch processing for bulk document uploads</li>
                    <li>Local Windows deployment with easy access for HR staff</li>
                    <li>Full documentation and remote support</li>
                </ul>
            </div>
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Technical Implementation</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Developed with Python, YOLOv8, OpenCV, and custom image processing for robust signature detection and extraction. Delivered as a local Windows app with full documentation and support.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Business Impact:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Eliminated manual signature cropping, saving hours of HR time</li>
                    <li>Improved accuracy and consistency of digital signature records</li>
                    <li>Scalable to new document types and formats</li>
                </ul>
                <div style="margin-top: 20px;">
                    <span style="background: rgba(76, 175, 80, 0.2); color: #4CAF50; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; font-weight: bold;">Project Value: $800</span>
                    <span style="background: rgba(102, 126, 234, 0.2); color: #667eea; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">Timeline: 5 days</span>
                    <span style="background: rgba(255, 193, 7, 0.2); color: #FFC107; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">Portugal</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Featured case study for the Lender Matchmaking AI Engine project
    st.markdown("""
    <div style="background: rgba(255,255,255,0.05); border-radius: 20px; padding: 30px; border: 1px solid rgba(255,255,255,0.1); margin-top: 40px;">
        <h2 style="color: #667eea; margin-bottom: 20px; text-align: center;">Featured Project: Lender Matchmaking AI Engine</h2>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 30px;">
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Client: Fintech Startup</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Built a production-grade AI matchmaking engine that pairs borrowers with optimal lenders based on credit profiles, application data, and historical lending trends. Collaborated with product and data teams to design, train, and deploy machine learning models for real-time recommendations.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Key Features:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Advanced recommender system for lender-borrower matching</li>
                    <li>Feature engineering from internal and external financial datasets</li>
                    <li>Model logic for lender eligibility, product fit, and borrower prioritization</li>
                    <li>Continuous model evaluation and improvement</li>
                    <li>Seamless integration with backend APIs (Dockerized for deployment)</li>
                    <li>Fully documented approach and deployment scripts</li>
                </ul>
            </div>
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Technical Implementation</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Developed with Python, scikit-learn, TensorFlow, and Pandas for robust model training and deployment. Dockerized for production and integrated with REST APIs for seamless platform integration.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Business Impact:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Increased loan approval rates and user satisfaction</li>
                    <li>Reduced manual review time for loan applications</li>
                    <li>Scalable foundation for future AI enhancements (credit scoring, fraud detection, etc.)</li>
                </ul>
                <div style="margin-top: 20px;">
                    <span style="background: rgba(76, 175, 80, 0.2); color: #4CAF50; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; font-weight: bold;">Project Value: $1,000</span>
                    <span style="background: rgba(102, 126, 234, 0.2); color: #667eea; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">Timeline: 2 weeks</span>
                    <span style="background: rgba(255, 193, 7, 0.2); color: #FFC107; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">Japan</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Featured case study for the Sports Prediction System project
    st.markdown("""
    <div style="background: rgba(255,255,255,0.05); border-radius: 20px; padding: 30px; border: 1px solid rgba(255,255,255,0.1); margin-top: 40px;">
        <h2 style="color: #667eea; margin-bottom: 20px; text-align: center;">Featured Project: Automated Sports Prediction System</h2>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 30px;">
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Client: Sports Analytics</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Built a robust Python system for a United States client to automate sports score predictions for NBA, NFL, and college games. The solution scrapes real-time stats, injuries, and expert picks, applies layered logic for predictions, and auto-updates daily. Delivered with intuitive dashboard, detailed analytics, and manual override capabilities.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Key Features:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Real-time data scraping (stats, injuries, expert picks)</li>
                    <li>Layered logic for score predictions</li>
                    <li>Daily automated updates (cron job ready)</li>
                    <li>Optional dashboard for tracking predictions</li>
                    <li>Fully documented and easy to maintain</li>
                </ul>
            </div>
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Technical Implementation</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Developed with Python, Pandas, Scikit-learn, BeautifulSoup, and API integrations for robust data processing and prediction. Automated with cron and delivered with a simple dashboard (Dash/Streamlit).
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Business Impact:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Automated daily sports predictions, saving manual effort</li>
                    <li>Improved accuracy and consistency for betting/analytics</li>
                    <li>Scalable to new sports and data sources</li>
                </ul>
                <div style="margin-top: 20px;">
                    <span style="background: rgba(76, 175, 80, 0.2); color: #4CAF50; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; font-weight: bold;">Project Value: $1,500</span>
                    <span style="background: rgba(102, 126, 234, 0.2); color: #667eea; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">Timeline: 7 days</span>
                    <span style="background: rgba(255, 193, 7, 0.2); color: #FFC107; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">United States</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Featured case study for the LLM-based AI toolkit
    st.markdown("""
    <div style="background: rgba(255,255,255,0.05); border-radius: 20px; padding: 30px; border: 1px solid rgba(255,255,255,0.1); margin-top: 40px;">
        <h2 style="color: #667eea; margin-bottom: 20px; text-align: center;">Featured Project: Portable AI Toolkit (LLM-Powered Desktop & USB Application)</h2>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 30px;">
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Client: French Entrepreneur</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Developed a unique, ready-to-sell AI toolkit for a French client, designed for students, entrepreneurs, and creators. This solution deploys a local application (and USB portable version) that brings the power of LLMs (Large Language Models) and advanced AI APIs directly to the user—no installation required for the USB version.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Key Features:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>LLM-Powered Tools: Integrated GPT-based models for reading, summarizing, writing, and Q&A, all accessible from a local menu.</li>
                    <li>Multi-API Integration: Seamless use of GPT (OpenAI), DeepL, and DALL·E for translation, text generation, and image creation.</li>
                    <li>Offline-First Design: Most features work locally; cloud APIs are used only when needed, keeping user data private and costs low.</li>
                    <li>Beautiful Local Menu: Interactive HTML/desktop menu for easy access to all tools, with a modern, user-friendly interface.</li>
                    <li>Multi-Language Support: French and English interfaces, with translation and rephrasing tools for global users.</li>
                    <li>Portable & Flexible: Delivered as both a standard desktop app and a portable .exe for USB, enabling direct use or resale.</li>
                    <li>No Installation Needed: USB version runs directly from the drive, perfect for on-the-go use or distribution.</li>
                </ul>
                <h5 style="color: #667eea; margin-bottom: 10px;">AI Modules Included:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>AI Reading & Summarization: Drag-and-drop PDFs, web pages, or text for instant summaries, revision plans, and quiz generation.</li>
                    <li>Smart Writing Assistant: Guided creation of emails, CVs, reports, articles, and more, with tone and style options.</li>
                    <li>Enhanced Note Organizer: Transforms raw notes into clear syntheses, mind maps, and prioritized checklists.</li>
                    <li>Voice Assistant: Speech-to-text, lecture summarization, and text-to-speech for accessibility and productivity.</li>
                    <li>Intelligent Translator & Rephraser: Translate, rewrite, and correct text in multiple languages and tones.</li>
                    <li>Visual Generator: DALL·E-powered image creation for creative projects.</li>
                </ul>
            </div>
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Technical Implementation</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Built with Python (Tkinter for GUI, PyInstaller for packaging), local LLM deployment (OpenAI GPT), DeepL and DALL·E APIs, HTML/JS for the menu, and SQLite for local data. USB deployment optimized for plug-and-play use.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Business Impact:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Ready-to-sell product for the client's business, enabling resale to students and professionals.</li>
                    <li>Hybrid local/cloud AI keeps costs low and privacy high.</li>
                    <li>Flexible payment and deployment (desktop and USB) for maximum client satisfaction.</li>
                </ul>
                <div style="margin-top: 20px;">
                    <span style="background: rgba(76, 175, 80, 0.2); color: #4CAF50; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; font-weight: bold;">Project Value: €700</span>
                    <span style="background: rgba(102, 126, 234, 0.2); color: #667eea; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">Timeline: 1 week</span>
                    <span style="background: rgba(255, 193, 7, 0.2); color: #FFC107; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">France</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Featured case study for the invoicing automation project
    st.markdown("""
    <div style="background: rgba(255,255,255,0.05); border-radius: 20px; padding: 30px; border: 1px solid rgba(255,255,255,0.1); margin-top: 40px;">
        <h2 style="color: #667eea; margin-bottom: 20px; text-align: center;">Featured Project: AI-Powered Invoicing Automation</h2>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 30px;">
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Client: Zinaps Fulfillment</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Developed a comprehensive automation solution for a Netherlands-based fulfillment business, 
                    eliminating manual invoicing processes and reducing processing time by 85%.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Key Achievements:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Integrated ChannelDoc WMS API for automated data extraction</li>
                    <li>Implemented AI agents using LangChain for error detection and validation</li>
                    <li>Automated Moneybird invoice generation with custom calculations</li>
                    <li>Added QLS/SendCloud shipping API integration for cost verification</li>
                    <li>Reduced manual processing time from 4 hours to 30 minutes daily</li>
                </ul>
            </div>
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Technical Implementation</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Built a robust system with error handling, data validation, and automated cost comparison 
                    to prevent financial losses in shipping operations.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Technologies Used:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Python with REST API integrations</li>
                    <li>LangChain for AI agent development</li>
                    <li>Pandas for data manipulation and calculations</li>
                    <li>Docker for containerized deployment</li>
                    <li>Automated testing and error handling</li>
                </ul>
                <div style="margin-top: 20px;">
                    <span style="background: rgba(76, 175, 80, 0.2); color: #4CAF50; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; font-weight: bold;">Project Value: $800</span>
                    <span style="background: rgba(102, 126, 234, 0.2); color: #667eea; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">Timeline: 2 weeks</span>
                    <span style="background: rgba(255, 193, 7, 0.2); color: #FFC107; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">Netherlands</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Featured case study for the FortifAI Fraud Detection System project
    st.markdown("""
    <div style="background: rgba(255,255,255,0.05); border-radius: 20px; padding: 30px; border: 1px solid rgba(255,255,255,0.1); margin-top: 40px;">
        <h2 style="color: #667eea; margin-bottom: 20px; text-align: center;">Featured Project: FortifAI Fraud Detection System</h2>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 30px;">
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Client: United States Fintech</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Developed an advanced fraud detection web application using CatBoost machine learning, real-time transaction simulation, and interactive risk analysis. Features include voice-based OTP verification via Twilio, risk factor breakdown, historical data analysis, and a modern Streamlit dashboard. Enables financial institutions to proactively detect and block high-risk transactions with explainable AI.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Key Features:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>CatBoost-powered fraud detection with explainable AI</li>
                    <li>Real-time transaction simulation and risk scoring</li>
                    <li>Voice-based OTP verification via Twilio</li>
                    <li>Risk factor breakdown and analysis</li>
                    <li>Historical data and system performance tabs</li>
                    <li>Modern Streamlit dashboard UI</li>
                </ul>
            </div>
            <div>
                <h4 style="color: #667eea; margin-bottom: 15px;">Technical Implementation</h4>
                <p style="color: #a8b2d1; line-height: 1.6; margin-bottom: 15px;">
                    Built with Python, Streamlit, CatBoost, scikit-learn, Twilio API, Pandas, Matplotlib, and Seaborn. Includes robust model loading, session state management, and interactive UI components for fraud analysis.
                </p>
                <h5 style="color: #667eea; margin-bottom: 10px;">Business Impact:</h5>
                <ul style="color: #a8b2d1; line-height: 1.8;">
                    <li>Proactive fraud detection for financial institutions</li>
                    <li>Improved security with voice-based OTP</li>
                    <li>Enhanced transparency with explainable risk factors</li>
                    <li>Scalable and user-friendly dashboard</li>
                </ul>
                <div style="margin-top: 20px;">
                    <span style="background: rgba(76, 175, 80, 0.2); color: #4CAF50; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; font-weight: bold;">Project Value: $900</span>
                    <span style="background: rgba(102, 126, 234, 0.2); color: #667eea; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">Timeline: 2 weeks</span>
                    <span style="background: rgba(255, 193, 7, 0.2); color: #FFC107; padding: 8px 15px; border-radius: 15px; font-size: 0.9rem; margin-left: 10px;">United States</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Expertise Page
elif selected == "Expertise":
    st.markdown('<h1 class="section-title">Areas of Expertise</h1>', unsafe_allow_html=True)
    
    # Expertise areas
    expertise_areas = [
        {
            "category": "Machine Learning & AI",
            "skills": ["Python", "TensorFlow", "Scikit-learn", "LangChain", "AI Agents", "NLP", "Time Series Analysis"]
        },
        {
            "category": "Trading & Financial Technology",
            "skills": ["Algorithmic Trading", "Technical Analysis", "Risk Management", "Portfolio Optimization", "Market Data APIs", "Backtesting"]
        },
        {
            "category": "Data Science & Analytics",
            "skills": ["Pandas", "NumPy", "Data Visualization", "Statistical Analysis", "Real-time Data", "Predictive Modeling"]
        },
        {
            "category": "Cloud & Infrastructure",
            "skills": ["AWS", "Docker", "PostgreSQL", "Redis", "API Development", "Deployment"]
        },
        {
            "category": "Blockchain & Cryptocurrency",
            "skills": ["Cryptocurrency APIs", "Exchange Integration", "Arbitrage", "Portfolio Tracking", "Risk Assessment"]
        },
        {
            "category": "Software Development",
            "skills": ["Python", "FastAPI", "Streamlit", "Tkinter", "PyInstaller", "REST APIs", "Git", "Testing"]
        }
    ]
    
    # Display expertise areas
    for area in expertise_areas:
        st.markdown(f"""
        <div class="expertise-item">
            <h3 style="color: #667eea; margin-bottom: 15px;">{area['category']}</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                {''.join([f'<span style="background: rgba(102, 126, 234, 0.2); color: #667eea; padding: 8px 15px; border-radius: 20px; font-size: 0.9rem;">{skill}</span>' for skill in area['skills']])}
            </div>
        </div>
        """, unsafe_allow_html=True)

# Contact Page
elif selected == "Contact":
    st.markdown('<h1 class="section-title">Get In Touch</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.05); border-radius: 20px; padding: 30px; border: 1px solid rgba(255,255,255,0.1);">
            <h3 style="color: #667eea; margin-bottom: 20px;">Contact Information</h3>
            <div style="margin-bottom: 15px;">
                <p style="color: #a8b2d1;"><strong>Email:</strong> <a href="mailto:maazjamshaid.123@gmail.com" style="color: #667eea; text-decoration: underline;">maazjamshaid.123@gmail.com</a></p>
            </div>
            <div style="margin-bottom: 15px;">
                <p style="color: #a8b2d1;"><strong>Location:</strong> Global</p>
            </div>
            <div style="margin-bottom: 25px;">
                <a href="https://wa.me/923095183754" target="_blank" style="text-decoration: none;">
                    <button style="background-color:#25D366;color:white;padding:12px 24px;border:none;border-radius:8px;font-size:1.1rem;cursor:pointer;width:100%;">
                        💬 Contact on WhatsApp
                    </button>
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.05); border-radius: 20px; padding: 30px; border: 1px solid rgba(255,255,255,0.1);">
            <h3 style="color: #667eea; margin-bottom: 20px;">Services</h3>
            <ul style="color: #a8b2d1; line-height: 2;">
                <li>Custom AI Solutions</li>
                <li>Computer Vision Applications</li>
                <li>Natural Language Processing</li>
                <li>Generative AI & Automation</li>
                <li>Predictive Analytics</li>
                <li>Trading Algorithms</li>
                <li>AI Consulting & Integration</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 40px 0; margin-top: 60px; border-top: 1px solid rgba(255,255,255,0.1);">
    <p style="color: #8892b0;">© 2024 Stellar AI. All rights reserved.</p>
    <p style="color: #667eea; font-size: 0.9rem;">Pioneering the Future of Artificial Intelligence & Machine Learning</p>
</div>
""", unsafe_allow_html=True) 