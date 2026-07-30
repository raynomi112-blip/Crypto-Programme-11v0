import streamlit as st

# --- 1. FULL MOBILE CANVASSING SETTINGS ---
st.set_page_config(page_title="Waqar Zaka Quantum Core", layout="wide", initial_sidebar_state="collapsed")
st.markdown("<style>header,footer,div[data-testid='stToolbar']{visibility:hidden!important;}.block-container{padding:0px!important;margin:0px!important;width:100vw!important;max-width:100%!important;}body{background-color:#000;overflow:hidden!important;}iframe{width:100vw!important;height:100vh!important;border:none!important;position:absolute;top:0;left:0;}</style>", unsafe_allow_html=True)

# --- 2. CINEMATIC LIVE MATRIX STRINGS AND TARGETS ---
simulation_code = """
<!DOCTYPE html><html><head><style>
* { margin:0; padding:0; box-sizing:border-box; }
body, html { width:100%; height:100%; background:#000; overflow:hidden; font-family:monospace; color:#fff; }
canvas { display:block; width:100vw; height:100vh; position:absolute; z-index:1; }
.hud { position:absolute; z-index:10; width:100%; height:100%; pointer-events:none; padding:30px; display:flex; flex-direction:column; justify-content:space-between; }
.panel { background:rgba(2,2,4,0.93); border:1px solid #107c41; padding:20px; border-radius:6px; pointer-events:auto; }
.glow-g { color:#2ecc71; font-weight:bold; text-shadow:0 0 10px rgba(46,204,113,0.7); }
.glow-r { color:#e74c3c; font-weight:bold; text-shadow:0 0 10px rgba(231,76,60,0.7); }
.glow-c { color:#00f2fe; font-weight:bold; text-shadow:0 0 10px rgba(0,242,254,0.7); }
.stamp { position:absolute; font-size:12px; letter-spacing:4px; color:rgba(255,255,255,0.25); font-weight:bold; transform:rotate(-90deg); transform-origin:left top; }
</style></head><body>
<canvas id="c"></canvas>
<div class="hud">
    <div style="display:flex; justify-content:space-between; width:100%;">
        <div class="panel" style="width:360px; border-left:5px solid #27ae60;">
            <div style="font-size:11px; color:#7f8c8d; margin-bottom:8px;">📡 GLOBAL INTELLIGENCE INGESTION FEED</div>
            <b>⚡ 1. GLOBAL USA NEWS (25%)</b> -> <span class="glow-g" id="s1">84% ONLINE</span><br><br>
            <b>⚔️ 2. WAR & GEOPOLITICS (25%)</b> -> <span class="glow-r" id="s2">28% STABILITY</span><br><br>
            <b>🧠 3. AI ANALYSIS & LEADERS (50%)</b> -> <span class="glow-g" id="s3">81% ANALYZED</span>
        </div>
        <div class="panel" style="position:absolute; top:30px; left:410px; width:300px; border-color:#27ae60;">
            <span style="color:#7f8c8d; font-size:10px;">AUTHORIZED TERMINAL CONTEXT:</span><br>
            <span class="glow-g" style="font-size:14px;">WAQAR ZAKA STUDENT</span><br><span style="font-size:11px;">SECURE NODE INFRASTRUCTURE #993</span>
        </div>
        <div class="panel" style="width:390px; border-top:5px solid #00f2fe;">
            <div class="glow-c" style="font-size:13px; margin-bottom:10px;">🤖 INFLUENCER & CHANNEL MATRIX (4H)</div>
            <div style="display:flex; justify-content:space-between; margin-bottom:5px;"><span>4H LIVE BTC PRICE:</span><br><span class="glow-c" id="p_btc">$94,120</span></div>
            <div style="display:flex; justify-content:space-between; margin-bottom:5px; color:#27ae60;"><span>🟢 TAKE PROFIT (TP):</span><span style="color:#fff" id="p_tp">$96,500</span></div>
            <div style="display:flex; justify-content:space-between; margin-bottom:5px; color:#e74c3c;"><span>🔴 STOP LOSS (SL):</span><span style="color:#fff" id="p_sl">$92,100</span></div>
            <div style="display:flex; justify-content:space-between; color:#f1c40f;"><span>⚡ BREAKOUT ACCEL:</span><span style="color:#f1c40f; font-weight:bold;" id="p_brk">$97,200</span></div>
        </div>
    </div>
    <div class="stamp" style="top:55%; left:420px;">★ WAQAR ZAKA TEAM SEALS GLOBAL NETWORK ★</div>
    <div class="stamp" style="top:55%; right:380px; transform:rotate(90deg); transform-origin:right top;">★ WAQAR ZAKA STUDENT QUANT INTERFACE ★</div>
    <div class="panel" style="width:100%; text-align:center; padding:15px; border-color:#27ae60;">
        <div style="font-size:12px;" id="f_str">🔮 WAQAR ZAKA ALGO PREDICTION ENGINE // DIRECTION BIAS // BTC: STRONG UPWARD TREND 📈 | ETH: ACCELERATING BULLISH 📈</div>
        <div style="font-size:11px; margin-top:5px; color:#7f8c8d;" id="t_str">📰 LIVE FEED: SCANNING BIG CRYPTO CHANNELS AND TOP INFLUENCERS AUTOMATICALLY...</div>
    </div>
</div>
<script>
const canvas = document.getElementById('c'), ctx = canvas.getContext('2d');
function resize() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
window.addEventListener('resize', resize); resize();
const fibers = [], mx = 415;
for(let i=0; i<800; i++) {
    let r = i/800, y = 60 + r*(canvas.height-180), cat = 1, fac = 0.84;
    if(r>0.25 && r<=0.5) { cat=2; fac=0.28; } else if(r>0.5) { cat=3; fac=0.81; }
    fibers.push({y:y, cat:cat, broken:Math.random()>fac, seed:Math.random()*100, v:0.01+Math.random()*0.02, sx:0.2+Math.random()*0.6, g:20+Math.random()*40});
}
let clock = 0;
const news = ["INFLUENCER STREAM: Top-tier channels aligning 4H buy structures with volume.", "CHANNEL ALPHA: Heavy whale configurations establishing target breakout metrics.", "USA FED UPDATE: Regulatory news flow monitors state crypto parameters positively."];
function loop() {
    clock += 0.04; ctx.clearRect(0,0,canvas.width,canvas.height); const tw = canvas.width - mx;
    ctx.fillStyle='#0f0f14'; ctx.strokeStyle='#27ae60'; ctx.lineWidth=1.5;
    ctx.fillRect(mx-22,40,22,canvas.height-110); ctx.strokeRect(mx-22,40,22,canvas.height-110);
    ctx.fillRect(tw,40,22,canvas.height-110); ctx.strokeRect(tw,40,22,canvas.height-110);
    for(let f of fibers) {
        let dy = f.y + Math.sin(clock*f.v*12+f.seed)*1.2;
        if(!f.broken) {
            ctx.beginPath(); ctx.moveTo(mx,dy); ctx.lineTo(tw,dy); ctx.strokeStyle='rgba(46,204,113,0.4)'; ctx.lineWidth=1; ctx.stroke();
        } else {
            let px = mx + (tw-mx)*f.sx;
            ctx.beginPath(); ctx.moveTo(mx,dy); ctx.bezierCurveTo(mx+(px-mx)*0.5,dy,px,dy+f.g*0.35,px-6,dy+f.g); ctx.strokeStyle='rgba(231,76,60,0.55)'; ctx.stroke();
            ctx.beginPath(); ctx.moveTo(tw,dy); ctx.bezierCurveTo(tw-(tw-px)*0.5,dy,px,dy+f.g*0.35,px+6,dy+f.g); ctx.stroke();
        }
    }
    if(Math.random()<0.005) {
        document.getElementById('t_str').innerText = "📰 STREAM: " + news[Math.floor(Math.random()*news.length)];
        let btc = parseInt(document.getElementById('p_btc').innerText.replace(/[^0-9]/g,'')) + Math.floor(Math.random()*120)-50;
        document.getElementById('p_btc').innerText = "$"+btc.toLocaleString();
        document.getElementById('p_tp').innerText = "$"+(btc+2380).toLocaleString();
        document.getElementById('p_sl').innerText = "$"+(btc-2020).toLocaleString();
        document.getElementById('p_brk').innerText = "$"+(btc+3080).toLocaleString();
    }
    requestAnimationFrame(loop);
}
loop();
</script></body></html>
"""

# --- 3. RUN INTERFACE AT 100% SIDE-TO-SIDE LENGTH ---
st.components.v1.html(simulation_code, height=940, scrolling=False)
