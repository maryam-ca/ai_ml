import streamlit as st
import base64
import os

# ================= IMAGE HELPER =================
def get_base64_image(filename):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(BASE_DIR, "assets", filename)
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


# ================= THEME + CENTER + EMPTY CARD FIX =================
def load_theme():
    st.markdown("""
    <style>
    html, body {
      background: linear-gradient(135deg, #020617, #0f172a, #1e1b4b);
    }

    /* CENTER MAIN CONTENT */
    .main > div {
      max-width: 1180px;
      margin-left: auto;
      margin-right: auto;
      padding-left: 1rem;
      padding-right: 1rem;
    }

    /* CARD STYLE */
    .card {
      background: rgba(255,255,255,0.12);
      border-radius: 30px;
      padding: 42px;
      margin: 36px auto;
      backdrop-filter: blur(20px);
      box-shadow: 0 30px 80px rgba(0,0,0,.65);
    }

    /* REMOVE EMPTY CARDS */
    .card:empty {
      display: none !important;
      margin: 0 !important;
      padding: 0 !important;
    }

    h1, h2, h3, p, label {
      color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)


# ================= HEADER =================
def render_header():
    img_base64 = get_base64_image("header.jpg")

    st.markdown(f"""
    <div style="
      margin: 36px auto;
      max-width: 1180px;
      border-radius: 30px;
      overflow: hidden;
      box-shadow: 0 30px 80px rgba(0,0,0,.65);
    ">
      <div style="position:relative; height:260px;">
        <img src="data:image/jpg;base64,{img_base64}"
             style="
               position:absolute;
               inset:0;
               width:100%;
               height:100%;
               object-fit:cover;
               filter:brightness(0.85);
             ">
        <div style="
          position:absolute;
          inset:0;
          background:linear-gradient(
            rgba(0,0,0,.25),
            rgba(0,0,0,.55)
          );
        "></div>
        <div style="
          position:absolute;
          inset:0;
          display:flex;
          align-items:center;
          justify-content:center;
          text-align:center;
        ">
          <h1 style="
            font-size:3.6rem;
            font-weight:900;
            letter-spacing:2px;
            text-shadow:0 8px 25px rgba(0,0,0,.9);
          ">
            🎓 STUDENT MANAGEMENT SYSTEM
          </h1>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)


# ================= MENU (SAFE DEFAULT) =================
def render_menu():
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    cols = st.columns(6)
    menu_items = ["Add Student", "View Students", "Import CSV", "Update Student", "Search", "Delete"]

    if "menu" not in st.session_state:
        st.session_state.menu = "Add Student"

    for col, item in zip(cols, menu_items):
        with col:
            if st.button(
                item,
                use_container_width=True,
                type="primary" if st.session_state.menu == item else "secondary"
            ):
                st.session_state.menu = item

    st.markdown("<div style='height:30px'></div>", unsafe_allow_html=True)
    return st.session_state.menu
