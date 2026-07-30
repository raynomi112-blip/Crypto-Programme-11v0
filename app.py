import streamlit as st
import plotly.graph_objects as go
import numpy as np
import time
import random

# --- 1. MAXIMUM FULL-SCREEN TECH CANVAS ---
st.set_page_config(
    page_title="Crypto Glass Intelligence // Waqar Zaka Quantum Matrix", 
    layout="wide",  
    initial_sidebar_state="collapsed"
)

# Deep system injection to force true full-screen layout on phone browsers
st.markdown("""
    <style>
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container {padding: 0px !important; margin: 0px !important; max-width: 100% !important;}
    .stPlotlyChart {width: 100vw !important; height: 100vh !important; background-color: #000000;}
    body {background-color: #000000; overflow: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE 2-SECOND LIVE STREAM REFRESH ENGINE ---
# This initializes or increments a continuous refresh counter
if "refresh_counter" not in st.session_state:
    st.session_state.refresh_counter = 0
st.session_state.refresh_counter += 1

# --- 3. DYNAMIC REAL-TIME AI CALCULATOR ---
def run_quantum_waqar_zaka_engine():
    """
    AI core simulating 5-second updates from Google News, X loops, and charts.
    Introduces slight randomized shifts to animate the hair movement live.
    """
    # Base baseline metrics
    usa_base = 78
    war_base = 34
    ai_base = 82
    
    # Generate live price data targets
    btc_price = 92450 + random.randint(-150, 180)
    resistance = btc_price + 1200 - (btc_price % 50)
    spot_support = btc_price - 1800 + (btc_price % 50)
    breakout_trigger = resistance + 350
    
    return {
        "usa_news": {"health": usa_base + random.randint(-3, 3)},
        "war_news": {"health": war_base + random.randint(-2, 4)},
        "influencer_ai_analysis": {"health": ai_base + random.randint(-2, 2)},
        "btc_next_hour": "STRONG UPWARD MOMENTUM 📈",
        "eth_next_hour": "BULLISH ACCELERATION 📈",
        "bullish_percentage": 74 + random.randint(-2, 1),
        "btc_live": btc_price,
        "resistance": resistance,
        "support": spot_support,
        "breakout": breakout_trigger
    }

intel = run_quantum_waqar_zaka_engine()
bull_score = intel["bullish_percentage"]
bear_score = 100 - bull_score

# --- 4. THE HIGH-TECH CHART GRAPH COMPOSITION ---
fig = go.Figure()

# Pure absolute deep black background void
fig.add_shape(
    type="rect", x0=-12, y0=-28, x1=23, y1=115,
    fillcolor="#000000", line=dict(width=0), layer="below"
)

# Sleek 3D Metallic Carbon-Fiber Pillars (Left and Right Rods)
fig.add_shape(type="rect", x0=-0.6, y0=-5, x1=0, y1=105, fillcolor="#111116", line=dict(color="#1f1f2e", width=2.5))
fig.add_shape(type="rect", x0=10, y0=-5, x1=10.6, y1=105, fillcolor="#111116", line=dict(color="#1f1f2e", width=2.5))

# --- 5. EXHAUSTIVE DENSE HAIR-STRAND PLOTTING SYSTEM ---
sections = [
    {"name": "⚡ 1. GLOBAL USA NEWS (25%)", "data": intel["usa_news"], "y_start": 75, "y_end": 100, "count": 150},
    {"name": "⚔️ 2. WAR & GEOPOLITICS (25%)", "data": intel["war_news"], "y_start": 50, "y_end": 75, "count": 150},
    {"name": "🧠 3. AI ANALYSIS & LEADERS (50%)", "data": intel["influencer_ai_analysis"], "y_start": 0, "y_end": 50, "count": 300},
]

for sec in sections:
    health_pct = sec["data"]["health"]
    y_lines = np.linspace(sec["y_start"] + 0.8, sec["y_end"] - 0.8, sec["count"])
    broken_limit = int(sec["count"] * (100 - health_pct) / 100)
    
    for idx, y_base_pos in enumerate(y_lines):
        is_broken = idx < broken_limit
        # Add micro-vibrations to every fiber for visual effect
        vibe = random.uniform(-0.15, 0.15)
        y_pos = y_base_pos + vibe
        
        if not is_broken:
            # POSITIVE STRANDS: Extremely dense glowing neon Matrix Green lines
            fig.add_trace(go.Scatter(
                x=[0, 10], y=[y_pos, y_pos], mode="lines",
                line=dict(color="rgba(39, 174, 96, 0.45)", width=0.8),
                hoverinfo="none", showlegend=False
            ))
        else:
            # NEGATIVE STRANDS: Dense Crimson Red falling curves draping down like real loose hair
            # Left side falling strands
            x_left = np.linspace(0, 2.8, 10)
            y_left = y_pos - (x_left ** 2) * 0.35  
            fig.add_trace(go.Scatter(
                x=x_left, y=y_left, mode="lines",
                line=dict(color="rgba(211, 47, 47, 0.55)", width=0.7),
                hoverinfo="none", showlegend=False
            ))
            
            # Right side falling strands
            x_right = np.linspace(7.2, 10, 10)
            y_right = y_pos - ((10 - x_right) ** 2) * 0.35
            fig.add_trace(go.Scatter(
                x=x_right, y=y_right, mode="lines",
                line=dict(color="rgba(211, 47, 47, 0.55)", width=0.7),
                hoverinfo="none", showlegend=False
            ))

    # Category Sector Tags
    fig.add_annotation(
        x=-5.8, y=(sec["y_start"] + sec["y_end"]) / 2,
        text=f"<b>{sec['name']}</b><br><span style='color:#a6b8c7;'>SECTOR SCORE: {health_pct}%</span>",
        showarrow=False, font=dict(size=12, color="#ffffff", family="Monospace"), align="left"
    )

# --- 6. EXTRAORDINARY REAL-TIME BREAKOUT TARGET BOX ---
# Glowing neon cyan info terminal positioned prominently on the right hand side
box_x = 17.5
fig.add_shape(
    type="rect", x0=box_x - 0.5, y0=15, x1=box_x + 5.0, y1=65,
    fillcolor="#09090d", line=dict(color="#00f2fe", width=2)
)

breakout_hud_text = (
    f"<span style='color:#00f2fe; font-size:13px;'><b>🤖 AI TARGET MATRIX LIVE</b></span><br><br>"
    f"<span style='color:#ffffff; font-size:11px;'>LIVE BTC INDEX:</span><br>"
    f"<span style='color:#00f2fe; font-size:16px;'><b>${intel['btc_live']:,}</b></span><br><br>"
    f"<span style='color:#27ae60; font-size:11px;'>🟢 PROMINENT SPOT SUPPORT:</span><br>"
    f"<span style='color:#ffffff; font-size:13px;'><b>${intel['support']:,}</b></span><br><br>"
    f"<span style='color:#e74c3c; font-size:11px;'>🔴 PROMINENT RESISTANCE AREA:</span><br>"
    f"<span style='color:#ffffff; font-size:13px;'><b>${intel['resistance']:,}</b></span><br><br>"
    f"<span style='color:#f1c40f; font-size:11px;'>⚡ NEXT BREAKING POINT:</span><br>"
    f"<span style='color:#ffffff; font-size:13px;'><b>${intel['breakout']:,}</b></span>"
)

fig.add_annotation(
    x=box_x + 2.2, y=40, text=breakout_hud_text,
    showarrow=False, font=dict(family="Courier New"), align="left"
)

# --- 7. BOTTOM HUD DIRECTIONAL FORECAST BAR ---
hud_y = -16
fig.add_shape(
    type="rect", x0=-11.5, y0=hud_y - 8, x1=22.5, y1=hud_y + 4,
    fillcolor="#09090d", line=dict(color="#27ae60", width=1.5)
)

hud_text = (
    f"🔮 WAQAR ZAKA ALGO PREDICTION ENGINE // NEXT 60-MIN BIAS // BTC: {intel['btc_next_hour']} | ETH: {intel['eth_next_hour']}<br>"
    f"📊 NETWORK SENTIMENT RATIO: {bull_score}% BULLISH INDICATION SYSTEM // SYSTEM HEARTBEAT REFRESH ACTIVE [5s REGULATED LOOP]"
)

fig.add_annotation(
    x=5, y=hud_y - 2, text=hud_text,
    showarrow=False, font=dict(size=12, color="#ffffff", family="Monospace"), align="center", xref="x", yref="y"
)

# --- 8. WAQAR ZAKA ULTRA-PROMINENT CUSTOM BRANDING ---
fig.add_annotation(
    x=-0.3, y=50, text="★ WAQAR ZAKA TEAM SEALS GLOBAL NETWORK ★",
    showarrow=False, font=dict(size=11, color="rgba(255, 255, 255, 0.22)", family="Impact"), textangle=-90
)

fig.add_annotation(
    x=10.3, y=50, text="★ WAQAR ZAKA STUDENT QUANT INTERFACE ★",
    showarrow=False, font=dict(size=11, color="rgba(255, 255, 255, 0.22)", family="Impact"), textangle=90
)

fig.add_annotation(
    x=17.5, y=100,
    text="<b>⚡ OPERATOR IDENTIFICATION:</b><br><span style='color:#27ae60; font-size:16px;'><b>WAQAR ZAKA STUDENT</b></span><br><span style='color:#7f8c8d; font-size:10px;'>OFFICIAL TEAM NODE #993</span>",
    showarrow=False, font=dict(size=12, color="#ffffff", family="Courier New"),
    bordercolor="#27ae60", borderwidth=1, borderpad=8, bgcolor="#0d0d11", align="left"
)

# --- 9. DIMENSIONAL GRAPH VIEWPORT CONTROL ---
fig.update_layout(
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-11.8, 22.8]),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[hud_y - 11, 108]),
    plot_bgcolor="#000000", paper_bgcolor="#000000",
    margin=dict(l=0, r=0, t=20, b=0),
    dragmode=False
)

# Render to user canvas screen
st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

# --- 10. FORCE THE AUTOMATIC REFRESH LOOP ---
time.sleep(2.0)  # Wait exactly 2 seconds
st.rerun()      # Trigger script to execute from the top with fresh numbers and shifts!
