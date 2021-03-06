# 6. ZigZag Conversion 
"""
Medium  The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P        I       N
A     L  S    I  G
Y  A     H  R
P        I
"""
# O(N) Time
def convert(strng, numRows):
    if numRows==1 or numRows>len(strng):  return strng
    listMatrix = ['']*numRows  # build the form for assigned numRows
    index, step = 0, 1  
    # use index to put letter in listMatrix[index], and loop forward/backward between 0 and numRows-1
    # use step as forwad(1) / backward(-1) to index
    for letter in strng:  # loop throught every letter of input strng
        listMatrix[index] += letter  # add letter to listMatrix[index], index indicates which row
        if index==0:  # Start position in numRows
            step = 1  # loop forward
        elif index==numRows-1:  # End position in numRows
            step = -1  # loop backward
        index += step  # update index from 0 to 1 to 2 to ... numRows-1, then numRow3-2 to numRows-3 to ... 1, 0
    return ''.join(listMatrix)  # join every row in the listMatrix as output
  
