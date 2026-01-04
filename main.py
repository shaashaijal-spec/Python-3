import streamlit as st
import os
import sys
from streamlit.web import cli as stcli

# ================= AUTO-FIX RUNNER =================
# This trick forces the Green Button to work!
if __name__ == '__main__':
    try:
        from streamlit.runtime.scriptrunner import get_script_run_ctx
        if not get_script_run_ctx():
            print("Restarting as Streamlit app...")
            sys.argv = ["streamlit", "run", __file__]
            sys.exit(stcli.main())
    except ImportError:
        pass

# ================= 1. CONFIG & DATA =================
st.set_page_config(page_title="Menu", layout="centered")

# Force Dark Theme Config
if not os.path.exists(".streamlit"):
    try:
        os.makedirs(".streamlit")
        with open(".streamlit/config.toml", "w") as f:
            f.write('[theme]\nbase="dark"\nprimaryColor="#4CAF50"')
    except:
        pass

# Shop Data
SHOP_EN = "SHAWARMA & BURGERLAK"
SHOP_AR = "شاورما و برجرلك"
PHONE = "+966 50 518 9381"
LOGO_FILE = "logo.png"
MENU_DATA = {
    "🌯 Shawarma / شاورما": [
        {"name": ("Shawarma Small", "شاورما صغير"), "price": 7.0, "cal": 380, "variants": [("With Cheese", "مع جبنة", 8.0)]},
        {"name": ("Shawarma Sarukh", "شاورما صاروخ"), "price": 8.0, "cal": 750, "variants": [("With Cheese", "مع جبنة", 9.0)]},
        {"name": ("Shawarma Arabi Small", "صحن عربي صغير"), "price": 11.0, "cal": 850, "variants": [("With Cheese", "مع جبنة", 12.0)]},
        {"name": ("Shawarma Arabi Big", "صحن عربي كبير"), "price": 16.0, "cal": 1300, "variants": [("With Cheese", "مع جبنة", 18.0)]},
        {"name": ("Shawarma Boshka", "شاورما بوشكا"), "price": 19.0, "cal": 950, "variants": [("With Cheese", "مع جبنة", 21.0)]},
    ],
    "🍔 Burgers / برجر": [
        {"name": ("Chicken Burger", "برجر دجاج"), "price": 8.0, "cal": 550, "variants": [("With Cheese", "مع جبنة", 9.0), ("Double", "دبل", 13.0)]},
        {"name": ("Beef Burger", "برجر لحم"), "price": 8.0, "cal": 600, "variants": [("With Cheese", "مع جبنة", 9.0), ("Double", "دبل", 13.0)]},
        {"name": ("Zinger Burger", "برجر زنجر"), "price": 11.5, "cal": 700, "variants": [("With Cheese", "مع جبنة", 12.5), ("Double", "دبل", 19.5)]},
        {"name": ("Fish Burger", "برجر سمك"), "price": 9.0, "cal": 500, "variants": [("With Cheese", "مع جبنة", 10.0), ("Double", "دبل", 15.0)]}
    ],
    "🥪 Sandwiches / ساندوتشات": [
        {"name": ("Nuggets Sandwich", "ساندوتش دجاج مسحب"), "price": 9.0, "cal": 600, "variants": [("With Cheese", "مع جبنة", 10.0)]},
        {"name": ("Chicken Fillet Sandwich", "ساندوتش دجاج فيلية"), "price": 9.0, "cal": 580, "variants": [("With Cheese", "مع جبنة", 10.0)]},
        {"name": ("Shrimp Sandwich", "ساندوتش جمبري"), "price": 9.0, "cal": 550, "variants": [("With Cheese", "مع جبنة", 10.0)]},
        {"name": ("Tortilla Sandwich", "ساندوتش تورتيلا"), "price": 10.0, "cal": 650, "variants": [("With Cheese", "مع جبنة", 11.0)]},
        {"name": ("Zinger Sandwich", "ساندوتش زنجر"), "price": 11.5, "cal": 720, "variants": [("With Cheese", "مع جبنة", 12.5)]},
    ],
    "🍽️ Plates & Meals / وجبات وصحون": [
        {"name": ("Chicken Nuggets Plate", "دجاج مسحب صحن"), "price": 20.0, "cal": 1100, "variants": []},
        {"name": ("Fish Broast", "بروست سمك"), "price": 19.0, "cal": 1200, "variants": []},
        {"name": ("Chicken Burger Meal", "وجبة برجر دجاج"), "price": 14.5, "cal": 950, "variants": [("With Cheese", "مع جبنة", 15.5)]},
        {"name": ("Beef Burger Meal", "وجبة برجر لحم"), "price": 14.5, "cal": 1000, "variants": [("With Cheese", "مع جبنة", 15.5)]},
        {"name": ("Zinger Meal", "وجبة زنجر"), "price": 18.0, "cal": 1100, "variants": [("With Cheese", "مع جبنة", 19.0)]},
    ],
    "🥤 Juices / عصائر": [
        {"name": ("Orange Juice", "عصير برتقال"), "price": 6.0, "cal": 120, "variants": [("Small", "صغير", 6.0), ("Big", "كبير", 8.0), ("Gallon", "جالون", 23.0)]},
        {"name": ("Mixed Juice", "عصير مشكل"), "price": 4.5, "cal": 160, "variants": [("Small", "صغير", 4.5), ("Big", "كبير", 7.0)]},
        {"name": ("Mango Juice", "عصير مانجو"), "price": 4.5, "cal": 170, "variants": [("Small", "صغير", 4.5), ("Big", "كبير", 7.0)]},
    ]
}

# CSS Styling
st.markdown("""
    <style>
    .variant-row { display: flex; justify-content: space-between; padding: 5px 0; border-bottom: 1px solid #333; }
    .base-price { color: #4CAF50; font-weight: bold; font-size: 1.1em; }
    .variant-price { color: #81C784; font-weight: bold; }
    .caption-text { color: #AAA; font-size: 0.9em; }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

if 'lang' not in st.session_state:
    st.session_state.lang = "EN"

# ================= 3. APP LAYOUT =================
# Logo & Title
try:
    c1, c2, c3 = st.columns([1,2,1])
    with c2: st.image(LOGO_FILE, use_container_width=True)
except: pass

st.markdown(f"<h2 style='text-align: center; margin:0;'>{SHOP_EN}</h2>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center; color: #BBB; margin:0;'>{SHOP_AR}</h3>", unsafe_allow_html=True)

# Language Button
if st.button("🔄 العربية / English", use_container_width=True):
    st.session_state.lang = "AR" if st.session_state.lang == "EN" else "EN"
    st.rerun()

st.divider()

# Search Bar
search_query = st.text_input("🔍 Search / بحث", "")

# ================= 4. MAIN LOOP =================
for category, items_list in MENU_DATA.items():
    visible_items = []

    # --- SEARCH FILTER ---
    if not search_query:
        visible_items = items_list
    else:
        for item in items_list:
            en, ar = item["name"]
            # Check Name
            found = (search_query.lower() in en.lower()) or (search_query in ar)
            # Check Variants
            if not found:
                for v in item["variants"]:
                    if (search_query.lower() in v[0].lower()) or (search_query in v[1]):
                        found = True
                        break
            if found:
                visible_items.append(item)

    # --- DISPLAY ITEMS ---
    if visible_items:
        # Category Title
        cat_title = category.split(" / ")[0] if st.session_state.lang == "EN" else category.split(" / ")[1]
        st.subheader(cat_title)

        for item in visible_items:
            en_name, ar_name = item["name"]
            base_price = item["price"]
            cal = item["cal"]
            variants = item["variants"]

            # Set Language Text
            main_txt = en_name if st.session_state.lang == "EN" else ar_name
            sub_txt = ar_name if st.session_state.lang == "EN" else en_name

            # Render Card
            if not variants:
                with st.container(border=True):
                    c_info, c_price = st.columns([3, 1])
                    with c_info:
                        st.markdown(f"**{main_txt}**")
                        st.markdown(f"<div class='caption-text'>{sub_txt} • 🔥 {cal}</div>", unsafe_allow_html=True)
                    with c_price:
                        st.markdown(f"<div class='base-price'>{base_price}</div>", unsafe_allow_html=True)
            else:
                with st.expander(f"{main_txt} ... {base_price} SAR"):
                    st.markdown(f"<div class='caption-text'>{sub_txt} • 🔥 {cal}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='variant-row'><span>Normal</span><span class='variant-price'>{base_price}</span></div>", unsafe_allow_html=True)
                    for v in variants:
                        v_en, v_ar, v_p = v
                        v_name = v_en if st.session_state.lang == "EN" else v_ar
                        st.markdown(f"<div class='variant-row'><span>{v_name}</span><span class='variant-price'>{v_p}</span></div>", unsafe_allow_html=True)

st.divider()
st.caption("Made for Shawarma & Burgerlak")
