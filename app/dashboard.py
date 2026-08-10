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
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Inter:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

:root {
  --forest: #113E21;
  --forest-deep: #0A2A17;
  --forest-black: #081C10;
  --forest-soft: #1B4E2C;
  --gold: #B38B59;
  --gold-soft: #CBA97E;
  --gray: #F0F0F0;
  --white: #FEFEFE;
  --ink: #132318;
  --ink-soft: #3F5348;
  --line: rgba(17,62,33,0.14);
  --line-dark: rgba(254,254,254,0.12);
  --serif: 'Fraunces', serif;
  --sans: 'Inter', sans-serif;
  --mono: 'IBM Plex Mono', monospace;

  /* Theme variable maps */
  --blue: #113E21;
  --purple: #B38B59;
  --pink: #3F5348;
  --teal: #1B4E2C;
  --gold-theme: #B38B59;
  --text1: #132318;
  --text2: #3F5348;
  --text3: #3F5348;
  --border: rgba(17, 62, 33, 0.14);
}

/* Override Streamlit visual background */
.stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
    background-color: var(--white) !important;
    background-image: none !important;
    font-family: var(--sans) !important;
    color: var(--ink) !important;
}
.orb { display: none !important; }
.grid-3d { display: none !important; }

/* Metrics / KPIs */
.kpi {
    background: var(--white) !important;
    border: 1px solid var(--line) !important;
    border-radius: 0px !important;
    padding: 1.5rem 1.2rem;
    text-align: left;
    box-shadow: none !important;
    transition: border-color .3s;
}
.kpi:hover {
    transform: none !important;
    border-color: var(--gold) !important;
    box-shadow: none !important;
}
.kpi::before { display: none !important; }
.kpi-em { display: none !important; }
.kpi-label {
    font-family: var(--mono);
    font-size: 10px;
    letter-spacing: 0.05em;
    color: var(--ink-soft);
    text-transform: uppercase;
    margin-top: 6px;
}
.kpi-val {
    font-family: var(--serif);
    font-size: 30px;
    color: var(--forest) !important;
    font-weight: 500;
}
.kpi-sub {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--ink-soft);
    opacity: 0.6;
    margin-top: 4px;
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background-color: var(--gray) !important;
    border-right: 1px solid var(--line) !important;
}
section[data-testid="stSidebar"] .stMarkdown h3 {
    font-family: var(--mono) !important;
    font-size: 11px !important;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: var(--gold) !important;
}
[data-testid="stSidebar"] div[role="radiogroup"] label {
    font-family: var(--mono) !important;
    font-size: 11px !important;
    letter-spacing: 0.05em !important;
    color: var(--ink-soft) !important;
    background-color: var(--white) !important;
    border: 1px solid var(--line) !important;
    border-radius: 0px !important;
    padding: 8px 14px !important;
    margin-bottom: 0.6rem !important;
    transition: all 0.2s ease !important;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background-color: var(--gray) !important;
    border-color: var(--gold) !important;
    color: var(--forest) !important;
}
[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"],
[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
    background-color: var(--forest) !important;
    border-color: var(--forest) !important;
    color: var(--white) !important;
}

/* Global button styling */
.stButton > button, .stDownloadButton > button {
    background: var(--forest) !important;
    color: var(--white) !important;
    border: none !important;
    border-radius: 0px !important;
    padding: 10px 20px !important;
    font-family: var(--mono) !important;
    font-size: 12px !important;
    letter-spacing: 0.05em !important;
    text-transform: uppercase !important;
    box-shadow: none !important;
    transition: background 0.3s ease !important;
}
.stButton > button:hover, .stDownloadButton > button:hover {
    background: var(--forest-deep) !important;
    color: var(--white) !important;
    border: none !important;
    transform: none !important;
}

/* Selectbox styling */
div[data-baseweb="select"] > div {
    background-color: var(--white) !important;
    border: 1px solid var(--line) !important;
    border-radius: 0px !important;
    color: var(--ink) !important;
    box-shadow: none !important;
}
div[data-baseweb="select"] > div:hover {
    border-color: var(--gold) !important;
}
div[data-baseweb="select"] span {
    color: var(--ink) !important;
    font-family: var(--sans) !important;
}

/* Section titles */
.stitle {
    font-family: var(--serif) !important;
    font-weight: 500 !important;
    font-size: 26px !important;
    color: var(--forest) !important;
    margin-bottom: 1.5rem !important;
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
}
.chip {
    font-family: var(--mono) !important;
    font-size: 10px !important;
    letter-spacing: 0.05em !important;
    text-transform: uppercase !important;
    padding: 4px 10px !important;
    border-radius: 0px !important;
}
.chip-blue, .chip-green, .chip-amber, .chip-red, .chip-purple {
    background: transparent !important;
    border: 1px solid var(--line) !important;
    color: var(--gold) !important;
}

/* Actions cards */
.acard {
    background: var(--white) !important;
    border: 1px solid var(--line) !important;
    border-radius: 0px !important;
    padding: 1.5rem !important;
    margin-bottom: 1rem !important;
    box-shadow: none !important;
    transform: none !important;
    transition: border-color .3s !important;
}
.acard:hover {
    background: var(--white) !important;
    border-color: var(--gold) !important;
    transform: none !important;
    box-shadow: none !important;
}
.acard-title {
    font-family: var(--serif) !important;
    font-weight: 500 !important;
    font-size: 20px !important;
    color: var(--forest) !important;
}
.acard-meta {
    font-family: var(--mono) !important;
    font-size: 11.5px !important;
    color: var(--ink-soft) !important;
}
.acard-score {
    font-family: var(--serif) !important;
    font-size: 24px !important;
    color: var(--forest) !important;
}

/* Tags */
.tag {
    font-family: var(--mono) !important;
    font-size: 9.5px !important;
    letter-spacing: 0.05em !important;
    text-transform: uppercase !important;
    padding: 3px 8px !important;
    border-radius: 0px !important;
    border: 1px solid var(--line) !important;
    background: transparent !important;
    color: var(--ink-soft) !important;
}
.tag.green { color: var(--forest) !important; border-color: var(--forest) !important; }
.tag.amber { color: var(--gold) !important; border-color: var(--gold) !important; }
.tag.purple { color: var(--gold) !important; border-color: var(--gold) !important; }

/* Insight block */
.insight {
    background: var(--gray) !important;
    border: 1px solid var(--line) !important;
    border-left: 3px solid var(--forest) !important;
    border-radius: 0px !important;
    padding: 1.2rem !important;
}
.insight-title {
    font-family: var(--serif) !important;
    font-weight: 500 !important;
    font-size: 16px !important;
    color: var(--forest) !important;
}
.insight-body {
    font-family: var(--sans) !important;
    font-size: 14px !important;
    color: var(--ink-soft) !important;
}

/* Dataframe tables */
.stDataFrame {
    border-radius: 0px !important;
    border: 1px solid var(--line) !important;
}

/* Text input search */
input[data-testid="stTextInput-Input"] {
    background-color: var(--white) !important;
    border: 1px solid var(--line) !important;
    border-radius: 0px !important;
    color: var(--ink) !important;
}
input[data-testid="stTextInput-Input"]:focus {
    border-color: var(--gold) !important;
}

/* Tab selector */
.stTabs [data-baseweb="tab-list"] {
    background: transparent !important;
    border: none !important;
    border-radius: 0px !important;
    padding: 0 !important;
    gap: 12px !important;
    box-shadow: none !important;
    margin-bottom: 2rem !important;
}
.stTabs [data-baseweb="tab"] {
    background: var(--white) !important;
    border: 1px solid var(--line) !important;
    border-radius: 0px !important;
    color: var(--ink-soft) !important;
    font-family: var(--mono) !important;
    font-size: 11px !important;
    letter-spacing: 0.04em !important;
    padding: 9px 18px !important;
    transition: all .25s !important;
}
.stTabs [data-baseweb="tab"]:hover {
    border-color: var(--gold) !important;
    color: var(--forest) !important;
    background: var(--white) !important;
}
.stTabs [aria-selected="true"] {
    background: var(--forest) !important;
    color: var(--white) !important;
    border-color: var(--forest) !important;
    box-shadow: none !important;
}

/* Hero section formatting */
.hero-subtitle {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--gold);
    letter-spacing: 1.5px;
    margin-bottom: 1rem;
    font-weight: 500;
}
.hero-heading {
    font-family: var(--serif);
    font-size: 3.2rem;
    line-height: 1.15;
    color: var(--forest);
    margin: 0 0 1.5rem 0;
    font-weight: 500;
}
.hero-heading .highlight {
    color: var(--gold);
    font-style: italic;
}
.hero-description {
    font-family: var(--sans);
    font-size: 0.95rem;
    color: var(--ink-soft);
    line-height: 1.6;
    margin-bottom: 2rem;
}

/* Hierarchy Tree Visual */
.hierarchy-tree-container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    padding: 1rem 0;
}
.hierarchy-tree {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    width: 100%;
}
.tree-node {
    background: var(--white);
    border: 1px solid var(--line);
    padding: 0.5rem 1rem;
    min-width: 200px;
    text-align: center;
    border-radius: 0px;
    z-index: 2;
    box-shadow: 0 4px 15px rgba(0,0,0,0.02);
    transition: all 0.3s ease;
}
.tree-node.active-node {
    background: var(--forest);
    border-color: var(--forest);
    color: var(--white);
}
.tree-node.active-node-bottom {
    background: var(--forest);
    border-color: var(--forest);
    color: var(--white);
}
.tree-node .node-tag {
    font-family: var(--mono);
    font-size: 8px;
    color: var(--gold);
    letter-spacing: 0.8px;
    text-transform: uppercase;
    margin-bottom: 0.15rem;
}
.tree-node .node-title {
    font-family: var(--sans);
    font-size: 12px;
    font-weight: 600;
}
.tree-node.active-node .node-title, .tree-node.active-node-bottom .node-title {
    font-family: var(--serif);
    font-size: 13px;
    font-weight: 500;
    color: var(--white);
}
.tree-line {
    width: 1px;
    height: 24px;
    border-left: 1px dashed var(--gold);
    z-index: 1;
}
</style>
<img src="x" onerror="
    if (!window.focusListenerAdded) {
        window.focusListenerAdded = true;
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
    template="plotly_white",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter, sans-serif", color="#132318", size=12),
    margin=dict(l=30, r=20, t=45, b=35),
    colorway=["#113E21","#B38B59","#1B4E2C","#3F5348","#CBA97E","#0A2A17"],
    legend=dict(bgcolor="rgba(240,240,240,0.8)", bordercolor="rgba(17,62,33,0.14)", borderwidth=1, font=dict(size=11)),
    xaxis=dict(gridcolor="rgba(17,62,33,0.06)", linecolor="rgba(17,62,33,0.14)"),
    yaxis=dict(gridcolor="rgba(17,62,33,0.06)", linecolor="rgba(17,62,33,0.14)"),
)

def playout(fig, title="", h=400):
    fig.update_layout(**PL,
        title=dict(text=title, font=dict(size=16, family="Fraunces, serif", color="#113E21")), height=h)
    return fig

COLOR_SCALES = {
    "blue": ["#F0F0F0","#113E21"],
    "purple": ["#F0F0F0","#B38B59"],
    "teal": ["#F0F0F0","#1B4E2C"],
    "gold": ["#F0F0F0","#B38B59"],
    "pink": ["#F0F0F0","#3F5348"],
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
        
    if "sport" in df.columns:
        def clean_sport(name):
            name = name.replace("§", "").strip()
            if name == "Athetics":
                return "Athletics"
            if name == "Kho kho":
                return "Kho Kho"
            return name
        df["sport"] = df["sport"].apply(clean_sport)
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

# Dynamically inject women athletes into df_all
women_path, women_mtime = find_file(["../data/women_athletes.json", "data/women_athletes.json", "./data/women_athletes.json"])
if women_path and df_all is not None:
    try:
        with open(women_path, "r", encoding="utf-8") as wf:
            women_athletes_data = json.load(wf)
        if women_athletes_data:
            df_women = pd.DataFrame(women_athletes_data)
            df_women["entity_type"] = "Athlete"
            
            # Map key names to match df_all columns
            if "notes" not in df_women.columns:
                df_women["notes"] = df_women["achievements"].fillna("") + " | " + df_women["remarks"].fillna("")
            if "cwg_2036_relevance" not in df_women.columns:
                df_women["cwg_2036_relevance"] = 8.0
            if "olympic_2032_relevance" not in df_women.columns:
                df_women["olympic_2032_relevance"] = 8.0
            if "digital_readiness" not in df_women.columns:
                df_women["digital_readiness"] = 7.0
            if "pipeline_stage" not in df_women.columns:
                df_women["pipeline_stage"] = "Discovery"
            if "participants_or_capacity" not in df_women.columns:
                df_women["participants_or_capacity"] = 1.0
            if "frequency" not in df_women.columns:
                df_women["frequency"] = "Daily"
            if "tags" not in df_women.columns:
                df_women["tags"] = df_women["sport"].str.lower() + ",women,grassroots"
            if "source_link" not in df_women.columns:
                df_women["source_link"] = "Official Registry"
            
            # Fill missing columns from df_all with default/None
            for col in df_all.columns:
                if col not in df_women.columns:
                    df_women[col] = None
                    
            df_women = df_women[df_all.columns]
            df_all = pd.concat([df_all, df_women], ignore_index=True)
    except Exception as e:
        pass

# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR NAVIGATION & FILTERS
# ─────────────────────────────────────────────────────────────────────────────
# ── TOP HORIZONTAL NAVIGATION ──
st.markdown('''<style>
/* Remove background transparent overlays and dark mode defaults */
.st-emotion-cache-1jicfl2 {
    background-color: var(--white) !important;
}

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
    /* Hide the radio button circles completely */
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
        border-radius: 0px !important;
        margin-right: 0.2rem;
        cursor: pointer;
        background: transparent;
        transition: all 0.2s ease;
    }
    div[data-testid="stRadio"] label p {
        font-family: var(--sans) !important;
        font-size: 13.5px !important;
        color: var(--ink-soft) !important;
        margin-bottom: 0 !important;
    }
    div[data-testid="stRadio"] label:hover {
        background: transparent !important;
    }
    div[data-testid="stRadio"] label:hover p {
        color: var(--forest) !important;
    }
    /* Active State styling */
    div[data-testid="stRadio"] label[data-checked="true"],
    div[data-testid="stRadio"] label:has(input:checked) {
        background: transparent !important;
        border: none !important;
        border-bottom: 2px solid var(--gold) !important;
    }
    div[data-testid="stRadio"] label[data-checked="true"] p,
    div[data-testid="stRadio"] label:has(input:checked) p {
        color: var(--forest) !important;
        font-weight: 600 !important;
        text-shadow: none !important;
    }
</style>''', unsafe_allow_html=True)

if "main_navigation" not in st.session_state:
    st.session_state.main_navigation = "Pathway Overview"

nav_options = [
    "Pathway Overview",
    "Discovery & Leagues",
    "Centres & Academies",
    "Sponsor Pipeline",
    "Profile",
    "Womens",
    "AI Assistant"
]

if "main_navigation" not in st.session_state:
    st.session_state.main_navigation = "Pathway Overview"

# Programmatic redirection handling
if st.session_state.get("nav_to_profile", False):
    st.session_state.nav_radio = "Profile"
    st.session_state.main_navigation = "Profile"
    st.session_state.nav_to_profile = False

# Set default of key-bound state if not set
if "nav_radio" not in st.session_state:
    st.session_state.nav_radio = st.session_state.main_navigation

selected_tab = st.radio(
    label="Navigation",
    options=nav_options,
    label_visibility="collapsed",
    key="nav_radio",
    horizontal=True
)

st.session_state.main_navigation = selected_tab

# Global Settings (API Key configuration shared by chatbot and live search features)
with st.sidebar:
    st.markdown("### Settings")
    api_key_input = st.text_input(
        "Gemini API Key",
        type="password",
        key="global_api_key",
        help="Enter your Gemini API Key or set GEMINI_API_KEY environment variable"
    )
api_key = api_key_input or os.environ.get("GEMINI_API_KEY")



# Track navigation history
if "nav_history" not in st.session_state:
    st.session_state.nav_history = []

if "current_tab" not in st.session_state:
    st.session_state.current_tab = selected_tab

if st.session_state.current_tab != selected_tab:
    # Only append to history if it is different from the last state in history
    if not st.session_state.nav_history or st.session_state.nav_history[-1] != st.session_state.current_tab:
        st.session_state.nav_history.append(st.session_state.current_tab)
    st.session_state.current_tab = selected_tab

# Back button handler
def go_back():
    if st.session_state.nav_history:
        prev_tab = st.session_state.nav_history.pop()
        st.session_state.main_navigation = prev_tab
        st.session_state.current_tab = prev_tab




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
          <div style="font-size:0.75rem;color:var(--ink-soft);margin-top:3px;">
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
<div class="hero" style="padding: 2.5rem 1rem 1.5rem; text-align: center; display: flex; flex-direction: column; align-items: center; gap: 10px;">
  <div class="wordmark" style="display: inline-flex; align-items: center; gap: 12px; text-align: left;">
    <svg viewBox="0 0 32 32" fill="none" style="width: 48px; height: 48px;">
      <circle cx="16" cy="16" r="13" stroke="#113E21" stroke-width="1.4"/>
      <circle cx="16" cy="16" r="2.4" fill="#B38B59"/>
      <path d="M16 3v6M16 23v6M3 16h6M23 16h6" stroke="#113E21" stroke-width="1.2"/>
    </svg>
    <span class="wordmark-text" style="font-family: 'Fraunces', serif; font-size: 32px; color: #113E21; font-weight: 500; line-height: 1.1;">
      AthletIQ
      <span class="sub" style="display: block; font-family: 'IBM Plex Mono', monospace; font-size: 11px; letter-spacing: 0.18em; color: #B38B59; text-transform: uppercase; margin-top: 1px;">India Sports Intelligence</span>
    </span>
  </div>
  <div class="eyebrow" style="margin-top: 1rem; font-family: 'IBM Plex Mono', monospace; font-size: 11px; letter-spacing: 0.16em; text-transform: uppercase; color: #B38B59; display: flex; align-items: center; gap: 10px; justify-content: center;">Live Pathway Tracking</div>
</div>
""", unsafe_allow_html=True)


def get_live_tournaments():
    import os
    import json
    import random
    import datetime
    
    # Try to load API key from global setting
    global_key = st.session_state.get("global_api_key") or os.environ.get("GEMINI_API_KEY")
    
    if global_key:
        try:
            from google import genai
            from google.genai import types
            
            # Cache the live search results for 1 hour to prevent hitting the API repeatedly on runs
            @st.cache_data(ttl=3600)
            def fetch_real_tournaments(key):
                client = genai.Client(api_key=key)
                prompt = """
                Search the web and return a JSON list of 12 real, actual sports tournaments (grassroots, junior, sub-junior, or national level) being held or scheduled to be held in India during August 2026 or late 2026.
                Examples: Khelo India Games, Senior/Junior National Championships, state selection trials, local cups.
                For each tournament, provide:
                1. "Tournament/League Name" (e.g. "Khelo India Women's Hockey League")
                2. "Sport" (e.g. "Hockey", "Wrestling", "Athletics", "Boxing", "Archery", "Shooting", "Weightlifting", "Badminton")
                3. "State" (e.g. "Haryana", "Maharashtra", "Punjab", etc.)
                4. "League Level" (e.g. "State Selection Trial", "Khelo India Cadet Roster", "Sub-Junior Nationals", "Zonal Championship", "District Cup")
                5. "Gender" (e.g. "Male", "Female", "Mixed")
                6. "Participants" (e.g. "120 Athletes")
                7. "Funding Status" (e.g. "Fully Funded", "Partially Funded", "Unfunded")
                8. "Live Status" (One of: '🔴 LIVE NOW', '⏳ STARTING SOON', 'Scheduled', 'Completed', 'Just Completed')
                9. "Action Details" (e.g. "Final rounds in progress" or "Starts in 4 hours" or "Results uploaded")
                
                Return ONLY a raw JSON array matching this exact format, with no markdown code block wraps:
                [
                  {
                    "Tournament/League Name": "Name",
                    "Sport": "Wrestling",
                    "State": "Haryana",
                    "League Level": "State Selection Trial",
                    "Gender": "Male/Female/Mixed",
                    "Participants": "120 Athletes",
                    "Funding Status": "Fully Funded",
                    "Live Status": "🔴 LIVE NOW",
                    "Action Details": "Final rounds in progress"
                  }
                ]
                """
                
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        tools=[types.Tool(google_search=types.GoogleSearch())],
                        response_mime_type="application/json"
                    )
                )
                
                text = response.text.strip()
                if text.startswith("```json"):
                    text = text[7:]
                if text.endswith("```"):
                    text = text[:-3]
                text = text.strip()
                
                return json.loads(text)
                
            real_data = fetch_real_tournaments(global_key)
            if real_data and isinstance(real_data, list) and len(real_data) > 0:
                formatted_tournaments = []
                for t in real_data:
                    formatted_tournaments.append({
                        "Tournament/League Name": t.get("Tournament/League Name", "Tournament"),
                        "Sport": t.get("Sport", "Athletics").title(),
                        "League Level": t.get("League Level", "Sub-Junior Nationals"),
                        "Gender": t.get("Gender", "Mixed"),
                        "State": t.get("State", "Delhi"),
                        "Participants": t.get("Participants", "100 Athletes"),
                        "Funding Status": t.get("Funding Status", "Partially Funded"),
                        "Live Status": t.get("Live Status", "Scheduled"),
                        "Action Details": t.get("Action Details", "Starts soon")
                    })
                return formatted_tournaments
        except Exception as e:
            pass

    # FALLBACK MOCK DATA GENERATOR (Used if no API key is supplied or search fails)
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
            "Participants": f"{t['participants']} Athletes",
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
    # 2-Column Hero Landing Section (as requested in the second photo)
    col_hero_l, col_hero_r = st.columns([3, 2])
    with col_hero_l:
        st.markdown("""
            <div class="hero-subtitle">—— INDIA'S SPORTS INTELLIGENCE LAYER</div>
            <h1 class="hero-heading">Every athlete.<br>Every coach.<br><span class="highlight">One intelligence system.</span></h1>
            <p class="hero-description">
                AthletIQ structures India's entire sporting ecosystem — athletes, coaches, sports, competitions and medals — into one connected, searchable, drillable intelligence platform.
            </p>
        """, unsafe_allow_html=True)
        
        # Render action buttons (Explore Platform redirects to Profile; See Map scrolls down)
        btn_col1, btn_col2 = st.columns([1, 1])
        with btn_col1:
            if st.button("Explore the Platform →", key="explore_platform_btn", type="primary", use_container_width=True):
                st.session_state.nav_to_profile = True
                st.session_state.main_navigation = "Profile"
                st.rerun()
        with btn_col2:
            st.markdown('<a href="#interactive-india-sports-map" style="display:inline-block; margin-top:0.6rem; color:var(--forest); font-family:var(--sans); font-size:0.95rem; font-weight:600; text-decoration:underline;">See the India map</a>', unsafe_allow_html=True)

    with col_hero_r:
        st.markdown("""
            <div class="hierarchy-tree-container">
                <div class="hierarchy-tree">
                    <div class="tree-node active-node">
                        <div class="node-tag" style="color: #FEFEFE !important;">INDIA</div>
                        <div class="node-title">National Layer</div>
                    </div>
                    <div class="tree-line"></div>
                    <div class="tree-node">
                        <div class="node-tag">STATE</div>
                        <div class="node-title">36 States & UTs</div>
                    </div>
                    <div class="tree-line"></div>
                    <div class="tree-node">
                        <div class="node-tag">DISTRICT</div>
                        <div class="node-title">700+ Districts</div>
                    </div>
                    <div class="tree-line"></div>
                    <div class="tree-node">
                        <div class="node-tag">SPORT</div>
                        <div class="node-title">42 Disciplines</div>
                    </div>
                    <div class="tree-line"></div>
                    <div class="tree-node">
                        <div class="node-tag">CATEGORY</div>
                        <div class="node-title">U-12 · Senior</div>
                    </div>
                    <div class="tree-line"></div>
                    <div class="tree-node active-node-bottom">
                        <div class="node-tag" style="color: #FEFEFE !important;">ATHLETE</div>
                        <div class="node-title">Priya Singh · Boxing</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")

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
        font-family: var(--sans);
        background-color: transparent;
    }}
    .section-heading {{
        color: var(--gold);
        font-family: var(--mono);
        font-size: 11px;
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
        background-color: var(--line);
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
        font-family: var(--mono);
        font-size: 0.75rem;
        color: var(--gold);
        margin-bottom: 0.5rem;
    }}
    .step-circle {{
        width: 55px;
        height: 55px;
        border-radius: 50%;
        background-color: var(--white);
        border: 1px solid var(--line);
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--ink-soft);
        margin-bottom: 0.8rem;
    }}
    .step-circle svg {{
        width: 24px;
        height: 24px;
        stroke: var(--forest);
    }}
    .step-circle.active {{
        background-color: var(--forest);
        border-color: var(--forest);
        color: var(--white);
        box-shadow: none;
    }}
    .step-circle.active svg {{
        stroke: var(--white);
    }}
    .step-label {{
        font-family: var(--serif);
        font-size: 15px;
        font-weight: 500;
        color: var(--forest);
    }}
    .step-label.active {{
        color: var(--gold);
    }}
    .stats-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.5rem;
    }}
    .stat-card {{
        background-color: var(--white);
        border-radius: 0px;
        padding: 2rem 1.5rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        position: relative;
        border: 1px solid var(--line);
    }}
    .stat-icon-wrapper {{
        display: none;
    }}
    .stat-value {{
        font-family: var(--serif);
        font-size: 30px;
        font-weight: 500;
        color: var(--forest);
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
        text-align: center;
    }}
    .stat-label {{
        font-family: var(--mono);
        font-size: 10px;
        text-transform: uppercase;
        color: var(--ink-soft);
        text-align: center;
        letter-spacing: 0.05em;
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

        # 4. Interactive India Sports Map
    st.markdown("""<div class="stitle" title="Interactive map of India's states. Click on a state to view top athlete profiles." style="font-size:1.15rem;margin-top:2rem;"> Interactive India Sports Map</div>""", unsafe_allow_html=True)
    st.markdown("<p style='font-family: var(--sans); font-size:0.9rem; color: var(--ink-soft); margin-bottom: 1.5rem;'>Click on any state to explore its mapped athlete profiles and regional registry:</p>", unsafe_allow_html=True)

    import json
    import plotly.express as px

    try:
        with open("data/india.geojson", "r") as f:
            india_geojson = json.load(f)
            
        # Get count of athletes in each state from df_all
        athletes_df = df_all[df_all["entity_type"] == "Athlete"]
        state_counts = athletes_df["state"].value_counts().reset_index()
        state_counts.columns = ["state", "athlete_count"]
        
        # Map database state names to the new optimized GeoJSON ST_NM values
        def map_state_name_to_geojson(st_name):
            if st_name == "Jammu & Kashmir":
                return "Jammu and Kashmir"
            return st_name
            
        state_counts["geojson_state"] = state_counts["state"].apply(map_state_name_to_geojson)
        
        # Assign a numerical ID for coloring to keep it as a single trace and avoid HTML duplication
        state_counts["state_color_id"] = range(len(state_counts))

        # Draw choropleth map using numerical state_color_id
        fig_map = px.choropleth(
            state_counts,
            geojson=india_geojson,
            locations="geojson_state",
            featureidkey="properties.ST_NM",
            color="state_color_id",
            color_continuous_scale=["#CBA97E", "#113E21", "#B38B59", "#1B4E2C", "#3F5348", "#CBA97E"],
            hover_name="state",
            hover_data={"geojson_state": False, "athlete_count": True, "state_color_id": False, "state": False},
            labels={"athlete_count": "Athletes Registered"}
        )
        fig_map.update_geos(
            projection_type="mercator",
            lonaxis_range=[68.0, 98.0],
            lataxis_range=[7.0, 36.0],
            visible=False
        )
        fig_map.update_coloraxes(showscale=False)
        fig_map.update_layout(
            height=750,
            margin=dict(l=0, r=0, t=10, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            showlegend=False,
            dragmode=False,
            clickmode="event+select"
        )
        
        # Render the map and handle click select event
        event = st.plotly_chart(fig_map, use_container_width=True, on_select='rerun', key='india_state_map_select', config={'scrollZoom': False, 'displayModeBar': False})
        
        # Support both dictionary and object formats
        points = []
        if event:
            if isinstance(event, dict):
                points = event.get("selection", {}).get("points", [])
            else:
                try:
                    points = event.selection.points
                except AttributeError:
                    pass
        
        if points and len(points) > 0:
            point0 = points[0]
            if isinstance(point0, dict):
                clicked_location = point0.get("location")
            else:
                clicked_location = getattr(point0, "location", None)
            if clicked_location:
                # Reverse map
                db_state = clicked_location
                if clicked_location == "Jammu and Kashmir":
                    db_state = "Jammu & Kashmir"
                    
                st.session_state.profile_state = db_state
                st.session_state.main_navigation = "Profile"
                st.session_state.profile_selected_athlete = "-- Select Athlete --"
                st.session_state.athlete_selected_level = None
                st.session_state.nav_to_profile = True
                st.rerun()
                
    except Exception as e:
        st.error(f"Error loading map: {e}")

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
    <div style="background:rgba(16, 229, 179, 0.08);border:1px solid rgba(16, 229, 179, 0.25);border-radius:12px;padding:0.8rem 1.2rem;margin-bottom:1rem;font-size:0.88rem;color:var(--forest);display:flex;align-items:center;gap:1.5rem;">
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
                    <div style="margin-top:1rem; padding-top:0.8rem; border-top:1px solid var(--line); font-size:0.75rem; display:flex; flex-direction: column; gap:0.3rem; color: var(--ink);">
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
        
    ca_sub_tab = st.segmented_control(
        label="Centres & Academies Sub-Navigation",
        options=[
            "Coach-to-Athlete Ratios & Capacity",
            "SAI Centres & NCOEs",
            "Private Academies & Akharas",
            "SAI Proximity Matcher"
        ],
        label_visibility="collapsed",
        key="ca_sub_navigation",
        selection_mode="single",
        default="Coach-to-Athlete Ratios & Capacity"
    )
    if not ca_sub_tab:
        ca_sub_tab = "Coach-to-Athlete Ratios & Capacity"
    
    if ca_sub_tab == "Coach-to-Athlete Ratios & Capacity":
        st.markdown('<div class="stitle" style="font-size:1.15rem;"> Coach Capacity & Ratio Insights</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            all_centres = sai_df["name"].unique().tolist()
            selected_centre = st.selectbox("Select SAI Centre", all_centres, key="ca_selected_centre")
        
        centre_row = sai_df[sai_df["name"] == selected_centre].iloc[0]
        centre_sports = centre_row["sports"]
        with col2:
            selected_sport = st.selectbox("Select Sport", centre_sports, key="ca_selected_sport")
        
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

    elif ca_sub_tab == "SAI Centres & NCOEs":
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

    elif ca_sub_tab == "Private Academies & Akharas":
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

    elif ca_sub_tab == "SAI Proximity Matcher":
        st.markdown('<div class="stitle" style="font-size:1.15rem;"> 🔍 SAI Training Centre Proximity & Suitability Matcher</div>', unsafe_allow_html=True)
        # Toggle between Database search and Custom Profile Creator
        matcher_mode = st.segmented_control(
            "Choose Athlete Matching Mode:",
            options=["Search Database Athletes", "Create Custom Athlete Profile"],
            selection_mode="single",
            default="Search Database Athletes",
            key="top_matcher_mode"
        )
        if not matcher_mode:
            matcher_mode = "Search Database Athletes"

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
    
    # 2. Category, Location, & Name Search Filters
    col_spt, col_st, col_name = st.columns([1, 1, 1.2])
    with col_spt:
        sports_list = ["All Sports"] + sorted(list(df_all["sport"].unique()))
        sport_choice = st.selectbox("Sport Focus", sports_list, key="profile_sport")
    with col_st:
        states_list = ["All States"] + sorted(list(df_all["state"].unique()))
        state_choice = st.selectbox("State Registry", states_list, key="profile_state")
    with col_name:
        name_query = st.text_input("Search Name", placeholder="Type athlete or coach name...", key="profile_name_search")
        
    # Filter datasets for both Athletes and Coaches
    filtered_athletes = df_all[df_all["entity_type"] == "Athlete"].copy()
    filtered_coaches = df_all[df_all["entity_type"] == "Coach"].copy()
    
    if sport_choice != "All Sports":
        filtered_athletes = filtered_athletes[filtered_athletes["sport"].str.lower() == sport_choice.lower()]
        filtered_coaches = filtered_coaches[filtered_coaches["sport"].str.lower() == sport_choice.lower()]
    if state_choice != "All States":
        filtered_athletes = filtered_athletes[filtered_athletes["state"].str.lower() == state_choice.lower()]
        filtered_coaches = filtered_coaches[filtered_coaches["state"].str.lower() == state_choice.lower()]
    if name_query.strip():
        filtered_athletes = filtered_athletes[filtered_athletes["name"].str.lower().str.contains(name_query.strip().lower(), na=False)]
        filtered_coaches = filtered_coaches[filtered_coaches["name"].str.lower().str.contains(name_query.strip().lower(), na=False)]
        
    # 3. Check for Empty State
    if filtered_athletes.empty and filtered_coaches.empty:
        st.warning("No results found matching your filters.")
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
            
            # Display Bio Card - Stacked vertically for narrow column layout
            st.markdown(f'<div style="font-size:0.95rem; font-weight:700; color:var(--gold); text-transform:uppercase; letter-spacing:0.8px; margin-top:0.5rem; margin-bottom:0.8rem;">Profile Details: {selected_name}</div>', unsafe_allow_html=True)
            
            # General details card
            st.markdown(f"""
            <div class="acard" style="margin-bottom: 1rem;">
                <span class="tag green" style="float:right;">{entity_type}</span>
                <b style="font-size:1.1rem;color:var(--teal);">{person_row['name']}</b><br>
                <span style="font-size:0.75rem;color:var(--text2);">{person_row['sport']} · {person_row['state']} · {person_row.get('city', 'Unknown')}</span>
                <hr style="margin:0.8rem 0;border:0;border-top:1px solid var(--line);">
                <div style="font-size:0.85rem;line-height:1.6;color:var(--text2);">
                    <b>Age:</b> {int(person_row['age']) if pd.notna(person_row['age']) else 'Unknown'}<br>
                    <b>Gender:</b> {person_row['gender']}<br>
                    <b>Tier:</b> {person_row['tier']}<br>
                    <b>Registry Base:</b> {person_row.get('city', 'Unknown')}, {person_row['state']}<br>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Training details card
            if entity_type == "Coach":
                st.markdown(f"""
                <div class="acard" style="margin-bottom: 1rem;">
                    <span class="tag blue" style="float:right;">Certification</span>
                    <b style="font-size:1.05rem;color:var(--blue);">Licence & Certificate Status</b>
                    <hr style="margin:0.8rem 0;border:0;border-top:1px solid var(--line);">
                    <div style="font-size:0.85rem;line-height:1.6;color:var(--text2);">
                        <b>Active Licence:</b> <span class="tag green">{person_row['performance_level']}</span><br>
                        <b>Licencing Body:</b> {person_row.get('source_link', 'Official Registry')}<br>
                        <b>Empanelled Stage:</b> {person_row.get('pipeline_stage', 'Empanelled')}<br>
                        <b>Notes:</b> {person_row.get('notes', 'No additional certificate notes recorded.')}<br>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                coach_val = "Assigned National Coach" if person_row['performance_level'] in ["International", "National"] else "Regional Academy Coach"
                centre_val = "SAI NCOE " + str(person_row.get('state', 'Unknown')) if person_row['performance_level'] in ["International", "National"] else "Local State Academy"
                
                st.markdown(f"""
                <div class="acard" style="margin-bottom: 1rem;">
                    <span class="tag blue" style="float:right;">Performance & Training</span>
                    <b style="font-size:1.05rem;color:var(--blue);">Training Profile & Metrics</b>
                    <hr style="margin:0.8rem 0;border:0;border-top:1px solid var(--line);">
                    <div style="font-size:0.85rem;line-height:1.6;color:var(--text2);">
                        <b>Primary Coach:</b> {coach_val}<br>
                        <b>Training Centre:</b> {centre_val}<br>
                        <b>Opportunity Score:</b> <span class="tag amber">{person_row['athletiq_opportunity_score']} / 10.0</span><br>
                        <b>Current Funding:</b> {person_row['funding_status']}<br>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
            # Elite achievements
            matching_elites = [e for e in elite_athletes if e["name"].lower() == selected_name.lower()]
            if matching_elites:
                elite_profile = matching_elites[0]
                st.markdown(f"""
                <div class="acard" style="margin-bottom: 1rem;">
                    <span class="tag amber" style="float:right;">Elite Registry</span>
                    <b style="font-size:1rem;color:var(--gold);">Major Achievements & Olympic Medals</b>
                    <hr style="margin:0.8rem 0;border:0;border-top:1px solid var(--line);">
                    <div style="font-size:0.88rem;line-height:1.6;color:var(--text2);">
                        <b>Medals / Placement:</b> {elite_profile.get('medals', 'None')}<br>
                        <b>National Records & Historical Profile:</b> {elite_profile.get('records', 'None')}<br>
                        <b>Category Event:</b> {elite_profile.get('category', 'None')}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
            # Wrestling TOPS slides
            selected_name_lower = selected_name.lower().strip()
            if selected_name_lower in wrestling_tops:
                w_bio = wrestling_tops[selected_name_lower]
                st.markdown(f"""
                <div class="acard" style="margin-bottom: 1rem;">
                    <span class="tag purple" style="float:right;">Wrestling TOPS Profile</span>
                    <b style="font-size:1rem;color:var(--purple);">Detailed Slide Bio</b>
                    <hr style="margin:0.8rem 0;border:0;border-top:1px solid var(--line);">
                    <div style="font-size:0.88rem;line-height:1.7;color:var(--text2);">
                        <b>Weight Category:</b> {w_bio['category']}<br>
                        <b>Date of Birth / Age:</b> {w_bio['dob_age']}<br>
                        <b>Training Base:</b> {w_bio['base']}<br>
                        <b>Best Career:</b> {w_bio['best']}<br>
                        <b>Latest:</b> {w_bio['latest']}<br>
                        <b>National Pos:</b> {w_bio['national_pos']}<br>
                        <b>Olympic Outlook:</b> {w_bio['outlook']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
            # Notes notes
            if person_row.get("notes") and pd.notna(person_row["notes"]) and selected_name_lower not in wrestling_tops:
                st.markdown(f"""
                <div class="acard" style="margin-bottom: 1rem;">
                    <b style="font-size:1rem;color:var(--teal);">Performance Records & History Notes</b>
                    <hr style="margin:0.8rem 0;border:0;border-top:1px solid var(--line);">
                    <div style="font-size:0.88rem;line-height:1.6;color:var(--text2);">
                        {person_row['notes']}
                    </div>
                </div>
                """, unsafe_allow_html=True)

        tab_ath, tab_coa, tab_aca = st.tabs(["Athlete Search", "Coach Search", "Academy Search"])
        
        with tab_ath:
            def render_athlete_cards_grid(df_disp, total_len, level_txt):
                limit = 24
                st.write(f"Showing top {min(limit, total_len)} matching {level_txt} athletes (total: {total_len:,}):")
                cols = st.columns(3)
                for idx, (_, row) in enumerate(df_disp.head(limit).iterrows()):
                    name = row["Sportsperson Name"]
                    spec = row["Specialization"]
                    state = row["State Registry"]
                    perf = row["Performance Level"]
                    age = row["DOB / Age"]
                    ach = row["Achievements / Notes"]
                    badge_color = "#10E5B3" if "Medalist" in perf or "Internat" in perf.lower() else ("#683DE4" if "National" in perf else "#FDD663")
                    
                    card_html = f"""
                    <div class="acard" style="border-left: 3px solid {badge_color}; margin-bottom: 1rem; padding: 1.2rem; height: 100%;">
                        <div class="acard-top">
                            <div class="acard-title" style="font-size:1.05rem;">{name}</div>
                            <span class="tag green" style="background: rgba(16,229,179,0.1); border: 1px solid rgba(16,229,179,0.25); color: #113E21; font-size: 0.68rem; padding: 1px 6px; border-radius: 4px;">{perf}</span>
                        </div>
                        <div class="acard-meta" style="margin-top:0.4rem; font-size:0.78rem; line-height: 1.5; color: var(--text2);">
                            <b>Specialization:</b> {spec} <br>
                            <b>State Registry:</b> {state} <br>
                            <b>DOB / Age:</b> {age}
                        </div>
                        <hr style="margin:0.6rem 0; border:0; border-top: 1px solid var(--line);">
                        <div style="font-size:0.75rem; color: var(--text3); line-height:1.4;">
                            {ach}
                        </div>
                    </div>
                    """
                    with cols[idx % 3]:
                        st.markdown(card_html, unsafe_allow_html=True)
                if total_len > limit:
                    st.info(f"Showing first {limit} athletes. Use the 'Select Athlete' dropdown in the right panel to search or inspect any specific profile.")

            athlete_names = sorted(filtered_athletes["name"].dropna().unique().tolist()) if not filtered_athletes.empty else []
            
            c_master, c_detail = st.columns([3, 2])
            
            with c_detail:
                st.markdown("<div style='font-size:0.95rem; font-weight:600; color:var(--forest); margin-bottom:0.4rem;'>Profile Inspector</div>", unsafe_allow_html=True)
                selected_athlete = st.selectbox(
                    "Inspect Profile Details:",
                    options=["-- Select Athlete --"] + athlete_names,
                    key="profile_selected_athlete"
                )
                if selected_athlete != "-- Select Athlete --":
                    person_row = filtered_athletes[filtered_athletes["name"] == selected_athlete].iloc[0]
                    render_bio(selected_athlete, False, person_row)
                else:
                    st.markdown("""
                    <div style="border: 1px dashed var(--line); border-radius:0px; padding: 2rem; text-align:center; color: var(--ink-soft); font-size:0.88rem; margin-top:0.5rem;">
                        Select an athlete from the dropdown above to view their comprehensive training metrics, achievements, and coach assignments.
                    </div>
                    """, unsafe_allow_html=True)
                    
            with c_master:
                if not filtered_athletes.empty:
                    # Initialize selected level in session state if not present
                    if "athlete_selected_level" not in st.session_state:
                        st.session_state.athlete_selected_level = None
                        
                    # Inject CSS active styling dynamically based on session state selection
                    style_intl = "background: var(--forest) !important; color: var(--white) !important; border-color: var(--forest) !important;" if st.session_state.athlete_selected_level == "International" else ""
                    style_nat = "background: var(--forest) !important; color: var(--white) !important; border-color: var(--forest) !important;" if st.session_state.athlete_selected_level == "National" else ""
                    style_state = "background: var(--forest) !important; color: var(--white) !important; border-color: var(--forest) !important;" if st.session_state.athlete_selected_level == "State-wise" else ""
                    
                    st.markdown(f"""
                    <style>
                    #level-selection-trigger ~ div[data-testid="column"] button {{
                        height: 50px !important;
                        background: var(--white) !important;
                        border: 1px solid var(--line) !important;
                        border-radius: 0px !important;
                        font-family: var(--serif) !important;
                        font-size: 0.95rem !important;
                        font-weight: 500 !important;
                        color: var(--forest) !important;
                        transition: all 0.3s ease !important;
                    }}
                    #level-selection-trigger ~ div[data-testid="column"] button:hover {{
                        background: var(--gray) !important;
                        border-color: var(--gold) !important;
                        color: var(--forest) !important;
                        transform: none !important;
                        box-shadow: none !important;
                    }}
                    #level-selection-trigger ~ div[data-testid="column"]:nth-of-type(1) button {{ {style_intl} }}
                    #level-selection-trigger ~ div[data-testid="column"]:nth-of-type(2) button {{ {style_nat} }}
                    #level-selection-trigger ~ div[data-testid="column"]:nth-of-type(3) button {{ {style_state} }}
                    </style>
                    <div id="level-selection-trigger"></div>
                    <div class="stitle" style="font-size:1.05rem;margin-top:0.5rem;margin-bottom:0.8rem;">Filter by Performance Level</div>
                    """, unsafe_allow_html=True)
                    
                    col_intl, col_nat, col_state = st.columns(3)
                    with col_intl:
                        if st.button("🌍 International Level", key="btn_level_intl", use_container_width=True):
                            st.session_state.athlete_selected_level = "International"
                            st.rerun()
                    with col_nat:
                        if st.button("🏆 National Level", key="btn_level_nat", use_container_width=True):
                            st.session_state.athlete_selected_level = "National"
                            st.rerun()
                    with col_state:
                        if st.button("📍 State & District", key="btn_level_state", use_container_width=True):
                            st.session_state.athlete_selected_level = "State-wise"
                            st.rerun()
                            
                    # Show table of the selected field if active
                    if st.session_state.athlete_selected_level:
                        lvl = st.session_state.athlete_selected_level
                        if lvl == "International":
                            filtered_ath_by_lvl = filtered_athletes[filtered_athletes["performance_level"].str.lower().str.contains("internat", na=False)]
                        elif lvl == "National":
                            filtered_ath_by_lvl = filtered_athletes[filtered_athletes["performance_level"].str.lower() == "national"]
                        else: # State-wise
                            filtered_ath_by_lvl = filtered_athletes[filtered_athletes["performance_level"].str.lower().isin(["state", "district"])]
                            
                        st.markdown("---")
                        
                        col_tbl_hdr, col_tbl_cls = st.columns([3, 1])
                        with col_tbl_hdr:
                            st.markdown(f'<div class="stitle" style="font-size:0.95rem;margin-top:0.3rem;">Matching {lvl} Athletes</div>', unsafe_allow_html=True)
                        with col_tbl_cls:
                            if st.button("❌ Close", key="btn_clear_level_filter", use_container_width=True):
                                st.session_state.athlete_selected_level = None
                                st.rerun()
                                
                        if not filtered_ath_by_lvl.empty:
                            ath_display = filtered_ath_by_lvl[["name", "sport", "state", "performance_level", "age", "notes"]].copy()
                            
                            ath_display["Specialization"] = ath_display["sport"]
                            ath_display["DOB / Age"] = ath_display["age"].apply(lambda x: f"{int(x)} yrs" if pd.notna(x) and float(x) > 0 else "Unknown")
                            ath_display["Achievements / Notes"] = ath_display["notes"].fillna("-")
                            
                            ath_display.drop(columns=["notes", "age", "sport"], inplace=True)
                            ath_display = ath_display[["name", "Specialization", "state", "performance_level", "DOB / Age", "Achievements / Notes"]]
                            ath_display.columns = ["Sportsperson Name", "Specialization", "State Registry", "Performance Level", "DOB / Age", "Achievements / Notes"]
                            
                            render_athlete_cards_grid(ath_display, len(ath_display), lvl.lower())
                        else:
                            st.info(f"No {lvl.lower()} athletes found matching the current filters.")
                    else:
                        if state_choice != "All States" or sport_choice != "All Sports" or name_query.strip():
                            st.markdown("---")
                            st.markdown('<div class="stitle" style="font-size:0.95rem;margin-top:0.3rem;">Matching Athletes</div>', unsafe_allow_html=True)
                            if not filtered_athletes.empty:
                                ath_display = filtered_athletes[["name", "sport", "state", "performance_level", "age", "notes"]].copy()
                                
                                ath_display["Specialization"] = ath_display["sport"]
                                ath_display["DOB / Age"] = ath_display["age"].apply(lambda x: f"{int(x)} yrs" if pd.notna(x) and float(x) > 0 else "Unknown")
                                ath_display["Achievements / Notes"] = ath_display["notes"].fillna("-")
                                
                                ath_display.drop(columns=["notes", "age", "sport"], inplace=True)
                                ath_display = ath_display[["name", "Specialization", "state", "performance_level", "DOB / Age", "Achievements / Notes"]]
                                ath_display.columns = ["Sportsperson Name", "Specialization", "State Registry", "Performance Level", "DOB / Age", "Achievements / Notes"]
                                
                                render_athlete_cards_grid(ath_display, len(ath_display), "")
                            else:
                                st.info("No athletes found matching the current filters.")
                        else:
                            pass

        with tab_coa:
            coach_names = sorted(filtered_coaches["name"].dropna().unique().tolist()) if not filtered_coaches.empty else []
            
            c_master_c, c_detail_c = st.columns([3, 2])
            
            with c_detail_c:
                st.markdown("<div style='font-size:0.95rem; font-weight:600; color:var(--forest); margin-bottom:0.4rem;'>Profile Inspector</div>", unsafe_allow_html=True)
                selected_coach = st.selectbox(
                    "Inspect Coach Details:",
                    options=["-- Select Coach --"] + coach_names,
                    key="profile_selected_coach"
                )
                if selected_coach != "-- Select Coach --":
                    person_row = filtered_coaches[filtered_coaches["name"] == selected_coach].iloc[0]
                    render_bio(selected_coach, True, person_row)
                else:
                    st.markdown("""
                    <div style="border: 1px dashed var(--line); border-radius:0px; padding: 2rem; text-align:center; color: var(--ink-soft); font-size:0.88rem; margin-top:0.5rem;">
                        Select a coach from the dropdown above to view their certifications, licences, and career details.
                    </div>
                    """, unsafe_allow_html=True)
            
            with c_master_c:
                if not filtered_coaches.empty:
                    st.markdown('<div class="stitle" style="font-size:0.95rem;margin-top:0.5rem;margin-bottom:0.8rem;">Matching Coaches</div>', unsafe_allow_html=True)
                    co_display = filtered_coaches[["name", "sport", "city", "state", "performance_level", "age", "notes"]].copy()
                    
                    co_display["Specialization"] = co_display["sport"]
                    co_display["DOB / Age"] = co_display["age"].apply(lambda x: f"{int(x)} yrs" if pd.notna(x) and float(x) > 0 else "Unknown")
                    co_display["Credentials"] = co_display["notes"].fillna("-")
                    co_display.drop(columns=["notes", "age", "sport", "city"], inplace=True)
                    co_display = co_display[["name", "Specialization", "state", "performance_level", "DOB / Age", "Credentials"]]
                    co_display.columns = ["Coach Name", "Specialization", "State Registry", "Performance Level", "DOB / Age", "Credentials"]
                    st.write(f"Showing all matching coaches (total: {len(co_display)}):")
                    st.dataframe(co_display.reset_index(drop=True), use_container_width=True, height=350, hide_index=True)
                else:
                    st.info("No coaches found matching the current filters.")

        with tab_aca:
            st.markdown('<div class="stitle" style="font-size:0.95rem;margin-top:0.5rem;margin-bottom:0.8rem;">Matching Academies</div>', unsafe_allow_html=True)
            sai_df_disp = sai_df[["name", "city", "state", "type", "region", "capacity", "coaches", "facilities"]].copy()
            if state_choice != "All States":
                sai_df_disp = sai_df_disp[sai_df_disp["state"].str.lower() == state_choice.lower()]
            sai_df_disp.columns = ["Centre Name", "City", "State", "Type", "Region", "Capacity", "Coaches", "Facilities"]
            st.write(f"Showing all matching academies (total: {len(sai_df_disp)}):")
            st.dataframe(sai_df_disp.reset_index(drop=True), use_container_width=True, height=450, hide_index=True)
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

    # 1. Sport Focus, State Registry, & Name Search Filters
    wcol_spt, wcol_st, wcol_name = st.columns([1, 1, 1.2])
    with wcol_spt:
        w_sports_list = ["All Sports"] + sorted(women_df["sport"].unique().tolist())
        w_sport_choice = st.selectbox("Sport Focus", w_sports_list, key="women_sport")
    with wcol_st:
        w_states_list = ["All States"] + sorted(women_df["state"].unique().tolist())
        w_state_choice = st.selectbox("State Registry", w_states_list, key="women_state")
    with wcol_name:
        w_name_query = st.text_input("Athlete Name", placeholder="Type athlete name...", key="women_search")

    # Filter datasets for Women
    filtered_women = women_df.copy()
    
    if w_sport_choice != "All Sports":
        filtered_women = filtered_women[filtered_women["sport"].str.lower() == w_sport_choice.lower()]
    if w_state_choice != "All States":
        filtered_women = filtered_women[filtered_women["state"].str.lower() == w_state_choice.lower()]
    if w_name_query.strip():
        filtered_women = filtered_women[filtered_women["name"].str.lower().str.contains(w_name_query.strip().lower(), na=False)]

    # 2. Check for Empty State
    if filtered_women.empty:
        st.warning("No results found matching your filters in the Women Athletes Directory.")
    else:
        def render_women_bio(selected_name, person_row):
            st.markdown(f'<div style="font-size:0.95rem; font-weight:700; color:var(--gold); text-transform:uppercase; letter-spacing:0.8px; margin-top:0.5rem; margin-bottom:0.8rem;">Profile Details: {selected_name}</div>', unsafe_allow_html=True)
            
            # General details card
            st.markdown(f"""
            <div class="acard" style="margin-bottom: 1rem;">
                <span class="tag green" style="float:right;">Sportsperson</span>
                <b style="font-size:1.1rem;color:var(--teal);">{person_row['name']}</b><br>
                <span style="font-size:0.75rem;color:var(--text2);">{person_row['sport']} · {person_row['state']} · {person_row.get('city', 'Unknown')}</span>
                <hr style="margin:0.8rem 0;border:0;border-top:1px solid var(--line);">
                <div style="font-size:0.85rem;line-height:1.6;color:var(--text2);">
                    <b>Age:</b> {int(person_row['age']) if pd.notna(person_row['age']) else 'Unknown'}<br>
                    <b>Gender:</b> {person_row['gender']}<br>
                    <b>Tier:</b> {person_row['tier']}<br>
                    <b>Status:</b> <span class="tag amber">{person_row.get('status', 'Scouted')}</span><br>
                    <b>Registry Base:</b> {person_row.get('city', 'Unknown')}, {person_row['state']}<br>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Performance & Training details card
            st.markdown(f"""
            <div class="acard" style="margin-bottom: 1rem;">
                <span class="tag blue" style="float:right;">Performance & Training</span>
                <b style="font-size:1.05rem;color:var(--blue);">Training Profile & Metrics</b>
                <hr style="margin:0.8rem 0;border:0;border-top:1px solid var(--line);">
                <div style="font-size:0.85rem;line-height:1.6;color:var(--text2);">
                    <b>Performance Level:</b> <span class="tag green">{person_row['performance_level']}</span><br>
                    <b>Opportunity Score:</b> <span class="tag amber">{person_row['athletiq_opportunity_score']} / 10.0</span><br>
                    <b>Current Funding:</b> {person_row['funding_status']}<br>
                    <b>Highlight:</b> {person_row.get('highlight', 'Identified through grassroots trials.')}<br>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Achievements & Scouting Remarks card
            st.markdown(f"""
            <div class="acard" style="margin-bottom: 1rem;">
                <span class="tag amber" style="float:right;">Achievements</span>
                <b style="font-size:1rem;color:var(--gold);">Key Achievements & Scouting Notes</b>
                <hr style="margin:0.8rem 0;border:0;border-top:1px solid var(--line);">
                <div style="font-size:0.88rem;line-height:1.6;color:var(--text2);">
                    <b>Achievements:</b> {person_row.get('achievements', 'Standard track performance recorded.')}<br>
                    <b>Scouting Remarks:</b> {person_row.get('remarks', 'High development potential.')}
                </div>
            </div>
            """, unsafe_allow_html=True)

        # 3. Master-Detail Column Split
        w_athlete_names = sorted(filtered_women["name"].dropna().unique().tolist())
        
        c_master_w, c_detail_w = st.columns([3, 2])
        
        with c_detail_w:
            st.markdown("<div style='font-size:0.95rem; font-weight:600; color:var(--forest); margin-bottom:0.4rem;'>Profile Inspector</div>", unsafe_allow_html=True)
            selected_w_athlete = st.selectbox(
                "Inspect Profile Details:",
                options=["-- Select Athlete --"] + w_athlete_names,
                key="women_selected_athlete"
            )
            if selected_w_athlete != "-- Select Athlete --":
                person_row = filtered_women[filtered_women["name"] == selected_w_athlete].iloc[0]
                render_women_bio(selected_w_athlete, person_row)
            else:
                st.markdown("""
                <div style="border: 1px dashed var(--line); border-radius:0px; padding: 2rem; text-align:center; color: var(--ink-soft); font-size:0.88rem; margin-top:0.5rem;">
                    Select a women athlete from the dropdown above to view her comprehensive training metrics, achievements, and scouting notes.
                </div>
                """, unsafe_allow_html=True)
                
        with c_master_w:
            def render_women_cards_grid(df_disp, total_len, level_txt):
                limit = 24
                st.write(f"Showing top {min(limit, total_len)} matching {level_txt} athletes (total: {total_len:,}):")
                cols = st.columns(3)
                for idx, (_, row) in enumerate(df_disp.head(limit).iterrows()):
                    name = row["name"]
                    spec = row["sport"] + (" - " + row["event"] if pd.notna(row.get("event")) and row.get("event") not in ["", "Unknown"] else "")
                    state = row["state"]
                    perf = row["performance_level"]
                    age = f"{int(row['age'])} yrs" if pd.notna(row['age']) and float(row['age']) > 0 else "Unknown"
                    ach = row["achievements"]
                    badge_color = "#10E5B3" if "Medalist" in perf or "Internat" in perf.lower() else ("#683DE4" if "National" in perf else "#FDD663")
                    
                    card_html = f"""
                    <div class="acard" style="border-left: 3px solid {badge_color}; margin-bottom: 1rem; padding: 1.2rem; height: 100%;">
                        <div class="acard-top">
                            <div class="acard-title" style="font-size:1.05rem;">{name}</div>
                            <span class="tag green" style="background: rgba(16,229,179,0.1); border: 1px solid rgba(16,229,179,0.25); color: #113E21; font-size: 0.68rem; padding: 1px 6px; border-radius: 4px;">{perf}</span>
                        </div>
                        <div class="acard-meta" style="margin-top:0.4rem; font-size:0.78rem; line-height: 1.5; color: var(--text2);">
                            <b>Specialization:</b> {spec} <br>
                            <b>State Registry:</b> {state} <br>
                            <b>DOB / Age:</b> {age}
                        </div>
                        <hr style="margin:0.6rem 0; border:0; border-top: 1px solid var(--line);">
                        <div style="font-size:0.75rem; color: var(--text3); line-height:1.4;">
                            {ach}
                        </div>
                    </div>
                    """
                    with cols[idx % 3]:
                        st.markdown(card_html, unsafe_allow_html=True)
                if total_len > limit:
                    st.info(f"Showing first {limit} athletes. Use the selectbox in the right panel to search or inspect any specific profile.")

            # Initialize selected level in session state if not present
            if "women_selected_level" not in st.session_state:
                st.session_state.women_selected_level = None
                
            # Inject CSS active styling dynamically based on session state selection
            style_intl = "background: var(--forest) !important; color: var(--white) !important; border-color: var(--forest) !important;" if st.session_state.women_selected_level == "International" else ""
            style_nat = "background: var(--forest) !important; color: var(--white) !important; border-color: var(--forest) !important;" if st.session_state.women_selected_level == "National" else ""
            style_state = "background: var(--forest) !important; color: var(--white) !important; border-color: var(--forest) !important;" if st.session_state.women_selected_level == "State-wise" else ""
            
            st.markdown(f"""
            <style>
            #women-level-selection-trigger ~ div[data-testid="column"] button {{
                height: 50px !important;
                background: var(--white) !important;
                border: 1px solid var(--line) !important;
                border-radius: 0px !important;
                font-family: var(--serif) !important;
                font-size: 0.95rem !important;
                font-weight: 500 !important;
                color: var(--forest) !important;
                transition: all 0.3s ease !important;
            }}
            #women-level-selection-trigger ~ div[data-testid="column"] button:hover {{
                background: var(--gray) !important;
                border-color: var(--gold) !important;
                color: var(--forest) !important;
                transform: none !important;
                box-shadow: none !important;
            }}
            #women-level-selection-trigger ~ div[data-testid="column"]:nth-of-type(1) button {{ {style_intl} }}
            #women-level-selection-trigger ~ div[data-testid="column"]:nth-of-type(2) button {{ {style_nat} }}
            #women-level-selection-trigger ~ div[data-testid="column"]:nth-of-type(3) button {{ {style_state} }}
            </style>
            <div id="women-level-selection-trigger"></div>
            <div class="stitle" style="font-size:1.05rem;margin-top:0.5rem;margin-bottom:0.8rem;">Filter by Performance Level</div>
            """, unsafe_allow_html=True)
            
            col_intl, col_nat, col_state = st.columns(3)
            with col_intl:
                if st.button("🌍 International Level", key="btn_w_level_intl", use_container_width=True):
                    st.session_state.women_selected_level = "International"
                    st.rerun()
            with col_nat:
                if st.button("🏆 National Level", key="btn_w_level_nat", use_container_width=True):
                    st.session_state.women_selected_level = "National"
                    st.rerun()
            with col_state:
                if st.button("📍 State & District", key="btn_w_level_state", use_container_width=True):
                    st.session_state.women_selected_level = "State-wise"
                    st.rerun()
                    
            # Show table of the selected field if active
            if st.session_state.women_selected_level:
                lvl = st.session_state.women_selected_level
                if lvl == "International":
                    filtered_w_by_lvl = filtered_women[filtered_women["performance_level"].str.lower().str.contains("internat", na=False)]
                elif lvl == "National":
                    filtered_w_by_lvl = filtered_women[filtered_women["performance_level"].str.lower() == "national"]
                else: # State-wise
                    filtered_w_by_lvl = filtered_women[filtered_women["performance_level"].str.lower().isin(["state", "district"])]
                    
                st.markdown("---")
                
                col_tbl_hdr, col_tbl_cls = st.columns([3, 1])
                with col_tbl_hdr:
                    st.markdown(f'<div class="stitle" style="font-size:0.95rem;margin-top:0.3rem;">Matching {lvl} Women Athletes</div>', unsafe_allow_html=True)
                with col_tbl_cls:
                    if st.button("❌ Close", key="btn_w_clear_level_filter", use_container_width=True):
                        st.session_state.women_selected_level = None
                        st.rerun()
                        
                if not filtered_w_by_lvl.empty:
                    render_women_cards_grid(filtered_w_by_lvl, len(filtered_w_by_lvl), lvl.lower())
                else:
                    st.info(f"No {lvl.lower()} women athletes found matching the current filters.")
            else:
                if w_state_choice != "All States" or w_sport_choice != "All Sports" or w_name_query.strip():
                    st.markdown("---")
                    st.markdown('<div class="stitle" style="font-size:0.95rem;margin-top:0.3rem;">Matching Women Athletes</div>', unsafe_allow_html=True)
                    if not filtered_women.empty:
                        render_women_cards_grid(filtered_women, len(filtered_women), "")
                    else:
                        st.info("No women athletes found matching the current filters.")
                else:
                    # Show nothing at start (same as Profile directory start condition)
                    pass

elif selected_tab == "AI Assistant":
    import requests
    
    st.markdown('<div class="header-container"><div class="header-title">🤖 AI Assistant</div></div>', unsafe_allow_html=True)
    st.markdown("<p style='color:#a0aec0;margin-bottom:2rem;'>Ask me anything about AthletIQ's data (athletes, coaches, events, etc.)</p>", unsafe_allow_html=True)

    # Custom CSS for the Chat Interface to match AthletIQ Forest Gold Theme
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
        background-color: var(--white) !important;
        color: var(--ink) !important;
        border: 1px solid var(--line) !important;
        border-radius: 0px !important;
    }
    /* Chat Message Backgrounds */
    div[data-testid="stChatMessage"] {
        background-color: var(--gray) !important;
        border-radius: 0px !important;
        padding: 1rem !important;
        margin-bottom: 1rem !important;
        border: 1px solid var(--line) !important;
    }
    /* AI specific chat bubble (usually has a different avatar) */
    div[data-testid="stChatMessage"]:has([data-testid="stIconMaterial"]) {
        background: var(--white) !important;
        border: 1px solid var(--line) !important;
        border-left: 3px solid var(--forest) !important;
    }
    div[data-testid="stChatMessage"] p, div[data-testid="stChatMessage"] div {
        color: var(--ink) !important;
        font-family: var(--sans) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # API Key is defined globally at the top of the app
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


