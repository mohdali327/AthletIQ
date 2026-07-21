with open("app/dashboard.py", "r") as f:
    content = f.read()

start_idx = content.find('if selected_tab == "Pathway Overview":')
end_idx = content.find('# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n# TAB 2 — TALENT DISCOVERY')

new_pathway_code = """if selected_tab == "Pathway Overview":
    st.markdown('<div class="stitle" title="Strategic Dashboard Homepage"> Pathway Overview <span class="chip chip-blue">Strategic Dashboard Homepage</span></div>', unsafe_allow_html=True)

    # 1. Pipeline Description
    st.markdown('<div class="stitle" title="Overview of athlete progression from grassroots to elite levels" style="font-size:1.15rem;margin-top:2rem;"> Grassroots-to-Podium Conversion Pipeline</div>', unsafe_allow_html=True)
    st.markdown(insight(" Pipeline Description", 
        "The athlete development pipeline tracks the progression of talent from district-level grassroots participation, through state and zonal championships, into national coaching camps (like SAI NCOEs), and finally to elite international podium finishes. Currently, significant drop-offs occur at the state-to-zonal and national-to-elite transitions due to funding and coaching bottlenecks.", "blue"), unsafe_allow_html=True)

    # 2. Simplified Leakage Analysis
    st.markdown('<div class="stitle" title="Analysis of major blockers causing talent drop-offs" style="font-size:1.15rem;margin-top:1.5rem;"> Pipeline Blocker & Leakage Analysis</div>', unsafe_allow_html=True)
    st.markdown('''
    <div class="acard" style="border-left:3px solid var(--purple);margin-bottom:0.6rem;padding:0.8rem 1.2rem;">
        <div style="font-weight:700;font-size:0.95rem;color:#FFF;">District ➔ State Transition</div>
        <div style="font-size:0.85rem;color:var(--text2);margin-top:0.25rem;">
            <b>Leakage Blocker:</b> Lack of standardized equipment kits & travel funding in Tier-3 districts.<br>
            <b>Recommended CSR Intervention:</b> Support village-level league travel grants.
        </div>
    </div>
    <div class="acard" style="border-left:3px solid var(--teal);margin-bottom:0.6rem;padding:0.8rem 1.2rem;">
        <div style="font-weight:700;font-size:0.95rem;color:#FFF;">State ➔ Zonal Transition</div>
        <div style="font-size:0.85rem;color:var(--text2);margin-top:0.25rem;">
            <b>Leakage Blocker:</b> Insufficient NIS certified coaches and sports science clinics at state levels.<br>
            <b>Recommended Intervention:</b> Train former state athletes as district coaches.
        </div>
    </div>
    <div class="acard" style="border-left:3px solid var(--gold);margin-bottom:0.6rem;padding:0.8rem 1.2rem;">
        <div style="font-weight:700;font-size:0.95rem;color:#FFF;">Zonal ➔ National Transition</div>
        <div style="font-size:0.85rem;color:var(--text2);margin-top:0.25rem;">
            <b>Leakage Blocker:</b> Lack of specialized residential sports academy placements and advanced nutrition.<br>
            <b>Recommended Intervention:</b> Partner with private/SAI NCOE centres.
        </div>
    </div>
    <div class="acard" style="border-left:3px solid var(--pink);margin-bottom:0.6rem;padding:0.8rem 1.2rem;">
        <div style="font-weight:700;font-size:0.95rem;color:#FFF;">National ➔ Elite Transition</div>
        <div style="font-size:0.85rem;color:var(--text2);margin-top:0.25rem;">
            <b>Leakage Blocker:</b> Insufficient corporate sponsorship for international exposure tournaments.<br>
            <b>Recommended Intervention:</b> Align private sponsor contracts to elite athletes.
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # 3. Pathway Breaks Detected (Clickable Insights Redirecting to Tabs)
    st.markdown('<div class="stitle" title="Clickable diagnostic alerts on talent drop-offs" style="font-size:1.15rem;margin-top:2rem;"> Pathway Breaks Detected</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button(" 1. Discovery Gaps (Go to Leagues)", use_container_width=True):
            st.session_state["main_navigation"] = "Discovery & Leagues"
            st.rerun()
        st.caption("9 regional talent clusters currently unmapped.")
    with col2:
        if st.button(" 2. Coaching Shortage (Go to Coaches)", use_container_width=True):
            st.session_state["main_navigation"] = "Centres & Academies"
            st.rerun()
        st.caption("Severe capacity gaps in NIS certified coaching.")
    with col3:
        if st.button(" 3. Funding Deficit (Go to Sponsors)", use_container_width=True):
            st.session_state["main_navigation"] = "Sponsor Pipeline"
            st.rerun()
        st.caption("82% of sub-junior athletes remain unfunded.")

    # 4. States Lagging in Opportunities
    st.markdown('<div class="stitle" title="States requiring immediate infrastructure and funding support" style="font-size:1.15rem;margin-top:2rem;"> States Lagging in Opportunities</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.markdown(insight(" Bihar & Jharkhand", "<b>Critical Gap:</b> Severe lack of modern training centres despite high raw talent in contact sports. Funding required for basic infrastructure.", "red"), unsafe_allow_html=True)
    c2.markdown(insight(" Chhattisgarh", "<b>Critical Gap:</b> No specialized NCOEs. Athletes forced to migrate early, leading to 60%+ dropout rates before state championships.", "red"), unsafe_allow_html=True)
    c3.markdown(insight(" Northeast (Non-Archery/Boxing)", "<b>Critical Gap:</b> While boxing and archery are supported, sports like athletics and swimming have zero elite coaching facilities in the region.", "red"), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

"""

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_pathway_code + content[end_idx:]
    with open("app/dashboard.py", "w") as f:
        f.write(content)
    print("Successfully updated Pathway Overview.")
else:
    print("Could not find block boundaries.")

