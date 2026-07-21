import re

with open("app/dashboard.py", "r") as f:
    content = f.read()

# Replace the Athlete Bio card rendering code
old_athlete_card = """                else:
                    st.markdown(f\"\"\"
                    <div class="acard" style="min-height:220px;">
                        <span class="tag blue" style="float:right;">Performance</span>
                        <b style="font-size:1.05rem;color:var(--blue);">AthletIQ Pathway Metrics</b>
                        <hr style="margin:0.8rem 0;border-color:rgba(16,229,179,0.15);">
                        <div style="font-size:0.85rem;line-height:1.6;color:var(--text2);">
                            <b>Opportunity Score:</b> <span class="tag amber">{person_row['athletiq_opportunity_score']} / 10.0</span><br>
                            <b>Performance Level:</b> {person_row['performance_level']}<br>
                            <b>Funding Status:</b> {person_row['funding_status']}<br>
                            <b>Pipeline Stage:</b> {person_row['pipeline_stage']}<br>
                        </div>
                    </div>
                    \"\"\", unsafe_allow_html=True)"""

new_athlete_card = """                else:
                    # Determine mock coach and centre based on performance/state
                    coach_val = "Assigned National Coach" if person_row['performance_level'] in ["International", "National"] else "Regional Academy Coach"
                    centre_val = "SAI NCOE " + str(person_row.get('state', 'Unknown')) if person_row['performance_level'] in ["International", "National"] else "Local State Academy"
                    
                    st.markdown(f\"\"\"
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
                    \"\"\", unsafe_allow_html=True)"""

content = content.replace(old_athlete_card, new_athlete_card)

with open("app/dashboard.py", "w") as f:
    f.write(content)
print("Updated Profile Card")
