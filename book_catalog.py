import random
from faker import Faker

class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.category}')"

class Shelf:
    def __init__(self, shelf_id):
        self.shelf_id = shelf_id
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def sort_books_by_title(self):
        self.books.sort(key=lambda book: book.title.lower())
    
    def __str__(self):
        return f"Shelf {self.shelf_id} with {len(self.books)} books"

class BookCatalog:
    def __init__(self):
        self.shelves = []
        self.book_count = 0
    
    def add_book_to_shelf(self, book, shelf_id=None):
        if shelf_id is None:
            shelf_id = len(self.shelves) + 1
        
        shelf = None
        for s in self.shelves:
            if s.shelf_id == shelf_id:
                shelf = s
                break
        
        if shelf is None:
            shelf = Shelf(shelf_id)
            self.shelves.append(shelf)
        
        shelf.add_book(book)
        self.book_count += 1
    
    def organize_books_by_category(self, books):
        category_to_shelves = {}
        for book in books:
            if book.category not in category_to_shelves:
                shelf_id = len(self.shelves) + 1
                category_to_shelves[book.category] = shelf_id
                shelf = Shelf(shelf_id)
                self.shelves.append(shelf)
            
            shelf_id = category_to_shelves[book.category]
            for shelf in self.shelves:
                if shelf.shelf_id == shelf_id:
                    shelf.add_book(book)
                    break
    
    def sort_all_shelves(self):
        for shelf in self.shelves:
            shelf.sort_books_by_title()
    
    def display_catalog(self):
        print("=== BOOK CATALOG ===")
        for shelf in self.shelves:
            print(f"\n{shelf}")
            for book in shelf.books:
                print(f"  - {book}")
        print("\n" + "="*50)

def generate_sample_books(count=20):
    fake = Faker()
    
    categories = ["Fiction", "Science Fiction", "Mystery", "Romance", 
                   "Biography", "History", "Science", "Fantasy", "Thriller"]
    
    books = []
    for i in range(count):
        title = fake.sentence(nb_words=4).rstrip('.')
        author = f"{fake.first_name()} {fake.last_name()}"
        category = random.choice(categories)
        books.append(Book(title, author, category))
    
    return books

def main():
    print("=== BOOK CATALOG SYSTEM DEMONSTRATION ===\n")
    
    print("Generating sample books...")
    books = generate_sample_books(20)
    print(f"Created {len(books)} sample books\n")
    
    print("Sample books:")
    for book in books[:5]:  
        print(f"  - {book} (Category: {book.category})")
    print("  ... and more\n")
    
    catalog = BookCatalog()
    
    print("Step 1: Organizing books by category...")
    catalog.organize_books_by_category(books)
    print("Books organized by categories!\n")
    
    print("Step 2: Sorting books by title on all shelves...")
    catalog.sort_all_shelves()
    print("Books sorted by title!\n")
    
    catalog.display_catalog()
    
    try:
        with open('book_catalog.txt', 'w', encoding='utf-8') as f:
            f.write("=== BOOK CATALOG ===\n")
            for shelf in catalog.shelves:
                f.write(f"\n{shelf}\n")
                for book in shelf.books:
                    f.write(f"  - {book}\n")
            f.write("\n" + "="*50 + "\n")
        print("Successfully created 'book_catalog.txt' file!")
    except Exception as e:
        print(f"Error creating file: {e}")
    
    print("\n=== DEMONSTRATION COMPLETE ===")

if __name__ == "__main__":
    main()