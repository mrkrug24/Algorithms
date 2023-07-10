1. Implement a counting sorting algorithm for arbitrary numbers modulo no more than 10000.
Input data
The input to the program is first supplied with the value n ≤ 100000 – the number of elements in the array. In the next line of input data, the array elements themselves are located – integers, modulo no more than 10000.
Output data
Print an array sorted by non-decreasing.

2. A word is called an anagram of another word if it can be obtained by permutation of its symbols.
Input data
Two words are given on separate lines. Words consist of lowercase Latin letters and numbers. The word lengths do not exceed 255.
Output data
It is required to output "YES" – if the entered words are anagrams of each other, "NO" – if not.

3. Given N integers that need to be sorted in non-decreasing order. Due to the SES norms, there will not be two numbers among the numbers, the difference between which exceeds 107.
Input data
The first line of the input file contains an integer N. (1 <= N <= 100000), the second line contains N integers not exceeding modulo 2*109. No two differ by more than 107.
Output data
Print these numbers in non-decreasing order.

4. Everyone knows that over time the keyboard wears out, and the keys on it begin to stick. Of course, such a keyboard can still be used for some time, but you have to use a lot of force to press the keys.
When making a keyboard, initially for each key, the number of clicks that it must withstand is set. If you know these values for the keyboard you are using, then for a certain sequence of pressed keys, you can determine which keys will break during their use, and which ones will not.
You need to write a program that determines which keys will break during a given keyboard operation option.
Input data
The first line of the input file contains an integer n (1 ≤ n ≤ 100) – the number of keys on the keyboard. The second line contains n integers – c1, c2, ... , sp, where ci (1 ≤ ci ≤ 100000) is the number of clicks sustained by the i–th key. The third line contains an integer k (1 ≤ k ≤ 100000) – the total number of keystrokes, and the last line contains k integers pj (1 ≤ pj ≤ n) – the sequence of keystrokes.
Output data
In the output file, you need to output n lines containing information about the health of the keys. If the i-th key is broken, then the i-th line should contain the word “yes” (without quotes), if the key is functional, the word “no”.

5. A palindrome is a string that reads the same way both from right to left and from left to right.
A set of large Latin letters (not necessarily different) is received at the input of the program. It is allowed to rearrange letters, as well as delete some letters. It is required to make a palindrome of the largest length from these letters according to the specified rules, and if there are several such palindromes, then select the first of them in alphabetical order.
Input data
The first line of the input data contains the number N (1 <= N <= 100000). The second line contains a sequence of N large Latin letters (the letters are written without spaces).
Output data
In a single line of output data, output the desired palindrome.

6. Input data
In each line, the class number is written first (a number equal to 9, 10 or 11), then (separated by a space) — the student's last name.
Output data
It is necessary to display a list of students by class: first, all the students of the 9th grade, then — 10, then — 11. Within one class, the order of output of surnames should be the same as at the input.

7. Vovochka breaks the Pentagon's security system. To do this, he needed to find out which characters in secret encrypted messages are used more often than others. For the convenience of studying, Vovochka wants to get a graphical representation of the occurrence of symbols. Therefore, he wants to build a histogram of the number of characters in the message. A histogram is a graph in which each character that occurs in a message at least once corresponds to a column whose height is proportional to the number of these characters in the message.
Input data
The input file contains the encrypted text of the message. It contains lowercase and uppercase Latin letters, numbers, punctuation marks (".", "!", "?", ":", "-", ",", ";", "(", ")"), spaces and line feeds. The size of the input file does not exceed 104 bytes. The text contains at least one non-whitespace character. All lines of the input file are no longer than 200 characters.
Output data
For each character c, except for spaces and line feeds, output a column of "#" characters, the number of which should be equal to the number of c characters in this text. Under each column, write the symbol corresponding to it. Format the histogram so that the lower ends of the columns are on the same row, the first row and the first column are non-empty. Do not separate the columns from each other. Sort the columns in order of increasing character codes.
