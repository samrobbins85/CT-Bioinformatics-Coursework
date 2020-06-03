#!/usr/bin/python
import time
import sys
import numpy as np


# YOUR FUNCTIONS GO HERE -------------------------------------
# 1. Populate the scoring matrix and the backtracking matrix
# ------------------------------------------------------------
def init_scoring(m,backtrack):
    for i in range(1,m.shape[1]):
        m[0,i]=-2*i
        backtrack[0,i]='L'
    for i in range(1,m.shape[0]):
        m[i,0]=-2*i
        backtrack[i,0]='U'
def fill_cell(m,backtrack,seq1,seq2,a,b):
    # Here m is the matrix and [b,a] is the location of the cell to fill out
    # Diagonal
    max=score(a,b,seq1,seq2)+m[b-1,a-1]
    pos='D'
    # Up
    temp=m[b-1,a]-2
    if temp>max:
        max=temp
        pos='U'
    # Left
    temp=m[b,a-1]-2
    if temp>max:
        max=temp
        pos='L'
    m[b,a]=max
    backtrack[b,a]=pos
    return




def score(a,b,seq1,seq2):
    # This function finds the score of the matching
    index_a=a-1
    index_b=b-1
    if seq1[index_a]==seq2[index_b]:
        if seq1[index_a]=='A':
            return 4
        if seq1[index_a]=='C':
            return 3
        if seq1[index_a]=='G':
            return 2
        if seq1[index_a]=='T':
            return 1
        else:
            print(str(seq1[index_a])+str(seq2[index_b])+str(index_a)+str(index_b))
    else:
        return -3

def gen_seq(backtrack,str1,str2):
    coord=(len(str2),len(str1))
    matchstring1=''
    matchstring2=''
    while coord!=(0,0):
        if backtrack[coord]=='D':
            coord=(coord[0]-1,coord[1]-1)
            matchstring1=matchstring1+str1[-1]
            str1=str1[:-1]
            matchstring2 = matchstring2 + str2[-1]
            str2 = str2[:-1]
        if backtrack[coord]=='U':
            coord=(coord[0]-1,coord[1])
            matchstring1 = matchstring1 + '-'
            matchstring2 = matchstring2 + str2[-1]
            str2 = str2[:-1]
        if backtrack[coord]=='L':
                coord=(coord[0],coord[1]-1)
                matchstring1 = matchstring1 + str1[-1]
                str1 = str1[:-1]
                matchstring2 = matchstring2 + '-'
    matchstring1=matchstring1[::-1]
    matchstring2 = matchstring2[::-1]
    return [matchstring1,matchstring2]

def fillrow(m,backtrack,seq1,seq2,a):
    for b in range (a,len(seq1)):
        fill_cell(m,backtrack,seq1,seq2,a,b)


def fillcolumn(m,backtrack,seq1,seq2,b):
    for a in range (b,len(seq2)):
        fill_cell(m,backtrack,seq1,seq2,a,b)















# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
# file1 = open(sys.argv[1], 'r')
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()


#-------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Intialise the scoring matrix and backtracking matrix and call the function to populate them
# Use the backtracking matrix to find the optimal alignment 
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score. 
seq1=seq1.rstrip()
seq2=seq2.rstrip()
size=(len(seq2)+1,len(seq1)+1)
m=np.zeros(size, dtype=int)
backtrack=np.chararray(size,unicode=True)
init_scoring(m,backtrack)
b=1


for a in range(1,len(seq1)+1):
    for b in range(1,len(seq2)+1):
        fill_cell(m,backtrack,seq1,seq2,a,b)



best_alignment=gen_seq(backtrack,seq1,seq2)
best_score=m[len(seq2),len(seq1)]



#-------------------------------------------------------------


# DO NOT EDIT (unless you want to turn off displaying alignments for large sequences)------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

