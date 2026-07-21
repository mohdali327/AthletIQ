import re

with open("app/dashboard.py", "r") as f:
    content = f.read()

start_idx = content.find('elif selected_tab == "Coach Capacity":')
end_idx = content.find('elif selected_tab == "Sponsor Pipeline":')

if start_idx != -1 and end_idx != -1:
    new_code = """elif selected_tab == "Centres & Academies":
    st.markdown('<div class="stitle" title="Monitor infrastructure, coaching capacity, and academies"> Centres & Academies <span class="chip chip-blue">Ecosystem Directory</span></div>', unsafe_allow_html=True)
    
    st.markdown(insight("ℹ Infrastructure & Coaching Capacity", 
        "AthletIQ maps government training centres (SAI), private academies, and tracks Coach-to-Athlete ratios to identify capacity gaps and sponsorship opportunities.", "blue"), unsafe_allow_html=True)
        
    ca_tabs = st.tabs(["Coach-to-Athlete Ratios & Capacity", "SAI Centres & NCOEs", "Private Academies & Akharas", "Add Custom Athlete Profile"])
    
    with ca_tabs[0]:
        st.markdown('<div class="stitle" style="font-size:1.15rem;"> Coach Capacity & Ratio Insights</div>', unsafe_allow_html=True)
        
        # Improved Coach-to-Athlete Ratio UI
        st.markdown('''
        <div style="display:flex; gap:1rem; margin-bottom:1.5rem;">
            <div class="acard" style="flex:1; border-left:4px solid var(--red);">
                <div style="color:var(--red); font-weight:700;">Archery (Jharkhand)</div>
                <div style="font-size:1.5rem; font-weight:900;">45 : 1</div>
                <div style="font-size:0.8rem; color:var(--text2);">Current Ratio (Athletes per Coach)</div>
                <div style="margin-top:0.5rem; font-size:0.8rem;"><b>Standard:</b> 15:1 <span style="color:var(--red);"> (Critical Deficit)</span></div>
                <div style="margin-top:0.5rem; font-size:0.8rem; color:var(--blue);"><b>Insight:</b> High risk of injury. Deploy NIS masterclass immediately.</div>
            </div>
            
            <div class="acard" style="flex:1; border-left:4px solid var(--amber);">
                <div style="color:var(--amber); font-weight:700;">Weightlifting (Assam)</div>
                <div style="font-size:1.5rem; font-weight:900;">32 : 1</div>
                <div style="font-size:0.8rem; color:var(--text2);">Current Ratio (Athletes per Platform)</div>
                <div style="margin-top:0.5rem; font-size:0.8rem;"><b>Standard:</b> 10:1 <span style="color:var(--amber);"> (Platform Shortage)</span></div>
                <div style="margin-top:0.5rem; font-size:0.8rem; color:var(--blue);"><b>Insight:</b> Physical safety hazard. Sponsor barbell platforms.</div>
            </div>
            
            <div class="acard" style="flex:1; border-left:4px solid var(--green);">
                <div style="color:var(--green); font-weight:700;">Wrestling (Haryana)</div>
                <div style="font-size:1.5rem; font-weight:900;">12 : 1</div>
                <div style="font-size:0.8rem; color:var(--text2);">Current Ratio (Athletes per Coach)</div>
                <div style="margin-top:0.5rem; font-size:0.8rem;"><b>Standard:</b> 15:1 <span style="color:var(--green);"> (Optimal)</span></div>
                <div style="margin-top:0.5rem; font-size:0.8rem; color:var(--blue);"><b>Insight:</b> Well-resourced. Focus on funding international exposure.</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('<div class="stitle" style="font-size:1rem; margin-top:2rem;"> Former-Athlete-to-Coach Registry</div>', unsafe_allow_html=True)
        st.markdown(insight(" Candidate: Vinesh Phogat (Wrestling)", "<b>Olympic finalist | Proposed: Head Coach, Haryana Women's Academy</b><br>Expertise in women's combat sports. Ready for empanelment.", "purple"), unsafe_allow_html=True)
        st.markdown(insight(" Candidate: PR Sreejesh (Hockey Goalkeeping)", "<b>2x Olympic medallist | Proposed: Goalkeeping Director, Odisha NCOE</b><br>World-class goalkeeping mentor.", "green"), unsafe_allow_html=True)

    with ca_tabs[1]:
        st.markdown('<div class="stitle" style="font-size:1rem;"> Sports Authority of India Training Network</div>', unsafe_allow_html=True)
        
        # Directory Table
        sai_df_disp = sai_df[["name", "city", "state", "type", "region", "capacity", "coaches", "facilities"]].copy()
        sai_df_disp.columns = ["Centre Name", "City", "State", "Type", "Region", "Capacity", "Coaches", "Facilities"]
        st.dataframe(sai_df_disp.reset_index(drop=True), use_container_width=True, height=280)

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
        st.markdown('<div class="stitle" style="font-size:1.15rem;"> Add Custom Athlete Profile</div>', unsafe_allow_html=True)
        st.markdown("Manually enter emerging athletes into the AthletIQ database for tracking and matching.")
        
        with st.form("custom_athlete_form"):
            ca_col1, ca_col2 = st.columns(2)
            c_name = ca_col1.text_input("Full Name")
            c_sport = ca_col2.selectbox("Sport", ["Wrestling", "Boxing", "Archery", "Athletics", "Hockey", "Shooting", "Weightlifting"])
            
            ca_col3, ca_col4, ca_col5 = st.columns(3)
            c_age = ca_col3.number_input("Age", min_value=8, max_value=40, value=18)
            c_gender = ca_col4.selectbox("Gender", ["Male", "Female"])
            c_state = ca_col5.selectbox("Home State", ["Haryana", "Punjab", "Delhi", "Maharashtra", "Manipur", "Kerala", "Assam", "Jharkhand", "Tamil Nadu", "Odisha", "Uttar Pradesh", "Madhya Pradesh", "Rajasthan", "Gujarat"])
            
            c_perf = st.selectbox("Current Performance Level", ["District", "State", "National", "International"])
            c_coach = st.text_input("Current Coach (Optional)")
            c_funding = st.selectbox("Funding Status", ["Fully Funded", "Partially Funded", "Unfunded"])
            
            submit_ath = st.form_submit_button("Add Athlete to Database")
            if submit_ath:
                if c_name:
                    st.success(f"Successfully added {c_name} to the {c_state} {c_sport} cohort!")
                else:
                    st.error("Please enter the athlete's name.")

"""
    content = content[:start_idx] + new_code + content[end_idx:]

# Also remove "Coach Capacity" from the st.radio options
nav_options_start = content.find('    options=[')
nav_options_end = content.find('    ],', nav_options_start)
if nav_options_start != -1:
    nav_options = content[nav_options_start:nav_options_end]
    new_nav_options = nav_options.replace('        "Coach Capacity",\n', '')
    content = content[:nav_options_start] + new_nav_options + content[nav_options_end:]

with open("app/dashboard.py", "w") as f:
    f.write(content)
print("Updated Centres & Academies tab.")
