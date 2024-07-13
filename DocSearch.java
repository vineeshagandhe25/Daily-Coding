
/*
Qsn:

You have 10 documents with text in it. 

Let's say: 

Doc A : " Hello, I'm document one. How are you doing..... My writer is khushi"

Doc B : " ... "

.
.
.. 
10 such documents...

Given a query "Khushi writes well" 

You print the documents in the order of score.

If Khushi word is present in a particular doc x times, increase doc_score by x.. and keep repeating..
 */

import java.util.Arrays;

class DocSearch
{
    public static void main(String[] args) 
    {
        // sample docs
        String docs[] ={ "I love java .",
                "I love coding coding.", "I love coding coding coding.",
                "I love coding coding coding coding.",
                "I love coding coding coding coding coding.",
                "I love coding coding coding coding coding coding.",
                "I love coding coding coding coding coding coding coding.",
                "I love coding coding coding coding coding coding coding coding.",
                "I love coding coding coding coding coding coding coding coding coding.",
                "I love coding coding coding coding coding coding coding coding coding coding." };
        // Search query
        String searchWord = "I love coding";        

        // Calculate scores for each document
        int[] scores = new int[docs.length];
        for (int i = 0; i < docs.length; i++)  // Time Complexity - O(D) where D is length of docs.
        {
            scores[i] = calculateScore(docs[i], searchWord); 
        }

        // Create an array of indices  sort it based on the scores
        Integer[] indices = new Integer[docs.length];
        for (int i = 0; i < indices.length; i++) // Time Complexity - O(D) where D is length of docs.
        {
            indices[i] = i;
        }
        
        Arrays.sort(indices, (i, j) -> Integer.compare(scores[i], scores[j]));  // sorting  based on the scores
        
        // Printing sorted documents with scores
        for (int index : indices) // Time Complexity - O(D) where D is length of docs.
        {
            System.out.println("Score: " + scores[index] + " - " + "doc"+(index+1));
        }

    }

    public static int calculateScore(String doc, String searchstr) {
        int length = searchstr.length();
        int score = 0;
        int index = 0;
    
        // Convert searchstr to lower case to ignore case
        String lowerSearchStr = searchstr.toLowerCase();
    
        while (index <= doc.length() - length) { // Time Complexity---O(N)  where  N is length of doc
            // Get the substring of the same length as searchstr from the current index
            String sub = doc.substring(index, index + length).toLowerCase();
            
            if (sub.equals(lowerSearchStr)) {
                score++;
                index += length; 
            } else {
                index++;
            }
        }
    
        return score;
    }
    
    
    
}

// Time Complexity --- O(N*D) where  N is length of doc and D is length of docs.
// Space Compleixty ---O(D)  where D is length of docs.