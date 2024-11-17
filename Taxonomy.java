/* All living things are either plants or animals; Animals can be invertebrates or 
vertebrates; Invertebrates include unicellular creatures (Eg. Amoeba), worms(eg. 
Ringworm, flatworm), nematoads (eg. cockroach) etc.; Vertebrates include 
amphibians (eg. Frog, toad), reptiles (eg. lizard), birds and mammals (eg. Dogs,monkeys, human beings). Write a JAVA program using object-oriented paradigms 
(inheritance) to represent this taxonomy and thereby create properties (data 
members) and functionalities (member functions) for each group. The user should 
able to choose an animal and therby view its charateristic features (data members) 
and its actions (member function). Eg. If the user chooses lizard, the output should 
be: ”lizards are living things”, ”lizards are animals, reptiles”, colour: brown,weight: 20 gms, lifespan: 5 days; “Lizards crawl on the ground”. */

import java.util.Scanner;

// Base class: LivingThings
class LivingThings {
    String classification = "Living Things";

    void characteristic() {
        System.out.println("All living things need air, water, and food to survive.");
    }
}

// Derived class: Animals
class Animals extends LivingThings {
    String classification = "Animals";

    // Override
    void characteristic() {
        System.out.println("Animals are multicellular organisms that rely on other organisms for food.");
    }
}

// Derived class: Invertebrates
class Invertebrates extends Animals {
    String classification = "Invertebrates";

    // Override
    void characteristic() {
        System.out.println("Invertebrates are animals without a backbone.");
    }
}

// Derived class: Vertebrates
class Vertebrates extends Animals {
    String classification = "Vertebrates";

    // Override
    void characteristic() {
        System.out.println("Vertebrates are animals with a backbone.");
    }
}

// Further subclasses of Invertebrates
class Unicellular extends Invertebrates {
    String name = "Amoeba";
    String color = "Transparent";
    double weight = 0.0001; // in grams
    int lifespan = 2; // in days

    // Override
    void characteristic() {
        System.out.println(name + " are microscopic, unicellular organisms.");
    }

    void action() {
        System.out.println(name + " move by changing their body shape.");
    }
}

// Class for Worms
class Worms extends Invertebrates {
    String name = "Ringworm";
    String color = "White";
    double weight = 5; // in grams
    int lifespan = 30; // in days

    void characteristic() {
        System.out.println(name + " are parasitic worms that live in various environments.");
    }

    void action() {
        System.out.println(name + " slither through the ground or inside hosts.");
    }
}

// Class for Vertebrates: Reptiles
class Reptiles extends Vertebrates {
    String name = "Lizard";
    String color = "Brown";
    double weight = 20; // in grams
    int lifespan = 5 * 365; // in days

    void characteristic() {
        System.out.println(name + " are cold-blooded animals with scaly skin.");
    }

    void action() {
        System.out.println(name + " crawl on the ground.");
    }
}

// Main class
public class Taxonomy {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Choose an animal: ");
        System.out.println("1. Amoeba (Unicellular Invertebrate)");
        System.out.println("2. Ringworm (Worm)");
        System.out.println("3. Lizard (Reptile)");

        int choice = scanner.nextInt();

        switch (choice) {
            case 1:
                Unicellular amoeba = new Unicellular();
                System.out.println(amoeba.name + " are " + amoeba.classification);
                amoeba.characteristic();
                System.out.println("Color: " + amoeba.color);
                System.out.println("Weight: " + amoeba.weight + " gms");
                System.out.println("Lifespan: " + amoeba.lifespan + " days");
                amoeba.action();
                break;
            case 2:
                Worms ringworm = new Worms();
                System.out.println(ringworm.name + " are " + ringworm.classification);
                ringworm.characteristic();
                System.out.println("Color: " + ringworm.color);
                System.out.println("Weight: " + ringworm.weight + " gms");
                System.out.println("Lifespan: " + ringworm.lifespan + " days");
                ringworm.action();
                break;
            case 3:
                Reptiles lizard = new Reptiles();
                System.out.println(lizard.name + " are " + lizard.classification);
                lizard.characteristic();
                System.out.println("Color: " + lizard.color);
                System.out.println("Weight: " + lizard.weight + " gms");
                System.out.println("Lifespan: " + lizard.lifespan + " days");
                lizard.action();
                break;
            default:
                System.out.println("Invalid choice! Please choose a valid option.");
        }

        scanner.close();
    }
}

// Time Complexity --- O(1)
// Space Complexity --- O(1)