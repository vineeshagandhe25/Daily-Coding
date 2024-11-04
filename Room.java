/* Create a class ‘Room’, with attributes length, breadth and height each of which 
defaults to one.  The class sholud have methods that calculate the area of the room 
and cost (Assume cost = Rs.250/Sq. feet). The class should also have methods to 
compare two rooms and return the difference in terms of size and cost.  */

public class Room {
    private double length;
    private double breadth;
    private double height;

    // Constructor with default values
    public Room() {
        this.length = 1;
        this.breadth = 1;
        this.height = 1;
    }

    // Constructor with custom dimensions
    public Room(double length, double breadth, double height) {
        this.length = length;
        this.breadth = breadth;
        this.height = height;
    }

    // Method to calculate the area of the room
    public double calculateArea() {
        return length * breadth;
    }

    // Method to calculate the cost based on area
    public double calculateCost() {
        final double COST = 250; // (Rs. 250 per square foot)
        return calculateArea() * COST;
    }

    // Method to compare two rooms by area and return the difference
    public double compareArea(Room otherRoom) {
        return Math.abs(this.calculateArea() - otherRoom.calculateArea());
    }

    // Method to compare two rooms by cost and return the difference
    public double compareCost(Room otherRoom) {
        return Math.abs(this.calculateCost() - otherRoom.calculateCost());
    }

    // Main method for testing
    public static void main(String[] args) {
        Room room1 = new Room(10, 15, 8); // Room 1
        Room room2 = new Room(12, 10, 9); // Room 2

        System.out.println("Room 1 area: " + room1.calculateArea() + " sq.ft");
        System.out.println("Room 1 cost: Rs. " + room1.calculateCost());

        System.out.println("Room 2 area: " + room2.calculateArea() + " sq.ft");
        System.out.println("Room 2 cost: Rs. " + room2.calculateCost());

        System.out.println("Difference in area: " + room1.compareArea(room2) + " sq.ft");
        System.out.println("Difference in cost: Rs. " + room1.compareCost(room2));
    }
}

// Time Complexity --- O(1)
// Space Complexity --- O(1) 