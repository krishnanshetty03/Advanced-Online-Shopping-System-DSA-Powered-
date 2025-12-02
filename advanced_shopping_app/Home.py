import streamlit as st
from product_data import products, product_hash, build_hash_table
from cart_linked_list import LinkedListCart
from stack_undo import UndoStack
from queue_orders import OrderQueue
from tree_categories import build_category_tree
from graph_delivery import bfs_shortest_path

# -------------------------------------------
# INITIALIZATION (PERSISTS ACROSS PAGES)
# -------------------------------------------

# Build hash table (runs once)
build_hash_table()

# Initialize cart (Linked List)
if "cart" not in st.session_state:
    st.session_state.cart = LinkedListCart()

# Initialize undo stack
if "undo_stack" not in st.session_state:
    st.session_state.undo_stack = UndoStack()

# Initialize order queue
if "order_queue" not in st.session_state:
    st.session_state.order_queue = OrderQueue()

# Initialize category tree
if "category_tree" not in st.session_state:
    st.session_state.category_tree = build_category_tree()


# -------------------------------------------
# STREAMLIT PAGE SETTINGS
# -------------------------------------------

st.set_page_config(page_title="Advanced Shopping System (DSA)", layout="wide")
st.title("🛒 Advanced Online Shopping System (DSA Powered)")


# -------------------------------------------
# SIDE NAVIGATION MENU
# -------------------------------------------

st.sidebar.header("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Products", "Cart", "Categories", "Delivery Routes", "Orders"]
)


# -------------------------------------------
# PRODUCT PAGE (ARRAY + HASH TABLE)
# -------------------------------------------

if page == "Products":
    st.header("📦 Product List (Array + Hash Table Search)")

    search = st.text_input("🔍 Search Product by Name")

    if search:
        item = product_hash.get(search.lower())
        if item:
            st.success(f"✨ Found: {item['name']} — ₹{item['price']}")
        else:
            st.error("❌ Product Not Found")

    st.subheader("Available Products:")
    st.write("---")

    for p in products:
        col1, col2, col3, col4 = st.columns([3, 3, 2, 2])

        col1.write(f"**{p['name']}**")
        col2.write(f"Category: {p['category']}")
        col3.write(f"₹{p['price']}")

        if col4.button("Add to Cart", key=f"add_{p['id']}"):
            st.session_state.cart.add(p)
            st.success(f"Added {p['name']} to cart!")


# -------------------------------------------
# CART PAGE (LINKED LIST + STACK)
# -------------------------------------------

elif page == "Cart":
    st.header("🛍️ Your Cart (Linked List + Undo Stack)")

    items = st.session_state.cart.get_all()

    if not items:
        st.info("Your cart is empty.")
    else:
        total = 0

        for item in items:
            col1, col2, col3 = st.columns([4, 3, 2])
            col1.write(f"{item['name']}")
            col2.write(f"₹{item['price']}")
            total += item["price"]

            if col3.button("Remove", key=f"remove_{item['id']}"):
                removed = st.session_state.cart.remove(item["id"])
                if removed:
                    st.session_state.undo_stack.push(removed)
                    st.warning(f"Removed {removed['name']}")

        st.write("---")
        st.write(f"### 💰 Total: ₹{total}")

        if st.button("Undo Last Remove"):
            item = st.session_state.undo_stack.pop()
            if item:
                st.session_state.cart.add(item)
                st.success(f"Restored: {item['name']}")
            else:
                st.error("Nothing to undo.")


# -------------------------------------------
# CATEGORY TREE PAGE
# -------------------------------------------

elif page == "Categories":
    st.header("🌳 Store Category Browser (Tree Structure)")
    
    def render_tree(node, indent=0):
        st.write(" " * indent + "📂 " + node.name)
        for child in node.children:
            render_tree(child, indent + 4)

    render_tree(st.session_state.category_tree)


# -------------------------------------------
# DELIVERY ROUTE PAGE (GRAPH + BFS)
# -------------------------------------------

elif page == "Delivery Routes":
    st.header("🚚 Delivery Route Finder (Graph + BFS Shortest Path)")

    path = bfs_shortest_path("Warehouse", "Destination")

    if path:
        st.success("Shortest Path:")
        st.write(" → ".join(path))
    else:
        st.error("No available route.")


# -------------------------------------------
# ORDER QUEUE PAGE
# -------------------------------------------

elif page == "Orders":
    st.header("📦 Order Queue (FIFO)")

    if st.button("Place Order"):
        items = st.session_state.cart.get_all()
        if items:
            st.session_state.order_queue.add_order(items.copy())
            st.success("Order added to queue!")
            st.session_state.cart = LinkedListCart()  # empty cart
        else:
            st.error("Cannot place empty order.")

    st.subheader("Pending Orders:")
    orders = st.session_state.order_queue.get_orders()

    if not orders:
        st.info("No pending orders.")
    else:
        for i, order in enumerate(orders):
            st.write(f"### Order {i+1}")
            for item in order:
                st.write(f"- {item['name']} (₹{item['price']})")
            st.write("---")

    if st.button("Process Order"):
        processed = st.session_state.order_queue.process_order()
        if processed:
            st.success(f"Processed Order containing {len(processed)} items.")
        else:
            st.error("No orders to process.")
