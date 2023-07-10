1. Stirlitz was driving a car, saw Bormann voting, and drove past. After a while, he saw Bormann voting again, and drove past again. Soon he saw Bormann voting again.
 - He's mocking me!  Bormann thought.
 - Ring road! - Stirlitz guessed.
There are N squares in the city. Any two squares are connected by exactly one two-way road. Stirlitz lives in this city. Stirlitz has a hobby - he likes to leave the house on Sunday morning, get in the car, choose some circular route that passes through exactly three squares (that is, first he goes from some square to some other, then to the third, then returns to the initial one, and again goes along this route). He imagines that Bormann is standing somewhere along the way. And so Stirlitz goes all Sunday, until his head gets dizzy, and rejoices...
Naturally, Stirlitz wants to drive past the point where, as he imagines, Borman is standing, as often as possible. To do this, of course, the route chosen by Stirlitz should be as short as possible. Write a program that will choose the optimal route for Stirlitz.
Input data
The first line specifies the number N (3 <= N <= 100). The following lines contain a matrix NxN of distances between squares (the number in position i, j denotes the length of the road connecting the i-th and j-th squares). All numbers in the matrix (except those on the main diagonal) are natural, not exceeding 1000. The matrix is symmetric with respect to the main diagonal, there are 0 on the main diagonal.
Output data
It is required to output three numbers — the numbers of squares in the optimal route. If there are several routes, output any of them.

2. An oriented graph is given. It is required to determine whether there is a cycle in it.
Input data
In the first line, enter the number of vertices N≤ 50. Then N numbers follow in N rows, each of which is 0 or 1. The j–th number in the i-th row is 1 if and only if there is an edge going from the i-th vertex to the j-th. It is guaranteed that there will be zeros on the diagonal of the matrix.
Output data
Output 0 if there is no cycle in the given graph, and 1 if there is one.

3. An undirected unweighted graph is given. It is necessary to determine whether it is a tree.
Input data
The first line of the input file contains one natural number N (N ≤ 100) - the number of vertices in the graph. Next, in N rows of N numbers, there is an adjacency matrix of the graph: in the ith row, in the jth place, there is 1 if the vertices i and j are connected by an edge, and 0 if there is no edge between them. There are zeros on the main diagonal of the matrix. The matrix is symmetric with respect to the main diagonal.
Output data
Print "YES" if the graph is a tree, and "NO" otherwise.

4. There is an undirected graph consisting of N vertices and M edges. It is necessary to check whether the graph is a tree. Recall that a tree is a connected graph in which there are no cycles (hence, there is exactly one simple path between any pair of vertices). A graph is called connected if there is a path from one vertex to any other.
Input data
In the input file, the first line contains two integers N and M (1 ≤ N ≤ 100, 0 ≤ M ≤ 1000), separated by a space. This is followed by M different lines with descriptions of edges, each of which contains two natural numbers Ai and Bi (1 ≤ Ai <Bi ≤ N), where Ai and Bi are the numbers of vertices connected by the i-th edge.
Output data
Output the word YES to the output file if the graph is a tree or NO otherwise.

5. An undirected unweighted graph is given. For it, you need to find the number of vertices lying in one component of connectivity with a given vertex (counting this vertex).
Input data
The first line of the input data contains two numbers: N and S (1 ≤ N ≤ 100; 1 ≤ S ≤ N), where N is the number of vertices of the graph, and S is a given vertex. The next N lines contain N numbers each – the adjacency matrix of the graph, in which 0 means the absence of an edge between the vertices, and 1 means its presence. It is guaranteed that there are always zeros on the main diagonal of the matrix.
Output data
Print a single integer – the desired number of vertices.

6. It is required to calculate the area of the room in a square maze.
Input data
In the first line, enter the number N – the size of the maze (3 <= N <= 10). The following N lines contain a maze (‘.’ is an empty cell, ‘*’ is a wall). And finally, the last row contains two numbers – the number of the row and column of the cell located in the room whose area needs to be calculated. It is guaranteed that this cell is empty and that the maze is surrounded by walls on all sides.
Output data
It is required to output a single number – the number of empty cells in this room
