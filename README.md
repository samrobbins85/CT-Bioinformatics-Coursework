# Computational Thinking Bioinformatics Coursework

Coursework for the Bioinformatics submodule of the Computational Thinking 1st Year Module at Durham University

## Objective One

Develop a Python program that uses Dynamic Programming to compute the optimal alignment of two sequences. It should meet the following conditions

- The algorithm should read in two sequences from text files (the sequences may be of different length)
- Initialise the scoring matrix and the backtracking matrix
- Score each alignment using the following scores
  - +4 for a matching pair of "A" bases
  - +3 for a matching pair of "C" bases
  - +2 for a matching pair of "G" bases
  - +1 for a matching pair of "T" bases
  - -3 for a mismatching pair of bases
  - -2 for a gap
- Use the backtracking matrix to determine an optimal alignment
- The program should print out the following
  - The optimal alignment and its score
  - Execution time

## Objective Two

Using the following matrix of inter-species distanced, construct a phylogenetic tree using the UPGMA algorithm.

|       | a   | b   | c   | d   | e   | f   |
| ----- | --- | --- | --- | --- | --- | --- |
| **a** | 0   | 15  | 24  | 29  | 25  | 37  |
| **b** | 15  | 0   | 32  | 31  | 23  | 43  |
| **c** | 24  | 32  | 0   | 30  | 43  | 49  |
| **d** | 29  | 31  | 30  | 0   | 45  | 57  |
| **e** | 25  | 23  | 43  | 45  | 0   | 55  |
| **f** | 27  | 43  | 49  | 57  | 55  | 0   |

## Objective Three

Develop a Python program that uses the WPGMA algorithm to draw a phylogenetic tree from an input matrix of inter-species distanced. It should meet the following conditions:

- Your code should have a function called WPGMA which takes as its input the name of a text file
- The algorithm should read in an inter-species distance matrix from this text file, and print this matrix to the screen
- Follow the WPGMA algorithm, and print out to the screen every reduced distance matrix
- After fully reducing the matrix, the code should draw the phylogenetic tree obtained to a file. This tree does not need to contain edge weights,
- Finally the program should print out the execution time to the screen
