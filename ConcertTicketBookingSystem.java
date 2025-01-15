// Concert Ticket Booking System

import java.util.*; 

// Concert class to hold concert details 
class Concert {

    private int concertID;
    private String artistName;
    private String venue;
    private String date;
    private String time;
    private List<String> seatArrangement;

    public Concert(int concertID, String artistName, String venue, String date, String time) {
        this.concertID = concertID;
        this.artistName = artistName;
        this.venue = venue;
        this.date = date;
        this.time = time;
        this.seatArrangement = new ArrayList<>();
    }

    public List<String> getAvailableSeats() {
        return seatArrangement;
    }

    public void addSeat(String seat) {
        seatArrangement.add(seat);
    }

}

// User class to hold user details 
class User {
    private int userID;
    private String name;
    private String email;
    private String phone;

    public User(int userID, String name, String email, String phone) {
        this.userID = userID;
        this.name = name;
        this.email = email;
        this.phone = phone;
    }
    

    public Booking selectSeats(Concert concert, List<String> seats) {
        return new Booking(this, concert, seats);
    }
}

// Booking class to hold booking details 
class Booking {
    private int bookingID;
    private static int counter = 1;
    private User user;
    private Concert concert;
    private List<String> selectedSeats;
    private String bookingStatus;

    public Booking(User user, Concert concert, List<String> selectedSeats) {
        this.bookingID = counter++;
        this.user = user;
        this.concert = concert;
        this.selectedSeats = selectedSeats;
        this.bookingStatus = "Pending";
    }

    public void confirmBooking() {
        this.bookingStatus = "Confirmed";
        System.out.println("Booking Confirmed for " + selectedSeats);
    }
}

// Payment  class to hold payment details 
class Payment {
    private int paymentID;
    private static int counter = 1;
    private Booking booking;
    private double paymentAmount;
    private String paymentStatus;

    public Payment(Booking booking, double paymentAmount) {
        this.paymentID = counter++;
        this.booking = booking;
        this.paymentAmount = paymentAmount;
        this.paymentStatus = "Pending";
    }

    public void processPayment() {
        this.paymentStatus = "Completed";
        System.out.println("Payment of $" + paymentAmount + " processed for Booking ID: " + booking);
    }
}

// Waiting List class to hold waiting list details 
class WaitingList {
    private int listID;
    private static int idCounter = 1;
    private Concert concert;
    private List<User> userList;

    public WaitingList(Concert concert) {
        this.listID = idCounter++;
        this.concert = concert;
        this.userList = new ArrayList<>();
    }

    public void addToWaitingList(User user) {
        userList.add(user);
        System.out.println("User added to waiting list for Concert: " + concert);
    }
}

public class ConcertTicketBookingSystem {
    public static void main(String[] args) {
        Concert concert = new Concert(1, "Vishwateja", "Hyderabad", "25-05-2025", "10:00 PM");
        concert.addSeat("A1");
        concert.addSeat("A2");

        User user = new User(101, "Vineesha", "vineesha@mail.com", "1234567890");
        List<String> selectedSeats = Arrays.asList("A1");
        Booking booking = user.selectSeats(concert, selectedSeats);

        booking.confirmBooking();
        Payment payment = new Payment(booking, 100.00);
        payment.processPayment();

        WaitingList waitingList = new WaitingList(concert);
        waitingList.addToWaitingList(user);
    }
}
