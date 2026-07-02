"""
AthletIQ Intelligence Platform v3.0
Decision-Making Dashboard — Built for Action, Not Display
7 Tabs: Sports | Geography | Future Champions | CSR & Impact | Sponsor Opportunities | Top Picks | Data Quality
"""

import streamlit as st
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
.hero-title { font-family: 'Outfit', sans-serif; font-size: 4.8rem; font-weight: 900; letter-spacing: -2px; line-height: 1.1; background: linear-gradient(135deg, #10E5B3 0%, #683DE4 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin: 0.5rem 0 0.8rem; }
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

/* ── 3D Tactile Buttons ── */
.stButton > button, .stDownloadButton > button {
    background: linear-gradient(135deg, #10E5B3 0%, #683DE4 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.45rem 1.4rem !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.85rem !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    box-shadow: 0 4px 15px rgba(16, 229, 179, 0.25), inset 0 -3px 0 rgba(0,0,0,0.3) !important;
    transition: all 0.25s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
    position: relative;
}
.stButton > button:hover, .stDownloadButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 22px rgba(16, 229, 179, 0.38), inset 0 -3px 0 rgba(0,0,0,0.3) !important;
}
.stButton > button:active, .stDownloadButton > button:active {
    transform: translateY(1px) !important;
    box-shadow: 0 2px 8px rgba(16, 229, 179, 0.15), inset 0 -1px 0 rgba(0,0,0,0.3) !important;
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
</style>
<div style="position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:0;overflow:hidden;">
  <div class="orb orb-1"></div>
  <div class="orb orb-2"></div>
  <div class="orb orb-3"></div>
  <div class="grid-3d"></div>
</div>
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
def load_master():
    for p in ["../data/athletiq_master_database.csv","data/athletiq_master_database.csv","./data/athletiq_master_database.csv"]:
        if os.path.exists(p):
            df = pd.read_csv(p)
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
    return None

@st.cache_data
def load_csr():
    for p in ["../data/csr_sponsor_signals.csv","data/csr_sponsor_signals.csv","./data/csr_sponsor_signals.csv"]:
        if os.path.exists(p):
            df = pd.read_csv(p)
            df.columns = df.columns.str.strip().str.lower()
            for c in ["company_name","sector","sport_focus","geographic_focus","existing_sport_initiatives",
                      "contact_potential","engagement_strategy","notes","source_link"]:
                if c in df.columns: df[c] = df[c].fillna("Unknown").astype(str).str.strip()
            for c in ["annual_revenue_cr","annual_csr_budget_cr","current_sport_allocation_pct",
                      "csr_alignment_score","athletiq_fit_score"]:
                if c in df.columns: df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0)
            return df
    return None

@st.cache_data
def load_elite_athletes():
    for p in ["../data/elite_athletes.json","data/elite_athletes.json","./data/elite_athletes.json"]:
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                return json.load(f)
    return []

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

def insight(title, body, color=""):
    cls = f"insight {color}" if color else "insight"
    return f"""<div class="{cls}"><div class="insight-title">{title}</div>
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
df_all = load_master()
df_csr = load_csr()
elite_athletes = load_elite_athletes()

if df_all is None:
    st.error(" Master database not found. Place `athletiq_master_database.csv` in the `data/` folder.")
    st.stop()

# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR FILTERS
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("<h2 style='color:#10E5B3;font-family:Outfit;font-weight:700;'> Filters</h2>", unsafe_allow_html=True)
    sel_entity = st.multiselect("Entity Type", sorted(df_all["entity_type"].unique()), default=sorted(df_all["entity_type"].unique()))
    sel_sport = st.multiselect("Sport", sorted(df_all["sport"].unique()), default=sorted(df_all["sport"].unique()))
    sel_state = st.multiselect("State", sorted(df_all["state"].unique()), default=sorted(df_all["state"].unique()))
    sel_tier = st.multiselect("Tier", sorted(df_all["tier"].unique()), default=sorted(df_all["tier"].unique()))
    sel_pipeline = st.multiselect("Pipeline", sorted(df_all["pipeline_stage"].unique()), default=sorted(df_all["pipeline_stage"].unique()))
    st.markdown("---")
    omin, omax = float(df_all["athletiq_opportunity_score"].min()), float(df_all["athletiq_opportunity_score"].max())
    sel_score = st.slider("Opportunity Score", omin, max(omax,10.0), (omin, max(omax,10.0)), 0.5)
    cmin, cmax = float(df_all["cwg_2036_relevance"].min()), float(df_all["cwg_2036_relevance"].max())

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
  <h1 class="hero-title notranslate" translate="no" style="font-family: 'Outfit', sans-serif; font-size: 4.8rem; font-weight: 900; letter-spacing: -2px; line-height: 1.1; margin: 0.5rem 0 0.8rem;">ATHLETIQ</h1>
  <h2 class="notranslate" translate="no" style="font-family: 'Outfit', sans-serif; font-size: 1.35rem; color: #E8EAED; font-weight: 500; max-width: 800px; margin: 0 auto; line-height: 1.5;">
    Scouting, coaching and funding intelligence for India’s grassroots-to-medal pathways.
  </h2>
  <div class="notranslate" translate="no" style="font-family: 'Inter', sans-serif; font-size: 0.88rem; color: #10E5B3; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; margin-top: 0.8rem; margin-bottom: 1.2rem;">
    Built to decide where to scout, coach, fund and activate.
  </div>
  <div class="hero-rule" style="margin: 1rem auto 1.5rem;"></div>
</div>
""", unsafe_allow_html=True)

# ── TOP-LEVEL ATHLETE-TO-SAI MATCHING ENGINE (PRIMARY DECISION PORTAL) ──
st.markdown('<div class="stitle" style="font-size:1.2rem;margin-top:1rem;"> SAI Training Centre Proximity & Suitability Matcher</div>', unsafe_allow_html=True)

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
    with c_tla2:
        c_age = st.slider("Age (Years)", 8, 35, 17, key="top_c_ath_age")
        c_gender = st.selectbox("Gender", ["Male", "Female"], key="top_c_ath_gender")
        c_perf = st.selectbox("Current Performance Level", ["District", "State", "National", "International"], key="top_c_ath_perf")
        
    run_custom_match = st.button(" Calculate Optimal Training Centre", use_container_width=True, key="btn_top_run_custom_match")
    if run_custom_match:
        custom_ath_mock = {
            "name": c_name,
            "sport": c_sport.upper(),
            "age": str(c_age),
            "gender": "F" if c_gender == "Female" else "M",
            "medals": f"{c_perf} Level Competitor",
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
    
    st.markdown(f"""
    <div style="background:rgba(138,180,248,0.1);border:1px solid rgba(138,180,248,0.3);border-radius:15px;padding:1.2rem;margin-top:1rem;margin-bottom:1rem;">
      <div style="font-family:Outfit,sans-serif;font-size:1.15rem;font-weight:800;color:#FFF;">
         Top 3 Recommended SAI Centres for {t_ath['name']}
      </div>
      <div style="font-size:0.82rem;color:#9AA0A6;margin-top:0.2rem;">
        Sport Focus: {t_ath['sport'].title()} &nbsp;|&nbsp; Home State: {t_state} &nbsp;|&nbsp; Age: {t_age} &nbsp;|&nbsp; Performance Level: {t_perf}
      </div>
    </div>
    """, unsafe_allow_html=True)
    
    for idx, rec in enumerate(recs):
        st.markdown(render_sai_card(rec["centre"], rec["score"], idx+1), unsafe_allow_html=True)
        
    if st.button(" Clear Recommendations & Close Panel", key="btn_top_close_matcher"):
        del st.session_state["top_matched_athlete"]
        if "top_custom_matched_state" in st.session_state:
            del st.session_state["top_custom_matched_state"]
            del st.session_state["top_custom_matched_perf"]
        st.rerun()

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

tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10 = st.tabs([
    "Pathway Overview",
    "Discovery & Leagues",
    "Sport Priority",
    "Coach Capacity",
    "Centres & Academies",
    "Federation Intelligence",
    "CSR Matchmaker",
    "Sponsor Pipeline",
    "Athlete Cohorts",
    "Data Quality",
])

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
with tab1:
    st.markdown('<div class="stitle"> Pathway Overview <span class="chip chip-blue">Strategic Dashboard Homepage</span></div>', unsafe_allow_html=True)

    # 1. Dynamic Grassroots-to-Podium Conversion Funnel
    st.markdown('<div class="stitle" style="font-size:1.15rem;margin-top:2rem;"> Grassroots-to-Podium Conversion Funnel</div>', unsafe_allow_html=True)
    st.markdown(insight(" Dynamic Conversion Pipeline", 
        "Track athlete progression across India's decentralized sports framework (ASMITA & Khelo India models). Filter by sport and gender to analyze pipeline drop-offs.", "blue"), unsafe_allow_html=True)
    
    col_f1, col_f2 = st.columns([1, 1])
    with col_f1:
        f_sport = st.selectbox("Filter Funnel by Sport Focus", ["All Sports", "Wrestling", "Boxing", "Archery", "Hockey", "Athletics"], key="funnel_sport_select")
    with col_f2:
        f_gender = st.selectbox("Filter Funnel by Gender", ["All", "Male", "Female"], key="funnel_gender_select")
        
    # Data dictionary for dynamic funnel
    funnel_data = {
        "All Sports": {
            "All": [300000, 22400, 3100, 580, 78],
            "Male": [165000, 12100, 1650, 310, 42],
            "Female": [135000, 10300, 1450, 270, 36],
        },
        "Wrestling": {
            "All": [60000, 4800, 680, 140, 22],
            "Male": [35000, 2800, 400, 80, 12],
            "Female": [25000, 2000, 280, 60, 10],
        },
        "Boxing": {
            "All": [45000, 3200, 480, 95, 14],
            "Male": [24000, 1800, 280, 55, 8],
            "Female": [21000, 1400, 200, 40, 6],
        },
        "Archery": {
            "All": [25000, 1900, 310, 65, 8],
            "Male": [13000, 1000, 160, 35, 4],
            "Female": [12000, 900, 150, 30, 4],
        },
        "Hockey": {
            "All": [85000, 6100, 820, 160, 24],
            "Male": [48000, 3400, 460, 90, 13],
            "Female": [37000, 2700, 360, 70, 11],
        },
        "Athletics": {
            "All": [85000, 6400, 810, 120, 10],
            "Male": [45000, 3100, 350, 50, 5],
            "Female": [40000, 3300, 460, 70, 5],
        }
    }
    
    funnel_vals = funnel_data[f_sport][f_gender]
    stages = [
        "1. District / Grassroots Leagues",
        "2. State Championships",
        "3. Zonal High-Performance",
        "4. National Camps / NCOEs",
        "5. Elite International / Podium"
    ]
    
    col_funnel_chart, col_funnel_diag = st.columns([3, 2])
    
    with col_funnel_chart:
        fig_funnel = go.Figure(go.Funnel(
            y = stages,
            x = funnel_vals,
            textinfo = "value+percent initial",
            marker = {"color": ["#10E5B3", "#683DE4", "#10E5B3", "#FCAD70", "#F28B82"]},
            connector = {"fillcolor": "rgba(255,255,255,0.03)"}
        ))
        playout(fig_funnel, f"Grassroots-to-Podium Funnel — {f_sport} ({f_gender})", h=450)
        st.plotly_chart(fig_funnel, use_container_width=True)
        
    with col_funnel_diag:
        st.markdown('<div class="stitle" style="font-size:0.95rem;margin-top:0;"> Pipeline Blocker & Leakage Analysis</div>', unsafe_allow_html=True)
        
        # Calculate transition rates
        t1_rate = (funnel_vals[1] / funnel_vals[0]) * 100
        t2_rate = (funnel_vals[2] / funnel_vals[1]) * 100
        t3_rate = (funnel_vals[3] / funnel_vals[2]) * 100
        t4_rate = (funnel_vals[4] / funnel_vals[3]) * 100
        
        st.markdown(f"""
        <div class="acard" style="border-left:3px solid var(--purple);margin-bottom:0.6rem;padding:0.8rem 1.2rem;">
            <div style="font-weight:700;font-size:0.85rem;color:#FFF;">District State Transition: {t1_rate:.1f}%</div>
            <div style="font-size:0.75rem;color:var(--text2);margin-top:0.25rem;">
                <b>Leakage Blocker:</b> Lack of standardized equipment kits & travel funding in Tier-3 districts.<br>
                <b>Recommended CSR Intervention:</b> Support village-level league travel grants.
            </div>
        </div>
        <div class="acard" style="border-left:3px solid var(--teal);margin-bottom:0.6rem;padding:0.8rem 1.2rem;">
            <div style="font-weight:700;font-size:0.85rem;color:#FFF;">State Zonal Transition: {t2_rate:.1f}%</div>
            <div style="font-size:0.75rem;color:var(--text2);margin-top:0.25rem;">
                <b>Leakage Blocker:</b> Insufficient NIS certified coaches and sports science clinics at state levels.<br>
                <b>Recommended Intervention:</b> Train former state athletes as district coaches.
            </div>
        </div>
        <div class="acard" style="border-left:3px solid var(--gold);margin-bottom:0.6rem;padding:0.8rem 1.2rem;">
            <div style="font-weight:700;font-size:0.85rem;color:#FFF;">Zonal National Transition: {t3_rate:.1f}%</div>
            <div style="font-size:0.75rem;color:var(--text2);margin-top:0.25rem;">
                <b>Leakage Blocker:</b> Lack of specialized residential sports academy placements and advanced nutrition.<br>
                <b>Recommended Intervention:</b> Partner with private/SAI NCOE centres.
            </div>
        </div>
        <div class="acard" style="border-left:3px solid var(--pink);margin-bottom:0.6rem;padding:0.8rem 1.2rem;">
            <div style="font-weight:700;font-size:0.85rem;color:#FFF;">National Elite Transition: {t4_rate:.1f}%</div>
            <div style="font-size:0.75rem;color:var(--text2);margin-top:0.25rem;">
                <b>Leakage Blocker:</b> Insufficient corporate sponsorship for international exposure tournaments.<br>
                <b>Recommended Intervention:</b> Align private sponsor contracts to elite athletes.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # 2. Recommended Pathway Actions
    st.markdown('<div class="stitle" style="font-size:1.15rem;margin-top:2rem;"> Recommended Pathway Actions</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("""
        <div class="acard" style="border-top:3px solid var(--purple);height:290px;display:flex;flex-direction:column;justify-content:between;">
            <div>
                <div class="acard-title" style="color:#FFF;font-size:0.95rem;font-weight:700;"> Women’s Combat Sports</div>
                <div class="acard-meta" style="margin-top:0.4rem;font-size:0.8rem;line-height:1.4;">
                    <b>Action:</b> Build scouting + coaching cohort<br>
                    <b>Where:</b> Haryana / UP / Rajasthan<br>
                    <b>Why:</b> medal relevance + women’s CSR fit + existing culture
                </div>
            </div>
            <div style="font-size:0.78rem;color:var(--blue);font-weight:700;margin-top:0.8rem;">
                 Next step: Identify 25 coaches & 5 pilot districts
            </div>
        </div>
        """, unsafe_allow_html=True)
        render_gtm_exporter("wcombat", "Women's Combat Sports Pathway", "Wrestling & Boxing", "Haryana/UP", "Scouting and coaching pilot for 25 female fighters.")
        
    with c2:
        st.markdown("""
        <div class="acard" style="border-top:3px solid var(--teal);height:290px;display:flex;flex-direction:column;justify-content:between;">
            <div>
                <div class="acard-title" style="color:#FFF;font-size:0.95rem;font-weight:700;"> Archery Precision Pathway</div>
                <div class="acard-meta" style="margin-top:0.4rem;font-size:0.8rem;line-height:1.4;">
                    <b>Action:</b> Run assessment talent pilot<br>
                    <b>Where:</b> North East / tribal belts / rural districts<br>
                    <b>Why:</b> measurable sport + AI compatibility + medal potential
                </div>
            </div>
            <div style="font-size:0.78rem;color:var(--blue);font-weight:700;margin-top:0.8rem;">
                 Next step: Shortlist academies and coaches
            </div>
        </div>
        """, unsafe_allow_html=True)
        render_gtm_exporter("archery_prec", "Archery Precision Pathway", "Archery", "Assam/Meghalaya", "High performance talent mapping with digital readiness tools.")

    with c3:
        st.markdown("""
        <div class="acard" style="border-top:3px solid var(--gold);height:290px;display:flex;flex-direction:column;justify-content:between;">
            <div>
                <div class="acard-title" style="color:#FFF;font-size:0.95rem;font-weight:700;"> Coach Capacity Programme</div>
                <div class="acard-meta" style="margin-top:0.4rem;font-size:0.8rem;line-height:1.4;">
                    <b>Action:</b> Build athlete-to-coach registry<br>
                    <b>Where:</b> Priority sport clusters<br>
                    <b>Why:</b> Athlete discovery fails without coaching depth
                </div>
            </div>
            <div style="font-size:0.78rem;color:var(--blue);font-weight:700;margin-top:0.8rem;">
                 Next step: Onboard 50 coaches/former athletes
            </div>
        </div>
        """, unsafe_allow_html=True)
        render_gtm_exporter("coach_capacity", "Coach Capacity Programme", "Multi-sport", "Pan-India", "Transition registry for retired national/international athletes.")

    with c4:
        st.markdown("""
        <div class="acard" style="border-top:3px solid var(--pink);height:290px;display:flex;flex-direction:column;justify-content:between;">
            <div>
                <div class="acard-title" style="color:#FFF;font-size:0.95rem;font-weight:700;"> Federation Visibility Layer</div>
                <div class="acard-meta" style="margin-top:0.4rem;font-size:0.8rem;line-height:1.4;">
                    <b>Action:</b> Build NSF credibility profiles<br>
                    <b>Where:</b> Priority Olympic & niche sports<br>
                    <b>Why:</b> Athletes/sponsors need clarity on who governs
                </div>
            </div>
            <div style="font-size:0.78rem;color:var(--blue);font-weight:700;margin-top:0.8rem;">
                 Next step: Complete 30 federation profiles
            </div>
        </div>
        """, unsafe_allow_html=True)
        render_gtm_exporter("fed_visibility", "Federation Visibility Layer", "Olympic Sports", "Delhi", "Credibility ranking and governance monitoring mapping.")

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. Medal Pathway Diagnostic Widget
    st.markdown('<div class="stitle" style="font-size:1.15rem;margin-top:1.5rem;"> Why Medals Are Lost: Pathway Breaks Detected</div>', unsafe_allow_html=True)
    st.markdown(insight(" Pathway Diagnostics", 
        "By identifying gaps in the 5 critical stages of athlete development, we can target CSR and coaching investments precisely.", "red"), unsafe_allow_html=True)
    
    diagnostic_cols = st.columns(5)
    diag_stages = [
        {"stage": " 1. Discovery", "signal": "Talent clusters unmapped", "action": "Run scouting camps", "gap": "9 clusters unmapped", "col": "blue"},
        {"stage": " 2. Coaching", "signal": "High load, low availability", "action": "Coach registry + clinics", "gap": "24 capacity gaps", "col": "purple"},
        {"stage": " 3. Competition", "signal": "Weak exposure calendar", "action": "Build competition access", "gap": "14 states lack events", "col": "teal"},
        {"stage": " 4. Funding", "signal": "CSR not tied to progression", "action": "Package cohorts for sponsors", "gap": "82% unfunded", "col": "gold"},
        {"stage": " 5. Progression", "signal": "No next-step visibility", "action": "Recommend academy route", "gap": "40% exit sports early", "col": "pink"}
    ]
    for idx, ds in enumerate(diag_stages):
        with diagnostic_cols[idx]:
            st.markdown(f"""
            <div class="acard" style="border-top:3px solid var(--{ds['col']});height:165px;text-align:center;margin-bottom:0.5rem;">
                <div style="font-weight:700;font-size:0.9rem;color:#FFF;">{ds['stage']}</div>
                <div style="font-size:0.75rem;color:var(--text3);margin-top:0.3rem;">{ds['gap']}</div>
                <div style="font-size:0.8rem;color:var(--pink);margin-top:0.5rem;font-weight:600;min-height:36px;"> {ds['signal']}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(ds['action'], key=f"btn_diag_action_{idx}", use_container_width=True):
                st.session_state["active_diag_action"] = ds
                st.rerun()

    if "active_diag_action" in st.session_state:
        action_ds = st.session_state["active_diag_action"]
        st.markdown(f"""
        <div style="background:rgba(138,180,248,0.06);border:1px solid var(--{action_ds['col']});border-radius:15px;padding:1.2rem;margin-top:1rem;margin-bottom:1rem;">
          <div style="font-family:Outfit,sans-serif;font-size:1.1rem;font-weight:800;color:#FFF;margin-bottom:0.6rem;">
             Active Action Guide: {action_ds['action']} ({action_ds['stage']})
          </div>
        </div>
        """, unsafe_allow_html=True)
        
        if action_ds["stage"].endswith("Discovery"):
            st.info("1. **Locate Grassroots Talent:** Head to **Tab 2 (Discovery & Leagues)** to identify states/districts with high tournament participation numbers.\n"
                    "2. **Export Scouting Plan:** Use the GTM Brief generator at the top of this page to export a structured **Scouting Plan** for Archery or Wrestling.\n"
                    "3. **Plan Screening:** Check **Tab 5 (Centres & Academies)** to find the nearest SAI NCOE to host the trials.")
        elif action_ds["stage"].endswith("Coaching"):
            st.info("1. **Run Reallocation Optimizer:** Scroll down and use the **Coach Deficit & Reallocation Optimizer** on **Tab 4** to identify and resolve load bottlenecks.\n"
                    "2. **Onboard Former Athletes:** Empanel elite candidates (like PR Sreejesh or Saina Nehwal) listed in the Former Athlete Registry.\n"
                    "3. **Schedule Masterclass:** Deploy a specialized NIS coach clinic using a **Coach Capacity Note** brief.")
        elif action_ds["stage"].endswith("Competition"):
            st.info("1. **Track Traditional & ASMITA Leagues:** Monitor the active competitions under the *Grassroots Leagues Tracker* in **Tab 2**.\n"
                    "2. **Map Infrastructure:** Review court and venue safety ratings in **Tab 5 (Centres & Academies)**.\n"
                    "3. **Validate Event Calendars:** Coordinate with State Associations tracked under **Tab 6 (Federation Intelligence)**.")
        elif action_ds["stage"].endswith("Funding"):
            st.info("1. **Align Corporate CSR:** Use the **Tab 7 (CSR Matchmaker)** to specify target budgets and demographics.\n"
                    "2. **Package Athlete Cohorts:** Package elite prospects in **Tab 9 (Athlete Cohorts)** into cohesive groups for corporate sponsorships.\n"
                    "3. **Download Pitch Deck:** Export the customized **Sponsor Brief** under the *Recommended Pathway Actions* on this tab.")
        elif action_ds["stage"].endswith("Progression"):
            st.info("1. **Run Athlete Proximity Matcher:** Use the **SAI Proximity & Suitability Matcher** at the top of the dashboard to align prospects to centres.\n"
                    "2. **Empanel at NCOEs:** Guide qualified national-level talent directly to residential training programs in **Tab 5**.\n"
                    "3. **Verify Compliance:** Audit athlete credentials and age certifications in **Tab 10 (Data Quality)**.")
            
        if st.button(" Close Action Guide", key="btn_close_diag_action"):
            del st.session_state["active_diag_action"]
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # 4. AthletIQ Opportunity Score Explainer
    st.markdown('<div class="stitle" style="font-size:1.15rem;margin-top:1.5rem;"> Medal Pathway Scoring Model</div>', unsafe_allow_html=True)
    o1, o2 = st.columns([1, 2])
    with o1:
        st.markdown("""
        <div class="acard" style="text-align:center;border-left:3px solid var(--teal);height:100%;">
            <div style="font-size:0.75rem;color:var(--text3);font-weight:700;letter-spacing:1.5px;text-transform:uppercase;">OPPORTUNITY SCORE</div>
            <div style="font-size:3.5rem;font-weight:900;color:var(--teal);font-family:Outfit,sans-serif;margin:0.4rem 0;">84<span style="font-size:1.5rem;color:var(--text2);">/100</span></div>
            <div style="font-size:0.75rem;color:var(--text2);margin-bottom:0.6rem;">Confidence: <span class="tag green">Medium-High</span></div>
            <div style="font-size:0.82rem;color:var(--blue);font-weight:700;border-top:1px solid rgba(255,255,255,0.06);padding-top:0.6rem;">
                 Action: Build Pilot Cohort
            </div>
        </div>
        """, unsafe_allow_html=True)
    with o2:
        st.markdown("""
        <div class="insight" style="height:100%;">
            <div class="insight-title" style="color:var(--blue);">What does the score represent?</div>
            <div class="insight-body" style="font-size:0.85rem;line-height:1.6;">
                Every sport, geography, and cohort gets a dynamic score compiled by AthletIQ's scoring engine. 
                Rather than generic statistics, it assesses:
                <ul>
                    <li><b>Talent Depth</b>: active grassroots counts (weight: 20%)</li>
                    <li><b>Medal Relevance</b>: Olympic/CWG potential (weight: 20%)</li>
                    <li><b>Demographic Impact</b>: female & rural representation (weight: 15%)</li>
                    <li><b>Infrastructure & Coach Availability</b>: nearby training centres (weight: 25%)</li>
                    <li><b>Execution Feasibility</b>: 90-day onboarding ease (weight: 20%)</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 5. Top Talent Clusters Preview
    st.markdown('<div class="stitle" style="font-size:1.15rem;margin-top:1.5rem;"> Top Regional Talent Clusters</div>', unsafe_allow_html=True)
    tc1, tc2, tc3 = st.columns(3)
    with tc1:
        st.markdown(insight(" Haryana Wrestling Cluster", "<b>12 Elite Prospects | 4 NCOEs | High CSR Appeal</b><br>State-level powerhouse with consistent podium results. High digital readiness. Best sponsor fit: BFSI / Mobility.", "green"), unsafe_allow_html=True)
    with tc2:
        st.markdown(insight(" Manipur & Assam Archery Precision", "<b>8 Elite Prospects | 2 Academy Partners | Tribal focus</b><br>Precision sports focus with natural grassroots talent depth. High CSR alignment for tribal development.", "purple"), unsafe_allow_html=True)
    with tc3:
        st.markdown(insight(" Punjab & Haryana Javelin Throw", "<b>6 Rising Talents | 2 NIS mentors | Coach gap identified</b><br>High medal appeal (Neeraj Chopra pipeline). Urgently needs certified coaching registry.", "amber"), unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 2 — TALENT DISCOVERY
# Purpose: Where talent is likely to emerge; who should be scouted.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab2:
    st.markdown('<div class="stitle"> Discovery & Leagues <span class="chip chip-purple">Grassroots & Emerging Athlete Prospects</span></div>', unsafe_allow_html=True)
    
    disc_tabs = st.tabs(["Grassroots Leagues Tracker", "Emerging Athlete Prospects"])
    
    with disc_tabs[0]:
        st.markdown(insight("ℹ Decentralized Leagues Tracker", 
            "Track local, district, state, and zonal tournaments mapping both Male & Female athletes. Inspired by the Khelo India and ASMITA frameworks.", "purple"), unsafe_allow_html=True)
        
        # League Stats KPIs
        l1, l2, l3, l4 = st.columns(4)
        with l1: st.markdown(mkpi("", "Total Leagues", "2,840+", "#10E5B3"), unsafe_allow_html=True)
        with l2: st.markdown(mkpi("", "Districts Mapped", "582", "#683DE4"), unsafe_allow_html=True)
        with l3: st.markdown(mkpi("", "Male Participants", "176,400+", "#10E5B3"), unsafe_allow_html=True)
        with l4: st.markdown(mkpi("", "Female Participants", "145,200+", "#F28B82"), unsafe_allow_html=True)
        
        # Participation Chart (Male vs Female)
        st.markdown('<div class="stitle" style="font-size:1rem;margin-top:1.5rem;"> Gender-Inclusive Participation across Core Sports</div>', unsafe_allow_html=True)
        participation_data = pd.DataFrame([
            {"Sport": "Wrestling", "Gender": "Male", "Participants": 35000},
            {"Sport": "Wrestling", "Gender": "Female", "Participants": 25000},
            {"Sport": "Boxing", "Gender": "Male", "Participants": 24000},
            {"Sport": "Boxing", "Gender": "Female", "Participants": 21000},
            {"Sport": "Archery", "Gender": "Male", "Participants": 13000},
            {"Sport": "Archery", "Gender": "Female", "Participants": 12000},
            {"Sport": "Hockey", "Gender": "Male", "Participants": 48000},
            {"Sport": "Hockey", "Gender": "Female", "Participants": 37000},
            {"Sport": "Athletics", "Gender": "Male", "Participants": 45000},
            {"Sport": "Athletics", "Gender": "Female", "Participants": 40000},
        ])
        fig_participation = px.bar(participation_data, x="Sport", y="Participants", color="Gender",
                                     barmode="group", color_discrete_map={"Male": "#10E5B3", "Female": "#683DE4"},
                                     labels={"Participants": "Total Mapped Participants", "Sport": ""})
        playout(fig_participation, "Decentralized Leagues Participation", h=350)
        st.plotly_chart(fig_participation, use_container_width=True)
        
        # Directory of Leagues
        st.markdown('<div class="stitle" style="font-size:1.15rem;margin-top:2rem;"> Active Grassroots Leagues & Tournaments</div>', unsafe_allow_html=True)
        
        # Load simulated live tournaments list
        live_data = get_live_tournaments()
        leagues_disp = pd.DataFrame(live_data)
        
        # Live Stats Dashboard Bar
        live_count = len(leagues_disp[leagues_disp["Live Status"] == "🔴 LIVE NOW"])
        soon_count = len(leagues_disp[leagues_disp["Live Status"] == "⏳ STARTING SOON"])
        st.markdown(f"""
        <div style="background:rgba(16, 229, 179, 0.08);border:1px solid rgba(16, 229, 179, 0.25);border-radius:12px;padding:0.8rem 1.2rem;margin-bottom:1rem;font-size:0.88rem;color:#FFF;display:flex;align-items:center;gap:1.5rem;">
          <span style="font-weight:700;color:var(--teal);">📡 LIVE STREAM SIGNAL:</span>
          <span><b>{live_count}</b> tournaments are actively <b>LIVE NOW</b></span>
          <span style="color:var(--text3);">|</span>
          <span><b>{soon_count}</b> matches starting in the next 10 minutes</span>
        </div>
        """, unsafe_allow_html=True)
        
        # Interactive filters
        fc1, fc2, fc3 = st.columns(3)
        with fc1:
            f_sport = st.selectbox("Filter by Sport Focus", ["All Core Sports"] + sorted(list(set(leagues_disp["Sport"]))), key="live_sport_select")
        with fc2:
            f_state = st.selectbox("Filter by State Hub", ["All Mapped States"] + sorted(list(set(leagues_disp["State"]))), key="live_state_select")
        with fc3:
            f_status = st.selectbox("Filter by Live Status", ["All Statuses", "🔴 LIVE NOW", "⏳ STARTING SOON", "⏳ SCHEDULED", "✅ COMPLETED / JUST COMPLETED"], key="live_status_select")
            
        # Apply filters
        filtered_leagues = leagues_disp.copy()
        if f_sport != "All Core Sports":
            filtered_leagues = filtered_leagues[filtered_leagues["Sport"] == f_sport]
        if f_state != "All Mapped States":
            filtered_leagues = filtered_leagues[filtered_leagues["State"] == f_state]
        if f_status != "All Statuses":
            if f_status == "✅ COMPLETED / JUST COMPLETED":
                filtered_leagues = filtered_leagues[filtered_leagues["Live Status"].str.contains("COMPLETED")]
            else:
                filtered_leagues = filtered_leagues[filtered_leagues["Live Status"] == f_status]
                
        # Render the high-fidelity live dataframe
        st.dataframe(filtered_leagues.reset_index(drop=True), use_container_width=True, height=350)
        
        # Export button
        dl_leagues = filtered_leagues.to_csv(index=False).encode("utf-8")
        st.download_button(" Download Leagues Directory (CSV)", dl_leagues, "grassroots_leagues.csv", "text/csv", use_container_width=True, key="btn_dl_leagues")
            
    with disc_tabs[1]:
        st.markdown(insight("ℹ Scouting Pipeline", 
            "Explore rising prospects mapped across India. Unlike 'Future Champions', we classify them as prospects "
            "by their current verified status and assign coach readiness indicators.", ""), unsafe_allow_html=True)
        
        # KPIs
        athletes_data = df_all[df_all["entity_type"]=="Athlete"].copy()
        a1, a2, a3, a4 = st.columns(4)
        with a1: st.markdown(mkpi("", "Total Prospects", str(len(athletes_data)), "#10E5B3"), unsafe_allow_html=True)
        with a2: st.markdown(mkpi("", "Female Prospects", str(len(athletes_data[athletes_data["gender"]=="Female"])), "#683DE4"), unsafe_allow_html=True)
        with a3: st.markdown(mkpi("", "Verified Profiles", str(len(athletes_data[athletes_data["digital_readiness"]>=7])), "#10E5B3"), unsafe_allow_html=True)
        with a4: st.markdown(mkpi("", "Needs Sponsor/Funding", str(len(athletes_data[athletes_data["funding_status"].str.lower()=="unfunded"])), "#F28B82"), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Table of prospects
        st.markdown('<div class="stitle" style="font-size:1rem;"> Active Prospects Directory</div>', unsafe_allow_html=True)
        
        # Format a cleaner display dataframe
        prospects_display = athletes_data.copy()
        prospects_display["coach_assigned"] = prospects_display["athletiq_opportunity_score"].apply(lambda x: "Yes (SAI Empanelled)" if x >= 7.5 else "No (Needs Assignment)")
        prospects_display["next_recommended_step"] = prospects_display["funding_status"].apply(lambda f: "Onboard corporate CSR" if "unfunded" in str(f).lower() else "Enroll in advanced regional trials")
        
        # Rename columns for clarity
        pd_table = prospects_display[["name", "sport", "state", "performance_level", "funding_status", "coach_assigned", "next_recommended_step"]].copy()
        pd_table.columns = ["Athlete Name", "Sport", "Home State", "Performance Level", "Funding Status", "Coach Assigned", "Next Recommended Step"]
        st.dataframe(pd_table.reset_index(drop=True), use_container_width=True, height=350)
        
        # Export button
        dl_prospects = pd_table.to_csv(index=False).encode("utf-8")
        st.download_button(" Download Prospects Scouting Plan (CSV)", dl_prospects, "scouting_pipeline.csv", "text/csv", use_container_width=True, key="btn_dl_prospects")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 3 — SPORT PRIORITY
# Purpose: Which sports AthletIQ should focus on and why.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab3:
    st.markdown('<div class="stitle"> Sport Priority Matrix <span class="chip chip-amber">Strategic Classification of Sports</span></div>', unsafe_allow_html=True)
    
    st.markdown(insight("ℹ Classification Matrix", 
        "AthletIQ maps sports into strategic classifications to guide sponsorships, CSR investments, and data tracking.", "green"), unsafe_allow_html=True)
        
    sport_category = st.radio("Choose Sport Category", 
                              [" Powerhouse Sports", " Women's Pathway Sports", " Precision / Data-Ready Sports", " Emerging Youth Sports", " Indigenous Sports"],
                              horizontal=True, key="sport_priority_radio")
                              
    st.markdown("<br>", unsafe_allow_html=True)
    
    if sport_category == " Powerhouse Sports":
        st.markdown(insight("Powerhouse Sports (Wrestling, Hockey, Athletics, Boxing)", 
            "<b>Strategic Intent:</b> Mass appeal, established depth, and historically high podium conversions. Focus on scale.", "green"), unsafe_allow_html=True)
        
        # Details
        st.markdown("""
        <div class="acard">
            <div class="acard-title"> Wrestling</div>
            <div class="acard-meta">
                <b>Why it matters:</b> Highest individual medal yield for India in recent Olympics.<br>
                <b>Where it is strong:</b> Haryana, Punjab, Delhi, Maharashtra (Kolhapur).<br>
                <b>The Gap:</b> Akhara infrastructure modernization, lack of sports science (physios, nutritionists) at local levels.<br>
                <b>AthletIQ Action:</b> Package Akhara cohorts for corporate sponsor name-rights.
            </div>
        </div>
        <div class="acard">
            <div class="acard-title"> Hockey</div>
            <div class="acard-meta">
                <b>Why it matters:</b> National sport with premium sponsor appeal (Tata, Odisha Govt).<br>
                <b>Where it is strong:</b> Odisha (Sundargarh), Punjab, Jharkhand, Haryana.<br>
                <b>The Gap:</b> Astroturf access in Tier-3 towns, youth academy coaching standardization.<br>
                <b>AthletIQ Action:</b> Digitize local school leagues on FitEvents OS for scouting.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    elif sport_category == " Women's Pathway Sports":
        st.markdown(insight("Women's Pathway Sports (Wrestling, Boxing, Judo, Taekwondo, Athletics, Weightlifting)", 
            "<b>Strategic Intent:</b> High capability CSR brand connection + high medal yield per athlete capital.", "purple"), unsafe_allow_html=True)
            
        st.markdown("""
        <div class="acard">
            <div class="acard-title"> Weightlifting</div>
            <div class="acard-meta">
                <b>Why it matters:</b> Mirabai Chanu pipeline. High medals/participants ratio.<br>
                <b>Where it is strong:</b> Manipur, Odisha, Andhra Pradesh.<br>
                <b>The Gap:</b> Grassroots barbells and safety equipment, lack of local female mentors.<br>
                <b>AthletIQ Action:</b> Launch the Manipur female weightlifting cohort sponsor brief.
            </div>
        </div>
        <div class="acard">
            <div class="acard-title"> Boxing</div>
            <div class="acard-meta">
                <b>Why it matters:</b> High international results (Nikhat Zareen, Lovlina Borgohain).<br>
                <b>Where it is strong:</b> Haryana, Assam, Manipur.<br>
                <b>The Gap:</b> Certified local female trainers, tournament travel sponsorships.<br>
                <b>AthletIQ Action:</b> Connect NBFC sponsors to boxing cohorts in Assam.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    elif sport_category == " Precision / Data-Ready Sports":
        st.markdown(insight("Precision & Data-Ready Sports (Archery, Shooting, Chess, Swimming)", 
            "<b>Strategic Intent:</b> Ideal for AI-assisted performance tracking, sensor integrations, and tech sponsorships.", "blue"), unsafe_allow_html=True)
            
        st.markdown("""
        <div class="acard">
            <div class="acard-title"> Archery</div>
            <div class="acard-meta">
                <b>Why it matters:</b> Strong junior pipeline. Measurable draw weight and release speed.<br>
                <b>Where it is strong:</b> Jharkhand, Manipur, Assam, Meghalaya.<br>
                <b>The Gap:</b> Import duties on archery bows, high cost of arrows for grassroots players.<br>
                <b>AthletIQ Action:</b> Build a precision data tracking dashboard for corporate tech sponsors.
            </div>
        </div>
        <div class="acard">
            <div class="acard-title"> Shooting</div>
            <div class="acard-meta">
                <b>Why it matters:</b> Manu Bhaker's double podium. Digital scoring makes it highly data-compatible.<br>
                <b>Where it is strong:</b> Haryana, Uttar Pradesh, Maharashtra.<br>
                <b>The Gap:</b> Range ammunition access and licensing bottleneck at local levels.<br>
                <b>AthletIQ Action:</b> Empower regional rifle clubs with FitEvents range-management modules.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    elif sport_category == " Emerging Youth Sports":
        st.markdown(insight("Emerging Youth Sports (Taekwondo, Wushu, Fencing, Judo)", 
            "<b>Strategic Intent:</b> Next-generation Olympic sports with massive growth potential and youth appeal.", "teal"), unsafe_allow_html=True)
            
        st.markdown("""
        <div class="acard">
            <div class="acard-title"> Fencing</div>
            <div class="acard-meta">
                <b>Why it matters:</b> Rapidly growing interest. High agility, perfect for early-age physical screening.<br>
                <b>Where it is strong:</b> Tamil Nadu, Manipur, Punjab.<br>
                <b>The Gap:</b> Extreme lack of localized coaches, high gear import costs.<br>
                <b>AthletIQ Action:</b> Launch fencing scouting camps in schools.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    elif sport_category == " Indigenous Sports":
        st.markdown(insight("Indigenous & Mass Participation Sports (Kho-Kho, Mallakhamb, Yogasana, Kabaddi)", 
            "<b>Strategic Intent:</b> Community activation, mass rural reach, and high-impact local storytelling for regional brands.", "gold"), unsafe_allow_html=True)
            
        st.markdown("""
        <div class="acard">
            <div class="acard-title"> Mallakhamb</div>
            <div class="acard-meta">
                <b>Why it matters:</b> Gymnastic foundation, extremely high physical literacy and coordination.<br>
                <b>Where it is strong:</b> Madhya Pradesh, Maharashtra, Gujarat.<br>
                <b>The Gap:</b> Lack of standardized safety landing mats, digital scoring framework.<br>
                <b>AthletIQ Action:</b> Package regional Mallakhamb displays for corporate rural CSR matches.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Opportunity Score chart by sport
    st.markdown("<br>", unsafe_allow_html=True)
    c_sp_1, c_sp_2 = st.columns(2)
    with c_sp_1:
        sport_summary = df_all.groupby("sport").agg(
            Count=("name","count"),
            Avg_Score=("athletiq_opportunity_score","mean"),
        ).sort_values("Avg_Score", ascending=False).reset_index()
        fig = px.bar(sport_summary, x="sport", y="Avg_Score",
                     color="Avg_Score", color_continuous_scale=COLOR_SCALES["teal"],
                     labels={"sport":"","Avg_Score":"Avg Opportunity Score"})
        playout(fig, "Opportunity Score by Sport (Grassroots Mapped)")
        st.plotly_chart(fig, use_container_width=True)
    with c_sp_2:
        fig2 = px.pie(sport_summary, values="Count", names="sport", hole=0.4,
                      color_discrete_sequence=px.colors.sequential.Teal)
        playout(fig2, "Sport Representation in Database", h=340)
        st.plotly_chart(fig2, use_container_width=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 4 — COACH CAPACITY
# Purpose: Where coaching is the bottleneck; former athlete-to-coach opportunities; masterclass needs.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab4:
    st.markdown('<div class="stitle"> Coach Capacity <span class="chip chip-purple">Empowerment & Capacity Gaps</span></div>', unsafe_allow_html=True)
    
    st.markdown(insight("ℹ The Bottleneck in Indian Sports", 
        "Athlete discovery fails without coaching depth. India lacks certified trainers in Tier-2/3 regions. "
        "AthletIQ maps coach availability and transitions former players into coaching roles.", "red"), unsafe_allow_html=True)
        
    c_coach_1, c_coach_2 = st.columns(2)
    
    with c_coach_1:
        st.markdown('<div class="stitle" style="font-size:1rem;"> Former-Athlete-to-Coach Registry</div>', unsafe_allow_html=True)
        st.markdown(insight(" Candidate: Vinesh Phogat (Wrestling)", "<b>Olympic finalist | Proposed: Head Coach, Haryana Women's Academy</b><br>Expertise in women's combat sports. Ready for empanelment. Next step: Secure corporate CSR sponsor for her masterclasses.", "purple"), unsafe_allow_html=True)
        st.markdown(insight(" Candidate: PR Sreejesh (Hockey Goalkeeping)", "<b>2x Olympic medallist | Proposed: Goalkeeping Director, Odisha NCOE</b><br>World-class goalkeeping mentor. Can head coach development programs for junior goalkeepers.", "green"), unsafe_allow_html=True)
        st.markdown(insight(" Candidate: Saina Nehwal (Badminton)", "<b>Olympic medallist | Proposed: Mentor, Badminton Academy, Hyderabad</b><br>Pioneer of women's singles. High capability candidate for masterclasses.", ""), unsafe_allow_html=True)
        
    with c_coach_2:
        st.markdown('<div class="stitle" style="font-size:1rem;"> Identified Capacity Bottlenecks</div>', unsafe_allow_html=True)
        st.markdown(insight(" Archery Coach Deficit (Jharkhand/Meghalaya)", "<b>Load Ratio: 45 athletes per coach (SAI standard: 15)</b><br>High risk of injury and progression stall. Action: Deploy NIS archery masterclass.", "red"), unsafe_allow_html=True)
        st.markdown(insight(" Weightlifting Barbell Safety Gap (Assam)", "<b>Load Ratio: 32 athletes per platform</b><br>High physical safety hazard. Action: Sponsor weightlifting platforms.", "amber"), unsafe_allow_html=True)
        st.markdown(insight(" Shooting Range Ammo Licensing (UP)", "<b>Lead time: 180 days for licensing trials</b><br>Limits high-frequency firing practice. Action: Connect federation lead.", ""), unsafe_allow_html=True)
        
    # Coaches Table
    st.markdown('<div class="stitle" style="font-size:1rem;"> Active Coaches Directory</div>', unsafe_allow_html=True)
    
    fco1, fco2 = st.columns(2)
    with fco1:
        f_coach_sport = st.selectbox("Filter Coaches by Sport", ["All Sports"] + sorted(list(df_all[df_all["entity_type"]=="Coach"]["sport"].unique())), key="coach_sport_filter")
    with fco2:
        f_coach_state = st.selectbox("Filter Coaches by State Registry", ["All States"] + sorted(list(df_all[df_all["entity_type"]=="Coach"]["state"].unique())), key="coach_state_filter")
        
    coaches_list = df_all[df_all["entity_type"]=="Coach"].copy()
    if f_coach_sport != "All Sports":
        coaches_list = coaches_list[coaches_list["sport"] == f_coach_sport]
    if f_coach_state != "All States":
        coaches_list = coaches_list[coaches_list["state"] == f_coach_state]
        
    if not coaches_list.empty:
        co_display = coaches_list[["name", "sport", "state", "performance_level", "digital_readiness", "notes"]].copy()
        co_display.columns = ["Coach Name", "Sport Focus", "State", "Licence Level", "Digital Readiness", "Specialization"]
        st.dataframe(co_display.reset_index(drop=True), use_container_width=True, height=250)
    else:
        st.info("No coaches match the selected sport/state filters.")

    # ── Coach Reallocation & Deficit Optimizer ──
    st.markdown('<div class="stitle" style="font-size:1.1rem;margin-top:1.5rem;"> Coach Deficit & Reallocation Optimizer</div>', unsafe_allow_html=True)
    st.markdown(insight(" Decision Engine: Dynamic Reallocation", 
        "This tool automatically scans SAI Centres, detects athlete-to-coach imbalances for a sport, "
        "and recommends a reallocation strategy from surplus centres to resolve the deficit based on capacities.", "purple"), unsafe_allow_html=True)
    
    # Select Sport
    all_sai_sports = sorted(list(set(sp for c in SAI_CENTRES for sp in c["sports"])))
    selected_opt_sport = st.selectbox("Select Sport to Optimize Load Ratios", all_sai_sports, index=all_sai_sports.index("Wrestling") if "Wrestling" in all_sai_sports else 0, key="opt_sport_select")
    
    # Gather capacity and coaches for each centre that supports this sport
    opt_data = []
    for c in SAI_CENTRES:
        if selected_opt_sport in c["sports"]:
            # Capacity for this sport
            cap = c.get("sports_capacity", {}).get(selected_opt_sport, c.get("capacity", 0) // len(c["sports"]))
            # Coaches for this sport
            coaches = c.get("sports_coaches", {}).get(selected_opt_sport, c.get("coaches", 0) // len(c["sports"]))
            if cap > 0:
                opt_data.append({
                    "name": c["name"],
                    "state": c["state"],
                    "capacity": cap,
                    "coaches": coaches,
                    "ratio": cap / coaches if coaches > 0 else float('inf')
                })
    
    if opt_data:
        df_opt = pd.DataFrame(opt_data)
        
        # Calculate Target Ratio
        total_athletes = df_opt["capacity"].sum()
        total_coaches = df_opt["coaches"].sum()
        target_ratio = 15.0 # Standard SAI Athlete-to-Coach ratio target
        
        # Calculate Deficits & Surpluses
        deficits = []
        surpluses = []
        
        for idx, row in df_opt.iterrows():
            # Desired coaches to meet the target ratio
            desired = max(1, int(round(row["capacity"] / target_ratio)))
            diff = desired - row["coaches"]
            
            if diff > 0:
                deficits.append({
                    "name": row["name"],
                    "state": row["state"],
                    "capacity": row["capacity"],
                    "current_coaches": row["coaches"],
                    "current_ratio": row["ratio"],
                    "needed": diff
                })
            elif diff < 0 and row["coaches"] > 1:
                surpluses.append({
                    "name": row["name"],
                    "state": row["state"],
                    "capacity": row["capacity"],
                    "current_coaches": row["coaches"],
                    "current_ratio": row["ratio"],
                    "surplus": abs(diff)
                })
        
        # Render current state metrics
        c_m1, c_m2, c_m3 = st.columns(3)
        with c_m1:
            st.metric("Total Sanctioned Athletes", f"{int(total_athletes)}")
        with c_m2:
            st.metric("Total Active Coaches", f"{int(total_coaches)}")
        with c_m3:
            st.metric("Global Ratio", f"{total_athletes/total_coaches:.1f} athletes/coach" if total_coaches > 0 else "N/A")
            
        # Display Imbalance Table
        st.markdown("##### Current Athlete-Coach Imbalance Directory")
        df_opt_disp = df_opt.copy()
        df_opt_disp.columns = ["Centre Name", "State", "Athlete Capacity", "Active Coaches", "Load Ratio"]
        df_opt_disp["Load Ratio"] = df_opt_disp["Load Ratio"].apply(lambda x: " Infinite (0 Coaches)" if x == float('inf') else f"{x:.1f}:1")
        st.dataframe(df_opt_disp.reset_index(drop=True), use_container_width=True, height=200)
        
        # Transfer matching
        transfers = []
        surpluses_sorted = sorted(surpluses, key=lambda x: x["surplus"], reverse=True)
        deficits_sorted = sorted(deficits, key=lambda x: x["needed"], reverse=True)
        
        s_idx, d_idx = 0, 0
        while s_idx < len(surpluses_sorted) and d_idx < len(deficits_sorted):
            s = surpluses_sorted[s_idx]
            d = deficits_sorted[d_idx]
            
            transfer_qty = min(s["surplus"], d["needed"])
            if transfer_qty > 0:
                transfers.append({
                    "from": s["name"],
                    "to": d["name"],
                    "qty": transfer_qty,
                    "reason": f"Reduces source ratio from {s['current_ratio']:.1f} to {s['capacity']/(s['current_coaches']-transfer_qty):.1f}, and fixes target ratio from {d['current_ratio'] if d['current_ratio']!=float('inf') else '0 coaches'} to {d['capacity']/(d['current_coaches']+transfer_qty):.1f}"
                })
                s["surplus"] -= transfer_qty
                d["needed"] -= transfer_qty
                
            if s["surplus"] == 0:
                s_idx += 1
            if d["needed"] == 0:
                d_idx += 1
                
        # Render Recommendations
        st.markdown("##### Recommended Reallocation Strategy Decisions")
        if transfers:
            for t in transfers:
                st.markdown(insight(
                    f" Transfer Decision: Move {int(t['qty'])} coach(es)", 
                    f" <b>From:</b> {t['from']}<br> <b>To:</b> {t['to']}<br> <b>Impact:</b> {t['reason']}", 
                    "green"
                ), unsafe_allow_html=True)
        else:
            st.success(" Coach loading ratios are balanced! No reallocation transfer is required for this sport.")
    else:
        st.info("No SAI Centres currently support or have capacity for the selected sport.")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 5 — CENTRES & ACADEMIES
# Purpose: SAI, private academies, schools, akharas, clubs, venues.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab5:
    st.markdown('<div class="stitle"> Centres & Academies <span class="chip chip-blue">Ecosystem Directory</span></div>', unsafe_allow_html=True)
    
    st.markdown(insight("ℹ What is this?", 
        "AthletIQ maps government training centres (SAI), private academies, and local wrestling akharas/boxing clubs "
        "to help sponsors invest in infrastructure name-rights, safety gear, and coaching scholarships.", ""), unsafe_allow_html=True)
        
    sub_centre_tabs = st.tabs(["SAI Centres & NCOEs", "Football Academies Directory", "Private Academies", "Akharas & Clubs", "Partner Network"])
    
    with sub_centre_tabs[0]:
        st.markdown('<div class="stitle" style="font-size:1rem;"> Sports Authority of India Training Network</div>', unsafe_allow_html=True)
        
        # Interactive Matcher Linkage
        st.markdown("""
        <div style="background:rgba(138,180,248,0.06);border:1px solid rgba(138,180,248,0.18);border-radius:15px;padding:1.2rem;margin-bottom:1rem;">
          <b> Smart SAI Matcher Ready:</b> Head over to the <b>Athlete Cohorts</b> tab, 
          select any athlete, and click "Match SAI Centre" to instantly score the recommended NCOEs here.
        </div>
        """, unsafe_allow_html=True)
        
        # Directory Table
        sai_df_disp = sai_df[["name", "city", "state", "type", "region", "capacity", "coaches", "facilities"]].copy()
        sai_df_disp.columns = ["Centre Name", "City", "State", "Type", "Region", "Capacity", "Coaches", "Facilities"]
        st.dataframe(sai_df_disp.reset_index(drop=True), use_container_width=True, height=280)
        
    with sub_centre_tabs[1]:
        st.markdown('<div class="stitle" style="font-size:1rem;"> AIFF Accredited Football Academies</div>', unsafe_allow_html=True)
        fb_acads = df_all[(df_all["entity_type"] == "Academy") & (df_all["sport"] == "Football")].copy()
        if not fb_acads.empty:
            def parse_acad_note(note_str, key):
                if not isinstance(note_str, str):
                    return ""
                parts = [p.strip() for p in note_str.split("|")]
                for p in parts:
                    if p.startswith(key + ":"):
                        return p.split(":", 1)[1].strip()
                return ""
            
            fb_acads["Age Groups Mapped"] = fb_acads["notes"].apply(lambda n: parse_acad_note(n, "Age Groups"))
            fb_acads["Leagues / Competitions"] = fb_acads["notes"].apply(lambda n: parse_acad_note(n, "Competitions"))
            fb_acads["Medical Facilities"] = fb_acads["notes"].apply(lambda n: parse_acad_note(n, "Medical"))
            
            fb_acads_disp = fb_acads[["name", "city", "state", "Age Groups Mapped", "Leagues / Competitions", "Medical Facilities"]].copy()
            fb_acads_disp.columns = ["Academy Name", "City", "State", "Age Groups Mapped", "Leagues & Tournaments", "Medical & Safety Provisions"]
            st.dataframe(fb_acads_disp.reset_index(drop=True), use_container_width=True, height=320)
            
            # Download button
            dl_fb_acads = fb_acads_disp.to_csv(index=False).encode("utf-8")
            st.download_button(" Download Football Academies Directory (CSV)", dl_fb_acads, "football_academies.csv", "text/csv", use_container_width=True, key="btn_dl_fb_acads")
        else:
            st.warning("No Football Academies found in the database.")
            
    with sub_centre_tabs[2]:
        st.markdown('<div class="stitle" style="font-size:1rem;"> Top Private Sports Academies</div>', unsafe_allow_html=True)
        private_acads = [
            {"name": "JSW Inspire Institute of Sport (IIS)", "location": "Vijayanagar, Karnataka", "sports": "Boxing · Wrestling · Athletics", "capacity": "150 athletes", "focus": "Elite performance training"},
            {"name": "Tata Archery Academy", "location": "Jamshedpur, Jharkhand", "sports": "Archery", "capacity": "40 athletes", "focus": "Precision archery pipelines"},
            {"name": "Pullela Gopichand Badminton Academy", "location": "Hyderabad, Telangana", "sports": "Badminton", "capacity": "120 athletes", "focus": "World-class badminton coaching"},
            {"name": "Prakash Padukone Badminton Academy", "location": "Bengaluru, Karnataka", "sports": "Badminton", "capacity": "60 athletes", "focus": "Junior talent development"},
            {"name": "Mary Kom Boxing Foundation", "location": "Imphal, Manipur", "sports": "Boxing", "capacity": "50 athletes", "focus": "Northeast women boxing"}
        ]
        for pa in private_acads:
            st.markdown(f"""
            <div class="acard" style="border-left:3px solid var(--teal);margin-bottom:0.6rem;">
                <div class="acard-title">{pa['name']}</div>
                <div class="acard-meta">
                     {pa['location']} &nbsp;|&nbsp; <b>Sports:</b> {pa['sports']} &nbsp;|&nbsp; <b>Capacity:</b> {pa['capacity']}<br>
                     <b>Strategic Focus:</b> {pa['focus']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
    with sub_centre_tabs[3]:
        st.markdown('<div class="stitle" style="font-size:1rem;"> Akharas & Regional Boxing Clubs</div>', unsafe_allow_html=True)
        akharas = [
            {"name": "Chhatrasal Akhara", "location": "Delhi", "sport": "Wrestling", "mentors": "Sushil Kumar, Ravi Dahiya, Aman Sehrawat", "status": "Podium breeding ground"},
            {"name": "Guru Hanuman Akhara", "location": "Delhi", "sport": "Wrestling", "mentors": "Legendary historic coaching foundation", "status": "Grassroots wrestling"},
            {"name": "Bhiwani Boxing Club (BBC)", "location": "Bhiwani, Haryana", "sport": "Boxing", "mentors": "Vijender Singh pipeline", "status": "Rural boxing hub"}
        ]
        for ak in akharas:
            st.markdown(f"""
            <div class="acard" style="border-left:3px solid var(--purple);margin-bottom:0.6rem;">
                <div class="acard-title"> {ak['name']} ({ak['sport']})</div>
                <div class="acard-meta">
                     {ak['location']} &nbsp;|&nbsp; <b>Mentors:</b> {ak['mentors']}<br>
                     <b>Ecosystem Role:</b> {ak['status']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
    with sub_centre_tabs[4]:
        st.markdown('<div class="stitle" style="font-size:1rem;"> Partner Network (Schools & Venues)</div>', unsafe_allow_html=True)
        st.markdown(insight(" Schools & Clubs Integration", 
            "AthletIQ partners with 50+ regional schools and state venues to host scouting trials. "
            "Sponsors can brand these venues or sponsor inter-school tournaments directly on FitEvents OS.", "green"), unsafe_allow_html=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 6 — FEDERATION INTELLIGENCE
# Purpose: NSF governance, office bearers, status, credibility, engagement opportunity.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab6:
    st.markdown('<div class="stitle"> Federation Intelligence <span class="chip chip-purple">NSF Governance & Engagement Opportunities</span></div>', unsafe_allow_html=True)
    
    st.markdown(insight("ℹ Why Federations Matter", 
        "Athletes, sponsors, and policymakers need absolute clarity on who governs what. "
        "We track NSF governance status, credibility scores, and joint trial empanelment opportunities.", ""), unsafe_allow_html=True)
        
    federations = [
        {"nsf": "AFI (Athletics Federation of India)", "sport": "Athletics", "president": "Adille Sumariwalla", "status": "Active", "score": 9, "col": "green", "opp": "Integrate FitEvents OS for state championship registrations"},
        {"nsf": "NRAI (National Rifle Association of India)", "sport": "Shooting", "president": "Kalikesh Singh Deo", "status": "Active", "score": 8, "col": "green", "opp": "Digitize NRAI junior trials and range score entries"},
        {"nsf": "WFI (Wrestling Federation of India)", "sport": "Wrestling", "president": "Sanjay Singh (Ad-hoc committee)", "status": "Under IOA Ad-hoc Monitor", "score": 4, "col": "red", "opp": "Coordinate talent discovery directly with state bodies"},
        {"nsf": "BAI (Badminton Association of India)", "sport": "Badminton", "president": "Himanta Biswa Sarma", "status": "Active", "score": 8, "col": "green", "opp": "Sponsor ranking tournaments for junior singles"},
        {"nsf": "BFI (Boxing Federation of India)", "sport": "Boxing", "president": "Ajay Singh", "status": "Active", "score": 7, "col": "amber", "opp": "Support local boxing sub-centres with headgears"},
        {"nsf": "AAI (Archery Association of India)", "sport": "Archery", "president": "Arjun Munda", "status": "Active", "score": 7, "col": "amber", "opp": "Partner for tribal archery screening drives"}
    ]
    
    for fed in federations:
        st.markdown(f"""
        <div class="acard" style="border-left:3px solid var(--{fed['col']});margin-bottom:0.7rem;">
            <div class="acard-top">
                <div class="acard-title">{fed['nsf']}</div>
                <div class="acard-score" style="color:var(--{fed['col']});">{fed['score']}/10</div>
            </div>
            <div class="acard-meta">
                 <b>President:</b> {fed['president']} &nbsp;|&nbsp; <b>Status:</b> {fed['status']}<br>
                 <b>AthletIQ Opportunity:</b> {fed['opp']}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Export button for federation brief
        st.download_button(f" Export Federation Credibility Brief ({fed['sport']})", 
                           data=generate_gtm_document("Validation Checklist", fed['nsf'], fed['sport'], "Delhi", fed['opp']),
                           file_name=f"{fed['sport'].lower()}_federation_brief.md",
                           key=f"btn_fed_{fed['sport']}")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 7 — CSR MATCHMAKER
# Purpose: Match brand/CSR mandate to sport/geography/demographic pathway.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab7:
    st.markdown('<div class="stitle"> CSR Matchmaker <span class="chip chip-green">Corporate CSR Mandate Alignment</span></div>', unsafe_allow_html=True)
    
    st.markdown(insight("ℹ Match Corporate Mandate to Sport Geographies", 
        "Corporates seek direct storytelling and compliance. AthletIQ aligns corporate CSR sport spends "
        "with demographics, target sports, and regional talent pipelines.", "green"), unsafe_allow_html=True)
        
    m1, m2 = st.columns([1, 2])
    with m1:
        st.markdown('<div class="stitle" style="font-size:1rem;"> Matcher Controls</div>', unsafe_allow_html=True)
        csr_budget = st.slider("Target CSR Budget (₹ Lakhs)", 10, 500, 50, step=10, key="csr_budget_slider")
        csr_demo = st.selectbox("Demographic Focus", ["Women Empowerment", "Rural Youth", "Tribal Development", "All"], key="csr_demo_select")
        
    with m2:
        st.markdown('<div class="stitle" style="font-size:1rem;">Recommended CSR Fits</div>', unsafe_allow_html=True)
        
        # Filtering logic
        fits = []
        if csr_demo in ["Women Empowerment", "All"]:
            fits.append({
                "company": "JSW Foundation",
                "sport": "Wrestling & Boxing (Women's Combat Sports Cohort)",
                "state": "Haryana / Manipur",
                "fit": "95%",
                "desc": "High storytelling value. Funding local coaches and training equipment. Best sponsor category: Steel / Heavy Industry.",
                "story": "Empowering young girls from rural Haryana to win international boxing championships."
            })
        if csr_demo in ["Rural Youth", "All"]:
            fits.append({
                "company": "Tata Steel CSR",
                "sport": "Archery Precision Pathway",
                "state": "Jharkhand (Jamshedpur)",
                "fit": "92%",
                "desc": "Funding archery equipment, bows, and arrows. Fits tribal development mandate. Best sponsor category: Metals & Mining.",
                "story": "Providing modern carbon bows to tribal archers to match global targets."
            })
        if csr_demo in ["Tribal Development", "All"] or not fits:
            fits.append({
                "company": "REC Limited (CSR)",
                "sport": "Grassroots Weightlifting & Athletics",
                "state": "Odisha & Manipur",
                "fit": "88%",
                "desc": "Supports setup of local mini-gyms and weightlifting platforms. Best sponsor category: Power / Infrastructure.",
                "story": "Providing safety lifting belts and weights to youth lifting camps in Manipur."
            })
            
        for f in fits:
            st.markdown(f"""
            <div class="acard" style="border-left:3px solid var(--teal);margin-bottom:0.7rem;">
                <div class="acard-top">
                    <div class="acard-title"> {f['company']}</div>
                    <div class="acard-score" style="color:var(--teal);">{f['fit']} Match</div>
                </div>
                <div class="acard-meta">
                     <b>Sport Pathway:</b> {f['sport']}<br>
                     <b>Geography:</b> {f['state']}<br>
                     <b>CSR Focus:</b> {f['desc']}<br>
                     <b>Storytelling Theme:</b> <i>"{f['story']}"</i>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Export CSR brief
            st.download_button(f" Download CSR Pitch Package ({f['company']})", 
                               data=generate_gtm_document("CSR One-Pager", f['company'], f['sport'], f['state'], f['story']),
                               file_name=f"{f['company'].lower().replace(' ', '_')}_pitch_pack.md",
                               key=f"btn_csr_{f['company'].replace(' ', '')}")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 8 — SPONSOR PIPELINE
# Purpose: Commercial prospects.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab8:
    st.markdown('<div class="stitle"> Sponsor Pipeline <span class="chip chip-amber">Commercial Prospects & Packages</span></div>', unsafe_allow_html=True)
    
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
with tab9:
    st.markdown('<div class="stitle"> Athlete Cohorts <span class="chip chip-blue">Packaged Groups for Funding</span></div>', unsafe_allow_html=True)
    
    st.markdown(insight("ℹ Pathway Cohorts Packaging", 
        "Corporates and sponsors prefer funding cohesive groups/cohorts with measurable impact. "
        "Below are priority athlete cohorts ready for pathway activation. Use the filters to check individual prospects "
        "and link them directly to the SAI Centre Matcher.", "green"), unsafe_allow_html=True)
        
    cohort_tabs = st.tabs(["Combat Sports Cohort", "NE Precision Archery", "Weightlifting Power", "Search Individual Profiles"])
    
    with cohort_tabs[0]:
        st.markdown('<div class="stitle" style="font-size:1rem;"> Combat Sports Cohort (Wrestling & Boxing - Men & Women)</div>', unsafe_allow_html=True)
        st.markdown(insight(" Target Sponsor Fit: NBFC / BFSI / FMCG / Mobility", 
            "<b>Impact Metrics:</b> 8 wrestlers & boxers (Male & Female) assessed · 2 regional akharas supported · 3 travel sponsorships.<br>"
            "<b>Annual Funding Target:</b> ₹24 Lakhs total package", "purple"), unsafe_allow_html=True)
            
        combat_athletes = [a for a in elite_athletes if a["sport"] in ["WRESTLING", "BOXING"]][:6]
        cols = st.columns(3)
        for idx, ca in enumerate(combat_athletes):
            with cols[idx % 3]:
                g_tag = "" if ca["gender"] == "F" else ""
                st.markdown(f"""
                <div class="acard" style="border-top:3px solid var(--purple);height:170px;">
                    <div class="acard-title">{g_tag} {ca['name']} ({ca['sport']})</div>
                    <div class="acard-meta" style="margin-top:0.4rem;">
                        <b>Category:</b> {ca['category']} &nbsp;|&nbsp; Age {ca['age']}<br>
                         Medals: {ca['medals'][:50]}...
                    </div>
                </div>
                """, unsafe_allow_html=True)
        st.download_button(" Download Combat Sports Sponsor Pitch Brief", 
                           data=generate_gtm_document("Sponsor Brief", "Combat Sports Cohort", "Wrestling & Boxing", "Haryana/Assam", "Empower 8 athletes (Male & Female)"),
                           file_name="combat_cohort_pitch.md", key="btn_gtm_combat_cohort")
                           
    with cohort_tabs[1]:
        st.markdown('<div class="stitle" style="font-size:1rem;"> Northeast Precision Archery Cohort</div>', unsafe_allow_html=True)
        st.markdown(insight(" Target Sponsor Fit: Heavy Industry / Public Sector / Tech", 
            "<b>Impact Metrics:</b> 6 tribal archers provided modern bows · digital draw-weight logs on FitEvents OS.<br>"
            "<b>Annual Funding Target:</b> ₹18 Lakhs total package", "blue"), unsafe_allow_html=True)
            
        archery_athletes = [a for a in elite_athletes if a["sport"] == "ARCHERY"][:6]
        cols = st.columns(3)
        for idx, aa in enumerate(archery_athletes):
            with cols[idx % 3]:
                st.markdown(f"""
                <div class="acard" style="border-top:3px solid var(--blue);height:170px;">
                    <div class="acard-title">{aa['name']}</div>
                    <div class="acard-meta" style="margin-top:0.4rem;">
                        <b>Event:</b> {aa['category']} &nbsp;|&nbsp; Age {aa['age']}<br>
                         Medals: {aa['medals'][:50]}...
                    </div>
                </div>
                """, unsafe_allow_html=True)
        st.download_button(" Download NE Archery Sponsor Pitch Brief", 
                           data=generate_gtm_document("Sponsor Brief", "NE Archery Cohort", "Archery", "Manipur/Assam", "Modern bows for 6 tribal archers"),
                           file_name="archery_cohort_pitch.md", key="btn_gtm_archery_cohort")
                           
    with cohort_tabs[2]:
        st.markdown('<div class="stitle" style="font-size:1rem;"> Weightlifting Power Cohort</div>', unsafe_allow_html=True)
        st.markdown(insight(" Target Sponsor Fit: Infrastructure / Logistics / Power", 
            "<b>Impact Metrics:</b> 5 female lifters provided standard barbell kits · 1 NIS coach clinic supported.<br>"
            "<b>Annual Funding Target:</b> ₹15 Lakhs total package", "gold"), unsafe_allow_html=True)
            
        lifting_athletes = [a for a in elite_athletes if a["sport"] == "WEIGHTLIFTING"][:6]
        cols = st.columns(3)
        for idx, la in enumerate(lifting_athletes):
            with cols[idx % 3]:
                st.markdown(f"""
                <div class="acard" style="border-top:3px solid var(--gold);height:170px;">
                    <div class="acard-title">{la['name']}</div>
                    <div class="acard-meta" style="margin-top:0.4rem;">
                        <b>Weight:</b> {la['category']} &nbsp;|&nbsp; Age {la['age']}<br>
                         Medals: {la['medals'][:50]}...
                    </div>
                </div>
                """, unsafe_allow_html=True)
        st.download_button(" Download Weightlifting Sponsor Pitch Brief", 
                           data=generate_gtm_document("Sponsor Brief", "Weightlifting Power Cohort", "Weightlifting", "Manipur/Odisha", "Standard barbells for 5 female lifters"),
                           file_name="lifting_cohort_pitch.md", key="btn_gtm_lifting_cohort")
                           
    with cohort_tabs[3]:
        st.markdown('<div class="stitle" style="font-size:1rem;"> Search Individual Athlete & Coach Profiles</div>', unsafe_allow_html=True)
        
        # Search controls
        c_sc1, c_sc2, c_sc3 = st.columns([2, 1, 1])
        with c_sc1:
            ind_search = st.text_input(" Search Profile Name", placeholder="e.g. Manu Bhaker, Neeraj Chopra", key="ind_profile_search")
        with c_sc2:
            ind_sport = st.selectbox("Sport Filter", ["All"] + sorted(list(set(a["sport"] for a in elite_athletes))), key="ind_sport_select")
        with c_sc3:
            ind_gender = st.selectbox("Gender", ["All", "M", "F"], key="ind_gender_select")

        # Custom Athlete Matcher Form
        with st.expander(" Or Run Matcher for a Custom Athlete Profile (Create & Assess Athlete)", expanded=False):
            st.markdown("##### Custom Athlete Attributes")
            c_csa1, c_csa2 = st.columns(2)
            with c_csa1:
                c_name = st.text_input("Athlete Name", value="Custom Athlete Profile", key="c_ath_name")
                all_sai_disciplines = sorted(list(set(sp for c in SAI_CENTRES for sp in c["sports"])))
                c_sport = st.selectbox("Sport Discipline", all_sai_disciplines, index=all_sai_disciplines.index("Wrestling") if "Wrestling" in all_sai_disciplines else 0, key="c_ath_sport")
                all_sai_states = sorted(list(set(c["state"] for c in SAI_CENTRES)))
                c_state = st.selectbox("Home State", all_sai_states, index=all_sai_states.index("Haryana") if "Haryana" in all_sai_states else 0, key="c_ath_state")
            with c_csa2:
                c_age = st.slider("Age (Years)", 8, 35, 17, key="c_ath_age")
                c_gender = st.selectbox("Gender", ["Male", "Female"], key="c_ath_gender")
                c_perf = st.selectbox("Current Performance Level", ["District", "State", "National", "International"], key="c_ath_perf")
            
            if st.button(" Calculate Optimal Training Centre", use_container_width=True, key="btn_run_custom_match"):
                custom_ath_mock = {
                    "name": c_name,
                    "sport": c_sport.upper(),
                    "age": str(c_age),
                    "gender": "F" if c_gender == "Female" else "M",
                    "medals": f"{c_perf} Level Competitor",
                    "records": f"Custom entered athlete from state of {c_state} competing in {c_sport}."
                }
                st.session_state["matched_athlete"] = custom_ath_mock
                st.session_state["custom_matched_state"] = c_state
                st.session_state["custom_matched_perf"] = c_perf
                st.rerun()
            
        filtered_ind = []
        for a in elite_athletes:
            if ind_search.strip() and ind_search.lower() not in a["name"].lower():
                continue
            if ind_sport != "All" and a["sport"] != ind_sport:
                continue
            if ind_gender != "All" and a["gender"] != ind_gender:
                continue
            filtered_ind.append(a)
            
        if not filtered_ind:
            st.info("No profiles match the filter criteria.")
        else:
            cols = st.columns(3)
            for idx, a in enumerate(filtered_ind[:30]):
                col = cols[idx % 3]
                with col:
                    medals_clean = a["medals"].replace("", " ").replace("", " ").replace("", " ")
                    tags_list = [tag(a["sport"], "purple"), tag(a["gender"], "")]
                    if a["age"].isdigit():
                        tags_list.append(tag(f"Age {a['age']}", "blue"))
                    tags_html = " ".join(tags_list)
                    
                    st.markdown(f"""
                    <div class="acard" style="border-top:3px solid var(--blue);height:360px;display:flex;flex-direction:column;justify-content:between;margin-bottom:1rem;">
                      <div>
                        <div class="acard-top">
                          <div class="acard-title" style="font-size:1.1rem;color:#FFF;font-family:Outfit,sans-serif;">{a['name']}</div>
                          <div style="font-size:0.75rem;color:var(--text2);font-weight:700;">#{a['id']}</div>
                        </div>
                        <div class="acard-meta" style="margin-top: 0.2rem; min-height:40px;">
                          <b>Event/Category:</b> {a['category']}<br>
                          <b>Gender:</b> {a['gender']} &nbsp;|&nbsp; <b>Age:</b> {a['age']}
                        </div>
                        <div style="margin-top: 0.5rem; font-size: 0.8rem; line-height: 1.4; color: #E8EAED; min-height:50px;">
                           <b>Key Medals:</b> {medals_clean}
                        </div>
                        <div style="margin-top: 0.5rem; font-size: 0.8rem; line-height: 1.4; color: var(--text2); background:rgba(255,255,255,0.02); padding:0.5rem; border-radius:8px; border:1px solid rgba(255,255,255,0.04); min-height:70px; max-height:100px; overflow-y:auto;">
                           <b>Records & Tally:</b> {a['records']}
                        </div>
                      </div>
                      <div>
                        <div class="acard-tags" style="margin-top: 0.6rem; justify-content: flex-start; margin-bottom:0.5rem;">
                          {tags_html}
                        </div>
                      </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button(" Match SAI Centre", key=f"btn_cohort_match_{a['sport']}_{a['id']}_{a['name']}", use_container_width=True):
                        st.session_state["matched_athlete"] = a
                        st.rerun()
                        
            if "matched_athlete" in st.session_state:
                m_ath = st.session_state["matched_athlete"]
                m_gender = "Female" if m_ath["gender"] == "F" else "Male"
                try: m_age = int(m_ath["age"])
                except ValueError: m_age = 17
                
                if "custom_matched_state" in st.session_state:
                    m_state = st.session_state["custom_matched_state"]
                    m_perf = st.session_state["custom_matched_perf"]
                else:
                    m_perf = "International" if any(x in m_ath["medals"].lower() for x in ["olympic", "world", "asian", "cwg", "issf", "international"]) else "National"
                    m_state = "Haryana"
                    state_keywords = {
                        "haryana": "Haryana", "punjab": "Punjab", "delhi": "Delhi", "manipur": "Manipur",
                        "maharashtra": "Maharashtra", "kerala": "Kerala", "tamil nadu": "Tamil Nadu",
                        "odisha": "Odisha", "uttar pradesh": "Uttar Pradesh", "madhya pradesh": "Madhya Pradesh",
                        "assam": "Assam", "telangana": "Telangana", "andhra": "Andhra Pradesh",
                        "west bengal": "West Bengal", "rajasthan": "Rajasthan", "gujarat": "Gujarat",
                        "jharkhand": "Jharkhand"
                    }
                    for kw, st_name in state_keywords.items():
                        if kw in m_ath["records"].lower() or kw in m_ath["medals"].lower():
                            m_state = st_name
                            break
                
                recs = recommend_sai_centres(m_ath["sport"].title(), m_state, m_perf, m_age, m_gender, top_n=3)
                st.markdown(f"""
                <div style="background:rgba(138,180,248,0.1);border:1px solid rgba(138,180,248,0.3);border-radius:15px;padding:1.2rem;margin-top:1.5rem;margin-bottom:1rem;">
                  <div style="font-family:Outfit,sans-serif;font-size:1.15rem;font-weight:800;color:#FFF;">
                     Recommended SAI Centres for {m_ath['name']}
                  </div>
                  <div style="font-size:0.82rem;color:#9AA0A6;margin-top:0.2rem;">
                    Profile: {m_ath['sport']} | {m_state} | Age {m_ath['age']} | Level: {m_perf}
                  </div>
                </div>
                """, unsafe_allow_html=True)
                for idx, rec in enumerate(recs):
                    st.markdown(render_sai_card(rec["centre"], rec["score"], idx+1), unsafe_allow_html=True)
                if st.button(" Close Matcher Panel", key="close_cohort_matcher"):
                    del st.session_state["matched_athlete"]
                    if "custom_matched_state" in st.session_state:
                        del st.session_state["custom_matched_state"]
                        del st.session_state["custom_matched_perf"]
                    st.rerun()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 10 — DATA QUALITY
# Purpose: Data Quality & Confidence internal validation layer.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab10:
    st.markdown('<div class="stitle"> Data Quality & Confidence <span class="chip chip-red">Internal Validation Layer</span></div>', unsafe_allow_html=True)
    
    st.markdown(insight("ℹ Internal Data Verification", 
        "This tab serves as AthletIQ's internal validation layer to track data completeness, "
        "verify official records, and list validation checklists before pitching to sponsors.", "red"), unsafe_allow_html=True)
        
    c_dq1, c_dq2 = st.columns(2)
    with c_dq1:
        st.markdown('<div class="stitle" style="font-size:1rem;"> Data Completeness Index</div>', unsafe_allow_html=True)
        total = len(df_all)
        has_src = df_all["has_source"].sum()
        has_notes_ = df_all["has_notes"].sum()
        
        st.markdown(f"""
        <div class="acard">
            <b>Source Links Coverage</b> ({has_src}/{total})
            <div class="dq-bar-wrap"><div class="dq-bar" style="width:{has_src/total*100}%;background:var(--teal);"></div></div>
            <br>
            <b>Performance Notes Completeness</b> ({has_notes_}/{total})
            <div class="dq-bar-wrap"><div class="dq-bar" style="width:{has_notes_/total*100}%;background:var(--blue);"></div></div>
        </div>
        """, unsafe_allow_html=True)
        
    with c_dq2:
        st.markdown('<div class="stitle" style="font-size:1rem;"> Internal GTM Validation Checklist</div>', unsafe_allow_html=True)
        st.markdown("""
        - [x] <b>Verify NIS coach certifications</b>: completed for all 30 coaches.
        - [x] <b>Cross-check NRAI trial records</b>: verified for Shooting profiles.
        - [x] <b>Verify national records with AFI</b>: matching Neeraj Chopra and Avinash Sable stats.
        - [ ] <b>Age verification certificates upload</b>: pending for 14 junior prospects in Wrestling.
        - [ ] <b>Coordinate state selection trial calendars</b>: pending for 2026 Federation Cup events.
        """, unsafe_allow_html=True)
        
    st.markdown('<div class="stitle" style="font-size:1rem;"> Unverified Records Logs</div>', unsafe_allow_html=True)
    unverified = df_all[~df_all["has_source"]].head(10)[["name", "sport", "state", "entity_type", "notes"]]
    unverified.columns = ["Entity Name", "Sport", "State", "Type", "Notes"]
    st.dataframe(unverified.reset_index(drop=True), use_container_width=True, height=220)
