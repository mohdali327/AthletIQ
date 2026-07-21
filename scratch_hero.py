import re

with open("app/dashboard.py", "r") as f:
    content = f.read()

# 1. Add Shopify Editions inspired CSS animations and classes
css_to_add = """
    /* --- EDITIONS HERO CSS --- */
    @keyframes editionsFadeUp {
        0% { opacity: 0; transform: translateY(40px) scale(0.95); filter: blur(10px); }
        100% { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }
    }
    @keyframes editionsFloat {
        0%, 100% { transform: translateY(0) scale(1); }
        50% { transform: translateY(-20px) scale(1.05); }
    }
    @keyframes editionsGlow {
        0%, 100% { opacity: 0.5; filter: blur(60px) hue-rotate(0deg); }
        50% { opacity: 0.8; filter: blur(80px) hue-rotate(90deg); }
    }
    .editions-hero {
        position: relative;
        text-align: center;
        padding: 6rem 1rem 4rem;
        overflow: hidden;
        border-radius: 24px;
        background: radial-gradient(circle at top, rgba(16,229,179,0.1) 0%, transparent 60%),
                    radial-gradient(circle at bottom, rgba(104,61,228,0.1) 0%, transparent 60%);
        border: 1px solid rgba(255,255,255,0.05);
        margin-bottom: 3rem;
    }
    .editions-orb-1 {
        position: absolute; top: -10%; left: 10%; width: 300px; height: 300px;
        background: rgba(16,229,179,0.4); border-radius: 50%;
        animation: editionsGlow 12s infinite ease-in-out;
        z-index: 0; pointer-events: none;
    }
    .editions-orb-2 {
        position: absolute; bottom: -20%; right: 10%; width: 400px; height: 400px;
        background: rgba(104,61,228,0.3); border-radius: 50%;
        animation: editionsGlow 15s infinite ease-in-out reverse;
        z-index: 0; pointer-events: none;
    }
    .editions-title {
        position: relative; z-index: 1;
        font-family: 'Outfit', sans-serif;
        font-size: 5rem;
        font-weight: 900;
        line-height: 1.1;
        letter-spacing: -2px;
        background: linear-gradient(135deg, #FFFFFF 0%, #10E5B3 50%, #683DE4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: editionsFadeUp 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        margin-bottom: 1rem;
    }
    .editions-subtitle {
        position: relative; z-index: 1;
        font-size: 1.2rem;
        color: rgba(255,255,255,0.7);
        max-width: 600px;
        margin: 0 auto 2rem;
        animation: editionsFadeUp 1.2s cubic-bezier(0.16, 1, 0.3, 1) 0.2s forwards;
        opacity: 0;
    }
    .editions-badge {
        display: inline-block;
        padding: 0.5rem 1.2rem;
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 50px;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #fff;
        backdrop-filter: blur(10px);
        animation: editionsFadeUp 1.2s cubic-bezier(0.16, 1, 0.3, 1) 0.4s forwards;
        opacity: 0;
    }
    .anim-fade-up {
        animation: editionsFadeUp 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    .delay-1 { animation-delay: 0.1s; opacity: 0; }
    .delay-2 { animation-delay: 0.2s; opacity: 0; }
    .delay-3 { animation-delay: 0.3s; opacity: 0; }
</style>
"""
content = content.replace("</style>", css_to_add)

# 2. Replace the first tab's header with the massive hero
old_pathway_start = """if selected_tab == "Pathway Overview":
    st.markdown('<div class="stitle sticky-header" title="Strategic Dashboard Homepage"> Pathway Overview <span class="chip chip-blue">Strategic Dashboard Homepage</span></div>', unsafe_allow_html=True)"""

new_pathway_start = """if selected_tab == "Pathway Overview":
    st.markdown('''
    <div class="editions-hero">
        <div class="editions-orb-1"></div>
        <div class="editions-orb-2"></div>
        
        <div class="editions-badge">✦ Spring 2026 Edition ✦</div>
        <div class="editions-title">ATHLETIQ<br>INTELLIGENCE</div>
        <div class="editions-subtitle">
            Scouting, coaching and funding intelligence for India's grassroots-to-medal pathways. 
            Experience our most immersive data pipeline yet.
        </div>
        
        <div style="display:flex; justify-content:center; gap:1rem; margin-top:2rem; position:relative; z-index:1;">
            <div style="background:rgba(255,255,255,0.05); padding:1rem 2rem; border-radius:12px; border:1px solid rgba(16,229,179,0.3); backdrop-filter:blur(10px); animation: editionsFadeUp 1s 0.6s forwards; opacity:0;">
                <div style="font-size:2rem; font-weight:900; color:#10E5B3;">34K+</div>
                <div style="font-size:0.8rem; color:#aaa; text-transform:uppercase; letter-spacing:1px;">Active Profiles</div>
            </div>
            <div style="background:rgba(255,255,255,0.05); padding:1rem 2rem; border-radius:12px; border:1px solid rgba(104,61,228,0.3); backdrop-filter:blur(10px); animation: editionsFadeUp 1s 0.7s forwards; opacity:0;">
                <div style="font-size:2rem; font-weight:900; color:#683DE4;">9</div>
                <div style="font-size:0.8rem; color:#aaa; text-transform:uppercase; letter-spacing:1px;">Talent Clusters</div>
            </div>
            <div style="background:rgba(255,255,255,0.05); padding:1rem 2rem; border-radius:12px; border:1px solid rgba(253,214,99,0.3); backdrop-filter:blur(10px); animation: editionsFadeUp 1s 0.8s forwards; opacity:0;">
                <div style="font-size:2rem; font-weight:900; color:#FDD663;">Live</div>
                <div style="font-size:0.8rem; color:#aaa; text-transform:uppercase; letter-spacing:1px;">Pipeline Sync</div>
            </div>
        </div>
    </div>
    
    <div class="stitle sticky-header" title="Strategic Dashboard Homepage" style="margin-top:0;"> Pathway Overview <span class="chip chip-blue">Strategic Dashboard Homepage</span></div>
    ''', unsafe_allow_html=True)"""

content = content.replace(old_pathway_start, new_pathway_start)

# 3. Add fade-up animations to the pipeline cards
old_cards = """<div class="acard" style="border-left:3px solid var(--purple);margin-bottom:0.6rem;padding:0.8rem 1.2rem;">"""
new_cards = """<div class="acard anim-fade-up delay-1" style="border-left:3px solid var(--purple);margin-bottom:0.6rem;padding:0.8rem 1.2rem;">"""
content = content.replace(old_cards, new_cards)

old_cards_2 = """<div class="acard" style="border-left:3px solid var(--teal);margin-bottom:0.6rem;padding:0.8rem 1.2rem;">"""
new_cards_2 = """<div class="acard anim-fade-up delay-2" style="border-left:3px solid var(--teal);margin-bottom:0.6rem;padding:0.8rem 1.2rem;">"""
content = content.replace(old_cards_2, new_cards_2)

old_cards_3 = """<div class="acard" style="border-left:3px solid var(--gold);margin-bottom:0.6rem;padding:0.8rem 1.2rem;">"""
new_cards_3 = """<div class="acard anim-fade-up delay-3" style="border-left:3px solid var(--gold);margin-bottom:0.6rem;padding:0.8rem 1.2rem;">"""
content = content.replace(old_cards_3, new_cards_3)

with open("app/dashboard.py", "w") as f:
    f.write(content)

print("Hero section added.")
