import streamlit as st
import requests
import json
import os
import bcrypt
import re
import random
from anime_data import ANIME_DB 

# 1. PAGE CONFIG
st.set_page_config(page_title="AnimeNexus", page_icon="⛩️", layout="wide")

# 2. DATABASE & SECURITY CONSTANTS
USER_DB_FILE = "users.json"

# --- SECURITY UTILITIES ---
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def is_strong_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search("[0-9]", password):
        return False, "Password must contain at least one number."
    if not re.search("[@_!#$%^&*()<>?/\|}{~:]", password):
        return False, "Password must contain at least one special character."
    return True, "Strong password!"

# --- DATABASE HELPERS ---
def load_users():
    if os.path.exists(USER_DB_FILE):
        with open(USER_DB_FILE, "r") as f:
            try: return json.load(f)
            except: return {}
    return {}

def save_user(username, password, recovery_answer):
    users = load_users()
    users[username] = {
        "password": hash_password(password),
        "recovery": recovery_answer.lower().strip()
    }
    with open(USER_DB_FILE, "w") as f:
        json.dump(users, f)

# 3. ANIMENEXUS THEME
def apply_nexus_theme():
    st.markdown(
        """
        <style>
        .stApp { background-color: #0b0b0b; color: #eeeeee; }
        .main-title {
            font-size: 50px;
            font-weight: 800;
            color: #ffbade;
            text-shadow: 3px 3px 5px rgba(0,0,0,0.7);
            text-align: center;
            margin-bottom: 20px;
        }
        /* Targets the login box area specifically */
        [data-testid="stVerticalBlock"] > div:has(div.stTabs) {
            background-color: #1a1a1a;
            padding: 30px;
            border-radius: 15px;
            border: 1px solid #ffbade;
        }
        .anime-container {
            background-color: #1a1a1a;
            padding: 20px;
            border-radius: 8px;
            border-left: 5px solid #ffbade;
            margin-bottom: 20px;
        }
        div.stButton > button:first-child {
            background-color: #ffbade;
            color: #0b0b0b;
            border: none;
            font-weight: bold;
            border-radius: 20px;
            width: 100%;
        }
        [data-testid="stMetricValue"] { color: #ffbade !important; }
        </style>
        """,
        unsafe_allow_html=True
    )

apply_nexus_theme()

# 4. INITIALIZE SESSION STATE
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# --- LOGIN PAGE ---
def login_page():
    st.markdown('<p class="main-title">⛩️ AnimeNexus Gateway</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        quotes = [
            "“Push through the pain. Giving up hurts more.” – Vegeta",
            "“If you don't take risks, you can't create a future.” – Luffy",
            "“Whatever you lose, you'll find it again.” – Kenshin",
            "“Fear is not evil. It tells you your weakness.” – Gildarts"
        ]
        st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <h2 style="color: #ffbade; margin-bottom: 5px;">Welcome to the Nexus</h2>
                <p style="font-style: italic; color: #888888;">{random.choice(quotes)}</p>
            </div>
        """, unsafe_allow_html=True)

        tab1, tab2, tab3 = st.tabs(["Login", "Register", "Recovery"])
        
        with tab1:
            u_login = st.text_input("Username", key="l_user")
            p_login = st.text_input("Password", type="password", key="l_pass")
            if st.button("Enter Nexus", key="btn_login"):
                users = load_users()
                if u_login == st.secrets["credentials"]["username"] and \
                   p_login == st.secrets["credentials"]["password"]:
                    st.session_state.logged_in = True
                    st.session_state.user_name = "Admin"
                    st.rerun()
                elif u_login in users and check_password(p_login, users[u_login]["password"]):
                    st.session_state.logged_in = True
                    st.session_state.user_name = u_login
                    st.rerun()
                else:
                    st.error("Invalid credentials.")

        with tab2:
            u_reg = st.text_input("New Username", key="r_user")
            p_reg = st.text_input("New Password", type="password", key="r_pass")
            rec_reg = st.text_input("Security Q: Favorite Anime?", key="r_rec")
            if st.button("Create Account", key="btn_reg"):
                users = load_users()
                strong, msg = is_strong_password(p_reg)
                if u_reg in users or u_reg == st.secrets["credentials"]["username"]:
                    st.error("Username taken!")
                elif not strong:
                    st.error(msg)
                elif not rec_reg:
                    st.error("Answer required!")
                else:
                    save_user(u_reg, p_reg, rec_reg)
                    st.success("Account Ready! Switch to Login tab.")

        with tab3:
            u_reset = st.text_input("Username", key="f_user")
            ans_reset = st.text_input("Answer: Favorite Anime?", key="f_ans")
            new_pass = st.text_input("New Password", type="password", key="f_pass")
            if st.button("Reset Password", key="btn_reset"):
                users = load_users()
                if u_reset in users and users[u_reset]["recovery"] == ans_reset.lower().strip():
                    strong, msg = is_strong_password(new_pass)
                    if strong:
                        users[u_reset]["password"] = hash_password(new_pass)
                        with open(USER_DB_FILE, "w") as f:
                            json.dump(users, f)
                        st.success("Updated! Login now.")
                    else: st.error(msg)
                else: st.error("Incorrect details.")

# --- DASHBOARD PAGE ---
def dashboard_page():
    head_col, out_col = st.columns([5, 1])
    with head_col:
        st.markdown('<p class="main-title" style="text-align:left;">⛩️ AnimeNexus Explorer</p>', unsafe_allow_html=True)
    with out_col:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

    @st.cache_data(show_spinner=False)
    def get_anime_poster(anime_name):
        try:
            url = f"https://api.jikan.moe/v4/anime?q={anime_name}&limit=1"
            response = requests.get(url, timeout=5)
            return response.json()['data'][0]['images']['jpg']['large_image_url']
        except: return "https://via.placeholder.com/300x450?text=Poster"

    search_query = st.text_input("", placeholder="Search the Nexus archive...", key="n_search").lower()
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Library", len(ANIME_DB))
    m2.metric("Security", "Hashed")
    m3.metric("User", st.session_state.user_name)
    st.divider()

    with st.sidebar:
        st.markdown(f"""
            <div style="text-align: center; padding: 15px; border-bottom: 1px solid #ffbade; margin-bottom: 20px;">
                <h3 style="color: #ffbade; margin: 0;">Konnichiwa,</h3>
                <h2 style="color: #eeeeee; margin: 0;">{st.session_state.user_name}! 🌸</h2>
            </div>
        """, unsafe_allow_html=True)
        st.header("Watch Category")
        category = st.radio("", ["Everything", "Series", "Movie", "OVA", "Special"])

    sorted_names = sorted(ANIME_DB.keys())
    for name in sorted_names:
        if search_query and search_query not in name.lower(): continue
        data = ANIME_DB[name]
        items = [i for i in (data if isinstance(data, list) else data.get("order", [])) if category == "Everything" or i['type'] == category]
        if items:
            st.markdown('<div class="anime-container">', unsafe_allow_html=True)
            c1, c2 = st.columns([1, 4])
            with c1: st.image(get_anime_poster(name), use_container_width=True)
            with c2:
                st.subheader(name)
                for item in items: st.markdown(f"📺 **:pink[{item['type']}]**: {item['title']}")
                st.link_button("▶ Stream", f"https://hianime.to/search?keyword={name.lower().replace(' ','-')}")
            st.markdown('</div>', unsafe_allow_html=True)

# 5. ROUTING
if st.session_state.logged_in:
    dashboard_page()
else:
    login_page()