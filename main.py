import streamlit as st
import os

# ================= 1. CONFIG & DATA =================
st.set_page_config(page_title="Menu", layout="centered")

# Shop Data
SHOP_EN = "SHAWARMA & BURGERLAK"
SHOP_AR = "شاورما و برجرلك"
PHONE = "+966 50 518 9381"
LOGO_FILE = "logo.png"

MENU_DATA = {
    "🌯 Shawarma / شاورما": [
        {"name": ("Shawarma Small", "شاورما صغير"), "price": 7.00, "cal": 430, "variants": [("With Cheese", "مع جبنة", 8.00)]},
        {"name": ("Shawarma Sarukh", "شاورما صاروخ"), "price": 8.00, "cal": 550, "variants": [("With Cheese", "مع جبنة", 9.00)]},
        {"name": ("Shawarma Arabi Small", "صحن شاورما عربي صغير"), "price": 11.00, "cal": 550, "variants": [("With Cheese", "مع جبنة", 12.00)]},
        {"name": ("Shawarma Arabi Big", "صحن شاورما عربي كبير"), "price": 16.00, "cal": 750, "variants": [("With Cheese", "مع جبنة", 18.00)]},
        {"name": ("Shawarma Boshka", "شاورما بوشكا"), "price": 19.00, "cal": 880, "variants": [("With Cheese", "مع جبنة", 21.00)]},
    ],
    "🍔 Burgers / برجر": [
        {"name": ("Chicken Burger", "برجر دجاج"), "price": 8.00, "cal": 420, "variants": [("Spicy", "حراق", 8.00), ("With Cheese", "جبنة", 9.00), ("With Cheese Spicy", "جبنة حراق", 9.00), ("Double", "دبل", 13.00), ("Double Cheese", "دبل جبنة", 14.00)]},
        {"name": ("Beef Burger", "برجر لحم"), "price": 8.00, "cal": 450, "variants": [("Spicy", "حراق", 9.00), ("With Cheese", "جبنة", 9.00), ("With Cheese Spicy", "جبنة حراق", 9.00), ("Double", "دبل", 13.00), ("Double Cheese", "دبل جبنة", 14.00)]},
        {"name": ("Fish Burger", "برجر سمك"), "price": 9.00, "cal": 400, "variants": [("With Cheese", "جبنة", 10.00), ("Double", "دبل", 15.00), ("Double Cheese", "دبل جبنة", 17.00)]},
        {"name": ("Zinger Burger", "برجر زنجر"), "price": 11.50, "cal": 480, "variants": [("With Cheese", "جبنة", 12.50), ("Double", "دبل", 19.50), ("Double Cheese", "دبل جبنة", 20.50)]},
    ],
    "🥪 Sandwiches / ساندوتشات": [
        {"name": ("Nuggets Sandwich", "ساندوتش دجاج مسحب"), "price": 9.00, "cal": 380, "variants": [("With Cheese", "جبنة", 10.00)]},
        {"name": ("Shrimps Sandwich", "ساندوتش جمبري"), "price": 9.00, "cal": 400, "variants": [("With Cheese", "جبنة", 10.00)]},
        {"name": ("Chicken Fillets Sandwich", "ساندوتش دجاج فيلية"), "price": 9.00, "cal": 400, "variants": [("With Cheese", "جبنة", 10.00)]},
        {"name": ("Tortilla Sandwich", "ساندوتش تورتيلا"), "price": 10.00, "cal": 430, "variants": [("With Cheese", "جبنة", 11.00)]},
        {"name": ("Sandwich Zinger", "ساندوتش زنجر"), "price": 11.50, "cal": 480, "variants": [("With Cheese", "جبنة", 12.50)]},
        {"name": ("Shrimps Tandoori Sandwich", "ساندوتش جمبري تندوري"), "price": 9.00, "cal": 400, "variants": [("With Cheese", "جبنة", 10.00)]},
        {"name": ("Fish Sandwich", "ساندوتش سمك"), "price": 9.00, "cal": 400, "variants": [("With Cheese", "جبنة", 10.00)]},
    ],
    "🍽️ Meals & Plates / وجبات وصحون": [
        {"name": ("Chicken Nuggets Plate", "دجاج مسحب صحن"), "price": 20.00, "cal": 850, "variants": []},
        {"name": ("Chicken Fillets Plate", "دجاج فيلية صحن"), "price": 20.00, "cal": 850, "variants": []},
        {"name": ("Shrimps Plate", "جمبري صحن"), "price": 20.00, "cal": 900, "variants": []},
        {"name": ("Fish Broast", "بروست سمك"), "price": 19.00, "cal": 880, "variants": []},
        {"name": ("Chicken Burger Meal", "برجر دجاج وجبة"), "price": 14.50, "cal": 900, "variants": [("With Cheese", "جبنة", 15.50), ("Double", "دبل", 19.50), ("Double Cheese", "دبل جبنة", 20.50)]},
        {"name": ("Beef Burger Meal", "برجر لحم وجبة"), "price": 14.50, "cal": 900, "variants": [("With Cheese", "جبنة", 15.50), ("Double", "دبل", 19.50), ("Double Cheese", "دبل جبنة", 20.50)]},
        {"name": ("Zinger Burger Meal", "برجر زنجر وجبة"), "price": 18.00, "cal": 980, "variants": [("With Cheese", "جبنة", 19.00), ("Double", "دبل", 26.00), ("Double Cheese", "دبل جبنة", 27.00)]},
        {"name": ("Fish Burger Meal", "برجر سمك وجبة"), "price": 15.50, "cal": 950, "variants": [("With Cheese", "جبنة", 16.50)]},
        {"name": ("Tortilla Meal", "تورتيلا وجبة"), "price": 16.50, "cal": 1020, "variants": [("With Cheese", "جبنة", 17.50)]},
    ],
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
st.caption("Made for Shawarma & Burgerluk")
