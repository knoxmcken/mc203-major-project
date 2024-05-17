from sympy import * 

A = Matrix([[1, 0, 2], [2, -1, 1], [0, 1, 2]])
encoded_msg = [38, -14, 29, 56, -15, 62, 17, 3, 38, 18, 20, 76, 18, -5, 21, 29, -7, 32, 32, 9, 77, 36, -8, 48, 33, -5, 51, 41, 3, 79, 12, 1, 26, 58, -22, 49, 63, -19, 69, 28, 8, 67, 31, -11, 27, 41, -18, 28]

decoded_msg = []  

for i in range(0, len(encoded_msg), 3):
            print(decoded_msg)
            matrix = Matrix([encoded_msg[i], encoded_msg[i+1], encoded_msg[i+2]])
            print(matrix)
            decoded_msg += [(A.inv() * matrix)[i] for i in range(3)]

print(decoded_msg)