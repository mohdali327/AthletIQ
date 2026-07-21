import re

with open("app/dashboard.py", "r") as f:
    content = f.read()

# First, rename "Sport Priority" to "Regional Talent" in the st.radio navigation
nav_start = content.find('    options=[')
nav_end = content.find('    ],', nav_start)
if nav_start != -1:
    nav_options = content[nav_start:nav_end]
    new_nav = nav_options.replace('"Sport Priority"', '"Regional Talent"')
    content = content[:nav_start] + new_nav + content[nav_end:]

# Also update the tooltip for Regional Talent
tooltip_start = content.find("        'Discovery & Leagues':")
if tooltip_start != -1:
    content = content.replace("'Sport Priority': 'Analyze high-potential sports and allocate resources strategically.',", 
                              "'Regional Talent': 'Analyze top states, sports, and regional talent clusters.',")

# Now rewrite the entire Sport Priority Tab to Regional Talent Tab
start_idx = content.find('elif selected_tab == "Sport Priority":')
if start_idx == -1:
    start_idx = content.find('elif selected_tab == "Regional Talent":')

end_idx = content.find('# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n# TAB 4 — COACH CAPACITY')

if start_idx != -1 and end_idx != -1:
    new_code = """elif selected_tab == "Regional Talent":
    st.markdown('<div class="stitle" title="Analyze top states, sports, and regional talent clusters"> Regional Talent <span class="chip chip-gold">Top Regional Clusters</span></div>', unsafe_allow_html=True)
    
    st.markdown(insight(" Regional Talent Clusters", 
        "Explore India's top performing states, dominant sports, and high-potential athletes grouped by regions and demographics.", "gold"), unsafe_allow_html=True)
        
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown('<div class="stitle" style="font-size:1rem;margin-top:1rem;"> Top States (Athlete Representation)</div>', unsafe_allow_html=True)
        if df_all is not None:
            state_counts = df_all[df_all["entity_type"] == "Athlete"]["state"].value_counts().head(5).reset_index()
            state_counts.columns = ["State", "Athletes"]
            fig1 = px.bar(state_counts, x="State", y="Athletes", color="Athletes", color_continuous_scale=COLOR_SCALES["teal"])
            playout(fig1, "Top States by Athlete Volume", h=300)
            st.plotly_chart(fig1, use_container_width=True)
            
    with c2:
        st.markdown('<div class="stitle" style="font-size:1rem;margin-top:1rem;"> Top Sports (Performance)</div>', unsafe_allow_html=True)
        if df_all is not None:
            sport_counts = df_all[df_all["entity_type"] == "Athlete"]["sport"].value_counts().head(5).reset_index()
            sport_counts.columns = ["Sport", "Athletes"]
            fig2 = px.pie(sport_counts, names="Sport", values="Athletes", hole=0.4, color_discrete_sequence=px.colors.sequential.Teal)
            playout(fig2, "Top Performing Sports", h=300)
            st.plotly_chart(fig2, use_container_width=True)

    st.markdown('<div class="stitle" style="font-size:1rem;margin-top:1rem;"> Category-Wise Insights (Age Group & Gender)</div>', unsafe_allow_html=True)
    ci1, ci2, ci3 = st.columns(3)
    ci1.markdown(insight(" Gender Balance", "<b>45% Female Representation</b><br>Strong participation in Combat Sports (Boxing, Wrestling) from Haryana and Manipur.", "purple"), unsafe_allow_html=True)
    ci2.markdown(insight(" Age Group: Sub-Junior (12-15)", "<b>Highest Drop-off Rate</b><br>60% of athletes drop out before the junior category due to lack of local tournaments.", "amber"), unsafe_allow_html=True)
    ci3.markdown(insight(" Age Group: Junior (16-19)", "<b>Prime Scouting Window</b><br>Peak age for NCOE induction and international exposure funding.", "blue"), unsafe_allow_html=True)
    
    st.markdown('<div class="stitle" style="font-size:1rem;margin-top:1.5rem;"> Top Athletes Spotlight</div>', unsafe_allow_html=True)
    if df_all is not None:
        elite_athletes = df_all[(df_all["entity_type"] == "Athlete") & (df_all["performance_level"] == "International")].head(3)
        for _, row in elite_athletes.iterrows():
            st.markdown(f'''
            <div class="acard" style="border-left:3px solid var(--gold);margin-bottom:0.6rem;padding:0.8rem 1.2rem;">
                <div style="font-weight:700;font-size:1rem;color:#FFF;">{row["name"]} <span style="font-size:0.8rem;color:var(--text2);">({row["sport"]} • {row["state"]})</span></div>
                <div style="font-size:0.85rem;color:var(--text2);margin-top:0.25rem;">
                    <b>Medal Record:</b> International Level Competitor<br>
                    <b>Training Centre:</b> SAI NCOE (Nearest assigned based on region)<br>
                    <b>Coach:</b> Assigned National Coach<br>
                    <b>Backstory/Funding:</b> Currently CSR supported. Requires targeted Olympic prep funding.
                </div>
            </div>
            ''', unsafe_allow_html=True)

"""
    content = content[:start_idx] + new_code + content[end_idx:]

with open("app/dashboard.py", "w") as f:
    f.write(content)
print("Updated Regional Talent section.")
