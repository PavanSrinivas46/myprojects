import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import numpy as np
import datetime

# ⏱️ 1-MINUTE AUTO-REFRESH TRIGGER
# This forces the app to refresh every 60,000 milliseconds (1 minute).
st_autorefresh(interval=60000, key="growth_os_refresh")

# ==========================================
# 📊 MOCK DATA FETCHING FUNCTIONS
# ==========================================
@st.cache_data(ttl=55)  
def fetch_overview_metrics():
    return {
        "yt_subs": 125430, "ig_followers": 89200, "wa_members": 4250,
        "total_views": 1540300, "watch_time": "45.2K hrs", "revenue": "$3,240",
        "today_growth": "+1.2%", "weekly_growth": "+8.5%", "monthly_growth": "+24.1%"
    }

@st.cache_data(ttl=55)
def fetch_realtime_panel():
    return {
        "live_subs": 125432, "live_ig": 89204,
        "last_video": {"title": "Build a SaaS with AI", "views": 12400, "ctr": "8.2%"},
        "last_reel": {"title": "DevOps Secret Tool 🤫", "views": 45100, "likes": 3200}
    }

@st.cache_data(ttl=55)
def fetch_analytics_data():
    dates = pd.date_range(start="2026-06-01", periods=30)
    return pd.DataFrame({
        "Date": dates,
        "Subscribers": np.cumsum(np.random.randint(50, 200, size=30)) + 120000,
        "Followers": np.cumsum(np.random.randint(30, 150, size=30)) + 85000,
        "Views": np.random.randint(5000, 25000, size=30)
    })

# ==========================================
# 🎨 DASHBOARD UI LAYOUT
# ==========================================
st.set_page_config(page_title="Growth OS Mission Control", page_icon="🚀", layout="wide")

st.title("🚀 Growth OS Mission Control")
st.caption(f"🔄 Auto-syncing every 60 seconds. Last updated: {datetime.datetime.now().strftime('%H:%M:%S')}")

metrics = fetch_overview_metrics()
realtime = fetch_realtime_panel()
df = fetch_analytics_data()

# --- Section 1: Overview ---
st.markdown("## 📊 Overview")
c1, c2, c3, c4, c5, c6 = st.columns(6)
c1.metric("YouTube Subs", f"{metrics['yt_subs']:,}", metrics['today_growth'])
c2.metric("Instagram Followers", f"{metrics['ig_followers']:,}", metrics['weekly_growth'])
c3.metric("WhatsApp Members", f"{metrics['wa_members']:,}", metrics['monthly_growth'])
c4.metric("Total Views", metrics['total_views'])
c5.metric("Watch Time", metrics['watch_time'])
c6.metric("Revenue (Est.)", metrics['revenue'])
st.divider()

# --- Section 2: Real-Time & Content ---
col_left, col_right = st.columns([1, 1])
with col_left:
    st.markdown("## 🔴 Real-Time Panel")
    rt1, rt2 = st.columns(2)
    rt1.metric("🔴 Live YT Subs", f"{realtime['live_subs']:,}")
    rt2.metric("🔴 Live IG Followers", f"{realtime['live_ig']:,}")
    
    st.info(f"**🎥 Last Video:** {realtime['last_video']['title']}\n\n👀 Views: {realtime['last_video']['views']:,} | 🎯 CTR: {realtime['last_video']['ctr']}")
    st.info(f"**📱 Last Reel:** {realtime['last_reel']['title']}\n\n👀 Views: {realtime['last_reel']['views']:,} | ❤️ Likes: {realtime['last_reel']['likes']:,}")

with col_right:
    st.markdown("## 🎯 Content Planner")
    st.checkbox("📅 Today: Python Automation Shorts", value=False)
    st.checkbox("🎬 Next Reel: Streamlit Dashboard", value=False)
    st.checkbox("📺 Next Video: Free APIs Guide", value=False)
    
    st.table(pd.DataFrame({
        "Platform": ["YouTube", "Instagram", "YouTube"],
        "Topic": ["Docker Tips", "Ansible Tricks", "DevOps Roadmap"],
        "Status": ["Ready", "Filming", "Scripting"]
    }))
st.divider()

# --- Section 3: Graphs ---
st.markdown("## 📈 Analytics Graphs")
g1, g2 = st.columns(2)
with g1:
    st.line_chart(df.set_index("Date")[["Subscribers", "Followers"]])
with g2:
    st.bar_chart(df.set_index("Date")["Views"])
