
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
        String searchWord = "coding";        

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

    public static int calculateScore(String doc, String searchWord) 
    {
        String[] words = doc.split("\\W+"); // Split by non-word characters
        int score = 0;
        for (String word : words) { // Time Complexity - O(N) where N is length of words.
            if (word.equalsIgnoreCase(searchWord)) 
            {
                score++;
            }
        }
        return score;
    }
}

// Time Complexity --- O(N*D) where  N is length of words and D is length of docs.
// Space Compleixty ---O(D)  where D is length of docs.