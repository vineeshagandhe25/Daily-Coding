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

import java.util.Scanner;

public class TicTacToe {

    public static void main(String[] args) {
        char[][] board = { { '1', '2', '3' }, { '4', '5', '6' }, { '7', '8', '9' } };
        char currentPlayer = 'X';
        boolean gameWon = false;
        Scanner sc = new Scanner(System.in);

        // Function to print the current board
        printBoard(board);

        // Main game loop
        while (!gameWon) {
            System.out.println("Player " + currentPlayer + ", enter your position: ");
            int position = sc.nextInt();

            if (positionIsValid(board, position)) {
                makeMove(board, position, currentPlayer);
                printBoard(board);

                if (checkWin(board)) {
                    System.out.println("Player " + currentPlayer + " wins!");
                    gameWon = true;
                } else if (boardIsFull(board)) {
                    System.out.println("It's draw!");
                    break;
                }

                // Switch player
                currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
            } else {
                System.out.println("Invalid position, try again.");
            }
        }
        sc.close();
    }

    // Function to print the board 
    public static void printBoard(char[][] board) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }

    // Function to make a move
    public static void makeMove(char[][] board, int position, char player) {
        switch (position) {
            case 1 -> board[0][0] = player;
            case 2 -> board[0][1] = player;
            case 3 -> board[0][2] = player;
            case 4 -> board[1][0] = player;
            case 5 -> board[1][1] = player;
            case 6 -> board[1][2] = player;
            case 7 -> board[2][0] = player;
            case 8 -> board[2][1] = player;
            case 9 -> board[2][2] = player;
        }
    }

    // Function to check if a move is valid
    public static boolean positionIsValid(char[][] board, int position) {
        switch (position) {
            case 1 -> {
                return board[0][0] == '1';
            }
            case 2 -> {
                return board[0][1] == '2';
            }
            case 3 -> {
                return board[0][2] == '3';
            }
            case 4 -> {
                return board[1][0] == '4';
            }
            case 5 -> {
                return board[1][1] == '5';
            }
            case 6 -> {
                return board[1][2] == '6';
            }
            case 7 -> {
                return board[2][0] == '7';
            }
            case 8 -> {
                return board[2][1] == '8';
            }
            case 9 -> {
                return board[2][2] == '9';
            }
            default -> {
                return false;
            }
        }
    }

    // Function to check if the game is won
    public static boolean checkWin(char[][] board) {
        // Check rows
        for (int i = 0; i < 3; i++) {
            if (board[i][0] == board[i][1] && board[i][1] == board[i][2]) {
                return true;
            }
        }
        // Check columns
        for (int j = 0; j < 3; j++) {
            if (board[0][j] == board[1][j] && board[1][j] == board[2][j]) {
                return true;
            }
        }
        // Check diagonals
        if (board[0][0] == board[1][1] && board[1][1] == board[2][2]) {
            return true;
        }
        if (board[0][2] == board[1][1] && board[1][1] == board[2][0]) {
            return true;
        }
        return false;
    }

    // Function to check if the board is full (draw condition)
    public static boolean boardIsFull(char[][] board) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] != 'X' && board[i][j] != 'O') {
                    return false;
                }
            }
        }
        return true;
    }
}

// Time Complexity --- O(1) 
// Space Complexity --- O(1) 