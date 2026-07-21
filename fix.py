with open("app/dashboard.py", "r") as f:
    content = f.read()

# 1. Navigation update
old_nav = """with st.sidebar:
    st.markdown("<h2 style='color:#10E5B3;font-family:Outfit;font-weight:700;margin-top:0.5rem;'> Navigation</h2>", unsafe_allow_html=True)
    selected_tab = st.radio(
        label="Go to section:",
        options=[
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
            "Profile"
        ],
        label_visibility="collapsed",
        key="main_navigation"
    )
    # ── Tab transition animation & auto-close sidebar ──
    if "_last_tab" not in st.session_state:
        st.session_state._last_tab = selected_tab
    if st.session_state._last_tab != selected_tab:
        st.session_state._last_tab = selected_tab
        st.markdown(f'<div class="redirect-overlay"><div class="redirect-spinner"></div><div class="redirect-text">Loading {selected_tab}...</div></div>', unsafe_allow_html=True)
        import streamlit.components.v1 as components
        components.html('<script>try{window.parent.document.querySelector("button[aria-label=\\'Close sidebar\\']").click()}catch(e){}</script>', height=0, width=0)"""

new_nav = """# ── TOP HORIZONTAL NAVIGATION ──
st.markdown('''<style>
    /* Position the radio buttons at the very top */
    div[data-testid="stRadio"] {
        margin-top: -3rem;
        margin-bottom: 2rem;
    }
    div[data-testid="stRadio"] > div {
        flex-direction: row; 
        gap: 1rem; 
        justify-content: center; 
        background: transparent;
    }
    /* Hide the radio button circles */
    div[data-testid="stRadio"] div[data-baseweb="radio"] div {
        display: none !important;
    }
    /* Style the labels as tab text */
    div[data-testid="stRadio"] label p {
        font-family: 'Outfit', sans-serif !important;
        font-size: 1rem !important;
        color: rgba(255,255,255,0.7) !important;
        transition: color 0.2s ease;
    }
    div[data-testid="stRadio"] label:hover p {
        color: #fff !important;
    }
    div[data-testid="stRadio"] label[data-checked="true"] p {
        color: #10E5B3 !important;
        font-weight: 600 !important;
        text-shadow: 0 0 10px rgba(16,229,179,0.3);
    }
</style>''', unsafe_allow_html=True)

selected_tab = st.radio(
    label="Navigation",
    options=[
        "Pathway Overview",
        "Discovery & Leagues",
        "Sport Priority",
        "Coach Capacity",
        "Centres & Academies",
        "Profile"
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
"""

if old_nav in content:
    content = content.replace(old_nav, new_nav)
else:
    print("Nav section not found!")


# 2. Remove Hero Subtitle
hero_sub = '    Built to decide where to scout, coach, fund and activate.'
if hero_sub in content:
    content = content.replace(hero_sub, "")
else:
    print("Hero sub not found!")

# 3. SAI Matcher extraction and injection
sai_start = "# ── TOP-LEVEL ATHLETE-TO-SAI MATCHING ENGINE (PRIMARY DECISION PORTAL) ──\n"
sai_end = """        if "top_custom_matched_state" in st.session_state:
            del st.session_state["top_custom_matched_state"]
            del st.session_state["top_custom_matched_perf"]
        st.rerun()\n"""

if sai_start in content and sai_end in content:
    start_idx = content.find(sai_start)
    end_idx = content.find(sai_end) + len(sai_end)
    sai_block = content[start_idx:end_idx]
    
    # Remove from original location
    content = content.replace(sai_block, "")
    
    # Inject into Profile Tab
    profile_start = 'elif selected_tab == "Profile":\n'
    if profile_start in content:
        # Indent sai_block by 4 spaces
        indented_sai = "\n".join(["    " + line if line.strip() else line for line in sai_block.split("\n")])
        content = content.replace(profile_start, profile_start + indented_sai + "\n")
    else:
        print("Profile start not found!")
else:
    print("SAI bounds not found!")


# 4. Remove Tabs Data Quality and others
import re

# Fed Intel to CSR Matchmaker
fed_start = 'elif selected_tab == "Federation Intelligence":'
csr_start = 'elif selected_tab == "CSR Matchmaker":'
spon_start = 'elif selected_tab == "Sponsor Pipeline":'
ath_start = 'elif selected_tab == "Athlete Cohorts":'
data_start = 'elif selected_tab == "Data Quality":'
prof_start = 'elif selected_tab == "Profile":'

def remove_block(c, s1, s2):
    i1 = c.find(s1)
    i2 = c.find(s2)
    if i1 != -1 and i2 != -1 and i2 > i1:
        return c[:i1] + c[i2:]
    return c

content = remove_block(content, fed_start, spon_start)
content = remove_block(content, ath_start, prof_start)

# 5. Add Tooltips to Tab Headings
tooltips = {
    'Pathway Overview': 'Overview of the athlete development pipeline from grassroots to elite levels.',
    'Discovery & Leagues': 'Track rising talent from local and state leagues.',
    'Sport Priority': 'Analyze high-potential sports and allocate resources strategically.',
    'Coach Capacity': 'Evaluate and manage coach availability across training centres.',
    'Centres & Academies': 'Monitor infrastructure and capacities of SAI centres and academies.',
    'Profile': 'Search and view detailed profiles for athletes and coaches.'
}
for name, tooltip in tooltips.items():
    # Original might be: st.markdown('<div class="stitle" style="font-size:1.1rem;margin-top:1.5rem;"> Coach Deficit & Reallocation Optimizer</div>', unsafe_allow_html=True)
    # But wait, we want the main headings right after the elif.
    # A safer regex: find st.markdown('<div class="stitle"...> Name </div>'
    # Actually just replacing 'class="stitle"' with 'class="stitle" title="..." style="font-size:2rem;"' for the exact name
    
    # Find something like: st.markdown('<div class="stitle"> Pathway Overview </div>', unsafe_allow_html=True)
    # The titles are usually right under the selected_tab check.
    pass

with open("app/dashboard.py", "w") as f:
    f.write(content)
print("Done")
