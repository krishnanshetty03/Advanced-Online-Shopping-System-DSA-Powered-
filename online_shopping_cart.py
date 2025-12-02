import streamlit as st

st.set_page_config(page_title="Online Shopping Cart", layout="centered")

# Products list
products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mouse", "price": 500},
    {"id": 3, "name": "Keyboard", "price": 1200},
    {"id": 4, "name": "Headphones", "price": 1500},
    {"id": 5, "name": "USB Cable", "price": 200},
]

# Initialize session state for cart
if "cart" not in st.session_state:
    st.session_state.cart = []


st.title("🛒 Online Shopping Cart (Using Lists)")
st.write("Select items and manage your cart easily!")


# ----------------- Show Products -----------------
st.subheader("📦 Available Products")

for item in products:
    col1, col2, col3 = st.columns([4, 2, 2])
    with col1:
        st.write(f"**{item['name']}**")
    with col2:
        st.write(f"₹{item['price']}")
    with col3:
        if st.button(f"Add to Cart", key=f"add_{item['id']}"):
            st.session_state.cart.append(item)
            st.success(f"{item['name']} added to cart!")


# ----------------- View Cart -----------------
st.subheader("🛍️ Your Cart")

if len(st.session_state.cart) == 0:
    st.info("Your cart is empty.")
else:
    total = 0
    for index, item in enumerate(st.session_state.cart):
        col1, col2, col3 = st.columns([4, 2, 2])
        with col1:
            st.write(f"{item['name']}")
        with col2:
            st.write(f"₹{item['price']}")
        with col3:
            if st.button("Remove", key=f"remove_{index}"):
                st.session_state.cart.pop(index)
                st.warning(f"{item['name']} removed from cart.")
                st.experimental_rerun()

    st.write("---")
    total = sum([item["price"] for item in st.session_state.cart])
    st.write(f"### 💰 Total: ₹{total}")


# ----------------- Checkout -----------------
if st.button("Checkout"):
    if len(st.session_state.cart) == 0:
        st.error("Cart is empty! Add items before checkout.")
    else:
        st.success("Checkout Successful! 🎉")
        st.write("### 🧾 Bill Summary")
        for item in st.session_state.cart:
            st.write(f"- {item['name']} — ₹{item['price']}")

        st.write(f"### **Total Amount: ₹{total}**")

        # Clear cart after checkout
        st.session_state.cart = []
