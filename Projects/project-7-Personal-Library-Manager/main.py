import json
import streamlit as st

class BookCollection:
    def __init__(self):
        self.storage_file = "books_data.json"
        self.book_list = []
        self.read_from_file()

    def read_from_file(self):
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def add_book(self, title, author, year, genre, read):
        new_book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read,
        }
        self.book_list.append(new_book)
        self.save_to_file()

    def delete_book(self, title):
        self.book_list = [book for book in self.book_list if book["title"].lower() != title.lower()]
        self.save_to_file()

    def find_books(self, search_text):
        return [
            book for book in self.book_list 
            if search_text.lower() in book["title"].lower() or search_text.lower() in book["author"].lower()
        ]

    def update_book(self, old_title, new_title, new_author, new_year, new_genre, new_read):
        for book in self.book_list:
            if book["title"].lower() == old_title.lower():
                book["title"] = new_title or book["title"]
                book["author"] = new_author or book["author"]
                book["year"] = new_year or book["year"]
                book["genre"] = new_genre or book["genre"]
                book["read"] = new_read
                self.save_to_file()
                return True
        return False

    def get_reading_progress(self):
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        return (completed_books / total_books) if total_books > 0 else 0


# Streamlit UI
st.title("📚 Book Collection Manager")

book_manager = BookCollection()

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📖 Add Book", "🔍 Search Book", "📋 View All Books", "✏️ Update Book", "📊 Progress"])

# Add Book
with tab1:
    st.header("➕ Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.text_input("Publication Year")
    genre = st.text_input("Genre")
    new_read = st.checkbox("Have you read this book?", key="unique_read_checkbox")
 
    
    if st.button("Add Book"):
        if title and author and year and genre:
            book_manager.add_book(title, author, year, genre, new_read)
            st.success(f"✅ '{title}' added successfully!")
        else:
            st.warning("⚠️ Please fill all fields!")

# Search Book
with tab2:
    st.header("🔎 Search Book")
    search_query = st.text_input("Enter title or author")
    if st.button("Search"):
        results = book_manager.find_books(search_query)
        if results:
            for book in results:
                st.write(f"📖 **{book['title']}** by *{book['author']}* ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Not Read'}")
        else:
            st.warning("⚠️ No matching books found.")

# View All Books
with tab3:
    st.header("📚 Your Book Collection")
    if book_manager.book_list:
        for book in book_manager.book_list:
            st.write(f"📖 **{book['title']}** by *{book['author']}* ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Not Read'}")
        
        # Delete book
        book_to_delete = st.text_input("Enter title to delete")
        if st.button("Delete Book"):
            book_manager.delete_book(book_to_delete)
            st.success(f"🗑️ '{book_to_delete}' deleted!")
    else:
        st.info("ℹ️ Your book collection is empty!")

# Update Book
with tab4:
    st.header("✏️ Update a Book")
    old_title = st.text_input("Enter book title to update")
    new_title = st.text_input("New Title (leave blank to keep same)")
    new_author = st.text_input("New Author (leave blank to keep same)")
    new_year = st.text_input("New Year (leave blank to keep same)")
    new_genre = st.text_input("New Genre (leave blank to keep same)")
    new_read = st.checkbox("Have you read this book?")

    if st.button("Update Book"):
        if book_manager.update_book(old_title, new_title, new_author, new_year, new_genre, new_read):
            st.success(f"✅ '{old_title}' updated successfully!")
        else:
            st.warning("⚠️ Book not found!")

# Progress
with tab5:
    st.header("📊 Reading Progress")
    progress = book_manager.get_reading_progress()
    st.progress(progress)
    st.write(f"📚 **{progress * 100:.2f}%** of your books are read.")
