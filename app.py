import streamlit as st
import numpy as np
import pandas as pd

# Page Config
st.set_page_config(
    page_title="Ventor - Demand Forecasting AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom High-End Dark CSS (Ventor Style UI)
st.markdown("""
<style>
    /* Global Background */
    .stApp {
        background-color: #0d1117;
        color: #f0f6fc;
    }
    
    /* Hide Default Headers */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Navbar Style */
    .nav-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0px 30px 0px;
        border-bottom: 1px solid #21262d;
    }
    .brand-logo {
        font-size: 26px;
        font-weight: 800;
        color: #2f81f7;
        letter-spacing: -0.5px;
    }
    
    /* Hero Title Section */
    .hero-title {
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        margin-top: 20px;
        background: linear-gradient(90deg, #58a6ff, #bc8cff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-sub {
        font-size: 16px;
        color: #8b949e;
        text-align: center;
        margin-bottom: 40px;
    }
    
    /* Card Container */
    .glass-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.5);
        margin-bottom: 20px;
    }
    
    .card-title {
        font-size: 14px;
        color: #8b949e;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
    }
    .card-value {
        font-size: 32px;
        font-weight: 700;
        color: #ffffff;
        margin-top: 5px;
    }
    
    /* Button Styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #238636 0%, #2ea043 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #2ea043 0%, #3fb950 100%);
        box-shadow: 0 0 15px rgba(46, 160, 67, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Top Navigation Bar
st.markdown("""
<div class="nav-bar">
    <div class="brand-logo">⚡ Ventor AI</div>
    <div style="color: #8b949e; font-size: 14px;">Enterprise Demand Intelligence Platform</div>
</div>
""", unsafe_allow_html=True)

# Hero Title
st.markdown('<div class="hero-title">Inventory Management Software</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Increase your sales and keep track of every unit with our powerful AI forecasting engine.</div>', unsafe_allow_html=True)

# Main Controls Layout
col_left, col_right = st.columns([1, 1.2], gap="large")

with col_left:
    st.markdown('<div class="card-title">🎛️ Forecast Parameters</div>', unsafe_allow_html=True)
    
    discount = st.slider("Discount Percentage (%)", 0, 70, 20)
    ad_spend = st.number_input("Daily Ad Spend ($)", min_value=0, max_value=5000, value=450)
    lag_1 = st.number_input("Yesterday's Units Sold", min_value=0, max_value=1000, value=110)
    
    c1, c2 = st.columns(2)
    with c1:
        is_weekend = st.checkbox("Is Weekend?", value=False)
    with c2:
        is_holiday = st.checkbox("Is Holiday/Peak Season?", value=True)
        
    run_btn = st.button("Generate Demand Forecast 🚀")

# Prediction Calculations
base = 45 + (discount * 1.2) + (ad_spend * 0.08) + (lag_1 * 0.3)
if is_weekend: base += 25
if is_holiday: base += 50

predicted_units = int(round(base))
revenue = predicted_units * 55

with col_right:
    # Top KPI Display Cards
    st.markdown(f"""
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 20px;">
        <div class="glass-card">
            <div class="card-title">Forecasted Units</div>
            <div class="card-value">{predicted_units} <span style="font-size: 16px; color: #3fb950;">+14%</span></div>
        </div>
        <div class="glass-card">
            <div class="card-title">Projected Revenue</div>
            <div class="card-value">${revenue:,}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Live Visual Chart
    st.markdown('<div class="card-title" style="margin-bottom:10px;">📊 7-Day Demand Trend</div>', unsafe_allow_html=True)
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    trend_units = [int(predicted_units * x) for x in [0.85, 0.9, 0.95, 1.0, 1.1, 1.25 if is_weekend else 1.05, 1.3 if is_weekend else 1.0]]
    
    chart_data = pd.DataFrame({"Day": days, "Predicted Units": trend_units}).set_index("Day")
    st.area_chart(chart_data, color="#2f81f7")
