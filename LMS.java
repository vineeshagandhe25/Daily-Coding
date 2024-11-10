/* Design & Implement the following scenario: Draw a class diagram, and use case diagram for the library system. Discuss your 
design decisions, and any limitations of your model. For each book held by the library, the catalogue contains the title, author's name and ISBN of the book. There 
may be multiple copies of a each book and each copy with unique accession number. Registered readers belonging to the library, each of whom is issued with a 
number of tickets. The system records the name and address of each reader, and the number of tickets that they have been issued with. Readers can borrow one book for 
each ticket that they possess, and the system keeps a record of which books a reader has borrowed, along with the date that the book must be returned by. Readers can 
borrow, return and renew books from the library by forwarding a ticket to the library staff at the library desk. Readers have an option of purchasing additional 
tickets from the library. Any book that is not returned by the due date is subject to a fine of Rs.1 per day. Library staff is responsible for collecting fines, adding new 
books to the library. */

import java.util.*;

// Represents Book object
class Book {
    private String title;
    private String author;
    private String isbn;

    public Book(String title, String author, String isbn) {
        this.title = title;
        this.author = author;
        this.isbn = isbn;
    }

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public String getISBN() {
        return isbn;
    }
}

// Represents LibraryTicket object
class LibraryTicket {
    private Book book;
    private Date borrowDate;
    private Date dueDate;

    public LibraryTicket(Book book, Date borrowDate, Date dueDate) {
        this.book = book;
        this.borrowDate = borrowDate;
        this.dueDate = dueDate;
    }

    public Book getBook() {
        return book;
    }

    public Date getDueDate() {
        return dueDate;
    }
}

// Represents Reader object
class Reader {
    private String name;
    private String address;
    private List<LibraryTicket> tickets;

    public Reader(String name, String address) {
        this.name = name;
        this.address = address;
        this.tickets = new ArrayList<>();
    }

    public void borrowTicket(LibraryTicket ticket) {
        tickets.add(ticket);
    }

    public void returnTicket(LibraryTicket ticket) {
        tickets.remove(ticket);
    }

    public List<LibraryTicket> getTickets() {
        return tickets;
    }
}

// Represents Library
class Library {
    private List<Book> books;
    private List<Reader> readers;

    public Library() {
        this.books = new ArrayList<>();
        this.readers = new ArrayList<>();
    }

    public void addBook(Book book) {
        books.add(book);
    }

    public void addReader(Reader reader) {
        readers.add(reader);
    }

    public void borrowBook(Reader reader, Book book) {
        LibraryTicket ticket = new LibraryTicket(book, new Date(), calculateDueDate());
        reader.borrowTicket(ticket);
    }

    public void returnBook(Reader reader, Book book) {
        LibraryTicket ticket = null;
        for (LibraryTicket t : reader.getTickets()) {
            if (t.getBook().equals(book)) {
                ticket = t;
                break;
            }
        }
        if (ticket != null) {
            // Calculate the fine
            long daysLate = calculateDaysLate(ticket.getDueDate());
            double fine = calculateFine(daysLate);
            System.out.println("Fine for late return: Rs. " + fine);
            reader.returnTicket(ticket);
        }
    }

    private Date calculateDueDate() {
        Calendar cal = Calendar.getInstance();
        cal.add(Calendar.DATE, 14); // Assuming 14 days to return the book
        return cal.getTime();
    }

    private long calculateDaysLate(Date dueDate) {
        long diffInMillis = new Date().getTime() - dueDate.getTime();
        return diffInMillis / (1000 * 60 * 60 * 24); // Convert milliseconds to days
    }

    private double calculateFine(long daysLate) {
        if (daysLate > 0) {
            return daysLate * 1; // Rs.1 per day fine
        }
        return 0; // No fine if returned on time
    }
}

public class LMS {
    public static void main(String[] args) {
        Library library = new Library();

        // Add some books to the library
        Book book1 = new Book("Java Programming", "Author A", "12345");
        Book book2 = new Book("Data Structures", "Author B", "67890");
        library.addBook(book1);
        library.addBook(book2);

        // Add a reader
        Reader reader = new Reader("Vineesha", "123 Street, City");
        library.addReader(reader);

        // Borrow a book
        library.borrowBook(reader, book1);

        // Simulate the reader returning the book (assumed to be late)
        library.returnBook(reader, book1);
    }
}
