import streamlit as st
from food_item import FoodItem
from manager import ExpiryManager
from storage import save_to_file, load_from_file

st.set_page_config(page_title="FreshGuard - Food Expiry Tracker", layout="wide")
st.title("🥫 FreshGuard - Food Expiry Tracker")

DATA_FILE = "data/food_data.json"
manager = ExpiryManager()

# Load previous data
manager.items = load_from_file(DATA_FILE)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["➕ Add Item", "📦 View All", "⏰ Expiry Alerts", "📊 Stats"])

with tab1:
    st.header("Add New Food Item")
    with st.form("add_form"):
        name = st.text_input("Food Name")
        quantity = st.number_input("Quantity", min_value=1)
        expiry_date = st.date_input("Expiry Date")
        category = st.selectbox("Category", ["Fruit", "Vegetable", "Dairy", "Meat", "Other"])
        submitted = st.form_submit_button("Add Item")

        if submitted:
            item = FoodItem(name, quantity, expiry_date.strftime("%Y-%m-%d"), category)
            manager.add_item(item)
            save_to_file(DATA_FILE, manager.items)
            st.success(f"Added {name} successfully!")

with tab2:
    st.header("All Food Items")
    all_items = manager.get_all_items()
    for item in all_items:
        st.write(f"{item.name} | Qty: {item.quantity} | Expires: {item.expiry_date.date()} | Category: {item.category}")

with tab3:
    st.header("Expiry Alerts")
    expired = manager.get_expired()
    soon = manager.get_soon_expiring()

    st.subheader("❌ Expired Items")
    for item in expired:
        st.error(f"{item.name} expired on {item.expiry_date.date()}")

    st.subheader("⚠️ Expiring Soon")
    for item in soon:
        st.warning(f"{item.name} will expire on {item.expiry_date.date()}")

with tab4:
    st.header("Food Stats")
    st.metric("Total Items", len(manager.items))
    st.metric("Expired", len(expired))
    st.metric("Expiring Soon", len(soon))