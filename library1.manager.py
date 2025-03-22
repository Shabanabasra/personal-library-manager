import streamlit as st
import pandas as pd
import json
import streamlit as st
import pandas as pd
import json
import os
import time
import datetime
import plotly.express as px
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import requests

# Set page configuration
st.set_page_config(
    page_title="Personal Library Management System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem !important;
        color: #1E3A8A;
        font-weight: 700;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub_header {
        font-size: 1.8rem !important;
        color: #3882F6;
        font-weight: 600;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    .success-message {
        padding: 1rem;
        background-color: #ECFDF5;
        border-left: 5px solid #10B981;
        border-radius: 0.375rem;
    }
    .warning-message {
        padding: 1rem;
        background-color: #FEF3C7;
        border-left: 5px solid #F59E0B;
        border-radius: 0.375rem;
    }
</style>
""", unsafe_allow_html=True)

# Load Lottie animation
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Session state initialization
if "library" not in st.session_state:
    st.session_state.library = []
if "search_results" not in st.session_state:
    st.session_state.search_results = []
if "book_added" not in st.session_state:
    st.session_state.book_added = False
if "book_removed" not in st.session_state:
    st.session_state.book_removed = False
if "current_view" not in st.session_state:
    st.session_state.current_view = "library"

# Load library data
def load_library():
    try:
        if os.path.exists("library.json"):
            with open("library.json", "r") as file:
                st.session_state.library = json.load(file)
    except Exception as e:
        st.error(f"Error loading library: {e}")

# Save library data
def save_library():
    try:
        with open("library.json", "w") as file:
            json.dump(st.session_state.library, file)
    except Exception as e:
        st.error(f"Error saving library: {e}")

# Add a book to library
def add_book(title, author, publication_year, genre, read_status):
    book = {
        "title": title,
        "author": author,
        "publication_year": publication_year,
        "genre": genre,
        "read_status": read_status,
        "added_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    st.session_state.library.append(book)
    save_library()
    st.session_state.book_added = True
    time.sleep(0.5)

# Remove a book
def remove_book(index):
    if 0 <= index < len(st.session_state.library):
        del st.session_state.library[index]
        save_library()
        st.session_state.book_removed = True

# Load library data on start
load_library()

# Sidebar Navigation
st.sidebar.markdown("<h1 style='text-align: center;'>Navigation</h1>", unsafe_allow_html=True)
lottie_book = load_lottieurl("https://assets9.lottiefiles.com/temp/1f20_akAfIn.json")
if lottie_book:
    with st.sidebar:
        st_lottie(lottie_book, height=200, key="book_animation")

nav_options = st.sidebar.radio(
    "Choose an option",
    ["View Library", "Add Book", "Search Books", "Library Statistics"]
)

if nav_options == "View Library":
    st.session_state.current_view = "library"
elif nav_options == "Add Book":
    st.session_state.current_view = "add"
elif nav_options == "Search Books":
    st.session_state.current_view = "search"
elif nav_options == "Library Statistics":
    st.session_state.current_view = "stats"

st.markdown("<h1 class='main-header'>Personal Library Manager</h1>", unsafe_allow_html=True)

# Add Book View
if st.session_state.current_view == "add":
    st.markdown("<h2 class='sub_header'>Add a New Book 📚</h2>", unsafe_allow_html=True)
    with st.form(key="add_book_form"):
        title = st.text_input("Book Title", max_chars=100)
        author = st.text_input("Author", max_chars=100)
        publication_year = st.number_input("Publication Year", min_value=1000, max_value=datetime.datetime.now().year, step=1, value=2023)
        genre = st.selectbox("Genre", ["Fiction", "Non-Fiction", "Science", "Technology", "Fantasy", "Romance", "Poetry", "Self-Help", "Art", "Religion", "History", "Other"])
        read_status = st.radio("Read Status", ["Read", "Unread"], horizontal=True)
        submit_button = st.form_submit_button(label="Add Book")
        if submit_button and title and author:
            add_book(title, author, publication_year, genre, read_status == "Read")
            st.success("Book added successfully! 🎉")

# View Library
elif st.session_state.current_view == "library":
    st.markdown("<h2 class='sub_header'>Your Library</h2>", unsafe_allow_html=True)
    if not st.session_state.library:
        st.markdown("<div class='warning-message'>Your library is empty. Add some books to get started!</div>", unsafe_allow_html=True)
    else:
        for i, book in enumerate(st.session_state.library):
            st.markdown(f"""
                <div class="book-card">
                    <h3>{book["title"]}</h3>
                    <p><strong>Author:</strong> {book["author"]}</p>
                    <p><strong>Publication Year:</strong> {book["publication_year"]}</p>
                    <p><strong>Genre:</strong> {book["genre"]}</p>
                    <p><span class="{'read-badge' if book['read_status'] else 'unread-badge'}">{
                        "Read" if book["read_status"] else "Unread"
                    }</span></p>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"Remove {book['title']}", key=f"remove_{i}"):
                remove_book(i)
                st.rerun()

# Footer
st.markdown("<br><br><center>© 2025 Personal Library Manager</center>", unsafe_allow_html=True)
