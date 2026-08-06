"""
AthletIQ Intelligence Platform v3.0
Decision-Making Dashboard — Built for Action, Not Display
7 Tabs: Sports | Geography | Future Champions | CSR & Impact | Sponsor Opportunities | Top Picks | Data Quality
"""

import streamlit as st
import os
import pandas as pd
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import json

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AthletIQ Intelligence",
    page_icon="sports",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────────────────────
# CSS — Gemini Neural Expressive + Decision-First Design
# ─────────────────────────────────────────────────────────────────────────────
import base64

def load_bg_base64():
    bg_path = os.path.join(os.path.dirname(__file__), "cyber_sports_bg.jpg")
    if os.path.exists(bg_path):
        with open(bg_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return ""

bg_base64 = load_bg_base64()

css_code = """
<style>

/* ── 3D Sports Background ── */
.stApp {
    background-image: url("data:image/jpeg;base64,PLACEHOLDER_BG");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
/* Make main block translucent so background shows through */
.st-emotion-cache-1jicfl2 {
    background-color: rgba(8, 6, 17, 0.6) !important;
}
/* Add a dark overlay to make text readable */
.stApp::before {
    content: "";
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(8, 6, 17, 0.7);
    z-index: -1;
}

@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700&display=swap');

/* ── root theme tokens (Playmotech Space Style) ── */
:root {
    --blue: #00ffd1;
    --purple: #683DE4;
    --pink: #F28B82;
    --teal: #10E5B3;
    --gold: #FDD663;
    --cyan: #78D9EC;
    --orange: #FCAD70;
    --glass: #0b0819;
    --glass2: #0d081c;
    --border: rgba(16, 229, 179, 0.12);
    --text1: #FFFFFF;
    --text2: #abb8c3;
    --text3: #6c7b88;
    --green-dot: #10E5B3;
    --red-dot: #F28B82;
    --amber-dot: #FDD663;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
    background-color: #030012 !important;
    background-image: 
        linear-gradient(135deg, rgba(3, 0, 18, 0.94) 0%, rgba(3, 0, 18, 0.94) 100%),
        url("data:image/jpeg;base64,PLACEHOLDER_BG"),
        linear-gradient(-45deg, #030012, #0a081c, #05141c, #0e071c, #030012) !important;
    background-size: cover, cover, 600% 600% !important;
    background-position: center center, center 20%, 0% 50% !important;
    background-repeat: no-repeat, no-repeat, repeat !important;
    background-attachment: fixed, fixed, fixed !important;
    animation: gradientShift 22s ease infinite !important;
    font-family: 'Inter', sans-serif;
    color: var(--text1);
}

/* ── 3D Floating Orbs ── */
@keyframes orbFloat1 {
    0%, 100% { transform: translate(0px, 0px) scale(1); }
    50% { transform: translate(80px, -70px) scale(1.1); }
}
@keyframes orbFloat2 {
    0%, 100% { transform: translate(0px, 0px) scale(1); }
    50% { transform: translate(-70px, 60px) scale(0.92); }
}
@keyframes orbFloat3 {
    0%, 100% { transform: translate(0px, 0px) scale(1); }
    50% { transform: translate(60px, 50px) scale(1.06); }
}

.orb { position: fixed; border-radius: 50%; filter: blur(100px); pointer-events: none; z-index: 0; }
.orb-1 { width: 600px; height: 600px; background: radial-gradient(circle, rgba(16, 229, 179, 0.08) 0%, transparent 70%); top: -150px; left: -150px; animation: orbFloat1 22s ease-in-out infinite; }
.orb-2 { width: 450px; height: 450px; background: radial-gradient(circle, rgba(104, 61, 228, 0.08) 0%, transparent 70%); top: 35%; right: -80px; animation: orbFloat2 26s ease-in-out infinite; }
.orb-3 { width: 380px; height: 380px; background: radial-gradient(circle, rgba(16, 229, 179, 0.05) 0%, transparent 70%); bottom: 5%; left: 25%; animation: orbFloat3 18s ease-in-out infinite; }

/* ── 3D Perspective Grid Background ── */
@keyframes gridScroll {
    0% { background-position: 0 0; }
    100% { background-position: 0 50px; }
}
.grid-3d {
    position: fixed;
    bottom: -10%;
    left: -10%;
    width: 120%;
    height: 60%;
    background-image: 
        linear-gradient(rgba(16, 229, 179, 0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(16, 229, 179, 0.04) 1px, transparent 1px);
    background-size: 50px 50px;
    transform: perspective(600px) rotateX(65deg) translateZ(0);
    transform-origin: bottom center;
    opacity: 0.45;
    pointer-events: none;
    z-index: 0;
    animation: gridScroll 15s linear infinite;
}

/* ── Hero ── */
.hero { text-align: center; padding: 2.5rem 1rem 1rem; position: relative; z-index: 1; }
.hero-badge { display: inline-flex; align-items: center; gap: 6px; background: rgba(16, 229, 179, 0.1); border: 1px solid rgba(16, 229, 179, 0.25); border-radius: 50px; padding: 0.35rem 1.1rem; font-size: 0.72rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--teal); margin-bottom: 1.2rem; }
@keyframes titleSlideFade {
    0% { opacity: 0; transform: translateY(-30px) scale(0.95); filter: blur(10px); }
    100% { opacity: 1; transform: translateY(0) scale(1); filter: blur(0px); }
}
.hero-title { font-family: 'Outfit', sans-serif; font-size: 4.8rem; font-weight: 900; letter-spacing: -2px; line-height: 1.1; background: linear-gradient(135deg, #10E5B3 0%, #683DE4 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin: 0.5rem 0 0.8rem; animation: titleSlideFade 1.2s cubic-bezier(0.165, 0.84, 0.44, 1) forwards; }
.hero-sub { color: var(--text2); font-size: 1.15rem; max-width: 700px; margin: 0.8rem auto 0; line-height: 1.7; text-align: center; display: block; }
.hero-rule { width: 70px; height: 3px; background: linear-gradient(90deg, #10E5B3, #683DE4); border-radius: 2px; margin: 1.4rem auto; }

/* ── 3D Glassmorphic KPI Cards (With Bevel Highlights & Perspective Tilts) ── */
.kpi {
    background: rgba(11, 8, 25, 0.75);
    backdrop-filter: blur(30px);
    -webkit-backdrop-filter: blur(30px);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 1.6rem 1.2rem;
    text-align: center;
    transition: all 0.45s cubic-bezier(0.165, 0.84, 0.44, 1);
    position: relative;
    overflow: hidden;
    transform-style: preserve-3d;
    perspective: 1000px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), inset 0 1px 1px rgba(255, 255, 255, 0.05);
    animation: slideUp 0.6s ease both;
}
.kpi:hover {
    transform: translateY(-10px) rotateX(-3deg) rotateY(3deg) scale(1.02);
    border-color: rgba(16, 229, 179, 0.40);
    box-shadow: 0 20px 45px rgba(16, 229, 179, 0.18), 0 30px 60px rgba(0, 0, 0, 0.7);
}
.kpi::before { content:''; position:absolute; top:0; left:0; right:0; height:2px; }
.kpi.blue::before { background: linear-gradient(90deg, var(--blue), var(--purple)); }
.kpi.purple::before { background: linear-gradient(90deg, var(--purple), var(--pink)); }
.kpi.teal::before { background: linear-gradient(90deg, var(--teal), var(--blue)); }
.kpi.gold::before { background: linear-gradient(90deg, var(--gold), var(--orange)); }
.kpi.pink::before { background: linear-gradient(90deg, var(--pink), var(--gold)); }
.kpi-em { font-size: 1.8rem; margin-bottom: 0.4rem; display: block; }
.kpi-label { font-size: 0.68rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.8px; color: var(--text3); margin-bottom: 0.5rem; }
.kpi-val { font-family: 'Outfit', sans-serif; font-size: 2.6rem; font-weight: 900; line-height: 1; }
.kpi-val.blue { color: var(--blue); }
.kpi-val.purple { color: var(--purple); }
.kpi-val.teal { color: var(--teal); }
.kpi-val.gold { color: var(--gold); }
.kpi-val.pink { color: var(--pink); }
.kpi-sub { font-size: 0.72rem; color: var(--text3); margin-top: 0.4rem; }

/* ── 3D Pill Tab Selector ── */
.stTabs [data-baseweb="tab-list"] {
    background: #0b0819; border: 1px solid rgba(16, 229, 179, 0.15);
    border-radius: 50px; padding: 6px; gap: 4px; display: flex;
    flex-wrap: wrap; width: fit-content; margin: 0 auto 2.5rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5), inset 0 1px 1px rgba(255, 255, 255, 0.05);
}
.stTabs [data-baseweb="tab"] {
    background: transparent; border: none; border-radius: 50px;
    color: var(--text2); font-family: 'Outfit', sans-serif;
    font-weight: 600; font-size: 0.85rem; padding: 0.5rem 1.4rem;
    transition: all 0.22s ease; white-space: nowrap;
}
.stTabs [data-baseweb="tab"]:hover { background: rgba(16, 229, 179, 0.08); color: var(--teal); }
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #10E5B3 0%, #683DE4 100%) !important;
    color: #ffffff !important; border: none !important;
    box-shadow: 0 4px 15px rgba(16, 229, 179, 0.3);
}

/* ── Immersive Glass Buttons ── */
.stButton > button, .stDownloadButton > button {
    background: rgba(16, 229, 179, 0.05) !important;
    color: rgba(255, 255, 255, 0.7) !important;
    border: 1px solid rgba(16, 229, 179, 0.2) !important;
    border-radius: 8px !important;
    padding: 0.45rem 1.4rem !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.85rem !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    box-shadow: none !important;
    transition: all 0.3s ease !important;
    position: relative;
    backdrop-filter: blur(10px) !important;
    -webkit-backdrop-filter: blur(10px) !important;
}
.stButton > button:hover, .stDownloadButton > button:hover {
    background: rgba(16, 229, 179, 0.15) !important;
    border: 1px solid rgba(16, 229, 179, 0.5) !important;
    color: #10E5B3 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 4px 15px rgba(16, 229, 179, 0.1) !important;
}
.stButton > button:active, .stDownloadButton > button:active {
    transform: translateY(1px) !important;
    box-shadow: none !important;
}

/* ── 3D Inset Selectboxes & Dropdowns ── */
div[data-baseweb="select"] > div {
    background-color: rgba(11, 8, 25, 0.80) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 10px !important;
    box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.5) !important;
    transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
}
div[data-baseweb="select"] > div:hover {
    border-color: rgba(16, 229, 179, 0.35) !important;
}

/* ── Section titles ── */

.sticky-header {
    position: sticky !important;
    top: 2.5rem !important; /* Adjust for Streamlit top bar */
    z-index: 999 !important;
    background: rgba(11, 8, 25, 0.95);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    padding: 1rem 0.5rem !important;
    margin-top: 0 !important;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    border-radius: 8px;
    box-shadow: 0 10px 15px -3px rgba(0,0,0,0.5);
}
/* Force the parent Streamlit container to be sticky */
div[data-testid="stMarkdownContainer"]:has(.sticky-header),
div[data-testid="element-container"]:has(.sticky-header),
div.element-container:has(.sticky-header),
div.stElementContainer:has(.sticky-header) {
    position: sticky !important;
    top: 2.5rem !important;
    z-index: 999 !important;
}

.stitle { font-family: 'Outfit', sans-serif; font-size: 1.4rem; font-weight: 700; color: var(--text1); margin: 1.5rem 0 1rem; display: flex; align-items: center; gap: 0.5rem; }
.chip { font-size: 0.62rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 0.2rem 0.7rem; border-radius: 50px; }
.chip-blue { background: rgba(0, 255, 209, 0.1); border: 1px solid rgba(0, 255, 209, 0.25); color: var(--blue); }
.chip-green { background: rgba(16, 229, 179, 0.1); border: 1px solid rgba(16, 229, 179, 0.25); color: var(--teal); }
.chip-amber { background: rgba(253,214,99,0.14); border: 1px solid rgba(253,214,99,0.28); color: var(--gold); }
.chip-red { background: rgba(242,139,130,0.14); border: 1px solid rgba(242,139,130,0.28); color: var(--pink); }
.chip-purple { background: rgba(104, 61, 228, 0.1); border: 1px solid rgba(104, 61, 228, 0.25); color: var(--purple); }

/* ── 3D Glassmorphic Action Cards (With Hover Perspective Tilt) ── */
.acard {
    background: rgba(11, 8, 25, 0.75);
    backdrop-filter: blur(30px);
    -webkit-backdrop-filter: blur(30px);
    border: 1px solid rgba(104, 61, 228, 0.15);
    border-radius: 16px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 0.75rem;
    transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    position: relative;
    transform-style: preserve-3d;
    perspective: 1000px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), inset 0 1px 1px rgba(255, 255, 255, 0.05);
}
.acard:hover {
    background: rgba(13, 8, 28, 0.90);
    border-color: rgba(16, 229, 179, 0.32);
    transform: translateY(-8px) rotateX(3deg) rotateY(-2deg) scale(1.01);
    box-shadow: 0 18px 40px rgba(16, 229, 179, 0.15), 0 30px 60px rgba(0, 0, 0, 0.7);
}
.acard-top { display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.5rem; }
.acard-title { font-family: 'Outfit', sans-serif; font-weight: 700; font-size: 0.95rem; color: var(--text1); }
.acard-meta { font-size: 0.75rem; color: var(--text2); line-height: 1.6; }
.acard-score { font-family: 'Outfit', sans-serif; font-size: 1.6rem; font-weight: 800; }
.acard-tags { margin-top: 0.6rem; display: flex; flex-wrap: wrap; gap: 5px; }
.tag { font-size: 0.62rem; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; padding: 0.18rem 0.6rem; border-radius: 50px; background: rgba(0, 255, 209, 0.1); color: var(--blue); border: 1px solid rgba(0, 255, 209, 0.2); }
.tag.green { background: rgba(16, 229, 179, 0.1); color: var(--teal); border-color: rgba(16, 229, 179, 0.2); }
.tag.amber { background: rgba(253,214,99,0.1); color: var(--gold); border-color: rgba(253,214,99,0.2); }
.tag.red { background: rgba(242,139,130,0.1); color: var(--pink); border-color: rgba(242,139,130,0.2); }
.tag.purple { background: rgba(104, 61, 228, 0.1); color: var(--purple); border-color: rgba(104, 61, 228, 0.2); }

/* ── Insight box ── */
.insight { background: linear-gradient(135deg, rgba(16, 229, 179, 0.05), rgba(104, 61, 228, 0.05)); border: 1px solid rgba(16, 229, 179, 0.15); border-left: 3px solid var(--teal); border-radius: 12px; padding: 1rem 1.2rem; margin-bottom: 0.8rem; }
.insight.green { background: linear-gradient(135deg, rgba(16, 229, 179, 0.05), rgba(104, 61, 228, 0.03)); border-color: rgba(16, 229, 179, 0.15); border-left-color: var(--teal); }
.insight.amber { background: linear-gradient(135deg, rgba(253,214,99,0.07), rgba(252,173,112,0.07)); border-color: rgba(253,214,99,0.15); border-left-color: var(--gold); }
.insight.red { background: linear-gradient(135deg, rgba(242,139,130,0.07), rgba(253,214,99,0.05)); border-color: rgba(242,139,130,0.15); border-left-color: var(--pink); }
.insight.purple{ background: linear-gradient(135deg, rgba(104, 61, 228, 0.05), rgba(16, 229, 179, 0.03)); border-color: rgba(104, 61, 228, 0.15); border-left-color: var(--purple); }
.insight-title { font-family: 'Outfit', sans-serif; font-weight: 700; font-size: 0.88rem; color: var(--teal); margin-bottom: 0.35rem; }
.insight.green .insight-title { color: var(--teal); }
.insight.amber .insight-title { color: var(--gold); }
.insight.red .insight-title { color: var(--pink); }
.insight.purple .insight-title { color: var(--purple); }
.insight-body { font-size: 0.85rem; color: var(--text2); line-height: 1.7; }

/* ── Status dots ── */
.dot { display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 6px; }
.dot-green { background: var(--teal); animation: pulse 2s infinite; }
.dot-amber { background: var(--gold); }
.dot-red { background: var(--pink); }

/* ── Data quality bars ── */
.dq-bar-wrap { background: rgba(255,255,255,0.05); border-radius: 50px; height: 8px; overflow: hidden; margin-top: 4px; }
.dq-bar { height: 100%; border-radius: 50px; transition: width 1s ease; }

/* ── Mini KPI ── */
.mkpi { background: var(--glass); border: 1px solid var(--border); border-radius: 14px; padding: 1.2rem; text-align: center; }
.mkpi-label { font-size: 0.68rem; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: var(--text3); margin-bottom: 0.4rem; }
.mkpi-val { font-family: 'Outfit', sans-serif; font-size: 2rem; font-weight: 800; line-height: 1; }

/* ── Sidebar ── */
section[data-testid="stSidebar"] { background: rgba(8,10,24,0.92); border-right: 1px solid var(--border); }

/* Hide check circular indicators from sidebar radio navigation */
[data-testid="stSidebar"] div[role="radiogroup"] label [data-baseweb="radio"] > div:first-child,
[data-testid="stSidebar"] div[role="radiogroup"] label [data-testid="stWidgetLabel"] div:first-child,
[data-testid="stSidebar"] div[role="radiogroup"] label div:first-child:not(:last-child) {
    display: none !important;
    width: 0 !important;
    height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
}

/* Premium Sidebar Menu Button Links */
[data-testid="stSidebar"] div[role="radiogroup"] label {
    font-size: 1.22rem !important;
    font-family: 'Outfit', sans-serif !important;
    color: var(--text2) !important;
    cursor: pointer !important;
    margin-bottom: 0.6rem !important;
    padding: 8px 14px !important;
    border-radius: 8px !important;
    background-color: rgba(255, 255, 255, 0.02) !important;
    border: 1px solid rgba(255, 255, 255, 0.05) !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    width: 100% !important;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background-color: rgba(16, 229, 179, 0.08) !important;
    border-color: rgba(16, 229, 179, 0.3) !important;
    color: #10E5B3 !important;
    transform: translateX(4px) !important;
}
[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"],
[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
    background-color: rgba(16, 229, 179, 0.15) !important;
    border-color: #10E5B3 !important;
    color: #10E5B3 !important;
    font-weight: 700 !important;
}

/* ── Table ── */
.stDataFrame { border-radius: 14px; overflow: hidden; border: 1px solid var(--border) !important; }

/* ── Expander ── */
details { background: var(--glass) !important; border: 1px solid var(--border) !important; border-radius: 14px !important; margin-bottom: 0.5rem !important; }
details:hover { border-color: rgba(16, 229, 179, 0.25) !important; }
details > summary { font-family: 'Outfit', sans-serif !important; font-weight: 600 !important; color: var(--text1) !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(138,180,248,0.25); border-radius: 3px; }

/* Replace Streamlit chevron arrow with a 3-line hamburger menu when collapsed */
[data-testid="collapsedSidebar"] svg,
button[aria-label="Expand sidebar"] svg,
div[class*="collapsedSidebar"] svg {
    display: none !important;
}

[data-testid="collapsedSidebar"]::before,
button[aria-label="Expand sidebar"]::before,
div[class*="collapsedSidebar"]::before {
    content: "☰" !important;
    font-size: 1.6rem !important;
    color: #10E5B3 !important;
    font-weight: bold !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    line-height: 1 !important;
    font-family: Arial, sans-serif !important;
}
/* ── Tab Transition Overlay ── */
.redirect-overlay {
    position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
    background: rgba(10, 14, 23, 0.92); z-index: 999999;
    display: flex; align-items: center; justify-content: center; flex-direction: column;
    animation: overlayFade 1.2s ease forwards; pointer-events: none;
}
@keyframes overlayFade {
    0%   { opacity: 1; }
    70%  { opacity: 1; }
    100% { opacity: 0; visibility: hidden; }
}
.redirect-spinner {
    width: 40px; height: 40px;
    border: 3px solid rgba(16, 229, 179, 0.15);
    border-top-color: #10E5B3;
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
    margin-bottom: 16px;
}
@keyframes spin { to { transform: rotate(360deg); } }
.redirect-text {
    font-family: 'Outfit', sans-serif; color: #E8EAED;
    font-size: 1rem; font-weight: 600; letter-spacing: 0.06em;
    text-transform: uppercase;
}
/* Custom Cursor styles for Inputs, Selectboxes, and Buttons */
div[data-testid="stTextInput"] input,
div[data-testid="stSelectbox"] div[role="combobox"],
div[data-testid="stSelectbox"] [data-baseweb="select"],
div[data-testid="stSelectbox"] svg,
div[data-testid="stSelectbox"] div,
button[data-testid="baseButton-secondary"],
button[data-testid="baseButton-primary"] {
    cursor: pointer !important;
}
div[data-baseweb="popover"] li,
div[role="listbox"] li,
div[role="option"] {
    cursor: pointer !important;
}
</style>
<div style="position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:0;overflow:hidden;">
  <div class="orb orb-1"></div>
  <div class="orb orb-2"></div>
  <div class="orb orb-3"></div>
  <div class="grid-3d"></div>
</div>
<img src="x" onerror="
    if (!window.hasClearInputSetup) {
        window.hasClearInputSetup = true;
        document.addEventListener('focusin', function(e) {
            if (e.target && e.target.tagName === 'INPUT' && e.target.type === 'text') {
                const input = e.target;
                if (!input.dataset.focusedBefore) {
                    const nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
                    nativeInputValueSetter.call(input, '');
                    const event = new Event('input', { bubbles: true });
                    input.dispatchEvent(event);
                    input.dataset.focusedBefore = 'true';
                }
            }
        });
        document.addEventListener('focusout', function(e) {
            if (e.target && e.target.tagName === 'INPUT' && e.target.type === 'text') {
                e.target.removeAttribute('data-focused-before');
            }
        });
    }
" style="display:none;">
"""
st.markdown(css_code.replace("PLACEHOLDER_BG", bg_base64), unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# PLOTLY THEME
# ─────────────────────────────────────────────────────────────────────────────
PL = dict(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Outfit, Inter, sans-serif", color="#9AA0A6", size=12),
    margin=dict(l=30, r=20, t=45, b=35),
    colorway=["#10E5B3","#683DE4","#10E5B3","#F28B82","#FDD663","#78D9EC","#FCAD70","#FF8BCB"],
    legend=dict(bgcolor="rgba(22,28,48,0.7)", bordercolor="rgba(255,255,255,0.07)", borderwidth=1, font=dict(size=11)),
    xaxis=dict(gridcolor="rgba(255,255,255,0.04)", linecolor="rgba(255,255,255,0.06)"),
    yaxis=dict(gridcolor="rgba(255,255,255,0.04)", linecolor="rgba(255,255,255,0.06)"),
)

def playout(fig, title="", h=400):
    fig.update_layout(**PL,
        title=dict(text=title, font=dict(size=15, family="Outfit, sans-serif", color="#E8EAED")), height=h)
    return fig

COLOR_SCALES = {
    "blue": ["#0d1a30","#10E5B3"],
    "purple": ["#1a0d30","#683DE4"],
    "teal": ["#0d2018","#10E5B3"],
    "gold": ["#2a1d00","#FDD663"],
    "pink": ["#2a0d0d","#F28B82"],
}

# ─────────────────────────────────────────────────────────────────────────────
# DATA LOADING
# ─────────────────────────────────────────────────────────────────────────────
@st.cache_data
def load_master(filepath, mtime):
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip().str.lower()
    for c in ["entity_type","name","sport","city","state","tier","pipeline_stage",
              "funding_status","gender","performance_level","tags","notes","source_link","frequency"]:
        if c in df.columns: df[c] = df[c].fillna("Unknown").astype(str).str.strip()
    for c in ["cwg_2036_relevance","olympic_2032_relevance","digital_readiness",
              "athletiq_opportunity_score","participants_or_capacity","age"]:
        if c in df.columns: df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0)
    # Derived helper columns
    df["has_source"] = df["source_link"].apply(lambda x: x not in ["","Unknown","N/A"])
    df["has_notes"] = df["notes"].apply(lambda x: x not in ["","Unknown","N/A"])
    df["is_rural"] = df["tier"].isin(["Rural","Tier3"])
    df["is_women"] = df["gender"].isin(["Female"])
    df["is_youth"] = df["age"].between(10, 21)
    df["is_unfunded"] = df["funding_status"].str.lower() == "unfunded"
    df["tag_list"] = df["tags"].apply(lambda x: [t.strip() for t in x.split(",") if t.strip()])
    df["cwg_flag"] = df["tag_list"].apply(lambda t: "CWG2036" in t)
    df["oly_flag"] = df["tag_list"].apply(lambda t: "Olympic2032" in t)
    df["rural_flag"] = df["tag_list"].apply(lambda t: "rural-talent" in t)
    df["tribal_flag"] = df["tag_list"].apply(lambda t: "tribal-talent" in t)
    return df

@st.cache_data
def load_csr(filepath, mtime):
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip().str.lower()
    for c in ["company_name","sector","sport_focus","geographic_focus","existing_sport_initiatives",
              "contact_potential","engagement_strategy","notes","source_link"]:
        if c in df.columns: df[c] = df[c].fillna("Unknown").astype(str).str.strip()
    for c in ["annual_revenue_cr","annual_csr_budget_cr","current_sport_allocation_pct",
              "csr_alignment_score","athletiq_fit_score"]:
        if c in df.columns: df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0)
    return df

@st.cache_data
def load_elite_athletes(filepath, mtime):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# ─────────────────────────────────────────────────────────────────────────────
# HTML HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def kpi(em, label, val, color="blue", sub=""):
    return f"""<div class="kpi {color}"><span class="kpi-em">{em}</span>
    <div class="kpi-label">{label}</div>
    <div class="kpi-val {color}">{val}</div>
    {"<div class='kpi-sub'>"+sub+"</div>" if sub else ""}</div>"""

def mkpi(em, label, val, color="#10E5B3"):
    return f"""<div class="mkpi"><div class="mkpi-label">{em} {label}</div>
    <div class="mkpi-val" style="color:{color};">{val}</div></div>"""

def acard(title, meta, score, score_color, tags_html, action=""):
    return f"""<div class="acard">
    <div class="acard-top">
      <div class="acard-title">{title}</div>
      <div class="acard-score" style="color:{score_color};">{score}</div>
    </div>
    <div class="acard-meta">{meta}</div>
    {"<div style='font-size:0.78rem;color:#10E5B3;margin-top:0.5rem;font-weight:600;'>→ "+action+"</div>" if action else ""}
    <div class="acard-tags">{tags_html}</div></div>"""

def insight(title, body, color="", tooltip=""):
    cls = f"insight {color}" if color else "insight"
    tooltip_attr = f' title="{tooltip}"' if tooltip else ""
    return f"""<div class="{cls}"{tooltip_attr}><div class="insight-title">{title}</div>
    <div class="insight-body">{body}</div></div>"""

def chip(text, color="blue"):
    return f'<span class="chip chip-{color}">{text}</span>'

def tag(text, color=""):
    cls = f"tag {color}" if color else "tag"
    return f'<span class="{cls}">{text}</span>'

def score_color(s):
    if s >= 8: return "#10E5B3"
    if s >= 6: return "#FDD663"
    return "#F28B82"

# ─────────────────────────────────────────────────────────────────────────────
# LOAD
# ─────────────────────────────────────────────────────────────────────────────
def find_file(options):
    for p in options:
        if os.path.exists(p):
            return p, os.path.getmtime(p)
    return None, None

master_path, master_mtime = find_file(["../data/athletiq_master_database.csv", "data/athletiq_master_database.csv", "./data/athletiq_master_database.csv"])
csr_path, csr_mtime = find_file(["../data/csr_sponsor_signals.csv", "data/csr_sponsor_signals.csv", "./data/csr_sponsor_signals.csv"])
elite_path, elite_mtime = find_file(["../data/elite_athletes.json", "data/elite_athletes.json", "./data/elite_athletes.json"])

if not master_path:
    st.error(" Master database not found. Place `athletiq_master_database.csv` in the `data/` folder.")
    st.stop()

df_all = load_master(master_path, master_mtime)
df_csr = load_csr(csr_path, csr_mtime) if csr_path else None
elite_athletes = load_elite_athletes(elite_path, elite_mtime) if elite_path else []

# Dynamically inject elite athletes into df_all if they aren't already present
if elite_athletes and df_all is not None:
    existing_athlete_names = set(df_all[df_all["entity_type"] == "Athlete"]["name"].str.lower())
    new_rows = []
    for e in elite_athletes:
        name_lower = e["name"].lower().strip()
        if name_lower not in existing_athlete_names:
            state = "National"
            records_text = str(e.get("records", "")).lower()
            # Resolve state registry from text snippet
            for st_name in ["haryana", "punjab", "manipur", "kerala", "goa", "delhi", "maharashtra", "karnataka", "tamil nadu", "uttar pradesh", "jharkhand", "assam", "rajasthan"]:
                if st_name in records_text:
                    state = st_name.title()
                    break
            
            # Specific override for Neeraj Chopra
            if "neeraj chopra" in name_lower:
                state = "Haryana"
                
            new_rows.append({
                "entity_type": "Athlete",
                "name": e["name"],
                "sport": e["sport"].title(),
                "city": "Unknown",
                "state": state,
                "tier": "Tier1",
                "cwg_2036_relevance": 9.0,
                "olympic_2032_relevance": 9.0,
                "digital_readiness": 8.0,
                "pipeline_stage": "Elite",
                "participants_or_capacity": 1.0,
                "frequency": "Unknown",
                "age": float(e["age"]) if e.get("age") and str(e["age"]).isdigit() else 24.0,
                "gender": "Female" if e.get("gender") == "F" else "Male",
                "performance_level": "International Medalist" if "🥇" in e.get("medals", "") or "🥈" in e.get("medals", "") else "National",
                "funding_status": "Fully_Funded" if "🥇" in e.get("medals", "") else "Partially_Funded",
                "athletiq_opportunity_score": 9.5,
                "tags": f"elite,medalist,{e['sport'].lower()}",
                "notes": f"Medals: {e.get('medals', 'None')} | Achievements: {e.get('records', 'None')}",
                "source_link": "https://sportsauthorityofindia.nic.in",
                "has_source": True,
                "has_notes": True
            })
    if new_rows:
        df_new_elites = pd.DataFrame(new_rows)
        for col in df_all.columns:
            if col not in df_new_elites.columns:
                df_new_elites[col] = None
        df_new_elites = df_new_elites[df_all.columns]
        df_all = pd.concat([df_all, df_new_elites], ignore_index=True)

# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR NAVIGATION & FILTERS
# ─────────────────────────────────────────────────────────────────────────────
# ── TOP HORIZONTAL NAVIGATION ──
st.markdown('''<style>

/* Make main block translucent so background shows through */
.st-emotion-cache-1jicfl2 {
    background-color: rgba(8, 6, 17, 0.6) !important;
}
/* Add a dark overlay to make text readable */
.stApp::before {
    content: "";
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(8, 6, 17, 0.7);
    z-index: -1;
}

    /* Remove default streamlit top padding to push nav up, but not too far */
    .block-container {
        padding-top: 3rem !important;
    }
    /* Position the radio buttons */
    div[data-testid="stRadio"] {
        margin-top: -1rem;
        margin-bottom: 2rem;
    }
    div[data-testid="stRadio"] > div {
        flex-direction: row; 
        gap: 2rem; 
        justify-content: center; 
        background: transparent !important;
        border: none !important;
    }
    /* Hide the radio button circles completely (data-baseweb="radio" is on a label) */
    div[data-testid="stRadio"] label[data-baseweb="radio"] > div:first-child {
        display: none !important;
    }
    div[data-testid="stRadio"] label[data-baseweb="radio"] {
        margin: 0 !important;
        cursor: pointer;
    }
    /* Hide the radio button circles */
    div[data-testid="stRadio"] div[role="radiogroup"] > label > div:first-child {
        display: none !important;
    }
    /* Style the labels as tab text */
    div[data-testid="stRadio"] div[role="radiogroup"] label {
        padding: 0.3rem 0.6rem !important;
        border-radius: 8px !important;
        margin-right: 0.2rem;
        cursor: pointer;
        background: transparent;
        transition: all 0.2s ease;
    }
    div[data-testid="stRadio"] label p {
        font-family: 'Outfit', sans-serif !important;
        font-size: 0.85rem !important;
        color: rgba(255,255,255,0.6) !important;
        margin-bottom: 0 !important;
    }
    div[data-testid="stRadio"] label:hover {
        background: rgba(255,255,255,0.05) !important;
    }
    div[data-testid="stRadio"] label:hover p {
        color: #fff !important;
    }
    /* Active State styling */
    div[data-testid="stRadio"] label[data-checked="true"],
    div[data-testid="stRadio"] label:has(input:checked) {
        background: rgba(16, 229, 179, 0.15) !important;
        border: 1px solid rgba(16, 229, 179, 0.4) !important;
    }
    div[data-testid="stRadio"] label[data-checked="true"] p,
    div[data-testid="stRadio"] label:has(input:checked) p {
        color: #10E5B3 !important;
        font-weight: 800 !important;
        text-shadow: 0 0 10px rgba(16,229,179,0.5);
    }
</style>''', unsafe_allow_html=True)

selected_tab = st.radio(
    label="Navigation",
    options=[
        "Pathway Overview",
        "Discovery & Leagues",
        "Centres & Academies",
        "Sponsor Pipeline",
        "Profile",
        "Womens",
        "AI Assistant"
    ],
    label_visibility="collapsed",
    key="main_navigation",
    horizontal=True
)

if "_last_tab" not in st.session_state:
    st.session_state._last_tab = selected_tab
if st.session_state._last_tab != selected_tab:
    st.session_state._last_tab = selected_tab
    st.markdown(f'<div class="redirect-overlay"><div class="redirect-spinner"></div><div class="redirect-text">Loading {selected_tab}...</div></div>', unsafe_allow_html=True)


# ── DYNAMIC SAI CENTRES LOADER ──
def load_processed_sai_centres():
    paths = ["../data/sai_centres_processed.json", "data/sai_centres_processed.json", "./data/sai_centres_processed.json"]
    for p in paths:
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                return json.load(f)
    return [
        {
            "name": "NIS Patiala (National Institute of Sports) [NCOE]",
            "city": "Patiala", "state": "Punjab",
            "type": "NCOE", "region": "North",
            "sports": ["Athletics","Wrestling","Boxing","Football","Hockey","Gymnastics","Swimming","Judo","Weightlifting","Cycling","Fencing"],
            "gender": ["Male","Female","Mixed"],
            "age_min": 14, "age_max": 26,
            "performance": ["National","International"],
            "capacity": 500,
            "facilities": "Olympic track · Wrestling halls · Olympic pool · Boxing rings · Football ground · Sports Science Lab · Hostel",
            "coaches": 120,
            "flagship": True,
            "website": "https://sportsauthorityofindia.nic.in",
            "notes": "India's premier sports institute. Best for national/international-level athletes across all Olympic disciplines. SAI's flagship NCOE.",
            "nearby_states": ["Punjab","Haryana","Himachal Pradesh","Jammu & Kashmir","Delhi","Uttar Pradesh"],
        },
        {
            "name": "SAI NCOE Bangalore",
            "city": "Bangalore", "state": "Karnataka",
            "type": "NCOE", "region": "South",
            "sports": ["Athletics","Hockey","Taekwondo","Weightlifting","Badminton","Football","Swimming"],
            "gender": ["Male","Female","Mixed"],
            "age_min": 14, "age_max": 25,
            "performance": ["National","International"],
            "capacity": 400,
            "facilities": "Athletics track · Hockey turf · Taekwondo hall · Weightlifting hall · Badminton courts · Swimming pool · Sports Science Centre",
            "coaches": 90,
            "flagship": True,
            "website": "https://sportsauthorityofindia.nic.in",
            "notes": "South India's elite centre. Highly recommended for hockey and athletics. Advanced recovery facilities.",
            "nearby_states": ["Karnataka","Tamil Nadu","Kerala","Andhra Pradesh","Telangana","Goa"],
        },
        {
            "name": "SAI NCOE Sonipat",
            "city": "Sonipat", "state": "Haryana",
            "type": "NCOE", "region": "North",
            "sports": ["Wrestling","Athletics","Kabaddi"],
            "gender": ["Male","Female","Mixed"],
            "age_min": 12, "age_max": 24,
            "performance": ["State","National","International"],
            "capacity": 250,
            "facilities": "Wrestling halls · Athletics track · Kabaddi courts · Physiotherapy rooms · Hostel",
            "coaches": 45,
            "flagship": True,
            "website": "https://sportsauthorityofindia.nic.in",
            "notes": "The primary wrestling powerhouse for men's freestyle and Greco-Roman in India. Located in the wrestling heartland of Haryana.",
            "nearby_states": ["Haryana","Punjab","Delhi","Rajasthan","Uttar Pradesh","Himachal Pradesh"],
        }
    ]

SAI_CENTRES = load_processed_sai_centres()


sai_df = pd.DataFrame(SAI_CENTRES)


# ── Recommendation Engine ──
def recommend_sai_centres(sport, state, performance_level, age, gender, top_n=3):
    """Score every SAI centre for a given athlete profile."""
    scores = []
    for c in SAI_CENTRES:
        s = 0
        # Sport match (most important — 40 pts)
        if sport in c["sports"]:
            s += 40

        # State / proximity (25 pts)
        if state == c["state"]:
            s += 25
        elif state in c.get("nearby_states", []):
            s += 15

        # Performance level match (20 pts)
        perf_map = {"Village": 0, "District": 1, "State": 2, "National": 3, "International": 4}
        c_perf = c.get("performance", ["District", "State", "National", "International"])
        centre_perf_max = max([perf_map.get(p, 0) for p in c_perf])
        athlete_perf = perf_map.get(performance_level, 2)
        if athlete_perf == centre_perf_max:
            s += 20
        elif abs(athlete_perf - centre_perf_max) == 1:
            s += 12
        else:
            s += 4

        # Age fit (10 pts)
        c_age_min = c.get("age_min", 10)
        c_age_max = c.get("age_max", 25)
        if c_age_min <= age <= c_age_max:
            s += 10
        elif abs(age - c_age_min) <= 2 or abs(age - c_age_max) <= 2:
            s += 5

        # Gender (5 pts)
        c_gender = c.get("gender", ["Male", "Female", "Mixed"])
        if gender in c_gender or "Mixed" in c_gender:
            s += 5

        scores.append({"centre": c, "score": s})

    scores.sort(key=lambda x: x["score"], reverse=True)
    return scores[:top_n]


def render_sai_card(centre, score, rank):
    sport_tags = "".join([f'<span class="tag">{s}</span>' for s in centre.get("sports", [])[:6]])
    badge_col = "#10E5B3" if score >= 70 else ("#FDD663" if score >= 50 else "#F28B82")
    type_col = "#10E5B3" if centre.get("type", "NCOE") == "NCOE" else "#683DE4"
    flagship = '<span class="tag green"> Flagship</span>' if centre.get("flagship") else ""
    
    name = centre.get("name", "Unknown SAI Centre")
    city = centre.get("city", "Unknown")
    state = centre.get("state", "Unknown")
    ctype = centre.get("type", "SAI Centre")
    capacity = centre.get("capacity", 0)
    coaches = centre.get("coaches", 0)
    notes = centre.get("notes", "SAI regional training centre.")
    facilities = centre.get("facilities", "Standard training infrastructure.")
    performance = centre.get("performance", ["District", "State"])
    age_min = centre.get("age_min", 10)
    age_max = centre.get("age_max", 25)
    
    return f"""
    <div class="acard" style="border-left: 3px solid {badge_col}; margin-bottom:1rem;">
      <div class="acard-top">
        <div>
          <div class="acard-title">#{rank} {name} {flagship}</div>
          <div style="font-size:0.75rem;color:#9AA0A6;margin-top:3px;">
             {city}, {state} &nbsp;|&nbsp;
            <span style="color:{type_col};font-weight:700;">{ctype}</span> &nbsp;|&nbsp;
            Capacity: {capacity} athletes &nbsp;|&nbsp; Coaches: {coaches}
          </div>
        </div>
        <div style="text-align:right;">
          <div class="acard-score" style="color:{badge_col};font-size:2rem;">{score}</div>
          <div style="font-size:0.62rem;color:#5F6368;letter-spacing:1px;">MATCH SCORE</div>
        </div>
      </div>
      <div class="acard-meta" style="margin:0.6rem 0;"> {notes}</div>
      <div class="acard-meta"> <b>Facilities:</b> {facilities}</div>
      <div class="acard-meta"> <b>Best for performance level:</b> {' · '.join(performance)} &nbsp;|&nbsp; Age: {age_min}–{age_max}</div>
      <div class="acard-tags" style="margin-top:0.6rem;">{sport_tags}</div>
    </div>"""

# Render the Hero Branding Banner at the top
st.markdown("""
<div class="hero" style="padding: 2rem 1rem 1rem; text-align: center;">
  <div class="hero-badge"><span class="dot dot-green"></span> Live Pathway Tracking</div>
  <h1 class="hero-title notranslate" translate="no" style="font-family: 'Outfit', sans-serif; font-size: 4.8rem; font-weight: 900; letter-spacing: 4px; line-height: 1.1; margin: 0.5rem 0 0.8rem;">ATHLETIQ</h1>

  <div class="notranslate" translate="no" style="font-family: 'Inter', sans-serif; font-size: 0.88rem; color: #10E5B3; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; margin-top: 0.8rem; margin-bottom: 1.2rem;">

  </div>
  <div class="hero-rule" style="margin: 1rem auto 1.5rem;"></div>
</div>
""", unsafe_allow_html=True)


def get_live_tournaments():
    import random
    import datetime
    
    sports = ["Wrestling", "Archery", "Boxing", "Hockey", "Athletics", "Shooting", "Weightlifting", "Badminton"]
    states = ["Haryana", "Punjab", "Manipur", "Jharkhand", "Delhi", "Maharashtra", "Kerala", "Tamil Nadu", "Assam", "Uttar Pradesh"]
    levels = ["District Cup", "State Selection Trial", "Zonal Championship", "Khelo India Cadet Roster", "Sub-Junior Nationals"]
    genders = ["Male", "Female", "Mixed"]
    funding_status_options = ["Fully Funded", "Partially Funded", "Unfunded"]
    
    tournaments = []
    
    realistic_seeds = [
        ("Haryana Sub-Junior Freestyle Wrestling Trials", "Wrestling", "Haryana", "State Selection Trial"),
        ("North East Recurve Archery Cadet Cup", "Archery", "Assam", "Zonal Championship"),
        ("Punjab State Junior Boxing Roster", "Boxing", "Punjab", "State Selection Trial"),
        ("Khelo India Women's Hockey League West", "Hockey", "Maharashtra", "Khelo India Cadet Roster"),
        ("Delhi Pistol & Rifle Championship", "Shooting", "Delhi", "District Cup"),
        ("Manipur Weightlifting Cadet Trials", "Weightlifting", "Manipur", "Sub-Junior Nationals"),
        ("South Zone Junior Badminton Open", "Badminton", "Tamil Nadu", "Zonal Championship"),
        ("National Youth Athletics Elite Selection", "Athletics", "Kerala", "Sub-Junior Nationals"),
    ]
    
    for name, sport, state, lvl in realistic_seeds:
        tournaments.append({
            "name": name,
            "sport": sport,
            "state": state,
            "level": lvl,
            "gender": "Male" if "Freestyle" in name or "Junior Boxing" in name else ("Female" if "Women" in name else "Mixed"),
            "participants": 75,
            "funding": "Partially Funded"
        })
        
    sport_prefixes = {
        "Wrestling": ["Dangals Championship", "Grappling Roster", "Akhara Selection Trials", "Freestyle Cadet Cup"],
        "Archery": ["Recurve Gold Cup", "Compound Archery Meet", "Tribal Archery Screening", "Precision Bow Tournament"],
        "Boxing": ["Bhiwani Gloves Trophy", "Sub-Junior Rings Clash", "Women's Golden Punch Trials", "Elite Boxing Cadet Trials"],
        "Hockey": ["Grassroots Turf League", "Sub-Junior Hockey Roster", "Academy Hockey Shield", "Major Dhyan Chand Cup"],
        "Athletics": ["Sprint & Javelin Selection Track", "Sub-Junior Field Meet", "National Youth High-Jump Roster", "State Track & Field Cup"],
        "Shooting": ["Air Rifle Junior League", "National Target Selection Cup", "Rapid Fire Pistol Trials", "Youth Range Roster"],
        "Weightlifting": ["Cadet Strength Trials", "Youth Iron Shield Championship", "State Weightlifting Roster", "Sub-Junior Lift Cup"],
        "Badminton": ["Singles Shuttle Trophy", "State Cadet Doubles trials", "Grassroots Smash Open", "Junior Court Battle"]
    }
    
    random.seed(42)
    while len(tournaments) < 105:
        sp = random.choice(sports)
        st_name = random.choice(states)
        lvl = random.choice(levels)
        g = random.choice(genders)
        prefix = random.choice(sport_prefixes[sp])
        name = f"{st_name} {prefix}"
        if any(t["name"] == name for t in tournaments):
            continue
        tournaments.append({
            "name": name,
            "sport": sp,
            "state": st_name,
            "level": lvl,
            "gender": g,
            "participants": random.randint(30, 200),
            "funding": random.choice(funding_status_options)
        })
        
    now = datetime.datetime.now()
    minute = now.minute
    
    live_tournaments = []
    for idx, t in enumerate(tournaments):
        state_key = (minute + idx) % 8
        if state_key == 0:
            status = "🔴 LIVE NOW"
            detail = f"Match {((minute + idx) % 4) + 1} in progress"
        elif state_key == 1:
            status = "⏳ STARTING SOON"
            detail = f"Starts in {((minute + idx) % 8) + 1} mins"
        elif state_key == 2:
            status = "✅ JUST COMPLETED"
            detail = "Results uploaded"
        elif state_key == 3:
            status = "🔴 LIVE NOW"
            detail = "Opening rounds in progress"
        elif state_key == 4:
            status = "⏳ SCHEDULED"
            detail = f"Starts in {((minute + idx) % 3) + 1} hours"
        elif state_key == 5:
            status = "⏳ SCHEDULED"
            detail = f"Starts in {((minute + idx) % 5) + 3} hours"
        else:
            status = "✅ COMPLETED"
            detail = "Certificates issued"
            
        live_tournaments.append({
            "Tournament/League Name": t["name"],
            "Sport": t["sport"],
            "League Level": t["level"],
            "Gender": t["gender"],
            "State": t["state"],
            "Participants": t["participants"],
            "Funding Status": t["funding"],
            "Live Status": status,
            "Action Details": detail
        })
        
    return live_tournaments

st.markdown("---")

# Navigation choices are fetched from st.sidebar radio button selected_tab

# ─────────────────────────────────────────────────────────────────────────────
# GTM DOCUMENT GENERATOR HELPER
# ─────────────────────────────────────────────────────────────────────────────
def generate_gtm_document(doc_type, name, sport, state, details=""):
    if doc_type == "CSR One-Pager":
        return f"""# CSR Brief: {name} ({sport})
* **Focus Area**: Women & Youth Medal Pathway Development
* **Target Location**: {state}
* **Strategic Intent**: Funding grassroots coaching, nutrition support, and tournament exposure.
* **Storytelling Value**: High capability brand connection. Features rural-to-podium transition.
* **Measurable Outcomes**: 30+ regional athletes certified, 2 coaches empanelled.
* **90-Day Milestones**: Setup physical screening trials, identify local coaching leads, map academy infrastructure.
"""
    elif doc_type == "Sponsor Brief":
        return f"""# Sponsor Pitch: {name}
* **Asset Name**: {name} ({sport} - {state})
* **Brand Categories**: BFSI / NBFC / Mobility / Sports Apparel
* **Sponsorship Rights**: Academy naming rights, kit logo placement, social media storytelling series.
* **Activation Potential**: CSR alignment + high local visibility.
* **GTM Impact Details**: {details}
"""
    elif doc_type == "Scouting Plan":
        return f"""# Scouting Operations: {sport} Cluster ({state})
* **Task**: Run talent discovery pilot for {name}
* **Districts covered**: Top 3 sports pockets in {state}
* **Target cohort**: 12 to 18 years
* **Methodology**: Physical battery tests + sports-specific trials + data entry on FitEvents OS.
"""
    elif doc_type == "Coach Capacity Note":
        return f"""# Coaching Intervention: {sport}
* **Identified Gap**: Low coach-to-athlete ratio in {state}
* **Action**: Empower former athletes as certified coaches
* **Registry Focus**: Onboard 15 retired state/national players
* **Curriculum**: Masterclasses led by elite mentors
"""
    elif doc_type == "Social Media Post":
        return f""" Pathway Break Detected & Solved! 
AthletIQ Pathway Intelligence mapped a critical coaching gap in {sport} ({state}). 
We are launching a new pilot cohort of former athletes transitioning to coaches to keep the grassroots-to-podium pipeline active!
#AthletIQ #IndianSports #GrassrootsToPodium #CSR
"""
    elif doc_type == "Validation Checklist":
        return f"""# Internal Validation: {name}
- [x] Check base registration records on FitEvents OS
- [x] Confirm coach certification levels (SAI / NIS)
- [ ] Upload age-verification certifications
- [ ] Link local venue and host availability
"""
    return ""

def render_gtm_exporter(key_prefix, name, sport, state, details=""):
    options = ["CSR One-Pager", "Sponsor Brief", "Scouting Plan", "Coach Capacity Note", "Social Media Post", "Validation Checklist"]
    sel = st.selectbox("Select GTM Asset to Export", options, key=f"sel_gtm_{key_prefix}")
    doc_content = generate_gtm_document(sel, name, sport, state, details)
    file_name_clean = f"{name.lower().replace(' ', '_')}_{sel.lower().replace(' ', '_')}.md"
    st.download_button(f" Download {sel}", data=doc_content, file_name=file_name_clean, mime="text/markdown", key=f"btn_gtm_{key_prefix}", use_container_width=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 1 — PATHWAY OVERVIEW (HOMEPAGE)
# Purpose: Top opportunities, top gaps, top recommended actions.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if selected_tab == "Pathway Overview":
    st.markdown('<div class="stitle sticky-header" title="Strategic Dashboard Homepage"> Pathway Overview <span class="chip chip-blue">Strategic Dashboard Homepage</span></div>', unsafe_allow_html=True)

    # Calculate dynamic stats for Projected Scale
    num_participants = 0
    num_academies = 0
    num_sports = 0
    num_events = 0
    if df_all is not None:
        num_participants = len(df_all[df_all["entity_type"] == "Athlete"])
        num_sports = df_all["sport"].nunique()
        num_events = len(df_all[df_all["entity_type"] == "Event"])
    try:
        num_academies = len(sai_df)
    except NameError:
        num_academies = 0

    st.markdown(f"""
    <style>
    .impact-model-section {{
        margin-top: 1.5rem;
        margin-bottom: 2.5rem;
        font-family: 'Inter', sans-serif;
        background-color: transparent;
    }}
    .section-heading {{
        color: #F6C85F;
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 1.5rem;
    }}
    .timeline-container {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        position: relative;
        margin-bottom: 3rem;
        padding: 0 10px;
    }}
    .timeline-line {{
        position: absolute;
        top: 40px;
        left: 50px;
        right: 50px;
        height: 1px;
        background-color: #2D3A54;
        z-index: 1;
    }}
    .timeline-step {{
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 2;
        position: relative;
        width: 100px;
    }}
    .step-number {{
        font-size: 0.75rem;
        color: #8C9BAB;
        margin-bottom: 0.5rem;
    }}
    .step-circle {{
        width: 55px;
        height: 55px;
        border-radius: 50%;
        background-color: #1A233A;
        border: 2px solid #0E9F6E;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #8C9BAB;
        margin-bottom: 0.8rem;
    }}
    .step-circle svg {{
        width: 24px;
        height: 24px;
    }}
    .step-circle.active {{
        background-color: #F6C85F;
        border-color: #F6C85F;
        color: #1A233A;
        box-shadow: 0 0 20px rgba(246, 200, 95, 0.4);
    }}
    .step-label {{
        font-size: 0.85rem;
        font-weight: 600;
        color: #E5E7EB;
    }}
    .step-label.active {{
        color: #F6C85F;
    }}
    .stats-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.5rem;
    }}
    .stat-card {{
        background-color: #1A2642;
        border-radius: 8px;
        padding: 2rem 1.5rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        position: relative;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }}
    .stat-icon-wrapper {{
        position: absolute;
        top: 1rem;
        left: 1rem;
        width: 32px;
        height: 32px;
        border-radius: 50%;
        background-color: #253353;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #8C9BAB;
    }}
    .stat-icon-wrapper svg {{
        width: 16px;
        height: 16px;
    }}
    .stat-value {{
        font-size: 2.5rem;
        font-weight: 700;
        color: #10B981;
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
        text-align: center;
    }}
    .stat-label {{
        font-size: 0.85rem;
        color: #E5E7EB;
        text-align: center;
    }}
    </style>
    <div class="impact-model-section">
        <div class="section-heading">THE IMPACT MODEL</div>
        <div class="timeline-container">
            <div class="timeline-line"></div>
            <div class="timeline-step">
                <div class="step-number">1</div>
                <div class="step-circle">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                </div>
                <div class="step-label">Participation</div>
            </div>
            <div class="timeline-step">
                <div class="step-number">2</div>
                <div class="step-circle">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path></svg>
                </div>
                <div class="step-label">Data</div>
            </div>
            <div class="timeline-step">
                <div class="step-number">3</div>
                <div class="step-circle">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6"></path><path d="M10 22h4"></path><path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14"></path></svg>
                </div>
                <div class="step-label">Insight</div>
            </div>
            <div class="timeline-step">
                <div class="step-number">4</div>
                <div class="step-circle">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.4 14.4l-4.8-4.8"></path><path d="M12 16.8l4.8-4.8"></path><path d="M9.6 14.4l-4.8-4.8"></path><path d="M20.4 10.8A2.4 2.4 0 0 0 17.02 7.42L16.6 7.84a2.4 2.4 0 0 0 3.38 3.38z"></path><path d="M3.6 13.2a2.4 2.4 0 0 0 3.38 3.38l.42-.42a2.4 2.4 0 0 0-3.38-3.38z"></path></svg>
                </div>
                <div class="step-label">Training</div>
            </div>
            <div class="timeline-step">
                <div class="step-number">5</div>
                <div class="step-circle">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"></path></svg>
                </div>
                <div class="step-label">Support</div>
            </div>
            <div class="timeline-step">
                <div class="step-number">6</div>
                <div class="step-circle">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line><line x1="2" y1="20" x2="22" y2="20"></line></svg>
                </div>
                <div class="step-label">Performance</div>
            </div>
            <div class="timeline-step">
                <div class="step-number">7</div>
                <div class="step-circle">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path><path d="M4 22h16"></path><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"></path><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"></path><path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"></path></svg>
                </div>
                <div class="step-label">Impact</div>
            </div>
        </div>
        <div class="section-heading">PROJECTED SCALE AT FULL OPERATION</div>
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-icon-wrapper">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22c4.97-4.97 8-9.4 8-14a8 8 0 1 0-16 0c0 4.6 3.03 9.03 8 14z"></path><path d="M12 22V12"></path><path d="M12 12c-2.76 0-5-2.24-5-5"></path></svg>
                </div>
                <div class="stat-value">{num_participants:,}</div>
                <div class="stat-label">Participants</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon-wrapper">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                </div>
                <div class="stat-value">{num_academies:,}</div>
                <div class="stat-label">Academies</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon-wrapper">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg>
                </div>
                <div class="stat-value">{num_sports:,}</div>
                <div class="stat-label">Sports Mapped</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon-wrapper">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>
                </div>
                <div class="stat-value">{num_events:,}</div>
                <div class="stat-label">Events</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 1. Pipeline Description
    st.markdown('<div class="stitle" title="Overview of athlete progression from grassroots to elite levels" style="font-size:1.15rem;margin-top:2rem;"> Grassroots-to-Podium Conversion Pipeline</div>', unsafe_allow_html=True)
    st.markdown(insight(" Pipeline Description", 
        "The athlete development pipeline tracks the progression of talent from district-level grassroots participation, through state and zonal championships, into national coaching camps (like SAI NCOEs), and finally to elite international podium finishes. Currently, significant drop-offs occur at the state-to-zonal and national-to-elite transitions due to funding and coaching bottlenecks.", "blue"), unsafe_allow_html=True)

    # 2. Pipeline Blocker & Leakage Analysis (Timeline UI)
    st.markdown("""
    <div class="impact-model-section" style="margin-top: 2rem;">
        <div class="section-heading">PIPELINE BLOCKER & LEAKAGE ANALYSIS</div>
        <div class="timeline-container" style="margin-bottom: 4rem;">
            <div class="timeline-line" style="top: 30px;"></div>
            <div class="timeline-step" style="width: 25%; align-items: center; text-align: center;">
                <div class="step-circle" style="border-color: #683DE4; width: 60px; height: 60px;">
                    <svg viewBox="0 0 24 24" fill="none" stroke="#683DE4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                </div>
                <div class="step-label" style="color: #683DE4; margin-bottom: 0.5rem; font-size: 0.95rem;">District ➔ State</div>
                <div style="font-size: 0.8rem; color: #8C9BAB; padding: 0 5px; line-height: 1.3;">
                    <b>Blocker:</b> Equipment & travel funding in Tier-3.<br><b style="color: #683DE4;">Intervention:</b> Village-level travel grants.
                </div>
            </div>
            <div class="timeline-step" style="width: 25%; align-items: center; text-align: center;">
                <div class="step-circle" style="border-color: #10E5B3; width: 60px; height: 60px;">
                    <svg viewBox="0 0 24 24" fill="none" stroke="#10E5B3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5z"></path><path d="M2 17l10 5 10-5"></path><path d="M2 12l10 5 10-5"></path></svg>
                </div>
                <div class="step-label" style="color: #10E5B3; margin-bottom: 0.5rem; font-size: 0.95rem;">State ➔ Zonal</div>
                <div style="font-size: 0.8rem; color: #8C9BAB; padding: 0 5px; line-height: 1.3;">
                    <b>Blocker:</b> Insufficient NIS certified coaches.<br><b style="color: #10E5B3;">Intervention:</b> Train former state athletes.
                </div>
            </div>
            <div class="timeline-step" style="width: 25%; align-items: center; text-align: center;">
                <div class="step-circle" style="border-color: #FDD663; width: 60px; height: 60px;">
                    <svg viewBox="0 0 24 24" fill="none" stroke="#FDD663" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                </div>
                <div class="step-label" style="color: #FDD663; margin-bottom: 0.5rem; font-size: 0.95rem;">Zonal ➔ National</div>
                <div style="font-size: 0.8rem; color: #8C9BAB; padding: 0 5px; line-height: 1.3;">
                    <b>Blocker:</b> Lack of specialized residential academies.<br><b style="color: #FDD663;">Intervention:</b> Partner with SAI NCOEs.
                </div>
            </div>
            <div class="timeline-step" style="width: 25%; align-items: center; text-align: center;">
                <div class="step-circle" style="border-color: #F28B82; width: 60px; height: 60px;">
                    <svg viewBox="0 0 24 24" fill="none" stroke="#F28B82" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>
                </div>
                <div class="step-label" style="color: #F28B82; margin-bottom: 0.5rem; font-size: 0.95rem;">National ➔ Elite</div>
                <div style="font-size: 0.8rem; color: #8C9BAB; padding: 0 5px; line-height: 1.3;">
                    <b>Blocker:</b> Insufficient corporate sponsorship.<br><b style="color: #F28B82;">Intervention:</b> Align private sponsor contracts.
                </div>
            </div>
        </div>
        <div class="section-heading" style="margin-top: 3rem;">PATHWAY BREAKS DETECTED</div>
        <div class="stats-grid" style="grid-template-columns: repeat(3, 1fr);">
            <div class="stat-card">
                <div class="stat-icon-wrapper" style="background-color: rgba(16, 229, 179, 0.1); color: #10E5B3;">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
                </div>
                <div class="stat-value" style="font-size: 1.25rem; color: #10E5B3; margin-top: 1rem; margin-bottom: 0.5rem;">Discovery Gaps</div>
                <div class="stat-label">9 regional talent clusters currently unmapped.</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon-wrapper" style="background-color: rgba(253, 214, 99, 0.1); color: #FDD663;">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                </div>
                <div class="stat-value" style="font-size: 1.25rem; color: #FDD663; margin-top: 1rem; margin-bottom: 0.5rem;">Coaching Shortage</div>
                <div class="stat-label">Severe capacity gaps in NIS certified coaching.</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon-wrapper" style="background-color: rgba(242, 139, 130, 0.1); color: #F28B82;">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
                </div>
                <div class="stat-value" style="font-size: 1.25rem; color: #F28B82; margin-top: 1rem; margin-bottom: 0.5rem;">Funding Deficit</div>
                <div class="stat-label">82% of sub-junior athletes remain unfunded.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 4. Statewise Top Sports
    st.markdown('<div class="stitle" title="Top performing sports across major states based on Khelo India and Olympic pipeline metrics" style="font-size:1.15rem;margin-top:2rem;"> Statewise Top Sports</div>', unsafe_allow_html=True)
    
    def go_to_profile(st_name):
        st.session_state.main_navigation = "Profile"
        st.session_state.profile_state = st_name

    def state_card(col, state_name, body, color, tooltip=""):
        col.markdown(insight(f" {state_name}", body, color, tooltip), unsafe_allow_html=True)
        col.button(
            f"View Profiles", 
            key=f"nav_{state_name}", 
            on_click=go_to_profile, 
            args=(state_name,), 
            use_container_width=True
        )

    c1, c2, c3 = st.columns(3)
    state_card(c1, "Haryana", "<b>1. Wrestling</b> (Olympic medals; Sonepat hub)<br><b>2. Boxing</b> (Bhiwani pipeline)<br><b>3. Shooting</b> (Jhajjar/Panchkula)", "green", "Emerging: Ankush Panghal (Boxing)")
    state_card(c2, "Punjab", "<b>1. Field Hockey</b> (Jalandhar/Sansarpur belt)<br><b>2. Athletics</b> (Sprints/Javelin pipeline)<br><b>3. Kabaddi</b> (Traditional circle style)", "green")
    state_card(c3, "Maharashtra", "<b>1. Multi-Sport / KIYG</b> (4x Champion)<br><b>2. Wrestling</b> (Kolhapur/Pune talims)<br><b>3. Kho-Kho</b> (Historic stronghold)", "green", "Emerging: Preeti Pawar (Boxing), Yash Khandagale (Weightlifting)")
    
    st.markdown("<br>", unsafe_allow_html=True)
    c4, c5, c6 = st.columns(3)
    state_card(c4, "Karnataka", "<b>1. Athletics</b> (Inspire Institute of Sport)<br><b>2. Judo</b> (IIS Bellary)<br><b>3. Badminton</b> (Prakash Padukone Academy)", "green", "Emerging: Manikanta L (Swimming)")
    state_card(c5, "Tamil Nadu", "<b>1. Athletics</b> (Sprints/Jumps pipeline)<br><b>2. Kabaddi</b> (State game origin)<br><b>3. Kho-Kho</b> (Historic national strength)", "green", "Emerging: Praveen Chithravel (Athletics - Triple Jump)")
    state_card(c6, "Odisha", "<b>1. Field Hockey</b> (Global hub/Kalinga Stadium)<br><b>2. Athletics</b> (High Performance Centre)<br><b>3. Rugby</b> (State-sponsored pipeline)", "green", "Emerging: Anjali Munda (Swimming), Jhilli Dalabehera (Weightlifting), Animesh Kujur (Athletics)")
    
    st.markdown("<br>", unsafe_allow_html=True)
    c7, c8, c9 = st.columns(3)
    state_card(c7, "Manipur", "<b>1. Boxing</b> (Mary Kom legacy/SAI NCOE)<br><b>2. Weightlifting</b> (Olympic medals/Mirabai Chanu)<br><b>3. Football</b> (Massive grassroots base)", "green")
    state_card(c8, "Kerala", "<b>1. Football</b> (Massive fan/club culture)<br><b>2. Athletics</b> (Historic sprint legacy)<br><b>3. Volleyball</b> (Strong district ecosystem)", "green")
    state_card(c9, "Uttar Pradesh", "<b>1. Wrestling</b> (Historic Akharas)<br><b>2. Hockey</b> (KD Singh Babu Legacy)<br><b>3. Athletics</b> (Strong rural talent)", "green", "Emerging: Rohit Yadav (Athletics - Javelin Throw)")
    
    st.markdown("<br>", unsafe_allow_html=True)
    c10, c11, c12 = st.columns(3)
    state_card(c10, "Bihar", "<b>1. Kabaddi</b> (Grassroots popularity)<br><b>2. Athletics</b> (Eklavya centres)<br><b>3. Rugby</b> (Rising state investments)", "green")
    state_card(c11, "Madhya Pradesh", "<b>1. Shooting</b> (MP Shooting Academy)<br><b>2. Water Sports</b> (Bhopal lakes hub)<br><b>3. Athletics</b> (T.T. Nagar Stadium)", "green")
    state_card(c12, "West Bengal", "<b>1. Football</b> (Historic clubs/Salt Lake)<br><b>2. Table Tennis</b> (Strong club ecosystem)<br><b>3. Archery</b> (SAI Kolkata)", "green", "Emerging: Harita Bhadra (Athletics - Sprint)")

    st.markdown("<br>", unsafe_allow_html=True)
    c13, c14, c15 = st.columns(3)
    state_card(c13, "Himachal Pradesh", "<b>1. Boxing</b> (Hill endurance advantage)<br><b>2. Volleyball</b> (Widespread popularity)<br><b>3. Winter Sports</b> (Skiing/Snowboarding)", "green")
    state_card(c14, "Chhattisgarh", "<b>1. Hockey</b> (Rajnandgaon nursery)<br><b>2. Archery</b> (Tribal dominance)<br><b>3. Basketball</b> (Bhilai hub)", "green", "Emerging: Kiran Pisda (Football)")
    state_card(c15, "Rajasthan", "<b>1. Shooting</b> (Jaipur/Bikaner ranges)<br><b>2. Athletics</b> (Desert endurance/Throws)<br><b>3. Archery</b> (Tribal belts)", "green")

    st.markdown("<br>", unsafe_allow_html=True)
    c16, c17, c18 = st.columns(3)
    state_card(c16, "Gujarat", "<b>1. Table Tennis</b> (State-sponsored leagues)<br><b>2. Tennis</b> (SAGG infrastructure)<br><b>3. Swimming</b> (Rajkot/Ahmedabad pools)", "green", "Emerging: Bhargavi Bhagora (Archery)")
    state_card(c17, "Arunachal Pradesh", "<b>1. Football</b> (Hangpan Dada Trophy)<br><b>2. Weightlifting</b> (Natural strength base)<br><b>3. Martial Arts</b> (Wushu/Karate focus)", "green")
    state_card(c18, "Mizoram", "<b>1. Football</b> (Mizoram Premier League)<br><b>2. Weightlifting</b> (Rising Olympic prospects)<br><b>3. Boxing</b> (Northeast combative edge)", "green")
    
    st.markdown("<br>", unsafe_allow_html=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 2 — TALENT DISCOVERY
# Purpose: Where talent is likely to emerge; who should be scouted.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
elif selected_tab == "Discovery & Leagues":
    st.markdown('<div class="stitle sticky-header" title="Track rising talent from local and state leagues"> Discovery & Leagues <span class="chip chip-purple">Live Grassroots & Emerging Athlete Prospects</span></div>', unsafe_allow_html=True)
    
    # 1. Grassroots Leagues & Tournaments (Dynamic API Mock)
    st.markdown('<div class="stitle" style="font-size:1.15rem;margin-top:2rem;"> Live Grassroots Leagues & Tournaments</div>', unsafe_allow_html=True)
    
    live_data = get_live_tournaments()
    leagues_disp = pd.DataFrame(live_data)
    
    live_count = len(leagues_disp[leagues_disp["Live Status"] == "🔴 LIVE NOW"]) if "Live Status" in leagues_disp.columns else 12
    soon_count = len(leagues_disp[leagues_disp["Live Status"] == "⏳ STARTING SOON"]) if "Live Status" in leagues_disp.columns else 24
    
    st.markdown(f'''
    <div style="background:rgba(16, 229, 179, 0.08);border:1px solid rgba(16, 229, 179, 0.25);border-radius:12px;padding:0.8rem 1.2rem;margin-bottom:1rem;font-size:0.88rem;color:#FFF;display:flex;align-items:center;gap:1.5rem;">
      <span style="font-weight:700;color:var(--teal);">📡 LIVE STREAM SIGNAL:</span>
      <span><b>{live_count}</b> tournaments are actively <b>LIVE NOW</b></span>
      <span style="color:var(--text3);">|</span>
      <span><b>{soon_count}</b> matches starting in the next 10 minutes</span>
    </div>
    ''', unsafe_allow_html=True)
    
    fc1, fc2, fc3 = st.columns(3)
    with fc1:
        f_sport = st.selectbox("Filter by Sport Focus", ["All Core Sports"] + sorted(list(set(leagues_disp["Sport"]))), key="live_sport_select")
    with fc2:
        f_state = st.selectbox("Filter by State Hub", ["All Mapped States"] + sorted(list(set(leagues_disp["State"]))), key="live_state_select")
    with fc3:
        status_options = [
            "All Statuses",
            "Live Now",
            "Starting Soon",
            "Scheduled",
            "Completed",
            "Just Completed"
        ]
        f_status = st.selectbox("Filter by Event Status", status_options, key="live_status_select")
        
    filtered_leagues = leagues_disp.copy()
    if f_sport != "All Core Sports":
        filtered_leagues = filtered_leagues[filtered_leagues["Sport"] == f_sport]
    if f_state != "All Mapped States":
        filtered_leagues = filtered_leagues[filtered_leagues["State"] == f_state]
    if f_status != "All Statuses":
        if f_status == "Live Now":
            filtered_leagues = filtered_leagues[filtered_leagues["Live Status"].str.upper().str.contains("LIVE NOW")]
        elif f_status == "Starting Soon":
            filtered_leagues = filtered_leagues[filtered_leagues["Live Status"].str.upper().str.contains("STARTING SOON")]
        elif f_status == "Scheduled":
            filtered_leagues = filtered_leagues[filtered_leagues["Live Status"].str.upper().str.contains("SCHEDULED") | filtered_leagues["Live Status"].str.upper().str.contains("STARTING SOON")]
        elif f_status == "Completed":
            filtered_leagues = filtered_leagues[filtered_leagues["Live Status"].str.upper().str.contains("COMPLETED")]
        elif f_status == "Just Completed":
            filtered_leagues = filtered_leagues[filtered_leagues["Live Status"].str.upper().str.contains("JUST COMPLETED")]
            
    st.markdown("<br>", unsafe_allow_html=True)
    if filtered_leagues.empty:
        st.info("No leagues found matching the current filters.")
    else:
        cols = st.columns(3)
        for i, (_, row) in enumerate(filtered_leagues.iterrows()):
            # Extract fields
            name = row.get("Tournament/League Name", "Tournament")
            sport = row.get("Sport", "")
            level = row.get("League Level", "")
            gender = row.get("Gender", "")
            state = row.get("State", "")
            participants = row.get("Participants", "")
            funding = row.get("Funding Status", "")
            live_status = str(row.get("Live Status", ""))
            action = row.get("Action Details", "")
            
            # Determine status color
            status_color = "var(--text2)"
            if "LIVE NOW" in live_status.upper():
                status_color = "var(--red)"
            elif "COMPLETED" in live_status.upper():
                status_color = "var(--green)"
            elif "SCHEDULED" in live_status.upper() or "STARTING SOON" in live_status.upper():
                status_color = "var(--amber)"
                
            with cols[i % 3]:
                st.markdown(f"""
                <div class="acard" style="border-left:4px solid {status_color}; margin-bottom: 1rem; padding: 1.2rem; height: 100%;">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:10px;">
                        <div style="width: 100%;">
                            <div class="acard-title" style="font-size:1.05rem; margin-bottom:0.4rem; min-height:2.4rem;">{name}</div>
                            <div style="font-size:0.8rem; color:var(--text2);">
                                <b>Sport:</b> {sport} <br>
                                <b>Level:</b> {level} <br>
                                <b>State:</b> {state}
                            </div>
                        </div>
                        <div style="text-align:left; background: rgba(255,255,255,0.05); padding: 0.5rem; border-radius: 6px; width: 100%; margin-top: 0.5rem;">
                            <div style="font-weight:800; color:{status_color}; font-size:0.85rem; margin-bottom:0.2rem;">{live_status}</div>
                            <div style="font-size:0.75rem; color:var(--text3);">{action}</div>
                        </div>
                    </div>
                    <div style="margin-top:1rem; padding-top:0.8rem; border-top:1px solid rgba(255,255,255,0.08); font-size:0.75rem; display:flex; flex-direction: column; gap:0.3rem; color: #FFF;">
                        <div><span style="color:var(--text3);">Gender:</span> <b>{gender}</b></div>
                        <div><span style="color:var(--text3);">Participants:</span> <b>{participants}</b></div>
                        <div><span style="color:var(--text3);">Funding:</span> <b>{funding}</b></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    

        

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 4 — COACH CAPACITY
# Purpose: Where coaching is the bottleneck; former athlete-to-coach opportunities; masterclass needs.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
elif selected_tab == "Centres & Academies":
    st.markdown('<div class="stitle sticky-header" title="Monitor infrastructure, coaching capacity, and academies"> Centres & Academies <span class="chip chip-blue">Ecosystem Directory</span></div>', unsafe_allow_html=True)
    
    st.markdown(insight("ℹ Infrastructure & Coaching Capacity", 
        "AthletIQ maps government training centres (SAI), private academies, and tracks Coach-to-Athlete ratios to identify capacity gaps and sponsorship opportunities.", "blue"), unsafe_allow_html=True)
        
    ca_tabs = st.tabs(["Coach-to-Athlete Ratios & Capacity", "SAI Centres & NCOEs", "Private Academies & Akharas", "SAI Proximity Matcher"])
    
    with ca_tabs[0]:
        st.markdown('<div class="stitle" style="font-size:1.15rem;"> Coach Capacity & Ratio Insights</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            all_centres = sai_df["name"].unique().tolist()
            selected_centre = st.selectbox("Select SAI Centre", all_centres)
        
        centre_row = sai_df[sai_df["name"] == selected_centre].iloc[0]
        centre_sports = centre_row["sports"]
        with col2:
            selected_sport = st.selectbox("Select Sport", centre_sports)
        
        total_capacity = int(centre_row["capacity"])
        total_coaches = int(centre_row["coaches"])
        
        # Algorithmic Sport Weighting to calculate realistic specific ratios
        sport_weights = {
            "Archery": {"a": 15, "c": 2}, "Weightlifting": {"a": 10, "c": 2}, 
            "Wrestling": {"a": 20, "c": 3}, "Boxing": {"a": 20, "c": 3}, 
            "Athletics": {"a": 40, "c": 2}, "Football": {"a": 30, "c": 1}, 
            "Hockey": {"a": 25, "c": 2}, "Gymnastics": {"a": 15, "c": 2}, 
            "Swimming": {"a": 25, "c": 2}, "Judo": {"a": 20, "c": 3}, 
            "Cycling": {"a": 15, "c": 2}, "Fencing": {"a": 12, "c": 2}, 
            "Taekwondo": {"a": 20, "c": 3}, "Badminton": {"a": 12, "c": 2}, 
            "Shooting": {"a": 15, "c": 2},
        }
        
        sum_a = sum([sport_weights.get(s, {"a": 20})["a"] for s in centre_sports])
        sum_c = sum([sport_weights.get(s, {"c": 2})["c"] for s in centre_sports])
        
        sel_weight = sport_weights.get(selected_sport, {"a": 20, "c": 2})
        sport_capacity = max(1, int(total_capacity * (sel_weight["a"] / sum_a)))
        sport_coaches = max(1, int(total_coaches * (sel_weight["c"] / sum_c)))
        
        ratio_val = int(sport_capacity / sport_coaches)
        ratio_str = f"{ratio_val} : 1"
        
        if ratio_val <= 15:
            color = "var(--green)"
            status = "Optimal"
            insight_text = f"Well-resourced for {selected_sport}. Focus on performance scaling."
        elif ratio_val <= 30:
            color = "var(--amber)"
            status = "Strained"
            insight_text = f"Coaching staff stretched for {selected_sport}. Consider empanelling additional coaches."
        else:
            color = "var(--red)"
            status = "Critical Deficit"
            insight_text = f"High risk of injury/burnout in {selected_sport}. Deploy NIS masterclass immediately."
            
        st.markdown(f'''
        <div class="acard" style="max-width: 600px; margin-top: 1rem; border-left:4px solid {color};">
            <div style="color:{color}; font-weight:700;">{selected_sport} ({centre_row['state']})</div>
            <div style="font-size:2rem; font-weight:900;">{ratio_str}</div>
            <div style="font-size:0.8rem; color:var(--text2);">Computed Sport Ratio ({sport_capacity} Athletes per {sport_coaches} Coaches)</div>
            <div style="margin-top:0.5rem; font-size:0.8rem;"><b>Standard:</b> 15:1 <span style="color:{color};"> ({status})</span></div>
            <div style="margin-top:0.5rem; font-size:0.8rem; color:var(--blue);"><b>Insight:</b> {insight_text}</div>
        </div>
        ''', unsafe_allow_html=True)

        # AI Decision Maker: Coach Redistribution
        if ratio_val < 15:
            # Use floor division to aggressively flag surpluses (e.g., 25 athletes = 1 ideal coach instead of 2)
            ideal_coaches_needed = max(1, sport_capacity // 15)
            surplus_coaches = sport_coaches - ideal_coaches_needed
            
            if surplus_coaches > 0:
                st.markdown('<div class="stitle" style="font-size:1.05rem; margin-top: 2rem; color:var(--teal);">Coach Redistribution</div>', unsafe_allow_html=True)
                st.markdown(f'<div style="font-size: 0.9rem; color: var(--text2); margin-bottom: 1rem;">Detected a surplus of <b style="color:var(--text1);">{surplus_coaches} {selected_sport} coach(es)</b> at {selected_centre}. Analyzing national deficit centres...</div>', unsafe_allow_html=True)
                
                deficit_centres = []
                for idx, row in sai_df.iterrows():
                    if row["name"] == selected_centre: continue
                    if selected_sport in row["sports"]:
                        t_cap = int(row["capacity"])
                        t_coa = int(row["coaches"])
                        sum_a_o = sum([sport_weights.get(s, {"a": 20})["a"] for s in row["sports"]])
                        sum_c_o = sum([sport_weights.get(s, {"c": 2})["c"] for s in row["sports"]])
                        s_cap = max(1, int(t_cap * (sel_weight["a"] / sum_a_o)))
                        s_coa = max(1, int(t_coa * (sel_weight["c"] / sum_c_o)))
                        
                        r_val = int(s_cap / s_coa)
                        if r_val > 15:
                            needed = ((s_cap + 14) // 15) - s_coa
                            if needed > 0:
                                deficit_centres.append({"name": row["name"], "state": row["state"], "ratio": r_val, "needed": needed})
                
                if deficit_centres:
                    deficit_centres = sorted(deficit_centres, key=lambda x: x["ratio"], reverse=True)
                    st.markdown('<div style="display:flex; flex-direction:column; gap:0.75rem; max-width: 600px;">', unsafe_allow_html=True)
                    for i, dc in enumerate(deficit_centres[:3]):
                        transfer_amt = min(surplus_coaches, dc['needed'])
                        st.markdown(f'''
                        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 1rem; display:flex; justify-content: space-between; align-items:center;">
                            <div>
                                <div style="font-weight: 700; color: var(--text1);">{dc['name']}</div>
                                <div style="font-size: 0.8rem; color: var(--text2);">{dc['state']} • Current Ratio: <span style="color:var(--red); font-weight:700;">{dc['ratio']}:1</span></div>
                            </div>
                            <div style="text-align: right;">
                                <div style="font-size: 0.75rem; color: var(--teal); text-transform: uppercase; letter-spacing: 0.05em;">Recommended Action</div>
                                <div style="font-weight: 700; color: var(--blue);">Transfer {transfer_amt} Coach(es) ➔</div>
                            </div>
                        </div>
                        ''', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div style="font-size: 0.9rem; color: var(--text2);">No critical deficits found across other centres for this sport. The ecosystem is balanced.</div>', unsafe_allow_html=True)

    with ca_tabs[1]:
        st.markdown('<div class="stitle" style="font-size:1rem;"> Sports Authority of India Training Network</div>', unsafe_allow_html=True)
        
        # Directory Table
        sai_df_disp = sai_df[["name", "city", "state", "type", "region", "capacity", "coaches", "facilities"]].copy()
        sai_df_disp.columns = ["Centre Name", "City", "State", "Type", "Region", "Capacity", "Coaches", "Facilities"]
        st.dataframe(
            sai_df_disp.reset_index(drop=True),
            use_container_width=True,
            height=280,
            hide_index=True
        )

    with ca_tabs[2]:
        st.markdown('<div class="stitle" style="font-size:1rem;"> Top Private Sports Academies & Akharas</div>', unsafe_allow_html=True)
        private_acads = [
            {"name": "JSW Inspire Institute of Sport (IIS)", "location": "Vijayanagar, Karnataka", "sports": "Boxing · Wrestling · Athletics", "capacity": "150 athletes", "focus": "Elite performance training"},
            {"name": "Tata Archery Academy", "location": "Jamshedpur, Jharkhand", "sports": "Archery", "capacity": "40 athletes", "focus": "Precision archery pipelines"},
            {"name": "Chhatrasal Akhara", "location": "Delhi", "sports": "Wrestling", "capacity": "100+ athletes", "focus": "Traditional wrestling podium breeding ground"}
        ]
        for pa in private_acads:
            st.markdown(f'''
            <div class="acard" style="border-left:3px solid var(--teal);margin-bottom:0.6rem;">
                <div class="acard-title">{pa['name']}</div>
                <div class="acard-meta">
                     {pa['location']} &nbsp;|&nbsp; <b>Sports:</b> {pa['sports']} &nbsp;|&nbsp; <b>Capacity:</b> {pa['capacity']}<br>
                     <b>Strategic Focus:</b> {pa['focus']}
                </div>
            </div>
            ''', unsafe_allow_html=True)

    with ca_tabs[3]:
        st.markdown('<div class="stitle" style="font-size:1.15rem;"> 🔍 SAI Training Centre Proximity & Suitability Matcher</div>', unsafe_allow_html=True)
        # Toggle between Database search and Custom Profile Creator
        matcher_mode = st.radio("Choose Athlete Matching Mode:", ["Search Database Athletes", "Create Custom Athlete Profile"], horizontal=True, key="top_matcher_mode")

        if matcher_mode == "Search Database Athletes":
            c_tla1, c_tla2 = st.columns([3, 1])
            with c_tla1:
                db_athletes = sorted(list(set(df_all[df_all["entity_type"] == "Athlete"]["name"].dropna().tolist() + [a["name"] for a in elite_athletes])))
                selected_athlete_name = st.selectbox("Select Athlete to Match", db_athletes, index=db_athletes.index("Manu Bhaker") if "Manu Bhaker" in db_athletes else 0, key="top_search_athlete_select")
            with c_tla2:
                st.write("")
                st.write("")
                run_db_match = st.button(" Match SAI Centre", key="btn_top_run_db_match", use_container_width=True)
                
            if run_db_match:
                # First check elite_athletes json list
                ath_data = next((a for a in elite_athletes if a["name"] == selected_athlete_name), None)
                if not ath_data:
                    # Fallback to master CSV database
                    match_rows = df_all[(df_all["entity_type"] == "Athlete") & (df_all["name"] == selected_athlete_name)]
                    if not match_rows.empty:
                        row = match_rows.iloc[0]
                        gender_val = "F" if str(row["gender"]).strip().lower().startswith("f") else "M"
                        perf_val = str(row["performance_level"]).strip()
                        ath_data = {
                            "name": row["name"],
                            "sport": str(row["sport"]).upper(),
                            "age": str(row["age"]) if pd.notna(row["age"]) else "17",
                            "gender": gender_val,
                            "medals": perf_val,
                            "records": str(row["notes"]) if pd.notna(row["notes"]) else f"Registered athlete in {row['sport']} representing {row['state']}."
                        }
                        # Set custom state and performance parameters for recommender mapping
                        st.session_state["top_custom_matched_state"] = str(row["state"])
                        st.session_state["top_custom_matched_perf"] = perf_val
                        
                if ath_data:
                    st.session_state["top_matched_athlete"] = ath_data
                    # Only delete previous custom session parameters if the selected athlete is indeed in elite_athletes (which defaults to Haryana/International)
                    if any(a["name"] == selected_athlete_name for a in elite_athletes):
                        if "top_custom_matched_state" in st.session_state:
                            del st.session_state["top_custom_matched_state"]
                            del st.session_state["top_custom_matched_perf"]
                    st.rerun()

        else:
            c_tla1, c_tla2 = st.columns(2)
            with c_tla1:
                c_name = st.text_input("Athlete Name", value="Custom Athlete Profile", key="top_c_ath_name")
                all_sai_disciplines = sorted(list(set(sp for c in SAI_CENTRES for sp in c["sports"])))
                c_sport = st.selectbox("Sport Discipline", all_sai_disciplines, index=all_sai_disciplines.index("Wrestling") if "Wrestling" in all_sai_disciplines else 0, key="top_c_ath_sport")
                all_sai_states = sorted(list(set(c["state"] for c in SAI_CENTRES)))
                c_state = st.selectbox("Home State", all_sai_states, index=all_sai_states.index("Haryana") if "Haryana" in all_sai_states else 0, key="top_c_ath_state")
                c_gold = st.number_input("Gold Medals", min_value=0, max_value=50, value=0, step=1, key="top_c_ath_gold")
                c_silver = st.number_input("Silver Medals", min_value=0, max_value=50, value=0, step=1, key="top_c_ath_silver")
                c_bronze = st.number_input("Bronze Medals", min_value=0, max_value=50, value=0, step=1, key="top_c_ath_bronze")

                st.markdown(f"""
                <div style='margin-top:1rem; display:flex; gap:0.75rem;'>
                    <div style='flex:1; background:rgba(255,215,0,0.12); border:1px solid rgba(255,215,0,0.25); border-radius:12px; padding:0.85rem;'>
                        <div style='font-size:0.8rem; color:#FFE066; font-weight:700; margin-bottom:0.35rem;'>Gold</div>
                        <div style='font-size:1.5rem; font-weight:800; color:#FFD700;'>{c_gold}</div>
                    </div>
                    <div style='flex:1; background:rgba(192,192,192,0.12); border:1px solid rgba(192,192,192,0.25); border-radius:12px; padding:0.85rem;'>
                        <div style='font-size:0.8rem; color:#D3D3D3; font-weight:700; margin-bottom:0.35rem;'>Silver</div>
                        <div style='font-size:1.5rem; font-weight:800; color:#C0C0C0;'>{c_silver}</div>
                    </div>
                    <div style='flex:1; background:rgba(205,127,50,0.12); border:1px solid rgba(205,127,50,0.25); border-radius:12px; padding:0.85rem;'>
                        <div style='font-size:0.8rem; color:#D2A679; font-weight:700; margin-bottom:0.35rem;'>Bronze</div>
                        <div style='font-size:1.5rem; font-weight:800; color:#CD7F32;'>{c_bronze}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            with c_tla2:
                c_age = st.slider("Age (Years)", 8, 35, 17, key="top_c_ath_age")
                c_gender = st.selectbox("Gender", ["Male", "Female"], key="top_c_ath_gender")
                c_perf = st.selectbox("Current Performance Level", ["District", "State", "National", "International"], key="top_c_ath_perf")
            
            run_custom_match = st.button(" Calculate Optimal Training Centre", use_container_width=True, key="btn_top_run_custom_match")
            if run_custom_match:
                medal_total = int(c_gold) + int(c_silver) + int(c_bronze)
                custom_ath_mock = {
                    "name": c_name,
                    "sport": c_sport.upper(),
                    "age": str(c_age),
                    "gender": "F" if c_gender == "Female" else "M",
                    "medals": f"Gold: {c_gold} | Silver: {c_silver} | Bronze: {c_bronze} | Total: {medal_total}",
                    "records": f"Custom entered athlete from state of {c_state} competing in {c_sport}."
                }
                st.session_state["top_matched_athlete"] = custom_ath_mock
                st.session_state["top_custom_matched_state"] = c_state
                st.session_state["top_custom_matched_perf"] = c_perf
                st.rerun()

        # Render top-level recommendation answers
        if "top_matched_athlete" in st.session_state:
            t_ath = st.session_state["top_matched_athlete"]
            t_gender = "Female" if t_ath["gender"] == "F" else "Male"
            try: t_age = int(t_ath["age"])
            except ValueError: t_age = 17
            
            if "top_custom_matched_state" in st.session_state:
                t_state = st.session_state["top_custom_matched_state"]
                t_perf = st.session_state["top_custom_matched_perf"]
            else:
                t_perf = "International" if any(x in t_ath["medals"].lower() for x in ["olympic", "world", "asian", "cwg", "issf", "international"]) else "National"
                t_state = "Haryana"
                state_keywords = {
                    "haryana": "Haryana", "punjab": "Punjab", "delhi": "Delhi", "manipur": "Manipur",
                    "maharashtra": "Maharashtra", "kerala": "Kerala", "tamil nadu": "Tamil Nadu",
                    "odisha": "Odisha", "uttar pradesh": "Uttar Pradesh", "madhya pradesh": "Madhya Pradesh",
                    "assam": "Assam", "telangana": "Telangana", "andhra": "Andhra Pradesh",
                    "west bengal": "West Bengal", "rajasthan": "Rajasthan", "gujarat": "Gujarat",
                    "jharkhand": "Jharkhand"
                }
                for kw, st_name in state_keywords.items():
                    if kw in t_ath["records"].lower() or kw in t_ath["medals"].lower():
                        t_state = st_name
                        break
                        
            recs = recommend_sai_centres(t_ath["sport"].title(), t_state, t_perf, t_age, t_gender, top_n=3)
            
            st.markdown(f'''
            <div style="background:rgba(138,180,248,0.1);border:1px solid rgba(138,180,248,0.3);border-radius:15px;padding:1.2rem;margin-top:1rem;margin-bottom:1rem;">
              <div style="font-family:Outfit,sans-serif;font-size:1.15rem;font-weight:800;color:#FFF;">
                 Top 3 Recommended SAI Centres for {t_ath['name']}
              </div>
              <div style="font-size:0.82rem;color:#9AA0A6;margin-top:0.2rem;">
                Sport Focus: {t_ath['sport'].title()} &nbsp;|&nbsp; Home State: {t_state} &nbsp;|&nbsp; Age: {t_age} &nbsp;|&nbsp; Performance Level: {t_perf}
              </div>
              <div style="font-size:0.82rem;color:#FFF;margin-top:0.6rem;">
                <b>Medals:</b> {t_ath.get('medals', 'Gold: 0 | Silver: 0 | Bronze: 0 | Total: 0')}
              </div>
            </div>
            ''', unsafe_allow_html=True)
            
            for idx, rec in enumerate(recs):
                st.markdown(render_sai_card(rec["centre"], rec["score"], idx+1), unsafe_allow_html=True)
                
            if st.button(" Clear Recommendations & Close Panel", key="btn_top_close_matcher"):
                del st.session_state["top_matched_athlete"]
                if "top_custom_matched_state" in st.session_state:
                    del st.session_state["top_custom_matched_state"]
                    del st.session_state["top_custom_matched_perf"]
                st.rerun()

elif selected_tab == "Sponsor Pipeline":
    st.markdown('<div class="stitle sticky-header" title="Discover and match commercial sponsors with academies and sports." style="font-size:1.8rem;"> Sponsor Pipeline <span class="chip chip-amber">Commercial Prospects & Packages</span></div>', unsafe_allow_html=True)
    
    st.markdown(insight("ℹ Commercial Opportunities Pipeline", 
        "View active corporate sponsor leads, budgets, and priority fits in the database. "
        "Each opportunity has ready-to-use GTM sales collateral downloads.", ""), unsafe_allow_html=True)
        
    leads_list = df_csr.copy() if df_csr is not None else pd.DataFrame()
    if not leads_list.empty:
        sc1, sc2, sc3 = st.columns(3)
        with sc1:
            st.markdown('<div class="stitle" style="font-size:0.95rem;color:var(--pink);"> Hot Leads (Active Pitch)</div>', unsafe_allow_html=True)
            hot_list = leads_list[leads_list["contact_potential"].str.lower()=="hot"].head(4)
            for _, row in hot_list.iterrows():
                st.markdown(f"""
                <div class="acard" style="border-top:3px solid var(--pink);margin-bottom:0.6rem;">
                    <div class="acard-title">{row['company_name']}</div>
                    <div class="acard-meta" style="font-size:0.8rem;">
                         Budget: ₹{row['annual_csr_budget_cr']:.1f} Cr &nbsp;|&nbsp; {row['sport_focus']}<br>
                         Strategy: {row['engagement_strategy']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
        with sc2:
            st.markdown('<div class="stitle" style="font-size:0.95rem;color:var(--gold);"> Warm Leads (Prospecting)</div>', unsafe_allow_html=True)
            warm_list = leads_list[leads_list["contact_potential"].str.lower()=="warm"].head(4)
            for _, row in warm_list.iterrows():
                st.markdown(f"""
                <div class="acard" style="border-top:3px solid var(--gold);margin-bottom:0.6rem;">
                    <div class="acard-title">{row['company_name']}</div>
                    <div class="acard-meta" style="font-size:0.8rem;">
                         Budget: ₹{row['annual_csr_budget_cr']:.1f} Cr &nbsp;|&nbsp; {row['sport_focus']}<br>
                         Strategy: {row['engagement_strategy']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
        with sc3:
            st.markdown('<div class="stitle" style="font-size:0.95rem;color:var(--blue);"> Cold / Future Opportunities</div>', unsafe_allow_html=True)
            cold_list = leads_list[leads_list["contact_potential"].str.lower()=="cold"].head(4)
            for _, row in cold_list.iterrows():
                st.markdown(f"""
                <div class="acard" style="border-top:3px solid var(--blue);margin-bottom:0.6rem;">
                    <div class="acard-title">{row['company_name']}</div>
                    <div class="acard-meta" style="font-size:0.8rem;">
                         Budget: ₹{row['annual_csr_budget_cr']:.1f} Cr &nbsp;|&nbsp; {row['sport_focus']}<br>
                         Strategy: {row['engagement_strategy']}
                    </div>
                </div>
                """, unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 9 — ATHLETE COHORTS
# Purpose: Not just elite athletes; package groups for funding and development.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
elif selected_tab == "Profile":
    # 1. Title
    st.markdown('<div class="stitle sticky-header"> Profile Directory <span class="chip chip-blue">Athlete & Coach Bios</span></div>', unsafe_allow_html=True)
    
    # 2. Category & Location Filters (Sport & State)
    col_spt, col_st = st.columns(2)
    with col_spt:
        sports_list = ["All Sports"] + sorted(list(df_all["sport"].unique()))
        sport_choice = st.selectbox("Choose Sport:", sports_list, key="profile_sport")
    with col_st:
        states_list = ["All States"] + sorted(list(df_all["state"].unique()))
        state_choice = st.selectbox("Choose State:", states_list, key="profile_state")
        
    # Filter datasets for both Athletes and Coaches
    filtered_athletes = df_all[df_all["entity_type"] == "Athlete"].copy()
    filtered_coaches = df_all[df_all["entity_type"] == "Coach"].copy()
    
    if sport_choice != "All Sports":
        filtered_athletes = filtered_athletes[filtered_athletes["sport"].str.lower() == sport_choice.lower()]
        filtered_coaches = filtered_coaches[filtered_coaches["sport"].str.lower() == sport_choice.lower()]
    if state_choice != "All States":
        filtered_athletes = filtered_athletes[filtered_athletes["state"].str.lower() == state_choice.lower()]
        filtered_coaches = filtered_coaches[filtered_coaches["state"].str.lower() == state_choice.lower()]
        
    # 3. Check for Empty State
    if filtered_athletes.empty and filtered_coaches.empty:
        st.warning("No result found")
    else:
        def render_bio(selected_name, is_coach_flag, person_row):
            entity_type = "Coach" if is_coach_flag else "Sportsperson"
            
            # Wrestling TOPS details dict
            wrestling_tops = {
                "sunil kumar": {
                    "category": "87 Kg GR",
                    "dob_age": "29/09/1999 (22 Years)",
                    "base": "SAI Sonipat / Guru Mehar Akhara Rohtak",
                    "best": "2020 Asian Championship Gold",
                    "latest": "3rd at 2022 Asian Championship",
                    "outlook": "Participant for 2028 LA Olympic Games",
                    "national_pos": "1st at Senior Nationals (2021)"
                },
                "ravinder": {
                    "category": "61/65 Kg FS",
                    "dob_age": "03/08/1997 (24 Years)",
                    "base": "SAI Sonipat / Naresh Akhara Delhi",
                    "best": "2019 U-23 World Championship Silver",
                    "latest": "5th at 2021 World Championship",
                    "outlook": "Participant for 2028 LA Olympic Games",
                    "national_pos": "2019 & 2020 Senior National Gold"
                },
                "aman": {
                    "category": "57 Kg FS",
                    "dob_age": "25/07/2005 (17 Years)",
                    "base": "Air Force Centre Jalahalli, Bangalore",
                    "best": "3rd at 2022 Cadet Nationals",
                    "latest": "2021 Cadet World Championship Gold",
                    "outlook": "Need time to assess for 2028 LA Olympic Games",
                    "national_pos": "3rd at Cadet Nationals"
                },
                "antim panghal": {
                    "category": "53 Kg WW",
                    "dob_age": "31/08/2004 (18 Years)",
                    "base": "SAI Lucknow",
                    "best": "U-20 World Championship Gold",
                    "latest": "Gold at 2022 Junior World Championship",
                    "outlook": "Need time to assess (Lost to Vinesh Phogat in Sr WCH trials final 7-0)",
                    "national_pos": "2022 Junior Nationals Gold"
                },
                "priya malik": {
                    "category": "76 Kg WW",
                    "dob_age": "16/02/2005 (17 Years)",
                    "base": "CBS Akhara Rohtak (Haryana)",
                    "best": "U-20 World Championship Silver",
                    "latest": "Silver at 2022 Junior World Championship",
                    "outlook": "Need time to assess for 2028 LA Olympic Games",
                    "national_pos": "2022 Junior Nationals Gold"
                },
                "sujeet": {
                    "category": "65 Kg FS",
                    "dob_age": "05/11/2002 (19 Years)",
                    "base": "Sonipat (Haryana)",
                    "best": "2022 4th Ranking Series Gold",
                    "latest": "Bronze at 2022 Junior World Championship",
                    "outlook": "Need time to assess (Lost by criteria in 70kg WCH trials to Ravinder, score 6-6)",
                    "national_pos": "2022 Junior Nationals Gold"
                },
                "suraj vasisth": {
                    "category": "55 Kg GR",
                    "dob_age": "16 Years",
                    "base": "Haryana",
                    "best": "2022 U-17 World Championship Gold",
                    "latest": "2022 U-17 World Championship Gold",
                    "outlook": "Need time to assess for 2028 LA Olympic Games",
                    "national_pos": "2022 Cadet Nationals Gold"
                },
                "ronit sharma": {
                    "category": "48 Kg GR",
                    "dob_age": "16 Years",
                    "base": "Haryana",
                    "best": "2022 U-17 World Championship Silver",
                    "latest": "2022 U-17 World Championship Silver",
                    "outlook": "Need time to assess for 2028 LA Olympic Games",
                    "national_pos": "2021 Cadet Nationals Gold"
                }
            }
            
            # Display Bio Card
            st.markdown("---")
            st.markdown(f'<div class="stitle" style="font-size:1.15rem;margin-top:0rem;">Bio-Data: {selected_name}</div>', unsafe_allow_html=True)
            
            # Main details columns
            c_bio1, c_bio2 = st.columns([1, 1])
            
            with c_bio1:
                st.markdown(f"""
                <div class="acard" style="min-height:220px;">
                    <span class="tag green" style="float:right;">{entity_type}</span>
                    <b style="font-size:1.1rem;color:var(--teal);">{person_row['name']}</b><br>
                    <span style="font-size:0.75rem;color:var(--text2);">{person_row['sport']} · {person_row['state']} · {person_row.get('city', 'Unknown')}</span>
                    <hr style="margin:0.8rem 0;border-color:rgba(16,229,179,0.15);">
                    <div style="font-size:0.85rem;line-height:1.6;color:var(--text2);">
                        <b>Age:</b> {int(person_row['age']) if pd.notna(person_row['age']) else 'Unknown'}<br>
                        <b>Gender:</b> {person_row['gender']}<br>
                        <b>Tier:</b> {person_row['tier']}<br>
                        <b>Registry Base:</b> {person_row.get('city', 'Unknown')}, {person_row['state']}<br>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
            with c_bio2:
                if entity_type == "Coach":
                    op_centre = "SAI NCOE " + str(person_row.get('state', 'Unknown')) if str(person_row.get('performance_level', '')) in ["International", "National"] else str(person_row.get('city', 'Unknown')) + " Academy"
                    
                    st.markdown(f"""
                    <div class="acard" style="min-height:220px;">
                        <span class="tag blue" style="float:right;">Certification</span>
                        <b style="font-size:1.05rem;color:var(--blue);">Licence & Certificate Status</b>
                        <hr style="margin:0.8rem 0;border-color:rgba(16,229,179,0.15);">
                        <div style="font-size:0.85rem;line-height:1.6;color:var(--text2);">
                            <b>Active Licence:</b> <span class="tag green">{person_row['performance_level']}</span><br>
                            <b>Licencing Body:</b> {person_row.get('source_link', 'Official Registry')}<br>
                            <b>Empanelled Stage:</b> {person_row.get('pipeline_stage', 'Empanelled')}<br>
                            <b>Notes:</b> {person_row.get('notes', 'No additional certificate notes recorded.')}<br>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    # Determine mock coach and centre based on performance/state
                    coach_val = "Assigned National Coach" if person_row['performance_level'] in ["International", "National"] else "Regional Academy Coach"
                    centre_val = "SAI NCOE " + str(person_row.get('state', 'Unknown')) if person_row['performance_level'] in ["International", "National"] else "Local State Academy"
                    
                    st.markdown(f"""
                    <div class="acard" style="min-height:220px;">
                        <span class="tag blue" style="float:right;">Performance & Training</span>
                        <b style="font-size:1.05rem;color:var(--blue);">Training Profile & Metrics</b>
                        <hr style="margin:0.8rem 0;border-color:rgba(16,229,179,0.15);">
                        <div style="font-size:0.85rem;line-height:1.6;color:var(--text2);">
                            <b>Primary Coach:</b> {coach_val}<br>
                            <b>Training Centre:</b> {centre_val}<br>
                            <b>Opportunity Score:</b> <span class="tag amber">{person_row['athletiq_opportunity_score']} / 10.0</span><br>
                            <b>Current Funding:</b> {person_row['funding_status']}<br>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
            # 4. Check for Elite Medals & Records (from JSON)
            matching_elites = [e for e in elite_athletes if e["name"].lower() == selected_name.lower()]
            if matching_elites:
                elite_profile = matching_elites[0]
                st.markdown(f"""
                <div class="acard">
                    <span class="tag amber" style="float:right;">Elite Registry</span>
                    <b style="font-size:1rem;color:var(--gold);">Major Achievements & Olympic Medals</b>
                    <hr style="margin:0.8rem 0;border-color:rgba(253,214,99,0.2);">
                    <div style="font-size:0.88rem;line-height:1.6;color:var(--text2);">
                        <b>Medals / Placement:</b> {elite_profile.get('medals', 'None')}<br>
                        <b>National Records & Historical Profile:</b> {elite_profile.get('records', 'None')}<br>
                        <b>Category Event:</b> {elite_profile.get('category', 'None')}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
            # 5. Check for Wrestling TOPS Slide Bios (from PPTX)
            selected_name_lower = selected_name.lower().strip()
            if selected_name_lower in wrestling_tops:
                w_bio = wrestling_tops[selected_name_lower]
                st.markdown(f"""
                <div class="acard">
                    <span class="tag purple" style="float:right;">Wrestling TOPS Profile</span>
                    <b style="font-size:1rem;color:var(--purple);">Detailed Slide Bio (parsed from Wrestling TOPS profile.pptx)</b>
                    <hr style="margin:0.8rem 0;border-color:rgba(104,61,228,0.25);">
                    <div style="font-size:0.88rem;line-height:1.7;color:var(--text2);">
                        <b>Weight Category / Event:</b> {w_bio['category']}<br>
                        <b>Date of Birth / Age:</b> {w_bio['dob_age']}<br>
                        <b>Training Base:</b> {w_bio['base']}<br>
                        <b>Best Career Performance:</b> {w_bio['best']}<br>
                        <b>Latest International Performance:</b> {w_bio['latest']}<br>
                        <b>Position at Senior/Cadet Nationals:</b> {w_bio['national_pos']}<br>
                        <b>2028 LA Olympic Games Outlook:</b> {w_bio['outlook']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
            # 6. Fallback Display Notes
            if person_row.get("notes") and pd.notna(person_row["notes"]) and selected_name_lower not in wrestling_tops:
                st.markdown(f"""
                <div class="acard">
                    <b style="font-size:1rem;color:var(--teal);">Performance Records & History Notes</b>
                    <hr style="margin:0.8rem 0;border-color:rgba(16,229,179,0.15);">
                    <div style="font-size:0.88rem;line-height:1.6;color:var(--text2);">
                        {person_row['notes']}
                    </div>
                </div>
                """, unsafe_allow_html=True)

        tab_ath, tab_coa, tab_aca = st.tabs(["Athlete Search", "Coach Search", "Academy Search"])
        
        with tab_ath:
            athlete_names = sorted(filtered_athletes["name"].dropna().unique().tolist()) if not filtered_athletes.empty else []
            selected_athlete = st.selectbox(
                "Select Athlete to View Bio-Data:",
                options=["-- Select Athlete --"] + athlete_names,
                key="profile_selected_athlete"
            )
            
            if selected_athlete == "-- Select Athlete --":
                if not filtered_athletes.empty:
                    st.markdown('<div class="stitle" style="font-size:1rem;margin-top:1.5rem;">Matching Athletes Directory</div>', unsafe_allow_html=True)
                    ath_display = filtered_athletes[["name", "sport", "state", "performance_level", "age", "notes"]].copy()
                    
                    ath_display["Specialization"] = ath_display["sport"]
                    ath_display["DOB / Age"] = ath_display["age"].apply(lambda x: f"{int(x)} yrs" if pd.notna(x) and float(x) > 0 else "Unknown")
                    ath_display["Achievements / Notes"] = ath_display["notes"].fillna("-")
                    
                    ath_display.drop(columns=["notes", "age", "sport"], inplace=True)
                    ath_display = ath_display[["name", "Specialization", "state", "performance_level", "DOB / Age", "Achievements / Notes"]]
                    ath_display.columns = ["Sportsperson Name", "Specialization", "State Registry", "Performance Level", "DOB / Age", "Achievements / Notes"]
                    
                    st.write(f"Showing all matching athletes (total: {len(ath_display)}):")
                    st.dataframe(ath_display.reset_index(drop=True), use_container_width=True, height=280, hide_index=True)
            else:
                person_row = filtered_athletes[filtered_athletes["name"] == selected_athlete].iloc[0]
                render_bio(selected_athlete, False, person_row)

        with tab_coa:
            coach_names = sorted(filtered_coaches["name"].dropna().unique().tolist()) if not filtered_coaches.empty else []
            selected_coach = st.selectbox(
                "Select Coach to View Bio-Data:",
                options=["-- Select Coach --"] + coach_names,
                key="profile_selected_coach"
            )
            
            if selected_coach == "-- Select Coach --":
                if not filtered_coaches.empty:
                    st.markdown('<div class="stitle" style="font-size:1rem;margin-top:1.5rem;">Matching Coaches Directory</div>', unsafe_allow_html=True)
                    co_display = filtered_coaches[["name", "sport", "city", "state", "performance_level", "age", "notes"]].copy()
                    
                    co_display["Specialization"] = co_display["sport"]
                    co_display["DOB / Age"] = co_display["age"].apply(lambda x: f"{int(x)} yrs" if pd.notna(x) and float(x) > 0 else "Unknown")
                    co_display["Credentials"] = co_display["notes"].fillna("-")
                    co_display.drop(columns=["notes", "age", "sport", "city"], inplace=True)
                    co_display = co_display[["name", "Specialization", "state", "performance_level", "DOB / Age", "Credentials"]]
                    co_display.columns = ["Coach Name", "Specialization", "State Registry", "Performance Level", "DOB / Age", "Credentials"]
                    st.write(f"Showing all matching coaches (total: {len(co_display)}):")
                    st.dataframe(co_display.reset_index(drop=True), use_container_width=True, height=280, hide_index=True)
            else:
                person_row = filtered_coaches[filtered_coaches["name"] == selected_coach].iloc[0]
                render_bio(selected_coach, True, person_row)

        with tab_aca:
            st.markdown('<div class="stitle" style="font-size:1rem;margin-top:1.5rem;">Matching Academies Directory</div>', unsafe_allow_html=True)
            sai_df_disp = sai_df[["name", "city", "state", "type", "region", "capacity", "coaches", "facilities"]].copy()
            if state_choice != "All States":
                sai_df_disp = sai_df_disp[sai_df_disp["state"].str.lower() == state_choice.lower()]
            sai_df_disp.columns = ["Centre Name", "City", "State", "Type", "Region", "Capacity", "Coaches", "Facilities"]
            st.write(f"Showing all matching academies (total: {len(sai_df_disp)}):")
            st.dataframe(sai_df_disp.reset_index(drop=True), use_container_width=True, height=280, hide_index=True)


elif selected_tab == "Womens":
    # ─── Load 5000 Women Athletes from JSON ───
    women_json_path = os.path.join(os.path.dirname(__file__), "..", "data", "women_athletes.json")
    if not os.path.exists(women_json_path):
        women_json_path = os.path.join(os.path.dirname(__file__), "data", "women_athletes.json")
    
    if os.path.exists(women_json_path):
        with open(women_json_path, "r", encoding="utf-8") as wf:
            women_athletes_data = json.load(wf)
    else:
        women_athletes_data = []

    women_df = pd.DataFrame(women_athletes_data)

    st.markdown('<div class="stitle sticky-header"> Womens Directory <span class="chip chip-blue">Emerging Women Athletes</span></div>', unsafe_allow_html=True)

    # ── Filters ──
    wcol_search, wcol_spt, wcol_st, wcol_lvl = st.columns([2, 1, 1, 1])
    with wcol_search:
        w_search = st.text_input("🔍 Search by Name:", placeholder="Type athlete name...", key="women_search")
    with wcol_spt:
        w_sports_list = ["All Sports"] + sorted(women_df["sport"].unique().tolist())
        w_sport_choice = st.selectbox("Sport:", w_sports_list, key="women_sport")
    with wcol_st:
        w_states_list = ["All States"] + sorted(women_df["state"].unique().tolist())
        w_state_choice = st.selectbox("State:", w_states_list, key="women_state")
    with wcol_lvl:
        w_levels_list = ["All Levels", "International", "National", "State", "District"]
        w_level_choice = st.selectbox("Level:", w_levels_list, key="women_level")

    filtered_women = women_df.copy()
    if w_search and w_search.strip():
        filtered_women = filtered_women[filtered_women["name"].str.lower().str.contains(w_search.strip().lower())]
    if w_sport_choice != "All Sports":
        filtered_women = filtered_women[filtered_women["sport"].str.lower() == w_sport_choice.lower()]
    if w_state_choice != "All States":
        filtered_women = filtered_women[filtered_women["state"].str.lower() == w_state_choice.lower()]
    if w_level_choice != "All Levels":
        filtered_women = filtered_women[filtered_women["performance_level"] == w_level_choice]

    if filtered_women.empty:
        st.warning("No women athletes found for the selected filters.")
    else:
        # ── KPI Summary Cards ──
        kpi_c1, kpi_c2, kpi_c3 = st.columns(3)
        with kpi_c1:
            st.markdown(f"""
            <div class="acard" style="text-align:center;padding:1rem;">
                <div style="font-size:2rem;font-weight:800;color:var(--teal);">{len(filtered_women)}</div>
                <div style="font-size:0.75rem;color:var(--text2);text-transform:uppercase;letter-spacing:1px;">Athletes</div>
            </div>
            """, unsafe_allow_html=True)
        with kpi_c2:
            intl_count = len(filtered_women[filtered_women["performance_level"] == "International"])
            st.markdown(f"""
            <div class="acard" style="text-align:center;padding:1rem;">
                <div style="font-size:2rem;font-weight:800;color:var(--blue);">{intl_count}</div>
                <div style="font-size:0.75rem;color:var(--text2);text-transform:uppercase;letter-spacing:1px;">International</div>
            </div>
            """, unsafe_allow_html=True)
        with kpi_c3:
            sport_count = filtered_women["sport"].nunique()
            st.markdown(f"""
            <div class="acard" style="text-align:center;padding:1rem;">
                <div style="font-size:2rem;font-weight:800;color:var(--purple);">{sport_count}</div>
                <div style="font-size:0.75rem;color:var(--text2);text-transform:uppercase;letter-spacing:1px;">Sports</div>
            </div>
            """, unsafe_allow_html=True)

    # ── Athlete Search & Directory ──
        w_athlete_names = sorted(filtered_women["name"].tolist())
        w_selected = st.selectbox(
            "Select Women Athlete to View Bio-Data:",
            options=["-- Select Athlete --"] + w_athlete_names,
            key="women_selected_athlete"
        )

        if w_selected != "-- Select Athlete --":
            person = filtered_women[filtered_women["name"] == w_selected].iloc[0]
            st.markdown("---")
            st.markdown(f'<div class="stitle" style="font-size:1.15rem;margin-top:0rem;">Bio-Data: {w_selected}</div>', unsafe_allow_html=True)

            # Bio card — Left: Personal Info, Right: Performance & Training
            w_c1, w_c2 = st.columns([1, 1])
            with w_c1:
                st.markdown(f"""
                <div class="acard" style="min-height:250px;">
                    <span class="tag green" style="float:right;">Sportsperson</span>
                    <b style="font-size:1.1rem;color:var(--teal);">{person['name']}</b><br>
                    <span style="font-size:0.75rem;color:var(--text2);">{person['sport']} · {person['state']} · {person['city']}</span>
                    <hr style="margin:0.8rem 0;border-color:rgba(16,229,179,0.15);">
                    <div style="font-size:0.85rem;line-height:1.6;color:var(--text2);">
                        <b>Age:</b> {person['age']}<br>
                        <b>Gender:</b> {person['gender']}<br>
                        <b>Tier:</b> {person['tier']}<br>
                        <b>Status:</b> <span class="tag amber">{person['status']}</span><br>
                        <b>Registry Base:</b> {person['city']}, {person['state']}<br>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            with w_c2:
                st.markdown(f"""
                <div class="acard" style="min-height:250px;">
                    <span class="tag blue" style="float:right;">Performance & Training</span>
                    <b style="font-size:1.05rem;color:var(--blue);">Training Profile & Metrics</b>
                    <hr style="margin:0.8rem 0;border-color:rgba(16,229,179,0.15);">
                    <div style="font-size:0.85rem;line-height:1.6;color:var(--text2);">
                        <b>Performance Level:</b> <span class="tag green">{person['performance_level']}</span><br>
                        <b>Opportunity Score:</b> <span class="tag amber">{person['athletiq_opportunity_score']} / 10.0</span><br>
                        <b>Current Funding:</b> {person['funding_status']}<br>
                        <b>Highlight:</b> {person['highlight']}<br>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            # Achievements & Remarks card
            st.markdown(f"""
            <div class="acard">
                <span class="tag amber" style="float:right;">Achievements</span>
                <b style="font-size:1rem;color:var(--gold);">Key Achievements & Scouting Notes</b>
                <hr style="margin:0.8rem 0;border-color:rgba(253,214,99,0.2);">
                <div style="font-size:0.88rem;line-height:1.6;color:var(--text2);">
                    <b>Achievements:</b> {person['achievements']}<br>
                    <b>Scouting Remarks:</b> {person['remarks']}
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown('<div class="stitle" style="font-size:1rem;margin-top:1.5rem;">Select an athlete above to view her full profile, or browse the directory below.</div>', unsafe_allow_html=True)
            
        st.markdown('<div class="stitle" style="font-size:1rem;margin-top:1.5rem;">Full Women Athletes Directory</div>', unsafe_allow_html=True)
        dir_display = filtered_women[["name", "sport", "event", "state", "city", "age", "performance_level", "status", "achievements"]].copy()
        dir_display.columns = ["Athlete Name", "Sport", "Event", "State", "City", "Age", "Level", "Status", "Achievements"]
        st.write(f"Showing all matching women athletes (total: {len(dir_display):,}):")
        st.dataframe(dir_display.reset_index(drop=True), use_container_width=True, height=500, hide_index=True)


elif selected_tab == "AI Assistant":
    import requests
    
    st.markdown('<div class="header-container"><div class="header-title">🤖 AI Assistant</div></div>', unsafe_allow_html=True)
    st.markdown("<p style='color:#a0aec0;margin-bottom:2rem;'>Ask me anything about AthletIQ's data (athletes, coaches, events, etc.)</p>", unsafe_allow_html=True)

    # Custom CSS for the Chat Interface to match AthletIQ Dark Theme
    st.markdown("""
    <style>
    /* Main bottom container */
    div[data-testid="stBottom"] {
        background-color: transparent !important;
    }
    div[data-testid="stBottom"] > div {
        background-color: transparent !important;
    }
    /* Chat Input Background */
    .stChatInputContainer {
        background-color: transparent !important;
    }
    div[data-testid="stChatInput"] {
        background-color: transparent !important;
    }
    div[data-testid="stChatInput"] textarea {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(16, 229, 179, 0.4) !important;
    }
    /* Chat Message Backgrounds */
    div[data-testid="stChatMessage"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border-radius: 8px !important;
        padding: 1rem !important;
        margin-bottom: 1rem !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
    }
    /* AI specific chat bubble (usually has a different avatar) */
    div[data-testid="stChatMessage"]:has([data-testid="stIconMaterial"]) {
        background: linear-gradient(145deg, rgba(16, 229, 179, 0.05) 0%, rgba(13, 22, 35, 0.8) 100%) !important;
        border: 1px solid rgba(16, 229, 179, 0.2) !important;
    }
    div[data-testid="stChatMessage"] p, div[data-testid="stChatMessage"] div {
        color: rgba(255, 255, 255, 0.9) !important;
        font-family: 'Outfit', sans-serif !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Sidebar for API Key
    with st.sidebar:
        st.markdown("### Settings")
        api_key_input = st.text_input("Gemini API Key", type="password", help="Enter your Gemini API Key or set GEMINI_API_KEY environment variable")
    
    api_key = api_key_input or os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        st.warning("Please provide a Gemini API Key in the sidebar or via the GEMINI_API_KEY environment variable to use the AI Assistant.")
    else:
        if "ai_messages" not in st.session_state:
            # Prepare context
            context = "ATHLETIQ MASTER DATABASE SUMMARY:\n"
            
            try:
                events = master_df[master_df["entity_type"] == "Event"]
                if not events.empty:
                    context += "EVENTS & CSR:\n"
                    context += events[["name", "sport", "funding_status", "notes"]].to_csv(index=False) + "\n"
                
                athletes = master_df[master_df["entity_type"] == "Athlete"]
                if not athletes.empty:
                    context += "ATHLETES:\n"
                    context += athletes[["name", "sport", "notes"]].to_csv(index=False) + "\n"
                    
                coaches = master_df[master_df["entity_type"] == "Coach"]
                if not coaches.empty:
                    context += "COACHES:\n"
                    context += coaches[["name", "sport", "notes"]].to_csv(index=False) + "\n"
            except Exception as e:
                context += f"Failed to load data: {e}"

            sys_prompt = f"You are the AthletIQ AI Assistant. You must ONLY answer questions based on the following database snapshot. If the user asks something outside of this data, politely decline.\n\n{context[:50000]}"
            
            st.session_state.ai_messages = []
            st.session_state.ai_system_instruction = sys_prompt

        # Display chat messages
        for msg in st.session_state.ai_messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if prompt := st.chat_input("Ask about athletes, sponsors, or coaches..."):
            st.session_state.ai_messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
                
            with st.chat_message("assistant"):
                response_placeholder = st.empty()
                response_placeholder.markdown("Thinking...")
                try:
                    from google import genai
                    
                    client = genai.Client(api_key=api_key)
                    
                    full_prompt = f"{st.session_state.ai_system_instruction}\\n\\nUser Question: {prompt}"
                    
                    response = client.models.generate_content(
                        model='gemini-1.5-flash',
                        contents=full_prompt,
                    )
                    
                    if response.text:
                        reply_text = response.text
                        response_placeholder.markdown(reply_text)
                        st.session_state.ai_messages.append({"role": "assistant", "content": reply_text})
                    else:
                        response_placeholder.error("Error: The model returned an empty response.")
                        
                except ImportError:
                    response_placeholder.error("The google-genai package is not installed. Please add google-genai to requirements.txt and reboot the app.")
                except Exception as e:
                    response_placeholder.error(f"Error communicating with Gemini via SDK: {e}")


