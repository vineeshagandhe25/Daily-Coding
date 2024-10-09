/* Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water.
You may assume water is surrounding the grid (i.e., all the edges are water). */


import java.util.Queue;
import java.util.LinkedList;
class Solution {

    public static void bfs(char[][] grid,int row,int col,boolean[][] visited) {
        int[] rowDirs = {-1, 1, 0, 0}; // Row movements (up, down)
        int[] colDirs = {0, 0, -1, 1}; // Column movements (left, right)

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{row, col});
        visited[row][col] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int currRow = current[0];
            int currCol = current[1];
            
            // Explore all 4 directions
            for (int i = 0; i < 4; i++) {
                int newRow = currRow + rowDirs[i];
                int newCol = currCol + colDirs[i];
                
                // Check if the new position is within bounds and unvisited land
                if (newRow >= 0 && newRow < grid.length && newCol >= 0 && newCol < grid[0].length && 
                    !visited[newRow][newCol] && grid[newRow][newCol] == '1') {
                    queue.add(new int[]{newRow, newCol});
                    visited[newRow][newCol] = true;
                }
            }
        }
    }

    public int numIslands(char[][] grid) {
         if (grid == null || grid.length == 0) {
            return 0; // for empty grid
        }

        int rows = grid.length;
        int cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];
        int islands = 0;

        // Traverse the grid
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // If we find an unvisited land it is a new island
                if (grid[i][j] == '1' && !visited[i][j]) {
                    bfs(grid, i, j, visited); // Perform BFS to mark the entire island
                    islands++; // Increment the island count
                }
            }
        }

        return islands; 
        
    }
}

// Time Complexity --- O(N*M) N is no of rows and M is no of cols.
// Space Complexity --- O(N*M) N is no of rows and M is no of cols.
