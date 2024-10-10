/* You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

The area of an island is defined as the number of cells within the island.

Return the maximum area of an island in grid. If no island exists, return 0. */


class Solution {

    public static int connectedGroup(int[][] grid,int row,int col,boolean[][] visited) {
        int rows = grid.length;
        int cols = grid[0].length;
        
        // Check if the current cell is out of bounds or is water or already visited
        if (row < 0 || row >= rows || col < 0 || col >= cols || grid[row][col] == 0 || visited[row][col]) {
            return 0;
        }

        visited[row][col] = true;
        
        // Initialize the area for this part of the island
        int area = 1;

        // Explore all 4 possible directions (up, down, left, right)
        area += connectedGroup(grid, row - 1, col, visited); // Up
        area += connectedGroup(grid, row + 1, col, visited); // Down
        area += connectedGroup(grid, row, col - 1, visited); // Left
        area += connectedGroup(grid, row, col + 1, visited); // Right
        
        return area;
    }
    public int maxAreaOfIsland(int[][] grid) {

        if (grid == null || grid.length == 0) {
            return 0; // empty grid
        }
        
        int rows = grid.length;
        int cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols]; // To keep track of visited cells
        int maxArea = 0;

        // Traverse the entire grid
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // If it's a land cell ('1') and not visited
                if (grid[i][j] == 1 && !visited[i][j]) {
                    // Perform DFS to find the area of this island
                    int area = connectedGroup(grid, i, j, visited);
                    // Update the maximum area if this island's area is larger
                    maxArea = Math.max(maxArea, area);
                }
            }
        }

        return maxArea; 
    }
}
