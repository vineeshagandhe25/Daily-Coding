/* Develop a Java program to represent each entity in the hierarchy shown in the 
figure as classes using object oriented paradigms. Use constructors to initialize 
properties (Eg. Cost, Weight, Dimensions). 
The user should be able to perform the following actions: 
1. Add new instances of clocks, watches and timepieces 
2. View existing items. 
3. Modify the values and functionalities of all items.  
(You can creatively add your own features and methods too.)  */


// Base Class
class Timepiece {
    protected double cost;
    protected double weight;
    protected double length;
    protected double width;

    public Timepiece(double cost, double weight, double length, double width) {
        this.cost = cost;
        this.weight = weight;
        this.length = length;
        this.width = width;
    }

    public void display() {
        System.out.println("Cost: $" + cost + ", Weight: " + weight + " grams, Dimensions: " + length + " x " + width + " cm");
    }
}

// Analog Timepiece
class AnalogTimepiece extends Timepiece {
    protected String dialShape;
    protected String material;

    public AnalogTimepiece(double cost, double weight, double length, double width, String dialShape, String material) {
        super(cost, weight, length, width);
        this.dialShape = dialShape;
        this.material = material;
    }

    // Override
    public void display() {
        super.display();
        System.out.println("Dial Shape: " + dialShape + ", Material: " + material);
    }
}

// Digital Timepiece
class DigitalTimepiece extends Timepiece {
    protected String displayType;

    public DigitalTimepiece(double cost, double weight, double length, double width, String displayType) {
        super(cost, weight, length, width);
        this.displayType = displayType;
    }

    // Override
    public void display() {
        super.display();
        System.out.println("Display Type: " + displayType);
    }
}

// AnalogClock class extending AnalogClock
class AnalogClock extends AnalogTimepiece {
    private boolean isPendulumClock; // Whether the clock has a pendulum

    // Constructor
    public AnalogClock(double cost, double weight, double length, double width, String dialShape, String material, boolean isPendulumClock) {
        super(cost, weight, length, width, dialShape, material);
        this.isPendulumClock = isPendulumClock;
    }

    public void display() {
        super.display(); // Call the parent class's display method
        System.out.println("Pendulum Feature: " + (isPendulumClock ? "Available" : "Not Available"));
    }

}

// Sundial class extending AnalogClock
class Sundial extends AnalogClock {
    private boolean isPortable; // Indicates if the sundial is portable
    private String locationUsage; // Indicates the location type 

    // Constructor
    public Sundial(double cost, double weight, double length, double width, String dialShape, String material, boolean isPendulumClock, boolean isPortable, String locationUsage) {
        super(cost, weight, length, width, dialShape, material, isPendulumClock); // Call parent constructor
        this.isPortable = isPortable;
        this.locationUsage = locationUsage;
    }

    
    //Override
    public void display() {
        super.display(); // Call AnalogClock's display method
        System.out.println("Portable: " + (isPortable ? "Yes" : "No"));
        System.out.println("Location Usage: " + locationUsage);
    }
}

// Watch class extending AnalogTimepiece
class Watch extends AnalogTimepiece {
    private boolean isWaterResistant; // Indicates if the watch is water-resistant

    // Constructor
    public Watch(double cost, double weight, double length, double width, String dialShape, String material, boolean isWaterResistant, String strapMaterial) {
        super(cost, weight, length, width, dialShape, material); // Call parent constructor
        this.isWaterResistant = isWaterResistant;
    }

    // Method to display water resistance capability
    public void checkWaterResistance() {
        System.out.println(isWaterResistant ? "The watch is water-resistant." : "The watch is not water-resistant.");
    }

    //Override
    public void display() {
        super.display(); // Call AnalogTimepiece's display method
        System.out.println("Water Resistance: " + (isWaterResistant ? "Yes" : "No"));
    }
}


// Main Class
public class TimePieceHierarchy {

    public static void main(String[] args) {
        
    }
}
