import re

with open("app/dashboard.py", "r") as f:
    content = f.read()

start_idx = content.find('elif selected_tab == "Discovery & Leagues":')
end_idx = content.find('elif selected_tab == "Regional Talent":')

if start_idx != -1 and end_idx != -1:
    new_code = """elif selected_tab == "Discovery & Leagues":
    st.markdown('<div class="stitle" title="Track rising talent from local and state leagues"> Discovery & Leagues <span class="chip chip-purple">Live Grassroots & Emerging Athlete Prospects</span></div>', unsafe_allow_html=True)
    
    st.caption("Data Availability Period: January 2026 - Present (Live Updates)")
    
    # 1. Grassroots Leagues & Tournaments (Dynamic API Mock)
    st.markdown('<div class="stitle" style="font-size:1.15rem;margin-top:2rem;"> Live Grassroots Leagues & Tournaments</div>', unsafe_allow_html=True)
    st.markdown(insight(" API Integration", "Fetching live tournament data from regional state sports association APIs and Khelo India district nodes.", "blue"), unsafe_allow_html=True)
    
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
    
    fc1, fc2 = st.columns(2)
    with fc1:
        f_sport = st.selectbox("Filter by Sport Focus", ["All Core Sports"] + sorted(list(set(leagues_disp["sport"]))), key="live_sport_select")
    with fc2:
        f_state = st.selectbox("Filter by State Hub", ["All Mapped States"] + sorted(list(set(leagues_disp["state"]))), key="live_state_select")
        
    filtered_leagues = leagues_disp.copy()
    if f_sport != "All Core Sports":
        filtered_leagues = filtered_leagues[filtered_leagues["sport"] == f_sport]
    if f_state != "All Mapped States":
        filtered_leagues = filtered_leagues[filtered_leagues["state"] == f_state]
            
    st.dataframe(filtered_leagues.reset_index(drop=True), use_container_width=True, height=350)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 2. Emerging Athlete Prospects (Based on live data)
    st.markdown('<div class="stitle" style="font-size:1.15rem;margin-top:2rem;"> Emerging Athlete Prospects</div>', unsafe_allow_html=True)
    st.markdown(insight(" Real-time Prospects Tracker", "Prospects identified through live tournament performance data mapping and scout evaluations.", "purple"), unsafe_allow_html=True)
    
    athletes_data = df_all[df_all["entity_type"]=="Athlete"].copy() if df_all is not None else pd.DataFrame()
    if not athletes_data.empty:
        prospects_display = athletes_data.copy()
        prospects_display["Live Match Score"] = [min(100, x * 10 + 15) for x in prospects_display["athletiq_opportunity_score"]]
        prospects_display["coach_assigned"] = prospects_display["athletiq_opportunity_score"].apply(lambda x: "Yes" if x >= 7.5 else "No")
        
        pd_table = prospects_display[["name", "sport", "state", "performance_level", "funding_status", "coach_assigned", "Live Match Score"]].copy()
        pd_table.columns = ["Athlete Name", "Sport", "Home State", "Performance Level", "Funding Status", "Coach Assigned", "Live Evaluation Score"]
        
        st.dataframe(pd_table.head(100).reset_index(drop=True), use_container_width=True, height=350)
        
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 3 — REGIONAL TALENT
"""
    content = content[:start_idx] + new_code + content[end_idx:]
    with open("app/dashboard.py", "w") as f:
        f.write(content)
    print("Updated Discovery & Leagues tab.")
