// Tower of Hanoi using recursion .
class TowerOfHanoi {

    public static void towerOfHanoi(int num,char source,char target,char auxilary) {

        // Base Condition 
        if ( num == 1 ) {
            System.out.println("Disc 1 moved from "+source + " to" + target);
            return ;
        }
        towerOfHanoi(num-1, source, auxilary, target);
        System.out.println("Disc"+ num +" moved from "+source + " to" + target);
        towerOfHanoi(num-1, auxilary, target,source);
    }

    public static void main(String[] args) {

        towerOfHanoi(3, 'A', 'C', 'B');
    }
}

// Time Complexity --- O(2^N) where N is the no of discs .
// Space Complexity --- O(N) where N is the no of discs .