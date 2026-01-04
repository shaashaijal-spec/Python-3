import streamlit as st
import os

# ================= 0. AUTO-FIX COLORS (Create Config) =================
# This section creates a settings file to FORCE Dark Mode
if not os.path.exists(".streamlit"):
    os.makedirs(".streamlit")

config_content = """
[theme]
base="dark"
primaryColor="#4CAF50"
backgroundColor="#000000"
secondaryBackgroundColor="#1A1A1A"
textColor="#FFFFFF"
font="sans serif"
"""

# Write the file if it doesn't exist or is different
try:
    with open(".streamlit/config.toml", "w") as f:
        f.write(config_content)
except:
    pass

# ================= 1. SHOP CONFIGURATION =================
SHOP_EN = "SHAWARMA & BURGERLAK"
SHOP_AR = "شاورما و برجرلك"
PHONE = "+966 50 518 9381"
LOGO_FILE = "logo.png"

# Location
LOC_TEXT_EN = "Jeddah, Burayman Dist (JFBA3706)"
LOC_TEXT_AR = "جدة - حي بريمان (JFBA3706)"

# Greeting
GREETING_EN = "Thank you for choosing us! Enjoy your meal."
GREETING_AR = "شكراً لاختياركم لنا! نتمنى لكم وجبة شهية."

# ================= 2. MENU DATA =================
MENU_DATA = {
    "🌯 Shawarma / شاورما": [
        {"name": ("Shawarma Small", "شاورما صغير"), "price": 7.0, "cal": 380, "variants": [("With Cheese", "مع جبنة", 8.0)]},
        {"name": ("Shawarma Sarukh", "شاورما صاروخ"), "price": 8.0, "cal": 750, "variants": [("With Cheese", "مع جبنة", 9.0)]},
        {"name": ("Shawarma Arabi Small", "صحن عربي صغير"), "price": 11.0, "cal": 850, "variants": [("With Cheese", "مع جبنة", 12.0)]},
        {"name": ("Shawarma Arabi Big", "صحن عربي كبير"), "price": 16.0, "cal": 1300, "variants": [("With Cheese", "مع جبنة", 18.0)]},
        {"name": ("Shawarma Boshka", "شاورما بوشكا"), "price": 19.0, "cal": 950, "variants": [("With Cheese", "مع جبنة", 21.0)]},
    ],
    "🍔 Burgers / برجر": [
        {"name": ("Chicken Burger", "برجر دجاج"), "price": 8.0, "cal": 550, "variants": [("With Cheese", "مع جبنة", 9.0), ("Double", "دبل", 13.0), ("Double Cheese", "دبل جبنة", 14.0)]},
        {"name": ("Beef Burger", "برجر لحم"), "price": 8.0, "cal": 600, "variants": [("With Cheese", "مع جبنة", 9.0), ("Double", "دبل", 13.0), ("Double Cheese", "دبل جبنة", 14.0)]},
        {"name": ("Zinger Burger", "برجر زنجر"), "price": 11.5, "cal": 700, "variants": [("With Cheese", "مع جبنة", 12.5), ("Double", "دبل", 19.5), ("Double Cheese", "دبل جبنة", 20.5)]},
        {"name": ("Fish Burger", "برجر سمك"), "price": 9.0, "cal": 500, "variants": [("With Cheese", "مع جبنة", 10.0), ("Double", "دبل", 15.0), ("Double Cheese", "دبل جبنة", 17.0)]}
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
        {"name": ("Fish Nuggets Plate", "سمك مسحب صحن"), "price": 20.0, "cal": 1050, "variants": []},
        {"name": ("Chicken Fillet Plate", "دجاج فيلية صحن"), "price": 20.0, "cal": 1000, "variants": []},
        {"name": ("Shrimps Plate", "جمبري صحن"), "price": 20.0, "cal": 950, "variants": []},
        {"name": ("Fish Broast", "بروست سمك"), "price": 19.0, "cal": 1200, "variants": []},
        {"name": ("Chicken Burger Meal", "وجبة برجر دجاج"), "price": 14.5, "cal": 950, "variants": [("With Cheese", "مع جبنة", 15.5)]},
        {"name": ("Beef Burger Meal", "وجبة برجر لحم"), "price": 14.5, "cal": 1000, "variants": [("With Cheese", "مع جبنة", 15.5)]},
        {"name": ("Zinger Meal", "وجبة زنجر"), "price": 18.0, "cal": 1100, "variants": [("With Cheese", "مع جبنة", 19.0), ("Double", "دبل", 26.0), ("Double Cheese", "دبل جبنة", 27.0)]},
        {"name": ("Fish Burger Meal", "وجبة برجر سمك"), "price": 15.5, "cal": 900, "variants": [("With Cheese", "مع جبنة", 16.5)]},
        {"name": ("Tortilla Meal", "وجبة تورتيلا"), "price": 16.5, "cal": 1050, "variants": [("With Cheese", "مع جبنة", 17.5)]}
    ],
    "🥤 Juices / عصائر": [
        {"name": ("Orange Juice", "عصير برتقال"), "price": 6.0, "cal": 120, "variants": [("Small", "صغير", 6.0), ("Big", "كبير", 8.0), ("Gallon", "جالون", 23.0)]},
        {"name": ("Melon Juice", "عصير شمام"), "price": 7.0, "cal": 150, "variants": []},
        {"name": ("Mixed Juice", "عصير مشكل"), "price": 4.5, "cal": 160, "variants": [("Small", "صغير", 4.5), ("Big", "كبير", 7.0)]},
        {"name": ("Guava Juice", "عصير جوافة"), "price": 4.5, "cal": 140, "variants": [("Small", "صغير", 4.5), ("Big", "كبير", 7.0)]},
        {"name": ("Mango Juice", "عصير مانجو"), "price": 4.5, "cal": 170, "variants": [("Small", "صغير", 4.5), ("Big", "كبير", 7.0)]},
        {"name": ("Fruit Gallon", "جالون فواكه"), "price": 17.5, "cal": 950, "variants": [("Mango", "مانجو", 17.5), ("Guava", "جوافة", 17.5), ("Mixed", "مشكل", 17.5)]},
    ]
}

# ================= 3. PAGE SETUP & CSS =================
st.set_page_config(page_title="Menu", layout="centered")

st.markdown("""
    <style>
    /* CSS FALLBACKS */
    .variant-row {
        display: flex;
        justify-content: space-between;
        padding: 8px 0;
        border-bottom: 1px solid #333;
    }
    .base-price { color: #4CAF50; font-weight: bold; font-size: 1.1em; }
    .variant-price { color: #81C784; font-weight: bold; }
    .caption-text { color: #AAA; font-size: 0.9em; }

    /* Hide Header/Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stElementToolbar"] {display: none;}
    </style>
""", unsafe_allow_html=True)

if 'lang' not in st.session_state:
    st.session_state.lang = "EN"

# ================= 4. HEADER =================
try:
    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        st.image(LOGO_FILE, use_container_width=True)
except:
    pass

st.markdown(f"<h2 style='text-align: center; margin-bottom:0;'>{SHOP_EN}</h2>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center; color: #BBB; margin-top:0;'>{SHOP_AR}</h3>", unsafe_allow_html=True)

loc = LOC_TEXT_EN if st.session_state.lang == "EN" else LOC_TEXT_AR
st.markdown(f"<div style='text-align: center; color: #999; font-size:0.9em;'>📍 {loc}<br>📞 {PHONE}</div>", unsafe_allow_html=True)
st.divider()

# Language Toggle
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    btn_text = "🔄 العربية" if st.session_state.lang == "EN" else "🔄 English"
    if st.button(btn_text, use_container_width=True):
        st.session_state.lang = "AR" if st.session_state.lang == "EN" else "EN"
        st.rerun()

# ================= 5. MENU DISPLAY =================
search_query = st.text_input("🔍 Search / بحث", "")

for category, items_list in MENU_DATA.items():
    visible_items = []
    if search_query == "":
        visible_items = items_list
    else:
        for item in items_list:
            en_n, ar_n = item["name"]
            found = False
            if search_query.lower() in en_n.lower() or search_query in ar_n: found = True
            for v in item["variants"]:
                if search_query.lower() in v[0].lower() or search_query in v[1]: found = True
            if found: visible_items.append(item)

    if visible_items:
        cat_title = category.split(" / ")[0] if st.session_state.lang == "EN" else category.split(" / ")[1]
        st.subheader(cat_title)

        for item in visible_items:
            en_name, ar_name = item["name"]
            base_price = item["price"]
            cal = item["cal"]
            variants = item["variants"]

            # Text Selection
            main_txt = en_name if st.session_state.lang == "EN" else ar_name
            sub_txt = ar_name if st.session_state.lang == "EN" else en_name

            # --- CARD LOGIC ---
            if not variants:
                with st.container(border=True):
                    c_info, c_price = st.columns([3, 1])
                    with c_info:
                        st.markdown(f"**{main_txt}**")
                        st.markdown(f"<div class='caption-text'>{sub_txt} • 🔥 {cal}</div>", unsafe_allow_html=True)
                    with c_price:
                        st.markdown(f"<div class='base-price'>{base_price}</div>", unsafe_allow_html=True)
                        st.markdown("<div style='font-size:0.7em; color:#BBB;'>SAR</div>", unsafe_allow_html=True)
            else:
                label_text = f"{main_txt} .................... {base_price} SAR"
                with st.expander(label_text):
                    st.markdown(f"<div class='caption-text' style='margin-bottom:10px;'>{sub_txt} • 🔥 {cal} kcal</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='variant-row'><span>Normal / عادي</span><span class='variant-price'>{base_price} SAR</span></div>", unsafe_allow_html=True)
                    for v in variants:
                        v_en, v_ar, v_price = v
                        v_name = v_en if st.session_state.lang == "EN" else v_ar
                        st.markdown(f"<div class='variant-row'><span>{v_name}</span><span class='variant-price'>{v_price} SAR</span></div>", unsafe_allow_html=True)

# Footer
st.divider()
final_greeting = GREETING_EN if st.session_state.lang == "EN" else GREETING_AR
st.markdown(f"<h4 style='text-align: center; color: #4CAF50; margin-top: 20px;'>{final_greeting}</h4>", unsafe_allow_html=True)
st.markdown("<div style='margin-bottom: 50px;'></div>", unsafe_allow_html=True)
