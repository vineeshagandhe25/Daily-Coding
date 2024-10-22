/* Write a program that will allow two users to play tic-tac-toe. The program should 
ask for moves alternately from player X and player O. The program displays the 
game positions as follows:
1 2 3
4 5 6
7 8 9
The players enter their moves by entering the position number they wish to mark. 
After each move, the program displays the changed board. A sample board 
configuration is as follows:
X X O
4 5 6
O 8 9 */

import java.util.*;
public class TicTacToe {
    
    public static void main(String[] args) {
        
        char[][] board = {{'1','2','3'},{'4','5','6'},{'7','8','9'}};  // board
        char position1 = ' ';  // user1  position 
        char position2 = ' ';  // user2 position
        Scanner sc = new Scanner(System.in);
        String temp ;

        // printing intial board.
        for(int i=0;i<3;i++) {
            for(int j=0;j<3;j++) {
                System.out.println(board[i][j]);
            }
        }

        while(true) {
            // for user1 
            System.out.println("user1 enter your position ");
            temp=sc.nextLine();
            position1=temp.charAt(0);
            for(int i=0;i<3;i++) {
                for(int j=0;j<3;j++) {
                    if(board[i][j] == position1) {
                        board[i][j] = 'X';
                    }
                }
            }
            // printing after user1 option
            for(int i=0;i<3;i++) {
                for(int j=0;j<3;j++) {
                    System.out.println(board[i][j]);
                }
            }

            // for user2 
            System.out.println("user2 enter your position ");
            temp=sc.nextLine();
            position2=temp.charAt(0);
            for(int i=0;i<3;i++) {
                for(int j=0;j<3;j++) {
                    if(board[i][j] == position2) {
                        board[i][j] = 'X';
                    }
                }
            }
            // printing after user2 option
            for(int i=0;i<3;i++) {
                for(int j=0;j<3;j++) {
                    System.out.println(board[i][j]);
                }
            }

        }
    }
}
