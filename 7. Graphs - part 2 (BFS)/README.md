1. In an undirected graph, you need to find the minimum path between two vertices.
Input data
The first input is the number N – the number of vertices in the graph (1 ≤ N ≤ 100). Then the adjacency matrix is written (0 denotes the absence of an edge, 1 – the presence of an edge). Next, the numbers of two vertices are set – the initial and the final.
Output data
Print first the L – length of the shortest path (the number of edges that need to be traversed), and then the path itself. If the path has a length of 0, then it is not necessary to output it, it is enough to output the length.
It is necessary to print the path (the numbers of all vertices in the correct order). If there is no way, you need to print -1.

2. On the chessboard NxN in the cell (x1, y1) there is a hungry chess knight. He wants to get into the cage (x2, y2), where the delicious chess grass grows. What is the least number of moves he has to make for this?
Input data
The program receives five numbers: N, x1, y1, x2, y2 (5 <= N <= 20, 1 <= x1, y1, x2, y2 <= N). The upper left cell of the board has coordinates (1, 1), the lower right - (N, N).
Output data
In the first line, print a single number K - the smallest required number of knight moves. In each of the following K+1 lines, 2 numbers should be written - the coordinates of the next cell in the knight's path.
The example of the output file below is incomplete, the correct example is:
4
3 3
2 1
1 3
3 2
5 1

3. A table consisting of N rows and M columns is given. Each cell of the table contains one of the numbers: 0 or 1. The distance between the cells (x1, y1) and (x2, y2) is the sum |x1-x2|+|y1-y2|. You need to build a table in the cell (i, j) of which the minimum distance between the cell (i, j) of the initial table and the cell in which 1 is written is recorded. It is guaranteed that at least one 1 is in the table.
Input data
In the first line, two natural numbers N and M are entered, not exceeding 500. Then there are N rows of M numbers - the elements of the table.
Output data
It is required to output N rows of M numbers - the elements of the desired table.

4. In the Milky Way galaxy, there are N cities on the planet Neptune, some of which are connected by roads. The Emperor "Maximus" of the Milky Way galaxy decided to conduct an inventory of roads on the planet "Neptune". But, as it turned out, he is not good at math, so he asks you to count the number of roads.
Input data
The first line contains the number N (0 ≤ N ≤ 100). The next N lines contain N numbers, each of which is a one or a zero. Moreover, if there is one in the position (i, j) of the square matrix, then the i-th and j-th cities are connected by roads, and if there is a zero, then they are not connected.
Output data
Print one number – the number of roads on the planet "Neptune".
