with open('app/dashboard.py', 'r') as f:
    content = f.read()

start_marker = "        # Combined names list"
end_marker = "# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n# TAB 4 — CENTRES & ACADEMIES"

if start_marker in content and end_marker in content:
    part1 = content.split(start_marker)[0]
    part3 = end_marker + content.split(end_marker)[1]
    
    new_code = '''        def render_bio(selected_name, is_coach_flag, person_row):
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

        tab_ath, tab_coa = st.tabs(["Athlete Search", "Coach Search"])
        
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
                    ath_display = filtered_athletes[["name", "sport", "state", "performance_level", "notes"]].copy()
                    notes_split = ath_display["notes"].str.split(r"\||;", expand=True, regex=True)
                    ath_display["Style / Category"] = notes_split[0].str.strip() if 0 in notes_split.columns else "-"
                    ath_display["Weight / Achievements"] = notes_split[1].str.strip() if 1 in notes_split.columns else "-"
                    ath_display["DOB / Profile"] = notes_split[2].str.strip() if 2 in notes_split.columns else "-"
                    ath_display["Father's Name / Outlook"] = notes_split[3].str.strip() if 3 in notes_split.columns else "-"
                    if "notes" in ath_display.columns:
                        ath_display.drop(columns=["notes"], inplace=True)
                    ath_display.columns = ["Sportsperson Name", "Sport", "State Registry", "Performance Level", "Style / Category", "Weight / Achievements", "DOB / Profile", "Father's Name / Outlook"]
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
                    co_display = filtered_coaches[["name", "sport", "state", "performance_level", "notes"]].copy()
                    notes_split = co_display["notes"].str.split(r"\||;", expand=True, regex=True)
                    co_display["Credentials"] = notes_split[0].str.strip() if 0 in notes_split.columns else "-"
                    co_display["Father's Name / Exp."] = notes_split[1].str.strip() if 1 in notes_split.columns else "-"
                    co_display["DOB / Specialization"] = notes_split[2].str.strip() if 2 in notes_split.columns else "-"
                    co_display["Additional Notes"] = notes_split[3].str.strip() if 3 in notes_split.columns else "-"
                    if "notes" in co_display.columns:
                        co_display.drop(columns=["notes"], inplace=True)
                    co_display.columns = ["Coach Name", "Sport Focus", "State Registry", "Licence / Certificate", "Credentials", "Father's Name / Exp.", "DOB / Specialization", "Additional Notes"]
                    st.write(f"Showing all matching coaches (total: {len(co_display)}):")
                    st.dataframe(co_display.reset_index(drop=True), use_container_width=True, height=280, hide_index=True)
            else:
                person_row = filtered_coaches[filtered_coaches["name"] == selected_coach].iloc[0]
                render_bio(selected_coach, True, person_row)
\n'''
    
    with open('app/dashboard.py', 'w') as f:
        f.write(part1 + new_code + part3)
    print("Patched dashboard.py successfully.")
else:
    print("Failed to find markers.")
