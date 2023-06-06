Rotate 2D Matrix
To rotate a 2D matrix 90 degrees clockwise in-place, you can use a combination of reverse and transpose operations. The rotate_2d_matrix function provided below implements this rotation algorithm.

Function Description
python
Copy code
def rotate_2d_matrix(matrix):
    # Implementation details
The function takes a 2D matrix as input and modifies it in-place to rotate it 90 degrees clockwise.

Example Usage
python
Copy code
from rotate_2d_matrix import rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
Output:

lua
Copy code
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
The original matrix has been rotated 90 degrees clockwise in-place.
