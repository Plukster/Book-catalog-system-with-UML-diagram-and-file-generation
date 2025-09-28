# Book Catalog System

## How to Use

This program helps organize books into a digital catalog system. Here's how to use it:

### Prerequisites
- Python 3.x installed
- Faker library (install with: `pip install faker`)

### Running the Program
1. Save the code as `book_catalog.py`
2. Run the program: `python book_catalog.py`

### What the Program Does

**Step 1: Organize Books by Category**
- Takes a collection of books with different categories
- Groups books by their category on the same shelf
- Each category gets its own shelf (or shares shelves if needed)

**Step 2: Sort Books by Title**
- Sorts all books on each shelf alphabetically by title
- Maintains the category grouping while sorting

### Output Files
- **Console output**: Displays the organized catalog with books sorted by title
- **book_catalog.txt**: Creates a text file with the complete catalog

### Example Usage

```bash
python book_catalog.py
```

The program will:
1. Generate 20 sample books with random titles, authors, and categories
2. Organize them into shelves by category
3. Sort each shelf's books alphabetically
4. Display the final organized catalog
5. Create a `book_catalog.txt` file with the results

### Classes Used
- **Book**: Represents individual books with title, author, and category
- **Shelf**: Contains multiple books and handles sorting
- **BookCatalog**: Manages all shelves and organization operations

### Features
- Books of the same category are always on the same shelf
- Each shelf contains books sorted by title in ascending order
- Flexible categorization system
- Easy to extend with additional features

### Sample Output Format
```
=== BOOK CATALOG ===

Shelf 1 with 5 books
  - A Book Title by Author Name
  - Another Book Title by Author Name
  ...

Shelf 2 with 3 books
  - Fiction Book Title by Author Name
  - Mystery Book Title by Author Name
  ...
```

The program will automatically create the `book_catalog.txt` file in the same directory where you run it, containing the complete organized catalog.

# Book Catalog System

System for organizing books into shelves by category with automatic sorting.

## UML Class Diagram

```mermaid
classDiagram
    class Book {
        +string title
        +string author
        +string category
        +string isbn
    }
    
    class Shelf {
        +string category
        +List~Book~ books
        +void sortBooks()
    }
    
    class BookCatalog {
        +List~Shelf~ shelves
        +void organizeByCategory(Set~Book~ books)
        +void sortAllShelves()
        +void displayCatalog()
    }
    
    Book "1" -- "0..*" Shelf : contains~
    Shelf "1" -- "0..*" BookCatalog : manages~