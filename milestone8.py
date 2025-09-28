from collections import defaultdict
from typing import List, Dict
import random

class Book:
    def __init__(self, title: str, author: str, category: str, isbn: str = None):
        self.title = title
        self.author = author
        self.category = category
        self.isbn = isbn
    
    def get_title(self) -> str:
        return self.title
    
    def get_author(self) -> str:
        return self.author
    
    def get_category(self) -> str:
        return self.category
    
    def get_isbn(self) -> str:
        return self.isbn
    
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.category})"
    
    def __repr__(self):
        return self.__str__()

class Shelf:
    def __init__(self, category: str = None):
        self.books = []
        self.category = category
    
    def add_book(self, book: Book):
        """Add a book to the shelf"""
        if self.category is None:
            self.category = book.get_category()
        elif self.category != book.get_category():
            raise ValueError(f"Cannot add book from category '{book.get_category()}' to shelf of category '{self.category}'")
        self.books.append(book)
    
    def get_books(self) -> List[Book]:
        return self.books
    
    def get_category(self) -> str:
        return self.category
    
    def sort_books(self):
        """Sort books by title in ascending order"""
        self.books.sort(key=lambda book: book.get_title().lower())
    
    def __str__(self):
        return f"Shelf - Category: {self.category}, Books: {len(self.books)}"

class BookCatalog:
    def __init__(self):
        self.shelves = []
    
    def add_book(self, book: Book):
        """Add a book to the catalog"""
        # Find existing shelf for this category or create new one
        existing_shelf = None
        for shelf in self.shelves:
            if shelf.get_category() == book.get_category():
                existing_shelf = shelf
                break
        
        if existing_shelf is None:
            existing_shelf = Shelf(book.get_category())
            self.shelves.append(existing_shelf)
        
        existing_shelf.add_book(book)
    
    def organize_by_category(self):
        """Organize books into shelves by category"""
        # This method is already handled in add_book, but we can ensure all books are properly categorized
        pass
    
    def sort_all_shelves(self):
        """Sort books on each shelf by title"""
        for shelf in self.shelves:
            shelf.sort_books()
    
    def display_catalog(self):
        """Display the entire catalog"""
        print("=== BOOK CATALOG ===")
        if not self.shelves:
            print("No books in catalog")
            return
        
        for i, shelf in enumerate(self.shelves, 1):
            print(f"\nShelf {i}: {shelf}")
            for book in shelf.get_books():
                print(f"  - {book}")

# Create sample books (using manual creation instead of Faker)
def create_sample_books():
    books = [
        Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"),
        Book("To Kill a Mockingbird", "Harper Lee", "Fiction"),
        Book("1984", "George Orwell", "Fiction"),
        Book("Pride and Prejudice", "Jane Austen", "Fiction"),
        Book("The Catcher in the Rye", "J.D. Salinger", "Fiction"),
        Book("The Hobbit", "J.R.R. Tolkien", "Fantasy"),
        Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy"),
        Book("The Lord of the Rings", "J.R.R. Tolkien", "Fantasy"),
        Book("Dune", "Frank Herbert", "Science Fiction"),
        Book("Neuromancer", "William Gibson", "Science Fiction"),
        Book("The Da Vinci Code", "Dan Brown", "Mystery"),
        Book("The Girl with the Dragon Tattoo", "Stieg Larsson", "Mystery"),
        Book("A Brief History of Time", "Stephen Hawking", "Science"),
        Book("The Selfish Gene", "Richard Dawkins", "Science"),
        Book("Sapiens", "Yuval Noah Harari", "History")
    ]
    return books

# Main function to demonstrate the organization
def main():
    # Create book catalog
    catalog = BookCatalog()
    
    # Create sample books
    books = create_sample_books()
    
    print("=== BEFORE ORGANIZATION ===")
    print("All books in pile:")
    for book in books:
        print(f"  - {book}")
    
    # Step 1: Organize books into shelves by category
    print("\n=== STEP 1: Organizing books by category ===")
    for book in books:
        catalog.add_book(book)
    
    print("Books organized into shelves:")
    for i, shelf in enumerate(catalog.shelves, 1):
        print(f"  Shelf {i}: {shelf}")
    
    # Step 2: Sort books on each shelf by title
    print("\n=== STEP 2: Sorting books by title ===")
    catalog.sort_all_shelves()
    
    # Display final organized catalog
    print("\n=== FINAL ORGANIZED CATALOG ===")
    catalog.display_catalog()

# Alternative implementation with more realistic scenario using Faker
def demo_with_faker():
    try:
        from faker import Faker
        fake = Faker()
        
        print("\n" + "="*50)
        print("DEMO WITH FAKE DATA")
        print("="*50)
        
        catalog = BookCatalog()
        
        # Generate more books using Faker
        categories = ["Fiction", "Fantasy", "Science Fiction", "Mystery", "Science", "History", "Biography"]
        books = []
        
        for i in range(20):
            title = fake.sentence(nb_words=4)[:-1]  # Remove the period
            author = fake.name()
            category = random.choice(categories)
            isbn = fake.isbn13()
            
            book = Book(title, author, category, isbn)
            books.append(book)
        
        print("Generated books:")
        for book in books[:5]:  # Show first 5
            print(f"  - {book}")
        
        print("... and more")
        
        # Add to catalog
        for book in books:
            catalog.add_book(book)
        
        # Sort and display
        catalog.sort_all_shelves()
        catalog.display_catalog()
        
    except ImportError:
        print("Faker library not installed. Skipping demo with Faker.")

if __name__ == "__main__":
    main()
    
    # Uncomment the line below if you have faker installed
    # demo_with_faker()