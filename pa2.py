import csv, sys, os, numpy, math, decimal, cv2
"""
@author     Arjun Albert
@email      aalbert@mit.edu
@modified   11/29/2020
@notes      COSI 175 PA2 DCT Compression
"""

"""
Read file name as a path relative to where the program was run.
Returns a list containing each line of the file as a string element of the list. 
"""
def get_file_as_text(fname):
    flines = []
    f = open(os.path.join(sys.path[0], fname),'rb')
    return cv2.imread(fname) 


"""
Read in all image files.
Returns the images as a list of 3D lists.
"""
def get_files():
    img_files = []
    folder = 'Images for Compression'
    prefix = 'Kodak'
    bw = 'gray'
    postfix = '-TN'
    ext = '.jpg'
    names = ['08', '09', '12', '18', '21', '22']
    for name in names:
        fname = os.path.join(folder, prefix + name + postfix + ext)
        bw_fname = os.path.join(folder, prefix + name + bw + postfix + ext)
        file_lines = get_file_as_text(fname)
        bw_file_lines = get_file_as_text(bw_fname)
        img_files.append(file_lines)
        img_files.append(bw_file_lines)
    return img_files


"""
Compress each image file.
Return the compressed version of each image file to be decompressed.
"""
def compress():
    files = get_files()
    compressed_files = []
    for img in files:
        compressed_img = get_compressed(img)
        compressed_files.append(compressed_img)
    return compressed_files


"""
Apply a sliding box to use DCT on each block of the image.
Block size is a parameter that can be adjusted.
Return the compressed image after DCT has been applied to each block in the image.
"""
def get_compressed(img):
    block_size = 8
    compressed_img = []
    num_rows = len(img)
    num_cols = len(img[0])
    print(img[0][0])
    row_iters = int(num_rows / block_size)
    col_iters = int(num_cols / block_size)
    for i in range(0, row_iters):
        for j in range(0, col_iters):
            block_x = i * block_size
            block_y = j * block_size
    return compressed_img


"""
Pure cosine transform.
"""
def c(x):
    if x == 0: return 1 / (2 ** 0.5)
    return 1


"""

"""
def g(u, v, N, P):
    return 2 * (c(u) * c(v)) / ((N * P) ** 0.5)


"""

"""
def dct(img, u, v, N, P):
    g_term = g(u, v, N, P)
    value = img[u][v]
    for n in range(0, N):
        for p in range(0, P):
            term1 = math.radians((2 * n + 1) * (u * math.pi / 2 * N))
            term2 = math.radians((2 * p + 1) * (v * math.pi / 2 * P))
            value *= math.cos(term1) * math.cos(term2)
    return value * g_term


"""

"""
def idct(img, u, v, N, P):
    g_term = g(u, v, N, P)
    value = img[u][v]
    for n in range(0, N):
        for p in range(0, P):
            term1 = math.radians((2 * n + 1) * (u * math.pi / 2 * N))
            term2 = math.radians((2 * p + 1) * (v * math.pi / 2 * P))
            value /= math.cos(term1) * math.cos(term2)
    return value / g_term


"""
Run the algorithm on the Kodak image dataset.
Write the compressed images to renamed files.
"""
compress()

# matrix = [[90, 100], [100, 105]]
# new_matrix = [[0, 0], [0, 0]]
matrix = [[10, 20, 30], [40, 50, 60], [130, 140, 150]]
new_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
N = len(matrix)
P = len(matrix[0])
for u in range(0, N):
    for v in range(0, P):
        dct_result = dct(matrix, u, v, N, P)
        new_matrix[u][v] = dct_result



new_new_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# new_new_matrix = [[0, 0], [0, 0]]
N = len(new_matrix)
P = len(new_matrix[0])
for u in range(0, N):
    for v in range(0, P):
        idct_result = idct(new_matrix, u, v, N, P)
        new_new_matrix[u][v] = idct_result

print(matrix)
print(new_matrix)
print(new_new_matrix)
