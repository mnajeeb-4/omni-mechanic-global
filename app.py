"""
OmniMechanic Global - The Ultimate AI Repair Copilot.
Master Execution File for Streamlit.
"""
import streamlit as st

# Import UI components and CSS
from ui_components.custom_css import load_clay_glass_css
from ui_components.global_tools_db import TOOLS_DB

# Import Domains
from domains import auto_mechanic, moto_mechanic, electrical_hub, home_appliances, plumbing_hvac

# 1. Apply Global Luxury CSS
st.set_page_config(page_title="OmniMechanic Global", page_icon="⚙️", layout="wide")
st.markdown(load_clay_glass_css(), unsafe_allow_html=True)

# 2. Sidebar Navigation
st.sidebar.image("https://img.icons8.com/color/120/artificial-intelligence.png", width=100)
st.sidebar.title("OmniMechanic Global")
st.sidebar.markdown("**The All-Knowing Mechanic AI**")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Repair Domain:",
    ["🚗 Automotive", "🏍️ Motorcycle", "⚡ Electrical", "🏠 Appliances", "💧 Plumbing/HVAC", "🧰 Global Tools"]
)

st.sidebar.markdown("---")
st.sidebar.warning("⚠️ Ensure your webcam/mic is active for live diagnostics.")

# 3. Main Page Routing
if page == "🚗 Automotive":
    auto_mechanic.render()
elif page == "🏍️ Motorcycle":
    moto_mechanic.render()
elif page == "⚡ Electrical":
    electrical_hub.render()
elif page == "🏠 Appliances":
    home_appliances.render()
elif page == "💧 Plumbing/HVAC":
    plumbing_hvac.render()
elif page == "🧰 Global Tools":
    st.markdown('<h1 style="text-shadow: 0 0 20px rgba(108,99,255,0.3);">🧰 Global Tool Encyclopedia</h1>', unsafe_allow_html=True)
    st.markdown("Browse the ultimate arsenal of mechanical, electrical, and plumbing tools.")
    
    # Massive Grid for Global Tools
    cols = st.columns(4)
    for i, (name, data) in enumerate(TOOLS_DB.items()):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="clay-card" style="text-align:center; height:100%;">
                <img src="{data['icon_url']}" width="80">
                <h4 style="color:#6C63FF; margin:10px 0;">{name}</h4>
                <p style="font-size:0.8rem; color:#aaa;">{data['description']}</p>
                <div style="background:#0E1117; border-radius:12px; padding:6px; margin-top:8px; font-size:0.7rem;">
                    {data['usage']}
                </div>
            </div>
            """, unsafe_allow_html=True)

# 4. Error Handling / Fallback
st.markdown("---")
st.caption("OmniMechanic Global v2.0 | Built with YOLOv8, Librosa, Groq, and Streamlit. If your camera fails, the AI will auto-fallback to mock diagnostics.")
