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
    page_icon="🏅",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────────────────────
# CSS — Gemini Neural Expressive + Decision-First Design
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700&display=swap');

/* ── Animated Gradient Background ── */
@keyframes gradientShift {
    0%   { background-position: 0% 50%; }
    25%  { background-position: 50% 0%; }
    50%  { background-position: 100% 50%; }
    75%  { background-position: 50% 100%; }
    100% { background-position: 0% 50%; }
}
@keyframes floatOrb {
    0%, 100% { transform: translate(0, 0) scale(1); }
    33%       { transform: translate(40px, -30px) scale(1.05); }
    66%       { transform: translate(-25px, 25px) scale(0.97); }
}
@keyframes slideUp {
    from { opacity: 0; transform: translateY(24px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes pulse {
    0%, 100% { box-shadow: 0 0 0 0 rgba(138,180,248,0.3); }
    50%       { box-shadow: 0 0 0 8px rgba(138,180,248,0); }
}

:root {
    --blue:    #8AB4F8;
    --purple:  #C58AF9;
    --pink:    #F28B82;
    --teal:    #81C995;
    --gold:    #FDD663;
    --cyan:    #78D9EC;
    --orange:  #FCAD70;
    --glass:   rgba(22, 28, 48, 0.60);
    --glass2:  rgba(30, 36, 60, 0.50);
    --border:  rgba(255,255,255,0.08);
    --text1:   #E8EAED;
    --text2:   #9AA0A6;
    --text3:   #5F6368;
    --green-dot: #81C995;
    --red-dot:   #F28B82;
    --amber-dot: #FDD663;
}

.stApp {
    background: linear-gradient(-45deg, #080818, #0b142a, #130b28, #08181a, #0b0828, #180b0a, #08142a, #080818);
    background-size: 600% 600%;
    animation: gradientShift 20s ease infinite;
    font-family: 'Inter', sans-serif;
    color: var(--text1);
}

/* ── Floating orbs ── */
.orb { position: fixed; border-radius: 50%; filter: blur(90px); pointer-events: none; z-index: 0; animation: floatOrb 22s ease-in-out infinite; }
.orb-1 { width: 600px; height: 600px; background: radial-gradient(circle, rgba(138,180,248,0.10) 0%, transparent 70%); top: -150px; left: -150px; }
.orb-2 { width: 450px; height: 450px; background: radial-gradient(circle, rgba(197,138,249,0.10) 0%, transparent 70%); top: 30%; right: -80px; animation-delay: -8s; }
.orb-3 { width: 380px; height: 380px; background: radial-gradient(circle, rgba(129,201,149,0.07) 0%, transparent 70%); bottom: 5%; left: 25%; animation-delay: -15s; }

/* ── Hero ── */
.hero { text-align: center; padding: 3.5rem 2rem 2.5rem; animation: slideUp 0.7s ease both; }
.hero-badge { display: inline-flex; align-items: center; gap: 6px; background: rgba(138,180,248,0.1); border: 1px solid rgba(138,180,248,0.25); border-radius: 50px; padding: 0.35rem 1.1rem; font-size: 0.72rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--blue); margin-bottom: 1.2rem; }
.hero-title { font-family: 'Outfit', sans-serif; font-size: 4rem; font-weight: 900; letter-spacing: -2px; line-height: 1.1; background: linear-gradient(135deg, #8AB4F8 0%, #C58AF9 40%, #F28B82 70%, #FDD663 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin: 0.5rem 0; }
.hero-sub { color: var(--text2); font-size: 1.15rem; max-width: 700px; margin: 0.8rem auto 0; line-height: 1.7; text-align: center; display: block; }
.hero-rule { width: 70px; height: 3px; background: linear-gradient(90deg, var(--blue), var(--purple), var(--pink)); border-radius: 2px; margin: 1.4rem auto; }

/* ── KPI Cards ── */
.kpi { background: var(--glass); backdrop-filter: blur(20px); border: 1px solid var(--border); border-radius: 18px; padding: 1.6rem 1.2rem; text-align: center; transition: all 0.3s ease; position: relative; overflow: hidden; animation: slideUp 0.6s ease both; }
.kpi:hover { transform: translateY(-5px); border-color: rgba(138,180,248,0.2); box-shadow: 0 20px 50px rgba(0,0,0,0.45); }
.kpi::before { content:''; position:absolute; top:0; left:0; right:0; height:2px; }
.kpi.blue::before   { background: linear-gradient(90deg, var(--blue), var(--purple)); }
.kpi.purple::before { background: linear-gradient(90deg, var(--purple), var(--pink)); }
.kpi.teal::before   { background: linear-gradient(90deg, var(--teal), var(--cyan)); }
.kpi.gold::before   { background: linear-gradient(90deg, var(--gold), var(--orange)); }
.kpi.pink::before   { background: linear-gradient(90deg, var(--pink), var(--gold)); }
.kpi-em { font-size: 1.8rem; margin-bottom: 0.4rem; display: block; }
.kpi-label { font-size: 0.68rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.8px; color: var(--text3); margin-bottom: 0.5rem; }
.kpi-val { font-family: 'Outfit', sans-serif; font-size: 2.6rem; font-weight: 900; line-height: 1; }
.kpi-val.blue   { color: var(--blue); }
.kpi-val.purple { color: var(--purple); }
.kpi-val.teal   { color: var(--teal); }
.kpi-val.gold   { color: var(--gold); }
.kpi-val.pink   { color: var(--pink); }
.kpi-sub { font-size: 0.72rem; color: var(--text3); margin-top: 0.4rem; }

/* ── Tabs — Gemini pill ── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(22,28,48,0.70); backdrop-filter: blur(20px);
    border: 1px solid var(--border); border-radius: 50px;
    padding: 5px; gap: 3px; display: flex; flex-wrap: wrap;
    width: fit-content; margin: 0 auto 2rem;
}
.stTabs [data-baseweb="tab"] {
    background: transparent; border: none; border-radius: 50px;
    color: var(--text2); font-family: 'Outfit', sans-serif;
    font-weight: 600; font-size: 0.85rem;
    padding: 0.5rem 1.2rem; transition: all 0.22s ease; white-space: nowrap;
}
.stTabs [data-baseweb="tab"]:hover { background: rgba(138,180,248,0.08); color: var(--blue); }
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, rgba(138,180,248,0.22), rgba(197,138,249,0.22)) !important;
    color: #fff !important; border: 1px solid rgba(138,180,248,0.28) !important;
}

/* ── Section titles ── */
.stitle { font-family: 'Outfit', sans-serif; font-size: 1.4rem; font-weight: 700; color: var(--text1); margin: 1.5rem 0 1rem; display: flex; align-items: center; gap: 0.5rem; }
.chip { font-size: 0.62rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 0.2rem 0.7rem; border-radius: 50px; }
.chip-blue   { background: rgba(138,180,248,0.14); border: 1px solid rgba(138,180,248,0.28); color: var(--blue); }
.chip-green  { background: rgba(129,201,149,0.14); border: 1px solid rgba(129,201,149,0.28); color: var(--teal); }
.chip-amber  { background: rgba(253,214,99,0.14);  border: 1px solid rgba(253,214,99,0.28);  color: var(--gold); }
.chip-red    { background: rgba(242,139,130,0.14); border: 1px solid rgba(242,139,130,0.28); color: var(--pink); }
.chip-purple { background: rgba(197,138,249,0.14); border: 1px solid rgba(197,138,249,0.28); color: var(--purple); }

/* ── Action cards ── */
.acard { background: var(--glass2); border: 1px solid var(--border); border-radius: 16px; padding: 1.4rem 1.6rem; margin-bottom: 0.75rem; transition: all 0.25s ease; position: relative; overflow: hidden; }
.acard:hover { background: rgba(30,40,70,0.65); border-color: rgba(138,180,248,0.18); transform: translateX(3px); }
.acard-top { display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.5rem; }
.acard-title { font-family: 'Outfit', sans-serif; font-weight: 700; font-size: 0.95rem; color: var(--text1); }
.acard-meta { font-size: 0.75rem; color: var(--text2); line-height: 1.6; }
.acard-score { font-family: 'Outfit', sans-serif; font-size: 1.6rem; font-weight: 800; }
.acard-tags { margin-top: 0.6rem; display: flex; flex-wrap: wrap; gap: 5px; }
.tag { font-size: 0.62rem; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; padding: 0.18rem 0.6rem; border-radius: 50px; background: rgba(138,180,248,0.1); color: var(--blue); border: 1px solid rgba(138,180,248,0.2); }
.tag.green  { background: rgba(129,201,149,0.1); color: var(--teal);   border-color: rgba(129,201,149,0.2); }
.tag.amber  { background: rgba(253,214,99,0.1);  color: var(--gold);   border-color: rgba(253,214,99,0.2); }
.tag.red    { background: rgba(242,139,130,0.1); color: var(--pink);   border-color: rgba(242,139,130,0.2); }
.tag.purple { background: rgba(197,138,249,0.1); color: var(--purple); border-color: rgba(197,138,249,0.2); }

/* ── Insight box ── */
.insight { background: linear-gradient(135deg, rgba(138,180,248,0.07), rgba(197,138,249,0.07)); border: 1px solid rgba(138,180,248,0.15); border-left: 3px solid var(--blue); border-radius: 12px; padding: 1rem 1.2rem; margin-bottom: 0.8rem; }
.insight.green { background: linear-gradient(135deg, rgba(129,201,149,0.07), rgba(120,217,236,0.07)); border-color: rgba(129,201,149,0.15); border-left-color: var(--teal); }
.insight.amber { background: linear-gradient(135deg, rgba(253,214,99,0.07), rgba(252,173,112,0.07)); border-color: rgba(253,214,99,0.15); border-left-color: var(--gold); }
.insight.red   { background: linear-gradient(135deg, rgba(242,139,130,0.07), rgba(253,214,99,0.05)); border-color: rgba(242,139,130,0.15); border-left-color: var(--pink); }
.insight.purple{ background: linear-gradient(135deg, rgba(197,138,249,0.07), rgba(138,180,248,0.07)); border-color: rgba(197,138,249,0.15); border-left-color: var(--purple); }
.insight-title { font-family: 'Outfit', sans-serif; font-weight: 700; font-size: 0.88rem; color: var(--blue); margin-bottom: 0.35rem; }
.insight.green  .insight-title  { color: var(--teal); }
.insight.amber  .insight-title  { color: var(--gold); }
.insight.red    .insight-title  { color: var(--pink); }
.insight.purple .insight-title  { color: var(--purple); }
.insight-body { font-size: 0.85rem; color: var(--text2); line-height: 1.7; }

/* ── Status dots ── */
.dot { display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 6px; }
.dot-green  { background: var(--teal); animation: pulse 2s infinite; }
.dot-amber  { background: var(--gold); }
.dot-red    { background: var(--pink); }

/* ── Data quality bars ── */
.dq-bar-wrap { background: rgba(255,255,255,0.05); border-radius: 50px; height: 8px; overflow: hidden; margin-top: 4px; }
.dq-bar { height: 100%; border-radius: 50px; transition: width 1s ease; }

/* ── Mini KPI ── */
.mkpi { background: var(--glass); border: 1px solid var(--border); border-radius: 14px; padding: 1.2rem; text-align: center; }
.mkpi-label { font-size: 0.68rem; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: var(--text3); margin-bottom: 0.4rem; }
.mkpi-val { font-family: 'Outfit', sans-serif; font-size: 2rem; font-weight: 800; line-height: 1; }

/* ── Sidebar ── */
section[data-testid="stSidebar"] { background: rgba(8,10,24,0.92); border-right: 1px solid var(--border); }

/* ── Download button ── */
.stDownloadButton > button { background: linear-gradient(135deg, rgba(138,180,248,0.12), rgba(197,138,249,0.12)) !important; border: 1px solid rgba(138,180,248,0.25) !important; color: var(--blue) !important; border-radius: 50px !important; font-family: 'Outfit', sans-serif !important; font-weight: 600 !important; }
.stDownloadButton > button:hover { background: linear-gradient(135deg, rgba(138,180,248,0.22), rgba(197,138,249,0.22)) !important; transform: translateY(-2px) !important; }

/* ── Table ── */
.stDataFrame { border-radius: 14px; overflow: hidden; border: 1px solid var(--border) !important; }

/* ── Expander ── */
details { background: var(--glass) !important; border: 1px solid var(--border) !important; border-radius: 14px !important; margin-bottom: 0.5rem !important; }
details:hover { border-color: rgba(138,180,248,0.18) !important; }
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
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# PLOTLY THEME
# ─────────────────────────────────────────────────────────────────────────────
PL = dict(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Outfit, Inter, sans-serif", color="#9AA0A6", size=12),
    margin=dict(l=30, r=20, t=45, b=35),
    colorway=["#8AB4F8","#C58AF9","#81C995","#F28B82","#FDD663","#78D9EC","#FCAD70","#FF8BCB"],
    legend=dict(bgcolor="rgba(22,28,48,0.7)", bordercolor="rgba(255,255,255,0.07)", borderwidth=1, font=dict(size=11)),
    xaxis=dict(gridcolor="rgba(255,255,255,0.04)", linecolor="rgba(255,255,255,0.06)"),
    yaxis=dict(gridcolor="rgba(255,255,255,0.04)", linecolor="rgba(255,255,255,0.06)"),
)

def playout(fig, title="", h=400):
    fig.update_layout(**PL,
        title=dict(text=title, font=dict(size=15, family="Outfit, sans-serif", color="#E8EAED")), height=h)
    return fig

COLOR_SCALES = {
    "blue":   ["#0d1a30","#8AB4F8"],
    "purple": ["#1a0d30","#C58AF9"],
    "teal":   ["#0d2018","#81C995"],
    "gold":   ["#2a1d00","#FDD663"],
    "pink":   ["#2a0d0d","#F28B82"],
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
            df["has_source"]   = df["source_link"].apply(lambda x: x not in ["","Unknown","N/A"])
            df["has_notes"]    = df["notes"].apply(lambda x: x not in ["","Unknown","N/A"])
            df["is_rural"]     = df["tier"].isin(["Rural","Tier3"])
            df["is_women"]     = df["gender"].isin(["Female"])
            df["is_youth"]     = df["age"].between(10, 21)
            df["is_unfunded"]  = df["funding_status"].str.lower() == "unfunded"
            df["tag_list"]     = df["tags"].apply(lambda x: [t.strip() for t in x.split(",") if t.strip()])
            df["cwg_flag"]     = df["tag_list"].apply(lambda t: "CWG2036" in t)
            df["oly_flag"]     = df["tag_list"].apply(lambda t: "Olympic2032" in t)
            df["rural_flag"]   = df["tag_list"].apply(lambda t: "rural-talent" in t)
            df["tribal_flag"]  = df["tag_list"].apply(lambda t: "tribal-talent" in t)
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

def mkpi(em, label, val, color="#8AB4F8"):
    return f"""<div class="mkpi"><div class="mkpi-label">{em} {label}</div>
    <div class="mkpi-val" style="color:{color};">{val}</div></div>"""

def acard(title, meta, score, score_color, tags_html, action=""):
    return f"""<div class="acard">
    <div class="acard-top">
      <div class="acard-title">{title}</div>
      <div class="acard-score" style="color:{score_color};">{score}</div>
    </div>
    <div class="acard-meta">{meta}</div>
    {"<div style='font-size:0.78rem;color:#8AB4F8;margin-top:0.5rem;font-weight:600;'>→ "+action+"</div>" if action else ""}
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
    if s >= 8: return "#81C995"
    if s >= 6: return "#FDD663"
    return "#F28B82"

# ─────────────────────────────────────────────────────────────────────────────
# LOAD
# ─────────────────────────────────────────────────────────────────────────────
df_all = load_master()
df_csr = load_csr()
elite_athletes = load_elite_athletes()

if df_all is None:
    st.error("⚠️ Master database not found. Place `athletiq_master_database.csv` in the `data/` folder.")
    st.stop()

# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR FILTERS
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("<h2 style='color:#8AB4F8;font-family:Outfit;font-weight:700;'>🎯 Filters</h2>", unsafe_allow_html=True)
    sel_entity   = st.multiselect("Entity Type", sorted(df_all["entity_type"].unique()), default=sorted(df_all["entity_type"].unique()))
    sel_sport    = st.multiselect("Sport",        sorted(df_all["sport"].unique()),       default=sorted(df_all["sport"].unique()))
    sel_state    = st.multiselect("State",        sorted(df_all["state"].unique()),       default=sorted(df_all["state"].unique()))
    sel_tier     = st.multiselect("Tier",         sorted(df_all["tier"].unique()),        default=sorted(df_all["tier"].unique()))
    sel_pipeline = st.multiselect("Pipeline",     sorted(df_all["pipeline_stage"].unique()), default=sorted(df_all["pipeline_stage"].unique()))
    st.markdown("---")
    omin, omax = float(df_all["athletiq_opportunity_score"].min()), float(df_all["athletiq_opportunity_score"].max())
    sel_score  = st.slider("Opportunity Score", omin, max(omax,10.0), (omin, max(omax,10.0)), 0.5)
    cmin, cmax = float(df_all["cwg_2036_relevance"].min()), float(df_all["cwg_2036_relevance"].max())
    sel_cwg    = st.slider("CWG 2036 Relevance", cmin, max(cmax,10.0), (cmin, max(cmax,10.0)), 0.5)
    st.markdown("<p style='text-align:center;color:#3C4043;font-size:0.72rem;margin-top:1rem;'>AthletIQ v3.0 — Decision Engine</p>", unsafe_allow_html=True)

df = df_all[
    df_all["entity_type"].isin(sel_entity) &
    df_all["sport"].isin(sel_sport) &
    df_all["state"].isin(sel_state) &
    df_all["tier"].isin(sel_tier) &
    df_all["pipeline_stage"].isin(sel_pipeline) &
    (df_all["athletiq_opportunity_score"] >= sel_score[0]) &
    (df_all["athletiq_opportunity_score"] <= sel_score[1]) &
    (df_all["cwg_2036_relevance"] >= sel_cwg[0]) &
    (df_all["cwg_2036_relevance"] <= sel_cwg[1])
]

# ─────────────────────────────────────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-badge">⚡ Built for Decision-Making, Not Data Display</div>
  <h1 class="hero-title">AthletIQ Intelligence</h1>
  <div class="hero-rule"></div>
  <p class="hero-sub">India's Grassroots-to-Podium Intelligence Platform &nbsp;·&nbsp; CWG 2036 &nbsp;·&nbsp; CSR Prospecting &nbsp;·&nbsp; Sponsor Pipeline &nbsp;·&nbsp; FitEvents OS</p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# TOP KPI ROW
# ─────────────────────────────────────────────────────────────────────────────
csr_pool  = df_csr["annual_csr_budget_cr"].sum() if df_csr is not None else 0
hot_leads = len(df_csr[df_csr["contact_potential"].str.lower()=="hot"]) if df_csr is not None else 0

c1,c2,c3,c4,c5 = st.columns(5)
with c1: st.markdown(kpi("📦","Entities Tracked", f"{len(df):,}", "blue", f"{df['sport'].nunique()} sports"), unsafe_allow_html=True)
with c2: st.markdown(kpi("🗺️","States Covered",   f"{df['state'].nunique()}", "purple", f"{df['tier'].nunique()} tiers"), unsafe_allow_html=True)
with c3: st.markdown(kpi("🏃","Athletes Profiled", f"{len(df[df['entity_type']=='Athlete']) + len(elite_athletes):,}", "teal", f"Across {df['sport'].nunique()} sports"), unsafe_allow_html=True)
with c4: st.markdown(kpi("💰","CSR Pool (₹ Cr)",  f"{csr_pool:,.0f}", "gold", f"{hot_leads} hot prospects"), unsafe_allow_html=True)
with c5: st.markdown(kpi("⭐","High Opp. (8+)",   f"{len(df[df['athletiq_opportunity_score']>=8]):,}", "pink", "Priority pipeline"), unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# 7 TABS
# ─────────────────────────────────────────────────────────────────────────────
tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8,tab9 = st.tabs([
    "🏟️ Sports Overview",
    "🗺️ Geography",
    "🌟 Future Champions",
    "🤝 CSR & Impact",
    "🎯 Sponsor Opportunities",
    "🏆 Top Picks",
    "🔍 Data Quality",
    "🏛️ SAI Centres",
    "🏅 Elite Profiles",
])


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 1 — SPORTS OVERVIEW
# Purpose: Which sports are active and worth tracking
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab1:
    st.markdown('<div class="stitle">🏟️ Sports Overview <span class="chip chip-blue">Which sports are worth tracking?</span></div>', unsafe_allow_html=True)

    # ── Decision-first insights ──
    top_sport     = df.groupby("sport")["athletiq_opportunity_score"].mean().idxmax()
    top_sport_sc  = df.groupby("sport")["athletiq_opportunity_score"].mean().max()
    most_entities = df["sport"].value_counts().idxmax()
    low_digital   = df.groupby("sport")["digital_readiness"].mean().idxmin()

    col_i1, col_i2, col_i3 = st.columns(3)
    with col_i1:
        st.markdown(insight("🔥 Highest-Potential Sport",
            f"<b>{top_sport}</b> has the highest average opportunity score ({top_sport_sc:.1f}/10). Prioritize this sport for the next activation event and CSR conversation.", "green"), unsafe_allow_html=True)
    with col_i2:
        st.markdown(insight("📦 Largest Pipeline",
            f"<b>{most_entities}</b> has the most entities in the database. Strong data coverage — ready for sponsor and white paper pitches.", ""), unsafe_allow_html=True)
    with col_i3:
        st.markdown(insight("📱 Biggest Digital Gap",
            f"<b>{low_digital}</b> has the lowest digital readiness. AthletIQ's WhatsApp-first tools can unlock this sport's data first.", "amber"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        sport_summary = df.groupby("sport").agg(
            Count=("name","count"),
            Avg_Score=("athletiq_opportunity_score","mean"),
            CWG_Avg=("cwg_2036_relevance","mean"),
            Olympic_Avg=("olympic_2032_relevance","mean"),
        ).sort_values("Avg_Score", ascending=False).reset_index()
        fig = px.bar(sport_summary, x="sport", y="Avg_Score",
                     color="Count", color_continuous_scale=COLOR_SCALES["blue"],
                     labels={"sport":"","Avg_Score":"Avg Opportunity Score","Count":"# Entities"},
                     hover_data=["Count","CWG_Avg","Olympic_Avg"])
        playout(fig, "Opportunity Score by Sport (size = entity count)")
        fig.update_xaxes(tickangle=-40)
        fig.update_coloraxes(colorbar_title="Entities")
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        cwg_sport = df.groupby("sport")[["cwg_2036_relevance","olympic_2032_relevance"]].mean().reset_index()
        cwg_sport = cwg_sport.sort_values("cwg_2036_relevance", ascending=False)
        fig = go.Figure()
        fig.add_trace(go.Bar(name="CWG 2036", x=cwg_sport["sport"], y=cwg_sport["cwg_2036_relevance"], marker_color="#8AB4F8"))
        fig.add_trace(go.Bar(name="Olympic 2032", x=cwg_sport["sport"], y=cwg_sport["olympic_2032_relevance"], marker_color="#C58AF9"))
        fig.update_layout(**PL, barmode="group", height=400)
        fig.update_layout(title=dict(text="CWG 2036 vs Olympic 2032 Relevance by Sport", font=dict(size=15,family="Outfit",color="#E8EAED")))
        fig.update_xaxes(tickangle=-40)
        st.plotly_chart(fig, use_container_width=True)

    c3, c4 = st.columns(2)
    with c3:
        pipeline_sport = df.groupby(["sport","pipeline_stage"]).size().reset_index(name="count")
        fig = px.bar(pipeline_sport, x="sport", y="count", color="pipeline_stage",
                     barmode="stack", color_discrete_sequence=["#F28B82","#FDD663","#81C995"],
                     labels={"sport":"","count":"Count","pipeline_stage":"Stage"})
        playout(fig, "Pipeline Stage by Sport — Discovery → Elite", h=360)
        fig.update_xaxes(tickangle=-40)
        st.plotly_chart(fig, use_container_width=True)

    with c4:
        # Sport coverage table — decision-ready
        tbl = df.groupby("sport").agg(
            Entities=("name","count"),
            Events=("entity_type", lambda x: (x=="Event").sum()),
            Academies=("entity_type", lambda x: (x=="Academy").sum()),
            Athletes=("entity_type", lambda x: (x=="Athlete").sum()),
            Opp_Score=("athletiq_opportunity_score","mean"),
            CWG=("cwg_2036_relevance","mean"),
        ).round(1).sort_values("Opp_Score",ascending=False).reset_index()
        tbl.columns=["Sport","Total","Events","Academies","Athletes","Avg Score","CWG Score"]
        st.markdown('<div class="stitle" style="font-size:1rem;">📊 Sport Coverage Matrix</div>', unsafe_allow_html=True)
        st.dataframe(tbl, use_container_width=True, height=340)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 2 — GEOGRAPHY
# Purpose: Which states/cities have visible grassroots activity
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab2:
    st.markdown('<div class="stitle">🗺️ Geography <span class="chip chip-green">Where is the visible grassroots activity?</span></div>', unsafe_allow_html=True)

    # ── Key geo decisions ──
    top_state   = df.groupby("state")["athletiq_opportunity_score"].mean().idxmax()
    blank_state = df.groupby("state")["athletiq_opportunity_score"].mean().idxmin()
    rural_count = df[df["is_rural"]].shape[0]
    metro_count = df[df["tier"]=="Metro"].shape[0]

    c1, c2, c3 = st.columns(3)
    with c1: st.markdown(insight("📍 Priority State for Pilot",
        f"<b>{top_state}</b> has the highest average opportunity score. Recommend this as the first state MOU — high activity, high potential.", "green"), unsafe_allow_html=True)
    with c2: st.markdown(insight("⚠️ Data-Thin State",
        f"<b>{blank_state}</b> has the lowest average score, likely reflecting data gaps more than talent gaps. Send an AthletIQ Mitra team here.", "amber"), unsafe_allow_html=True)
    with c3: st.markdown(insight("🌾 Rural vs Metro Balance",
        f"<b>{rural_count} entries</b> from Tier-3/Rural vs <b>{metro_count}</b> from Metro. Rural coverage is thin — this is where the real discovery gap lives.", "red"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns([3,2])

    with c1:
        state_df = df.groupby("state").agg(
            Count=("name","count"),
            Avg_Score=("athletiq_opportunity_score","mean"),
            Sports=("sport","nunique"),
            Unfunded=("is_unfunded","sum"),
        ).sort_values("Count",ascending=True).reset_index()
        fig = px.bar(state_df.tail(18), y="state", x="Count", orientation="h",
                     color="Avg_Score", color_continuous_scale=COLOR_SCALES["blue"],
                     labels={"state":"","Count":"Entities","Avg_Score":"Avg Score"},
                     hover_data=["Sports","Unfunded"])
        playout(fig, "Entity Count by State (color = avg opportunity score)", h=540)
        fig.update_coloraxes(colorbar_title="Score")
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        tier_dist = df["tier"].value_counts().reset_index()
        tier_dist.columns = ["Tier","Count"]
        tier_c = {"Metro":"#8AB4F8","Tier1":"#C58AF9","Tier2":"#81C995","Tier3":"#FDD663","Rural":"#F28B82"}
        fig = px.pie(tier_dist, names="Tier", values="Count", hole=0.52,
                     color="Tier", color_discrete_map=tier_c)
        playout(fig, "Metro vs Tier-2/3 vs Rural", h=280)
        fig.update_traces(textinfo="percent+label", textposition="inside")
        st.plotly_chart(fig, use_container_width=True)

        dr = df.groupby("tier")["digital_readiness"].mean().reset_index()
        fig2 = px.bar(dr, x="tier", y="digital_readiness", color="tier",
                      color_discrete_map=tier_c,
                      labels={"tier":"","digital_readiness":"Digital Readiness (1-10)"})
        playout(fig2, "Digital Readiness Gap by Tier", h=230)
        fig2.update_layout(showlegend=False)
        st.plotly_chart(fig2, use_container_width=True)

    # ── State decision matrix ──
    st.markdown('<div class="stitle" style="font-size:1rem;">📋 State Decision Matrix — Where to Act First</div>', unsafe_allow_html=True)
    state_matrix = df.groupby("state").agg(
        Entities=("name","count"),
        Avg_Score=("athletiq_opportunity_score","mean"),
        Top_Sport=("sport", lambda x: x.value_counts().index[0] if len(x) > 0 else "N/A"),
        Rural_Entries=("is_rural","sum"),
        Unfunded=("is_unfunded","sum"),
        CWG_Ready=("cwg_flag","sum"),
        Digital_Readiness=("digital_readiness","mean"),
    ).round(1).sort_values("Avg_Score",ascending=False).reset_index()
    state_matrix.columns = ["State","Entities","Avg Score","Top Sport","Rural","Unfunded","CWG Ready","Digital Score"]
    st.dataframe(state_matrix, use_container_width=True, height=350)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 3 — FUTURE CHAMPIONS
# Purpose: Athletes/coaches with high potential
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab3:
    st.markdown('<div class="stitle">🌟 Future Champions <span class="chip chip-purple">Athletes & coaches with highest potential</span></div>', unsafe_allow_html=True)

    athletes = df[df["entity_type"]=="Athlete"].copy()
    coaches  = df[df["entity_type"]=="Coach"].copy()

    a1, a2, a3, a4 = st.columns(4)
    with a1: st.markdown(mkpi("🏃","Athletes Tracked", str(len(athletes)), "#8AB4F8"), unsafe_allow_html=True)
    with a2: st.markdown(mkpi("⚠️","Unfunded",         str(athletes["is_unfunded"].sum()), "#F28B82"), unsafe_allow_html=True)
    with a3: st.markdown(mkpi("👩","Women Athletes",   str(athletes["is_women"].sum()), "#C58AF9"), unsafe_allow_html=True)
    with a4: st.markdown(mkpi("🌾","Rural Talent",    str(athletes["is_rural"].sum()), "#81C995"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns([3, 2])

    with c1:
        # Top athletes — decision table
        top_athletes = athletes.nlargest(15,"athletiq_opportunity_score")[
            ["name","sport","state","tier","age","gender","performance_level",
             "funding_status","cwg_2036_relevance","olympic_2032_relevance",
             "athletiq_opportunity_score","notes"]
        ].reset_index(drop=True)
        top_athletes.index += 1

        st.markdown('<div class="stitle" style="font-size:1rem;">🏅 Priority Athletes — Act Now</div>', unsafe_allow_html=True)
        for _, row in top_athletes.head(8).iterrows():
            sc = row["athletiq_opportunity_score"]
            sc_col = score_color(sc)
            fund_tag = tag("Unfunded","red") if "unfunded" in str(row["funding_status"]).lower() else tag("Funded","green")
            cwg_tag  = tag("CWG2036","blue") if row["cwg_2036_relevance"] >= 7 else ""
            oly_tag  = tag("Olympic2032","purple") if row["olympic_2032_relevance"] >= 7 else ""
            gender_tag = tag("Woman","purple") if str(row["gender"])=="Female" else ""
            rural_tag  = tag("Rural","amber") if str(row["tier"]) in ["Rural","Tier3"] else ""
            tags_html  = fund_tag + cwg_tag + oly_tag + gender_tag + rural_tag
            meta = f"{row['sport']} • {row['state']} • Age {int(row['age'])} • {row['performance_level']} level<br>{row['notes']}"
            action = "Identify CSR funding match" if "unfunded" in str(row["funding_status"]).lower() else "Track for CWG selection"
            st.markdown(acard(f"{row['name']}", meta, f"{sc:.0f}", sc_col, tags_html, action), unsafe_allow_html=True)

    with c2:
        # Scatter: age vs score
        athletes_plot = athletes[athletes["age"]>0].copy()
        fig = px.scatter(athletes_plot,
                         x="age", y="athletiq_opportunity_score",
                         color="sport", size="cwg_2036_relevance",
                         hover_name="name",
                         labels={"age":"Age","athletiq_opportunity_score":"Opportunity Score"},
                         size_max=22,
                         color_discrete_sequence=["#8AB4F8","#C58AF9","#81C995","#F28B82","#FDD663","#78D9EC","#FCAD70","#FF8BCB"])
        playout(fig, "Athletes — Age vs Opportunity Score", h=340)
        st.plotly_chart(fig, use_container_width=True)

        # Gender breakdown
        gender_sport = athletes.groupby(["sport","gender"]).size().reset_index(name="count")
        fig2 = px.bar(gender_sport, x="sport", y="count", color="gender",
                      barmode="stack",
                      color_discrete_map={"Male":"#8AB4F8","Female":"#C58AF9","Mixed":"#81C995"},
                      labels={"sport":"","count":"Athletes","gender":"Gender"})
        playout(fig2, "Gender Spread by Sport", h=280)
        fig2.update_xaxes(tickangle=-40)
        st.plotly_chart(fig2, use_container_width=True)

    # ── Coaches ──
    st.markdown('<div class="stitle" style="font-size:1rem;">👨‍🏫 Key Coaches — Partnership Opportunities</div>', unsafe_allow_html=True)
    top_coaches = coaches.nlargest(12,"athletiq_opportunity_score")[
        ["name","sport","state","tier","performance_level","digital_readiness","athletiq_opportunity_score","notes"]
    ].reset_index(drop=True)
    top_coaches.index += 1
    st.dataframe(top_coaches, use_container_width=True, height=280)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 4 — CSR & IMPACT
# Purpose: Women, youth, rural, health, education, inclusion opportunities
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab4:
    st.markdown('<div class="stitle">🤝 CSR & Impact <span class="chip chip-green">Women · Youth · Rural · Health · Inclusion</span></div>', unsafe_allow_html=True)

    if df_csr is None:
        st.warning("⚠️ CSR data file not found.")
    else:
        total_csr  = df_csr["annual_csr_budget_cr"].sum()
        hot_count  = len(df_csr[df_csr["contact_potential"].str.lower()=="hot"])
        avg_align  = df_csr["csr_alignment_score"].mean()
        sport_pct  = (df_csr["annual_csr_budget_cr"] * df_csr["current_sport_allocation_pct"] / 100).sum()
        gap        = total_csr * 0.05 - sport_pct  # 5% target vs current

        m1,m2,m3,m4 = st.columns(4)
        with m1: st.markdown(mkpi("💰","Total CSR Pool", f"₹{total_csr:,.0f} Cr", "#81C995"), unsafe_allow_html=True)
        with m2: st.markdown(mkpi("⚽","Current Sport Spend", f"₹{sport_pct:,.0f} Cr", "#FDD663"), unsafe_allow_html=True)
        with m3: st.markdown(mkpi("📈","Unlockable (5% target)", f"₹{max(gap,0):,.0f} Cr", "#8AB4F8"), unsafe_allow_html=True)
        with m4: st.markdown(mkpi("🔥","Hot Leads Now", str(hot_count), "#F28B82"), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ── Impact segments — CSR narrative ──
        st.markdown('<div class="stitle" style="font-size:1rem;">🎯 CSR Narrative Angles — Use These in Meetings</div>', unsafe_allow_html=True)

        women_ath   = df[(df["entity_type"]=="Athlete") & (df["is_women"])].shape[0]
        youth_ath   = df[(df["entity_type"]=="Athlete") & (df["is_youth"])].shape[0]
        rural_all   = df[df["is_rural"]].shape[0]
        tribal_all  = df[df["tribal_flag"]].shape[0]
        unfunded_ath = df[(df["entity_type"]=="Athlete") & (df["is_unfunded"])].shape[0]

        n1,n2 = st.columns(2)
        with n1:
            st.markdown(insight("👩 Women in Sport",
                f"<b>{women_ath} women athletes</b> profiled — spanning boxing (Manipur), weightlifting, badminton, athletics. "
                f"CSR angle: Gender inclusion, women's empowerment, UNGC SDG-5 alignment. "
                f"<b>Top pitch:</b> 'Fund 50 women athletes to the next level in 12 months.'", "purple"), unsafe_allow_html=True)
            st.markdown(insight("🌾 Rural & Tribal Talent",
                f"<b>{rural_all} rural/Tier-3 entities</b>, <b>{tribal_all} tribal-tagged</b> (Jharkhand archery, NE boxing, Odisha hockey). "
                f"CSR angle: Rural development, tribal inclusion, SDG-10. "
                f"<b>Top pitch:</b> 'Bring 100 village athletes into the digital sports ecosystem.'", "amber"), unsafe_allow_html=True)
        with n2:
            st.markdown(insight("🧒 Youth Development",
                f"<b>{youth_ath} athletes aged 10–21</b> tracked — this is the CWG 2036 cohort. "
                f"CSR angle: Youth employability, skill development, education through sport. "
                f"<b>Top pitch:</b> 'Sponsor structured development for 200 youth athletes through 2027.'", ""), unsafe_allow_html=True)
            st.markdown(insight("⚠️ Unfunded Athletes at Risk",
                f"<b>{unfunded_ath} athletes currently unfunded</b> — at high dropout risk between ages 17–21. "
                f"CSR angle: Each dropped athlete = national talent loss. AthletIQ matches athletes to sponsors with full traceability. "
                f"<b>Top pitch:</b> '₹2 Lakh/year funds one athlete's full development cycle.'", "red"), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)

        with c1:
            fig = px.scatter(df_csr,
                             x="csr_alignment_score", y="athletiq_fit_score",
                             size="annual_csr_budget_cr", color="contact_potential",
                             hover_name="company_name",
                             labels={"csr_alignment_score":"CSR Alignment","athletiq_fit_score":"AthletIQ Fit","contact_potential":"Lead"},
                             size_max=50,
                             color_discrete_map={"Cold":"#5F6368","Warm":"#FDD663","Hot":"#F28B82"})
            playout(fig, "CSR Alignment vs AthletIQ Fit — Bubble = Budget", h=400)
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            contact_d = df_csr["contact_potential"].value_counts().reset_index()
            contact_d.columns = ["Status","Count"]
            fig = px.pie(contact_d, names="Status", values="Count", hole=0.55,
                         color="Status", color_discrete_map={"Cold":"#5F6368","Warm":"#FDD663","Hot":"#F28B82"})
            playout(fig, "Sponsor Lead Pipeline Status", h=220)
            fig.update_traces(textinfo="label+percent", textposition="inside")
            st.plotly_chart(fig, use_container_width=True)

            top_csr = df_csr.nlargest(5,"annual_csr_budget_cr")[["company_name","annual_csr_budget_cr","contact_potential"]]
            top_csr.columns = ["Company","CSR Budget (Cr)","Lead Status"]
            st.markdown("**Top 5 by CSR Budget**")
            st.dataframe(top_csr, use_container_width=True, height=170)

        # ── Full CSR pipeline ──
        st.markdown('<div class="stitle" style="font-size:1rem;">📋 Full Sponsor Pipeline</div>', unsafe_allow_html=True)
        show_cols = ["company_name","sector","annual_csr_budget_cr","current_sport_allocation_pct",
                     "sport_focus","contact_potential","csr_alignment_score","athletiq_fit_score","engagement_strategy"]
        st.dataframe(df_csr[show_cols].sort_values("athletiq_fit_score",ascending=False), use_container_width=True, height=320)

        dl1, dl2 = st.columns(2)
        with dl1:
            csr_csv = df_csr.to_csv(index=False).encode("utf-8")
            st.download_button("📥 Export CSR Pipeline (CSV)", csr_csv, "athletiq_csr_pipeline.csv","text/csv", use_container_width=True)
        with dl2:
            hot_csv = df_csr[df_csr["contact_potential"].str.lower()=="hot"].to_csv(index=False).encode("utf-8")
            st.download_button("🔥 Export Hot Leads Only (CSV)", hot_csv, "athletiq_hot_leads.csv","text/csv", use_container_width=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 5 — SPONSOR OPPORTUNITIES
# Purpose: Brand-fit events, academies, stories and regions
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab5:
    st.markdown('<div class="stitle">🎯 Sponsor Opportunities <span class="chip chip-amber">Events · Academies · Stories · Regions</span></div>', unsafe_allow_html=True)

    events    = df[df["entity_type"]=="Event"].copy()
    academies = df[df["entity_type"]=="Academy"].copy()

    st.markdown(insight("💡 How to Use This Tab",
        "Each card below is a sponsorable asset — an event, academy, or region that AthletIQ can package for a brand partner. "
        "Filter by sport, state, or CWG flag using the sidebar. Share this view directly in a sponsor meeting.", ""), unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown('<div class="stitle" style="font-size:1rem;">📅 Sponsorable Events <span class="chip chip-blue">High Visibility</span></div>', unsafe_allow_html=True)
        top_events = events.nlargest(10,"athletiq_opportunity_score")
        for _, row in top_events.iterrows():
            sc     = row["athletiq_opportunity_score"]
            sc_col = score_color(sc)
            cwg_t  = tag("CWG2036","blue") if row["cwg_flag"] else ""
            oly_t  = tag("Olympic2032","purple") if row["oly_flag"] else ""
            rural_t= tag("Rural","amber") if row["is_rural"] else ""
            part   = f"{int(row['participants_or_capacity'])} participants" if row["participants_or_capacity"]>0 else ""
            meta   = f"{row['sport']} • {row['state']} • {row['tier']} • {part}<br>{row['notes']}"
            action = f"Package for {row['sport']} brand partnership — {part} reach"
            st.markdown(acard(row["name"], meta, f"{sc:.0f}", sc_col, cwg_t+oly_t+rural_t, action), unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="stitle" style="font-size:1rem;">🏫 Sponsorable Academies <span class="chip chip-green">Infrastructure Play</span></div>', unsafe_allow_html=True)
        top_acad = academies.nlargest(10,"athletiq_opportunity_score")
        for _, row in top_acad.iterrows():
            sc     = row["athletiq_opportunity_score"]
            sc_col = score_color(sc)
            cwg_t  = tag("CWG2036","blue") if row["cwg_flag"] else ""
            fund_t = tag("Needs Funding","red") if row["is_unfunded"] else tag("Partially Funded","amber")
            cap    = f"Capacity: {int(row['participants_or_capacity'])}" if row["participants_or_capacity"]>0 else ""
            meta   = f"{row['sport']} • {row['state']} • {cap}<br>{row['notes']}"
            action = f"Name-rights or equipment sponsorship opportunity"
            st.markdown(acard(row["name"], meta, f"{sc:.0f}", sc_col, cwg_t+fund_t, action), unsafe_allow_html=True)

    # ── Chart: Events by participation ──
    st.markdown("<br>", unsafe_allow_html=True)
    c3, c4 = st.columns(2)

    with c3:
        events_part = events[events["participants_or_capacity"]>0].sort_values("participants_or_capacity",ascending=False).head(12)
        fig = px.bar(events_part, y="name", x="participants_or_capacity", orientation="h",
                     color="athletiq_opportunity_score", color_continuous_scale=COLOR_SCALES["gold"],
                     labels={"name":"","participants_or_capacity":"Participants","athletiq_opportunity_score":"Opp Score"},
                     hover_data=["sport","state"])
        playout(fig, "Top Events by Reach (Participants)", h=420)
        fig.update_coloraxes(colorbar_title="Score")
        fig.update_layout(yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig, use_container_width=True)

    with c4:
        # Sport × tier opportunity matrix for brands
        brand_matrix = events.groupby(["sport","tier"]).agg(
            Events=("name","count"),
            Reach=("participants_or_capacity","sum"),
            Avg_Score=("athletiq_opportunity_score","mean"),
        ).reset_index()
        fig = px.scatter(brand_matrix,
                         x="sport", y="tier", size="Reach", color="Avg_Score",
                         color_continuous_scale=COLOR_SCALES["blue"],
                         labels={"sport":"Sport","tier":"Tier","Reach":"Total Reach","Avg_Score":"Score"},
                         size_max=50)
        playout(fig, "Brand Reach Matrix — Sport × Tier × Participation", h=420)
        fig.update_coloraxes(colorbar_title="Score")
        st.plotly_chart(fig, use_container_width=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 6 — TOP PICKS
# Purpose: AthletIQ's recommended shortlist for action
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab6:
    st.markdown('<div class="stitle">🏆 Top Picks <span class="chip chip-purple">AthletIQ recommended shortlist — act on these</span></div>', unsafe_allow_html=True)

    st.markdown(insight("📌 What This Is",
        "This is AthletIQ's curated shortlist — the 20 highest-priority opportunities across all entity types. "
        "These are not just high-scoring records; they represent the best combination of medal potential, "
        "funding gap, geographic reach, and AthletIQ's ability to add value right now.", ""), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Segmented shortlists ──
    tab6a, tab6b, tab6c = st.tabs(["🌟 All Types (Top 20)", "🏃 Athletes Only", "📅 Events Only"])

    with tab6a:
        top20 = df.nlargest(20,"athletiq_opportunity_score").reset_index(drop=True)
        for i, row in top20.iterrows():
            sc     = row["athletiq_opportunity_score"]
            sc_col = score_color(sc)
            cwg_t  = tag("CWG2036","blue")   if row["cwg_flag"]  else ""
            oly_t  = tag("Olympic","purple")  if row["oly_flag"]  else ""
            fund_t = tag("Unfunded","red")    if row["is_unfunded"] else ""
            rural_t= tag("Rural","amber")     if row["is_rural"]   else ""
            women_t= tag("Women","purple")    if row["is_women"]   else ""
            tribe_t= tag("Tribal","amber")    if row["tribal_flag"] else ""
            tags_h = cwg_t+oly_t+fund_t+rural_t+women_t+tribe_t

            with st.expander(f"#{i+1}  •  {row['name']}  —  {row['entity_type']} | {row['sport']} | {row['state']} | Score: {sc:.0f}", expanded=False):
                ex1, ex2, ex3 = st.columns(3)
                with ex1:
                    st.markdown(f"**Entity:** {row['entity_type']}")
                    st.markdown(f"**Sport:** {row['sport']}")
                    st.markdown(f"**Location:** {row['city']}, {row['state']} ({row['tier']})")
                    st.markdown(f"**Pipeline:** {row['pipeline_stage']}")
                with ex2:
                    st.markdown(f"**CWG 2036:** {row['cwg_2036_relevance']:.0f}/10")
                    st.markdown(f"**Olympic 2032:** {row['olympic_2032_relevance']:.0f}/10")
                    st.markdown(f"**Digital Readiness:** {row['digital_readiness']:.0f}/10")
                    st.markdown(f"**Funding:** {row['funding_status']}")
                with ex3:
                    if str(row["notes"]) not in ["Unknown","","N/A"]:
                        st.info(row["notes"])
                    if str(row["source_link"]) not in ["Unknown","","N/A"]:
                        st.markdown(f"🔗 [Source Link]({row['source_link']})")
                st.markdown(tags_h, unsafe_allow_html=True)

    with tab6b:
        top_ath = df[df["entity_type"]=="Athlete"].nlargest(15,"athletiq_opportunity_score").reset_index(drop=True)
        for i, row in top_ath.iterrows():
            sc = row["athletiq_opportunity_score"]
            with st.expander(f"#{i+1}  •  {row['name']}  |  {row['sport']} | {row['state']} | Age {int(row['age'])} | Score: {sc:.0f}"):
                e1,e2 = st.columns(2)
                with e1:
                    st.markdown(f"**Gender:** {row['gender']}  •  **Performance:** {row['performance_level']}")
                    st.markdown(f"**CWG 2036:** {row['cwg_2036_relevance']:.0f}/10  •  **Olympic 2032:** {row['olympic_2032_relevance']:.0f}/10")
                    st.markdown(f"**Funding:** {row['funding_status']}")
                with e2:
                    if str(row["notes"]) not in ["Unknown","","N/A"]:
                        st.info(row["notes"])

    with tab6c:
        top_ev = df[df["entity_type"]=="Event"].nlargest(15,"athletiq_opportunity_score").reset_index(drop=True)
        for i, row in top_ev.iterrows():
            sc = row["athletiq_opportunity_score"]
            part = f"{int(row['participants_or_capacity'])} participants" if row["participants_or_capacity"]>0 else ""
            with st.expander(f"#{i+1}  •  {row['name']}  |  {row['sport']} | {row['state']} | {part} | Score: {sc:.0f}"):
                e1,e2 = st.columns(2)
                with e1:
                    st.markdown(f"**Tier:** {row['tier']}  •  **Frequency:** {row['frequency']}")
                    st.markdown(f"**CWG 2036:** {row['cwg_2036_relevance']:.0f}/10  •  **Digital Ready:** {row['digital_readiness']:.0f}/10")
                with e2:
                    if str(row["notes"]) not in ["Unknown","","N/A"]:
                        st.info(row["notes"])
                    if str(row["source_link"]) not in ["Unknown","","N/A"]:
                        st.markdown(f"🔗 [Source Link]({row['source_link']})")

    st.markdown("<br>", unsafe_allow_html=True)
    top_csv = df.nlargest(20,"athletiq_opportunity_score").to_csv(index=False).encode("utf-8")
    st.download_button("📥 Export Top 20 Shortlist (CSV)", top_csv, "athletiq_top20.csv","text/csv", use_container_width=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 7 — DATA QUALITY
# Purpose: Verified vs unverified, missing fields, source links
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab7:
    st.markdown('<div class="stitle">🔍 Data Quality <span class="chip chip-red">Verified vs unverified · Missing fields · Source coverage</span></div>', unsafe_allow_html=True)

    # ── Overall quality metrics ──
    total      = len(df_all)
    has_src    = df_all["has_source"].sum()
    has_notes_ = df_all["has_notes"].sum()
    has_score  = (df_all["athletiq_opportunity_score"] > 0).sum()
    has_age    = (df_all["age"] > 0).sum()
    has_part   = (df_all["participants_or_capacity"] > 0).sum()

    q1,q2,q3,q4 = st.columns(4)
    with q1: st.markdown(mkpi("🔗","Source Links",     f"{has_src}/{total}", "#81C995"), unsafe_allow_html=True)
    with q2: st.markdown(mkpi("📝","Notes Filled",     f"{has_notes_}/{total}", "#8AB4F8"), unsafe_allow_html=True)
    with q3: st.markdown(mkpi("⭐","Scored Entities",  f"{has_score}/{total}", "#FDD663"), unsafe_allow_html=True)
    with q4: st.markdown(mkpi("📊","Participation Data",f"{has_part}/{total}", "#C58AF9"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Decision insight ──
    missing_src = total - has_src
    st.markdown(insight("⚠️ Action Required",
        f"<b>{missing_src} records</b> have no source link — these are unverified entries. "
        f"Do not use these for white papers or sponsor pitches until verified. "
        f"Assign an AthletIQ Mitra team to verify and add source links before the next pitch cycle.", "red"), unsafe_allow_html=True)

    st.markdown(insight("✅ Ready to Use",
        f"<b>{has_src} records with verified source links</b> are pitch-ready. "
        f"<b>{has_notes_} records with detailed notes</b> can be used for white paper inputs and social media content right now.", "green"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)

    with c1:
        # Field completeness by entity type
        st.markdown('<div class="stitle" style="font-size:1rem;">📊 Field Completeness by Entity Type</div>', unsafe_allow_html=True)
        completeness = []
        for etype in df_all["entity_type"].unique():
            sub = df_all[df_all["entity_type"]==etype]
            completeness.append({
                "Entity": etype,
                "Total": len(sub),
                "Has Source (%)": round(sub["has_source"].mean()*100,1),
                "Has Notes (%)": round(sub["has_notes"].mean()*100,1),
                "Scored (%)": round((sub["athletiq_opportunity_score"]>0).mean()*100,1),
                "Has Age (%)": round((sub["age"]>0).mean()*100,1),
            })
        comp_df = pd.DataFrame(completeness)
        st.dataframe(comp_df, use_container_width=True, height=200)

        # Bar chart of completeness
        comp_melt = comp_df.melt(id_vars="Entity", var_name="Field", value_name="Completeness %",
                                  value_vars=["Has Source (%)","Has Notes (%)","Scored (%)"])
        fig = px.bar(comp_melt, x="Entity", y="Completeness %", color="Field",
                     barmode="group",
                     color_discrete_sequence=["#8AB4F8","#81C995","#FDD663"])
        playout(fig, "Data Completeness by Entity Type (%)", h=320)
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        # Source coverage by sport
        st.markdown('<div class="stitle" style="font-size:1rem;">🔗 Source Coverage by Sport</div>', unsafe_allow_html=True)
        src_sport = df_all.groupby("sport").agg(
            Total=("name","count"),
            Sourced=("has_source","sum"),
            Noted=("has_notes","sum"),
        ).reset_index()
        src_sport["Source %"] = (src_sport["Sourced"]/src_sport["Total"]*100).round(1)
        src_sport["Notes %"]  = (src_sport["Noted"] /src_sport["Total"]*100).round(1)
        src_sport = src_sport.sort_values("Source %", ascending=True)

        fig = px.bar(src_sport, y="sport", x="Source %", orientation="h",
                     color="Source %",
                     color_continuous_scale=["#F28B82","#FDD663","#81C995"],
                     labels={"sport":"","Source %":"% Entries with Source Link"})
        playout(fig, "Source Verification by Sport", h=440)
        fig.update_coloraxes(showscale=False)
        st.plotly_chart(fig, use_container_width=True)

    # ── Unverified records table ──
    st.markdown('<div class="stitle" style="font-size:1rem;">⚠️ Unverified Records — Needs Verification Before Pitch Use</div>', unsafe_allow_html=True)
    unverified = df_all[~df_all["has_source"]][
        ["entity_type","name","sport","state","tier","athletiq_opportunity_score","notes"]
    ].sort_values("athletiq_opportunity_score",ascending=False).reset_index(drop=True)
    unverified.index += 1
    if len(unverified) > 0:
        st.dataframe(unverified, use_container_width=True, height=300)
    else:
        st.success("✅ All records have source links — data is fully verified.")

    st.markdown("<br>", unsafe_allow_html=True)
    uv_csv = unverified.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Export Unverified Records (CSV)", uv_csv, "athletiq_unverified.csv","text/csv", use_container_width=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 8 — SAI CENTRES
# Purpose: Map of India's SAI centres + smart athlete-to-centre matcher
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ── SAI Centres Master Data ──
SAI_CENTRES = [
    {
        "name": "NIS Patiala (National Institute of Sports)",
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
        "performance": ["State","National","International"],
        "capacity": 300,
        "facilities": "Athletics track · Hockey turf · Badminton courts · Swimming pool · Gymnasium · Hostel",
        "coaches": 70,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "Strong in athletics and hockey. Para-athletics support available. Good for South Indian athletes reducing travel burden.",
        "nearby_states": ["Karnataka","Tamil Nadu","Kerala","Andhra Pradesh","Telangana","Goa"],
    },
    {
        "name": "SAI NCOE Sonipat",
        "city": "Sonipat", "state": "Haryana",
        "type": "NCOE", "region": "North",
        "sports": ["Wrestling","Athletics","Boxing","Kabaddi","Judo"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 13, "age_max": 24,
        "performance": ["District","State","National"],
        "capacity": 280,
        "facilities": "Wrestling halls · Athletics track · Boxing rings · Kabaddi courts · Hostel",
        "coaches": 55,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "India's wrestling capital. Haryana athletes get proximity advantage. Excellent for rural wrestlers moving into structured training.",
        "nearby_states": ["Haryana","Delhi","Punjab","Uttar Pradesh","Rajasthan"],
    },
    {
        "name": "SAI NCOE Bhopal",
        "city": "Bhopal", "state": "Madhya Pradesh",
        "type": "NCOE", "region": "Central",
        "sports": ["Athletics","Boxing","Hockey","Judo","Canoeing","Kabaddi","Wrestling"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 14, "age_max": 25,
        "performance": ["State","National"],
        "capacity": 320,
        "facilities": "Athletics track · Boxing rings · Hockey turf · Kayak/Canoe facility · Hostel · Sports Science support",
        "coaches": 60,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "Central India hub. Strong for boxing and hockey. Excellent gateway for athletes from MP, CG, and surrounding tribal regions.",
        "nearby_states": ["Madhya Pradesh","Chhattisgarh","Rajasthan","Maharashtra","Uttar Pradesh"],
    },
    {
        "name": "SAI NERC Imphal",
        "city": "Imphal", "state": "Manipur",
        "type": "NCOE", "region": "Northeast",
        "sports": ["Boxing","Football","Weightlifting","Archery","Athletics"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 13, "age_max": 24,
        "performance": ["District","State","National"],
        "capacity": 200,
        "facilities": "Boxing rings · Football ground · Weightlifting hall · Archery range · Hostel",
        "coaches": 45,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "Northeast's most important SAI centre. Mary Kom's home base. Best for NE athletes to train locally. Boxing and weightlifting powerhouse.",
        "nearby_states": ["Manipur","Nagaland","Mizoram","Assam","Meghalaya","Tripura","Arunachal Pradesh"],
    },
    {
        "name": "SAI NCOE Kolkata",
        "city": "Kolkata", "state": "West Bengal",
        "type": "NCOE", "region": "East",
        "sports": ["Archery","Athletics","Gymnastics","Hockey","Table Tennis","Football","Swimming"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 14, "age_max": 25,
        "performance": ["State","National"],
        "capacity": 260,
        "facilities": "Archery range · Athletics track · Gymnastics hall · Hockey turf · TT tables · Pool · Hostel",
        "coaches": 58,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "East India hub. Strong in archery (Deepika Kumari connection). Table tennis growing fast. Good for WB, Jharkhand, Odisha athletes.",
        "nearby_states": ["West Bengal","Jharkhand","Odisha","Bihar","Assam"],
    },
    {
        "name": "SAI STC Rohtak",
        "city": "Rohtak", "state": "Haryana",
        "type": "STC", "region": "North",
        "sports": ["Wrestling","Boxing","Athletics","Kabaddi"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 10, "age_max": 21,
        "performance": ["Village","District","State"],
        "capacity": 180,
        "facilities": "Wrestling akharas · Boxing rings · Athletics track · Hostel",
        "coaches": 30,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "Grassroots feeder centre for NIS Patiala. Ideal for young rural wrestlers and boxers from Haryana. SAI's discovery pipeline entry point.",
        "nearby_states": ["Haryana","Delhi","Punjab","Rajasthan"],
    },
    {
        "name": "SAI STC Lucknow",
        "city": "Lucknow", "state": "Uttar Pradesh",
        "type": "STC", "region": "North",
        "sports": ["Athletics","Hockey","Wrestling","Boxing","Shooting","Badminton"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 10, "age_max": 22,
        "performance": ["District","State"],
        "capacity": 220,
        "facilities": "Athletics track · Hockey turf · Shooting range · Boxing rings · Hostel",
        "coaches": 40,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "Primary SAI centre for UP athletes. Shooting range is a key asset — UP has strong Olympian shooting history from this belt.",
        "nearby_states": ["Uttar Pradesh","Bihar","Madhya Pradesh","Uttarakhand"],
    },
    {
        "name": "SAI STC Gandhinagar",
        "city": "Gandhinagar", "state": "Gujarat",
        "type": "STC", "region": "West",
        "sports": ["Wrestling","Boxing","Athletics","Volleyball","Kabaddi","Swimming"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 12, "age_max": 22,
        "performance": ["State","National"],
        "capacity": 200,
        "facilities": "Wrestling halls · Boxing rings · Athletics track · Volleyball courts · Pool · Hostel",
        "coaches": 38,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "Primary SAI centre for West India. Gujarat athletes avoid long travel. Growing wrestling and boxing pipeline feeding into Patiala.",
        "nearby_states": ["Gujarat","Rajasthan","Maharashtra","Madhya Pradesh"],
    },
    {
        "name": "SAI STC Thiruvananthapuram (LNCPE)",
        "city": "Thiruvananthapuram", "state": "Kerala",
        "type": "STC", "region": "South",
        "sports": ["Athletics","Badminton","Football","Swimming","Volleyball","Table Tennis"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 13, "age_max": 23,
        "performance": ["State","National"],
        "capacity": 220,
        "facilities": "Athletics track · Badminton courts · Football ground · Pool · TT tables · Hostel",
        "coaches": 45,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "South Kerala hub. LNCPE is one of India's oldest sports institutes. PV Sindhu-effect driving badminton boom in this region.",
        "nearby_states": ["Kerala","Tamil Nadu","Karnataka"],
    },
    {
        "name": "SAI STC Pune",
        "city": "Pune", "state": "Maharashtra",
        "type": "STC", "region": "West",
        "sports": ["Boxing","Shooting","Athletics","Wrestling","Swimming","Cycling"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 12, "age_max": 24,
        "performance": ["State","National"],
        "capacity": 240,
        "facilities": "Boxing rings · Shooting range · Athletics track · Pool · Cycling track · Hostel",
        "coaches": 48,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "Maharashtra's primary SAI centre. Strong shooting infrastructure — Anjali Bhagwat connection. Cycling is growing rapidly here.",
        "nearby_states": ["Maharashtra","Goa","Karnataka","Madhya Pradesh"],
    },
    {
        "name": "SAI NCOE Delhi (Jawaharlal Nehru Stadium)",
        "city": "New Delhi", "state": "Delhi",
        "type": "NCOE", "region": "North",
        "sports": ["Athletics","Boxing","Wrestling","Shooting","Badminton","Volleyball"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 15, "age_max": 28,
        "performance": ["National","International"],
        "capacity": 350,
        "facilities": "Olympic track · Boxing rings · Shooting range · Badminton courts · Gymnasium · Sports Science Lab",
        "coaches": 80,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "National-level camp venue. Best for athletes who already have national selection and need camp-level preparation for international events.",
        "nearby_states": ["Delhi","Haryana","Uttar Pradesh","Punjab","Rajasthan","Uttarakhand"],
    },
    {
        "name": "SAI NCOE Jamshedpur",
        "city": "Jamshedpur", "state": "Jharkhand",
        "type": "NCOE", "region": "East",
        "sports": ["Hockey","Football","Archery","Athletics"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 12, "age_max": 22,
        "performance": ["District","State","National"],
        "capacity": 180,
        "facilities": "Hockey turf · Football ground · Archery range · Athletics track · Hostel",
        "coaches": 35,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "Jharkhand tribal talent pipeline. Hockey and archery are natural strengths from this region (Deepika Kumari's home state).",
        "nearby_states": ["Jharkhand","Odisha","West Bengal","Bihar","Chhattisgarh"],
    },
    {
        "name": "SAI STC Shillong",
        "city": "Shillong", "state": "Meghalaya",
        "type": "STC", "region": "Northeast",
        "sports": ["Archery","Football","Athletics","Boxing"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 10, "age_max": 21,
        "performance": ["Village","District","State"],
        "capacity": 120,
        "facilities": "Archery range · Football ground · Athletics track · Hostel",
        "coaches": 22,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "Key SAI feeder for Meghalaya and surrounding NE states. Entry point for tribal archery and football talent into the SAI system.",
        "nearby_states": ["Meghalaya","Assam","Nagaland","Tripura","Manipur","Mizoram"],
    },
    {
        "name": "SAI STC Guwahati",
        "city": "Guwahati", "state": "Assam",
        "type": "STC", "region": "Northeast",
        "sports": ["Athletics","Football","Boxing","Wrestling","Volleyball"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 11, "age_max": 22,
        "performance": ["District","State"],
        "capacity": 150,
        "facilities": "Athletics track · Football ground · Boxing rings · Hostel",
        "coaches": 28,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "Regional hub for Assam and NE athletes. Gateway to Imphal NCOE for athletes who advance to state/national level.",
        "nearby_states": ["Assam","Meghalaya","Nagaland","Arunachal Pradesh","Tripura"],
    },
    {
        "name": "SAI STC Chandigarh",
        "city": "Chandigarh", "state": "Chandigarh",
        "type": "STC", "region": "North",
        "sports": ["Hockey","Athletics","Wrestling","Cycling","Shooting"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 12, "age_max": 22,
        "performance": ["State","National"],
        "capacity": 160,
        "facilities": "Hockey turf · Athletics track · Cycling velodrome · Shooting range · Hostel",
        "coaches": 32,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "Close to NIS Patiala — athletes can easily upgrade. Strong cycling facility. Good for Punjab/Haryana hockey and cycling athletes.",
        "nearby_states": ["Punjab","Haryana","Himachal Pradesh","Chandigarh"],
    },
    {
        "name": "SAI STC Jalandhar",
        "city": "Jalandhar", "state": "Punjab",
        "type": "STC", "region": "North",
        "sports": ["Hockey","Wrestling","Athletics","Boxing"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 10, "age_max": 21,
        "performance": ["Village","District","State"],
        "capacity": 140,
        "facilities": "Hockey turf · Wrestling halls · Athletics track · Hostel",
        "coaches": 25,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "Deep grassroots feeder. Jalandhar is India's hockey heartland. Rural hockey players from Punjab villages enter the SAI system here.",
        "nearby_states": ["Punjab","Haryana","Himachal Pradesh"],
    },
    {
        "name": "SAI STC Hyderabad",
        "city": "Hyderabad", "state": "Telangana",
        "type": "STC", "region": "South",
        "sports": ["Athletics","Badminton","Boxing","Football","Table Tennis","Shooting"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 12, "age_max": 23,
        "performance": ["State","National"],
        "capacity": 200,
        "facilities": "Athletics track · Badminton courts · Shooting range · Football ground · Hostel",
        "coaches": 40,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "Growing hub for AP and Telangana athletes. Badminton boom post-Sindhu. Shooting growing fast with infrastructure investment.",
        "nearby_states": ["Telangana","Andhra Pradesh","Karnataka","Maharashtra"],
    },
    {
        "name": "SAI STC Chennai",
        "city": "Chennai", "state": "Tamil Nadu",
        "type": "STC", "region": "South",
        "sports": ["Athletics","Chess","Table Tennis","Badminton","Football","Swimming"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 12, "age_max": 24,
        "performance": ["State","National"],
        "capacity": 190,
        "facilities": "Athletics track · TT tables · Chess academy · Badminton courts · Pool · Hostel",
        "coaches": 38,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "TN's primary SAI centre. Chess is a unique offering (Viswanathan Anand effect). Strong athletics with TN sprinting culture.",
        "nearby_states": ["Tamil Nadu","Kerala","Karnataka","Andhra Pradesh"],
    },
    {
        "name": "SAI STC Bhubaneswar",
        "city": "Bhubaneswar", "state": "Odisha",
        "type": "STC", "region": "East",
        "sports": ["Hockey","Athletics","Football","Archery","Boxing"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 12, "age_max": 23,
        "performance": ["District","State","National"],
        "capacity": 220,
        "facilities": "World-class hockey turf · Athletics track · Football ground · Archery range · Hostel",
        "coaches": 45,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "Odisha is India's new hockey capital (Kalinga Stadium). SAI centre here feeds into Indian hockey national team pipeline directly.",
        "nearby_states": ["Odisha","Jharkhand","Chhattisgarh","West Bengal","Andhra Pradesh"],
    },
    {
        "name": "SAI STC Jaipur",
        "city": "Jaipur", "state": "Rajasthan",
        "type": "STC", "region": "North",
        "sports": ["Wrestling","Athletics","Archery","Kabaddi","Volleyball","Shooting"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 11, "age_max": 22,
        "performance": ["District","State"],
        "capacity": 150,
        "facilities": "Wrestling halls · Athletics track · Archery range · Shooting range · Hostel",
        "coaches": 28,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "Rajasthan's primary SAI centre. Rural wrestler and kabaddi talent pipeline. Archery growing from tribal communities in Udaipur/Banswara.",
        "nearby_states": ["Rajasthan","Gujarat","Madhya Pradesh","Haryana","Uttar Pradesh"],
    },
    {
        "name": "SAI STC Ranchi",
        "city": "Ranchi", "state": "Jharkhand",
        "type": "STC", "region": "East",
        "sports": ["Hockey","Archery","Football","Athletics","Wrestling"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 10, "age_max": 21,
        "performance": ["Village","District","State"],
        "capacity": 130,
        "facilities": "Hockey turf · Archery range · Football ground · Athletics track · Hostel",
        "coaches": 24,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "Tribal grassroots feeder in Jharkhand. Archery natural talent hotspot. MS Dhoni's home city — cricket culture, but hockey and archery are the real SAI strengths.",
        "nearby_states": ["Jharkhand","Bihar","Odisha","West Bengal","Chhattisgarh"],
    },
    {
        "name": "SAI STC Gwalior",
        "city": "Gwalior", "state": "Madhya Pradesh",
        "type": "STC", "region": "Central",
        "sports": ["Wrestling","Athletics","Shooting","Boxing","Cycling"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 12, "age_max": 22,
        "performance": ["District","State"],
        "capacity": 140,
        "facilities": "Wrestling halls · Athletics track · Shooting range · Cycling track · Hostel",
        "coaches": 26,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "Central India's secondary SAI centre. Cycling is unique strength. Wrestling pipeline feeding into Bhopal NCOE and then Patiala.",
        "nearby_states": ["Madhya Pradesh","Uttar Pradesh","Rajasthan","Chhattisgarh"],
    },
    {
        "name": "SAI STC Nagpur",
        "city": "Nagpur", "state": "Maharashtra",
        "type": "STC", "region": "West",
        "sports": ["Athletics","Boxing","Wrestling","Hockey","Kabaddi"],
        "gender": ["Male","Female","Mixed"],
        "age_min": 11, "age_max": 22,
        "performance": ["District","State"],
        "capacity": 160,
        "facilities": "Athletics track · Boxing rings · Hockey turf · Kabaddi courts · Hostel",
        "coaches": 30,
        "flagship": False,
        "website": "https://sportsauthorityofindia.nic.in",
        "notes": "Vidarbha region SAI centre. Feeds into Pune STC and then Patiala. Hockey from this region connects to the UP/MP hockey belt.",
        "nearby_states": ["Maharashtra","Madhya Pradesh","Chhattisgarh","Telangana"],
    },
]

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
        centre_perf_max = max([perf_map.get(p, 0) for p in c["performance"]])
        athlete_perf    = perf_map.get(performance_level, 2)
        if athlete_perf == centre_perf_max:
            s += 20
        elif abs(athlete_perf - centre_perf_max) == 1:
            s += 12
        else:
            s += 4

        # Age fit (10 pts)
        if c["age_min"] <= age <= c["age_max"]:
            s += 10
        elif abs(age - c["age_min"]) <= 2 or abs(age - c["age_max"]) <= 2:
            s += 5

        # Gender (5 pts)
        if gender in c["gender"] or "Mixed" in c["gender"]:
            s += 5

        scores.append({"centre": c, "score": s})

    scores.sort(key=lambda x: x["score"], reverse=True)
    return scores[:top_n]


def render_sai_card(centre, score, rank):
    sport_tags = "".join([f'<span class="tag">{s}</span>' for s in centre["sports"][:6]])
    badge_col  = "#81C995" if score >= 70 else ("#FDD663" if score >= 50 else "#F28B82")
    type_col   = "#8AB4F8" if centre["type"] == "NCOE" else "#C58AF9"
    flagship   = '<span class="tag green">★ Flagship</span>' if centre.get("flagship") else ""
    return f"""
    <div class="acard" style="border-left: 3px solid {badge_col}; margin-bottom:1rem;">
      <div class="acard-top">
        <div>
          <div class="acard-title">#{rank} {centre['name']} {flagship}</div>
          <div style="font-size:0.75rem;color:#9AA0A6;margin-top:3px;">
            📍 {centre['city']}, {centre['state']} &nbsp;|&nbsp;
            <span style="color:{type_col};font-weight:700;">{centre['type']}</span> &nbsp;|&nbsp;
            Capacity: {centre['capacity']} athletes &nbsp;|&nbsp; Coaches: {centre['coaches']}
          </div>
        </div>
        <div style="text-align:right;">
          <div class="acard-score" style="color:{badge_col};font-size:2rem;">{score}</div>
          <div style="font-size:0.62rem;color:#5F6368;letter-spacing:1px;">MATCH SCORE</div>
        </div>
      </div>
      <div class="acard-meta" style="margin:0.6rem 0;">📋 {centre['notes']}</div>
      <div class="acard-meta">🏟️ <b>Facilities:</b> {centre['facilities']}</div>
      <div class="acard-meta">🎯 <b>Best for performance level:</b> {' · '.join(centre['performance'])} &nbsp;|&nbsp; Age: {centre['age_min']}–{centre['age_max']}</div>
      <div class="acard-tags" style="margin-top:0.6rem;">{sport_tags}</div>
    </div>"""


with tab8:
    st.markdown('<div class="stitle">🏛️ SAI Centres <span class="chip chip-blue">Sports Authority of India — National Training Network</span></div>', unsafe_allow_html=True)

    st.markdown(insight("ℹ️ What is this?",
        "This section maps all major SAI (Sports Authority of India) centres across India — NCOEs (National Centres of Excellence) "
        "and STCs (SAI Training Centres). Use the <b>Smart Matcher</b> below to find the best SAI centre "
        "for any athlete based on their sport, state, age, and performance level.", ""), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Top stats ──
    s1,s2,s3,s4 = st.columns(4)
    with s1: st.markdown(mkpi("🏛️","Total SAI Centres", str(len(SAI_CENTRES)), "#8AB4F8"), unsafe_allow_html=True)
    with s2: st.markdown(mkpi("⭐","NCOEs (Elite)", str(len([c for c in SAI_CENTRES if c["type"]=="NCOE"])), "#FDD663"), unsafe_allow_html=True)
    with s3: st.markdown(mkpi("🏋️","STCs (Grassroots)", str(len([c for c in SAI_CENTRES if c["type"]=="STC"])), "#81C995"), unsafe_allow_html=True)
    with s4: st.markdown(mkpi("🤸","Total Capacity", f"{sum(c['capacity'] for c in SAI_CENTRES):,}", "#C58AF9"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # SMART ATHLETE-TO-CENTRE MATCHER
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    st.markdown("""
    <div style="background:linear-gradient(135deg,rgba(138,180,248,0.08),rgba(197,138,249,0.08));
         border:1px solid rgba(138,180,248,0.2);border-radius:20px;padding:2rem;margin-bottom:1.5rem;">
      <div style="font-family:Outfit,sans-serif;font-size:1.4rem;font-weight:800;color:#E8EAED;margin-bottom:0.3rem;">
        🎯 Smart SAI Centre Matcher
      </div>
      <div style="font-size:0.9rem;color:#9AA0A6;">
        Enter any athlete's profile and instantly get the top 3 SAI centres recommended for their training journey.
      </div>
    </div>
    """, unsafe_allow_html=True)

    all_sports_sai = sorted(set(s for c in SAI_CENTRES for s in c["sports"]))
    all_states_sai = sorted(set(c["state"] for c in SAI_CENTRES))
    all_states_india = sorted([
        "Andaman & Nicobar", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chandigarh",
        "Chhattisgarh", "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh",
        "Jammu & Kashmir", "Jharkhand", "Karnataka", "Kerala", "Ladakh", "Madhya Pradesh",
        "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha",
        "Puducherry", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
        "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
    ])

    f1, f2, f3, f4, f5 = st.columns([2,2,2,1,1])
    with f1:
        athlete_name = st.text_input("👤 Athlete Name", placeholder="e.g. Rohit Yadav", key="sai_name")
    with f2:
        athlete_sport = st.selectbox("🏃 Sport", all_sports_sai, key="sai_sport")
    with f3:
        athlete_state = st.selectbox("📍 Home State", all_states_india,
                                     index=all_states_india.index("Haryana") if "Haryana" in all_states_india else 0,
                                     key="sai_state")
    with f4:
        athlete_age = st.number_input("🎂 Age", min_value=8, max_value=35, value=17, step=1, key="sai_age")
    with f5:
        athlete_gender = st.selectbox("⚥ Gender", ["Male","Female","Mixed"], key="sai_gender")

    perf_options = ["Village","District","State","National","International"]
    athlete_perf = st.select_slider(
        "📈 Current Performance Level",
        options=perf_options,
        value="State",
        key="sai_perf",
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Results ──
    recommendations = recommend_sai_centres(athlete_sport, athlete_state, athlete_perf, athlete_age, athlete_gender, top_n=3)

    name_display = athlete_name.strip() if athlete_name.strip() else "This Athlete"
    st.markdown(f"""
    <div style="font-family:Outfit,sans-serif;font-size:1.1rem;font-weight:700;color:#E8EAED;margin:0.5rem 0 1rem;">
        📋 Top SAI Centre Recommendations for <span style="color:#8AB4F8;">{name_display}</span>
        &nbsp;—&nbsp; {athlete_sport} | {athlete_state} | Age {athlete_age} | {athlete_perf} Level
    </div>
    """, unsafe_allow_html=True)

    top_match_score = recommendations[0]["score"] if recommendations else 0

    if top_match_score < 40:
        st.markdown(insight("⚠️ Limited Match",
            f"No SAI centre has a strong match for <b>{athlete_sport}</b> from <b>{athlete_state}</b>. "
            f"Consider NIS Patiala (India's flagship, accepts all sports) or check if the athlete "
            f"can relocate to a state with a stronger {athlete_sport} SAI facility.", "amber"), unsafe_allow_html=True)
    else:
        st.markdown(insight("✅ Match Found",
            f"Showing top 3 SAI centre matches for this athlete profile. "
            f"The <b>Match Score</b> is calculated from sport fit (40 pts), location proximity (25 pts), "
            f"performance level alignment (20 pts), age range fit (10 pts), and gender inclusivity (5 pts).", "green"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    for i, rec in enumerate(recommendations):
        st.markdown(render_sai_card(rec["centre"], rec["score"], i+1), unsafe_allow_html=True)

    # ── What happens next ──
    st.markdown('<div class="stitle" style="font-size:1rem;">📌 Next Steps for the Athlete</div>', unsafe_allow_html=True)
    steps = [
        ("1️⃣","Apply to the top-matched SAI centre",
         f"Visit <b>sportsauthorityofindia.nic.in</b> and find open selection trials for <b>{athlete_sport}</b>. "
         f"Registration typically requires proof of performance (state championship result, district medals, coach recommendation)."),
        ("2️⃣","Get AthletIQ documentation",
         "AthletIQ can generate a standardised athlete profile card (performance records, physical stats, video links) "
         "that is accepted by SAI selection panels. This significantly improves selection chances."),
        ("3️⃣","Apply for funding if unfunded",
         "If the athlete is unfunded, AthletIQ's CSR matching engine can pair them with a corporate sponsor or "
         "government scheme (TOPS — Target Olympic Podium Scheme, Khelo India Scholarship) within 30 days."),
        ("4️⃣","Track development on AthletIQ's pipeline",
         f"Once at the SAI centre, the athlete enters AthletIQ's <b>Development → Elite → Podium</b> pipeline tracker. "
         f"CWG 2036 and Olympic 2032 selection dates are mapped automatically."),
    ]
    for em, title, body in steps:
        st.markdown(f"""
        <div class="acard" style="margin-bottom:0.6rem;">
          <div class="acard-title">{em} {title}</div>
          <div class="acard-meta" style="margin-top:0.4rem;">{body}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # ALL SAI CENTRES DIRECTORY
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    st.markdown('<div class="stitle">📂 Full SAI Centre Directory <span class="chip chip-green">Filterable</span></div>', unsafe_allow_html=True)

    dir_col1, dir_col2, dir_col3 = st.columns(3)
    with dir_col1:
        filter_region = st.multiselect("Region", sorted(sai_df["region"].unique()), default=sorted(sai_df["region"].unique()), key="dir_region")
    with dir_col2:
        filter_type = st.multiselect("Centre Type", sorted(sai_df["type"].unique()), default=sorted(sai_df["type"].unique()), key="dir_type")
    with dir_col3:
        filter_sport_dir = st.selectbox("Filter by Sport", ["All"] + all_sports_sai, key="dir_sport")

    sai_filtered = sai_df[sai_df["region"].isin(filter_region) & sai_df["type"].isin(filter_type)]
    if filter_sport_dir != "All":
        sai_filtered = sai_filtered[sai_filtered["sports"].apply(lambda s: filter_sport_dir in s)]

    # Charts
    dc1, dc2 = st.columns(2)
    with dc1:
        region_cap = sai_df.groupby("region")["capacity"].sum().reset_index()
        fig = px.bar(region_cap, x="region", y="capacity",
                     color="capacity", color_continuous_scale=COLOR_SCALES["purple"],
                     labels={"region":"","capacity":"Total Capacity"})
        playout(fig, "SAI Training Capacity by Region", h=280)
        fig.update_coloraxes(showscale=False)
        st.plotly_chart(fig, use_container_width=True)

    with dc2:
        # Sport coverage across all SAI centres
        sport_count = {}
        for c in SAI_CENTRES:
            for s in c["sports"]:
                sport_count[s] = sport_count.get(s,0) + 1
        sport_df_sai = pd.DataFrame(list(sport_count.items()), columns=["Sport","Centres"]).sort_values("Centres",ascending=True)
        fig = px.bar(sport_df_sai, y="Sport", x="Centres", orientation="h",
                     color="Centres", color_continuous_scale=COLOR_SCALES["teal"],
                     labels={"Sport":"","Centres":"# SAI Centres offering this sport"})
        playout(fig, "Which Sports Have the Most SAI Coverage?", h=400)
        fig.update_coloraxes(showscale=False)
        st.plotly_chart(fig, use_container_width=True)

    # Directory table
    dir_display = sai_filtered[["name","city","state","type","region","capacity","coaches"]].copy()
    dir_display.columns = ["Centre Name","City","State","Type","Region","Capacity","Coaches"]
    st.dataframe(dir_display, use_container_width=True, height=320)

    dl_sai = sai_df[["name","city","state","type","region","capacity","coaches","facilities","notes"]].to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download SAI Centres Directory (CSV)", dl_sai, "sai_centres_india.csv","text/csv", use_container_width=True)


with tab9:
    st.markdown('<div class="stitle">🏅 Elite Profiles <span class="chip chip-blue">India\'s Grassroots-to-Podium Elite</span></div>', unsafe_allow_html=True)

    st.markdown(insight("ℹ️ What is this?",
        "This directory profiles 180+ real elite Indian athletes across 10 sports. "
        "Use the search and filter controls below to explore. Click <b>🎯 Match SAI Centre</b> on any athlete "
        "card to find the best-matched Sports Authority of India (SAI) training centre for them.", "green"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Inline Filters ──
    f1, f2, f3, f4 = st.columns([2,2,1,2])
    with f1:
        search_query = st.text_input("🔍 Search Athlete Name", placeholder="e.g. Neeraj Chopra, Manu Bhaker", key="elite_search")
    with f2:
        all_sports = sorted(list(set(a["sport"] for a in elite_athletes)))
        selected_sports = st.multiselect("🏃 Sport Focus", all_sports, default=[], placeholder="All Sports", key="elite_sport_filter")
    with f3:
        selected_gender = st.selectbox("⚥ Gender", ["All", "M", "F"], key="elite_gender_filter")
    with f4:
        ages = []
        for a in elite_athletes:
            try: ages.append(int(a["age"]))
            except ValueError: pass
        min_age = min(ages) if ages else 10
        max_age = max(ages) if ages else 50
        selected_age_range = st.slider("🎂 Age Range", min_age, max_age, (min_age, max_age), key="elite_age_filter")

    # Filter data
    filtered_athletes = []
    for a in elite_athletes:
        if search_query.strip() and search_query.lower() not in a["name"].lower():
            continue
        if selected_sports and a["sport"] not in selected_sports:
            continue
        if selected_gender != "All" and a["gender"] != selected_gender:
            continue
        try:
            age_val = int(a["age"])
            if not (selected_age_range[0] <= age_val <= selected_age_range[1]):
                continue
        except ValueError:
            if selected_age_range[0] > min_age or selected_age_range[1] < max_age:
                continue
        filtered_athletes.append(a)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── KPIs ──
    k1, k2, k3, k4 = st.columns(4)
    with k1: st.markdown(mkpi("🏅", "Athletes Profiled", str(len(filtered_athletes)), "#8AB4F8"), unsafe_allow_html=True)
    with k2: st.markdown(mkpi("🥉", "Olympic Medallists", str(len([a for a in filtered_athletes if any(x in a["medals"].lower() for x in ["olympic", "paris 2024", "tokyo 2020", "london 2012", "rio 2016", "sydney 2000"])])), "#FDD663"), unsafe_allow_html=True)
    with k3: st.markdown(mkpi("🥇", "World/Junior Champions", str(len([a for a in filtered_athletes if any(x in a["medals"].lower() or x in a["records"].lower() for x in ["world champ", "world gold", "world record", "junior world", "youth world", "u20 world"])])), "#81C995"), unsafe_allow_html=True)
    with k4: st.markdown(mkpi("👩", "Female Representation", f"{len([a for a in filtered_athletes if a['gender'] == 'F'])} / {len(filtered_athletes)}", "#C58AF9"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── SAI CENTRE RECOMMENDATIONS PANEL (if an athlete is selected) ──
    if "matched_athlete" in st.session_state:
        m_ath = st.session_state["matched_athlete"]
        
        # Gender mapping
        m_gender = "Female" if m_ath["gender"] == "F" else "Male"
        
        # Age mapping
        try: m_age = int(m_ath["age"])
        except ValueError: m_age = 17
            
        # Performance level
        m_perf = "International" if any(x in m_ath["medals"].lower() for x in ["olympic", "world", "asian", "cwg", "issf", "international"]) else "National"
        
        # Infer home state
        m_state = "Haryana"
        state_keywords = {
            "haryana": "Haryana", "punjab": "Punjab", "delhi": "Delhi", "manipur": "Manipur",
            "maharashtra": "Maharashtra", "kerala": "Kerala", "tamil nadu": "Tamil Nadu",
            "odisha": "Odisha", "uttar pradesh": "Uttar Pradesh", "madhya pradesh": "Madhya Pradesh",
            "assam": "Assam", "telangana": "Telangana", "andhra": "Andhra Pradesh",
            "west bengal": "West Bengal", "rajasthan": "Rajasthan", "gujarat": "Gujarat",
            "jharkhand": "Jharkhand", "ranchi": "Jharkhand", "doha": "Haryana", "cairo": "Haryana"
        }
        for kw, st_name in state_keywords.items():
            if kw in m_ath["records"].lower() or kw in m_ath["medals"].lower():
                m_state = st_name
                break
                
        # Get recommendations
        recs = recommend_sai_centres(m_ath["sport"].title(), m_state, m_perf, m_age, m_gender, top_n=3)
        
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,rgba(138,180,248,0.1),rgba(197,138,249,0.1));
             border:1px solid rgba(138,180,248,0.3);border-radius:20px;padding:1.5rem;margin-bottom:1rem;position:relative;">
          <div style="font-family:Outfit,sans-serif;font-size:1.3rem;font-weight:800;color:#FFF;">
            🎯 Recommended SAI Centres for <span style="color:#8AB4F8;">{m_ath['name']}</span>
          </div>
          <div style="font-size:0.88rem;color:#9AA0A6;margin-top:0.2rem;">
            Profile: {m_ath['sport']} | {m_state} | Age {m_ath['age']} | {m_perf} Level
          </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Render top 3 SAI cards
        for idx, rec in enumerate(recs):
            st.markdown(render_sai_card(rec["centre"], rec["score"], idx+1), unsafe_allow_html=True)
            
        if st.button("❌ Close Matcher", key="clear_matched_athlete"):
            del st.session_state["matched_athlete"]
            st.rerun()
            
        st.markdown("<hr style='border-color:rgba(255,255,255,0.08);margin-bottom:2rem;'>", unsafe_allow_html=True)

    # ── Athlete Cards Grid ──
    if not filtered_athletes:
        st.info("No athletes match the selected filter criteria.")
    else:
        cols = st.columns(3)
        for idx, a in enumerate(filtered_athletes):
            col = cols[idx % 3]
            with col:
                medals_clean = a["medals"].replace("🥇", "🥇 ").replace("🥈", "🥈 ").replace("🥉", "🥉 ")
                
                tags_list = [tag(a["sport"], "purple"), tag(a["gender"], "")]
                if "olympic" in a["medals"].lower() or "olympics" in a["medals"].lower():
                    tags_list.append(tag("Olympic Medallist", "amber"))
                elif "world champ" in a["medals"].lower() or "world championships" in a["medals"].lower():
                    tags_list.append(tag("World Medalist", "green"))
                
                if a["age"].isdigit():
                    age_val = int(a["age"])
                    tags_list.append(tag(f"Age {age_val}", "blue"))
                    if age_val <= 20:
                        tags_list.append(tag("U20 Prospect", "green"))
                    elif age_val <= 23:
                        tags_list.append(tag("U23 Talent", "blue"))
                else:
                    tags_list.append(tag("Team / Crossover", "blue"))
                    
                tags_html = " ".join(tags_list)
                
                card_html = f"""
                <div class="acard" style="border-top: 3px solid var(--blue); height: 380px; display: flex; flex-direction: column; justify-content: space-between; margin-bottom:1rem;">
                  <div>
                    <div class="acard-top">
                      <div class="acard-title" style="font-size:1.15rem;color:#FFF;font-family:Outfit,sans-serif;">{a['name']}</div>
                      <div style="font-size:0.75rem;color:var(--text2);font-weight:700;">#{a['id']}</div>
                    </div>
                    <div class="acard-meta" style="margin-top: 0.2rem; min-height: 40px;">
                      <b>Event/Category:</b> {a['category']}<br>
                      <b>Gender:</b> {a['gender']} &nbsp;|&nbsp; <b>Age:</b> {a['age']}
                    </div>
                    <div style="margin-top: 0.6rem; font-size: 0.82rem; line-height: 1.5; color: #E8EAED; min-height: 50px;">
                      🏆 <b>Key Medals:</b> {medals_clean}
                    </div>
                    <div style="margin-top: 0.6rem; font-size: 0.82rem; line-height: 1.5; color: var(--text2); background:rgba(255,255,255,0.02); padding:0.6rem; border-radius:8px; border:1px solid rgba(255,255,255,0.04); min-height: 70px; max-height: 110px; overflow-y: auto;">
                      📝 <b>Records & Tally:</b> {a['records']}
                    </div>
                  </div>
                  <div>
                    <div class="acard-tags" style="margin-top: 0.8rem; justify-content: flex-start; margin-bottom:0.8rem;">
                      {tags_html}
                    </div>
                  </div>
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)
                if st.button("🎯 Match SAI Centre", key=f"btn_{a['sport']}_{a['id']}_{a['name']}", use_container_width=True):
                    st.session_state["matched_athlete"] = a
                    st.rerun()

    # ── Export ──
    st.markdown("<br>", unsafe_allow_html=True)
    df_export = pd.DataFrame(filtered_athletes)
    if not df_export.empty:
        csv_data = df_export.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Export Filtered Athletes to CSV", csv_data, "elite_athletes_filtered.csv", "text/csv", use_container_width=True)


# ─────────────────────────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
fl, fc, fr = st.columns([1,3,1])
with fc:
    full_csv = df_all.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download Full Master Database (CSV)", full_csv, "athletiq_master_database.csv","text/csv", use_container_width=True)

st.markdown("""
<div style="text-align:center;padding:2rem 0 1rem;border-top:1px solid rgba(255,255,255,0.05);margin-top:2rem;">
  <div style="font-family:Outfit,sans-serif;font-size:1.1rem;font-weight:700;
    background:linear-gradient(135deg,#8AB4F8,#C58AF9,#F28B82,#FDD663);
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">
    AthletIQ Intelligence Platform v3.0
  </div>
  <div style="color:#3C4043;font-size:0.78rem;margin-top:0.3rem;">
    Decision-first intelligence for CSR conversations · Sponsor prospecting · White paper inputs · FitEvents OS roadmap
  </div>
</div>
""", unsafe_allow_html=True)
