import cv2
import numpy as np
#i = cv2.imread('file22img.png')
#j = cv2.imread('file33image.png')
filename = np.loadtxt('approx add camt.csv',delimiter=',', dtype=int)
filename1 = np.loadtxt('exact add camt.csv',delimiter=',', dtype=int)
#filename = np.uint8(filename)
#filename = np.uint8(filename)
#print(filename1)
#print(filename)
#k = cv2.addWeighted(i, 0.9, j, 1,0)
sub = np.zeros((512, 512))
subexact = 0
subapprox = 0
for i in range(0,512):
    for j in range(0,512):
        sub[i][j] = filename1[i][j] - filename[i][j]
        subexact += filename1[i][j]
        subapprox += filename[i][j]

#print(sub)
#cv2.imshow("add", k)
filename = np.uint8(filename)
#SUM_SQUARE_MAT = cv2.imsub(k-filename)
SUM_SUB = 0
SUM_SUB_SQUARE = 0
SUM_SQUAREEXACT = 0
SUM_SQUAREAPPROX = 0
PRODUCT_NK = 0
SQUARE_EXACT = np.zeros((512, 512))
SQUARE_APPROX = np.zeros((512, 512))
m = 512;
n = 512;
#print(sub[0][0])
for i in range(m):
    for j in range(n):
        SQUARE_EXACT[i][j] = np.double(filename1[i][j]**2)
        SQUARE_APPROX[i][j] = np.double(filename[i][j]**2)
        SUM_SQUAREEXACT = SUM_SQUAREEXACT + SQUARE_EXACT[i][j]
        SUM_SQUAREAPPROX = SUM_SQUAREAPPROX + SQUARE_APPROX[i][j]
        SUM_SUB = SUM_SUB + np.uint8(sub[i][j])
        SUM_SUB_SQUARE += sub[i][j]**2

MSE = SUM_SUB_SQUARE/(m*n)
temp = MSE
MAE = SUM_SUB/(m*n)
AD = SUM_SUB/(m*n)
NAE = SUM_SUB/SUM_SQUAREEXACT
MAD = sub.max()
SC = SUM_SQUAREEXACT/SUM_SQUAREAPPROX
SNR = ((2**512)-1)/(temp)
PSNR1 = 10*(np.log10(SNR))
PSNR = 10*(np.log10(PSNR1))
msexact = SUM_SQUAREEXACT/(m*n)
msapprox = SUM_SQUAREAPPROX/(m*n)
maexact = subexact/(m*n)
maapprox = subapprox/(m*n)
adexact = subexact/(m*n)
adapprox = subapprox/(m*n)
naexact = subexact/SUM_SQUAREEXACT
naapprox = subapprox/SUM_SQUAREAPPROX
print()
print()
print('The quality parameters for both combined(approx and exact):')
print('MSE=',MSE)
print('MAE=',MAE)
print('AD=',AD)
print('NAE=',NAE)
print('MAD=',MAD)
print('SC=',SC)
print('PSNR=',PSNR,'DB')
print()
print()
print('The quality parameters for exact addition:')
print('MSEXACT=',msexact)
print('MAEXACT=',maexact)
print('ADEXACT=',adexact)
print('NAEXACT=',naexact)
print()
print()
print('The quality parameters for approximate addition:')
print('MSAPPROX=',msapprox)
print('MAAPPROX=',maapprox)
print('ADAPPROX=',adapprox)
print('NAAPPROX=',naapprox)
