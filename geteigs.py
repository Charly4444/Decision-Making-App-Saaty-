import numpy as np

"""assuming of course that it has unique eigen values for this matrix"""

# # Example:
# matrix = np.array([[1, 9, 8, 4, 4],
#     [5, 6, 3, 5, 5],
#     [8, 5, 8, 6, 8],
#     [7, 6, 2, 7, 5],
#     [4, 5, 7, 2, 6]])

def geteigs(matrixin):
    matrix = np.array(matrixin)
    nrow,ncol = matrix.shape
    
    print("Original Matrix:")
    print(matrix)

    # Step 2: Preprocessing - Divide each entry of the matrix by the sum of elements in that row
    row_sums = matrix.sum(axis=1).reshape(-1,1)

    print("matrix", matrix)

    # Step 3: Calculate the geometric mean vector
    geometric_prods = np.prod(matrix, axis=1)
    # print("geom_prods", geometric_prods)

    geometric_mean_vector = geometric_prods ** (1/ncol)
    # print("\nGeometric Mean Vector:")
    # print(geometric_mean_vector)

    gsum = geometric_mean_vector.sum()
    # print(gsum)

    # Step 4: Normalize the geometric mean vector
    eigvecs = geometric_mean_vector / gsum
    print("eigvx:",eigvecs)

    # Step 5: Calculate the sum of columns to now find eigenval max
    sum_of_columns = matrix.sum(axis=0)
    # print(sum_of_columns)

    # Step 6: Calculate the dot product
    eigvalmax = np.dot(eigvecs, sum_of_columns)
    print("\nEigenvalue (eigmax):", eigvalmax)


    # ==========================================================
    # TEST AX = LAMBDA X
    # print("AX:",np.matmul(normalized_matrix,eigvecs))
    # print("LAMBDA X:",eigvalmax*eigvecs)  #OK


    return eigvecs, eigvalmax
