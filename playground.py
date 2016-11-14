
half = float(0.5)

numHalf = 1
fourNine = float(0.44444444)
numFourNine = 0
threeNine = float(0.33333333)
result = 0.0000

for i in range (0,100):

    this = (half**numHalf)*(fourNine**numFourNine)*threeNine
    result = result + this
    numHalf = numHalf + 1
    numFourNine = numFourNine + 1
print result

result = 0.0000
numHalf = 0
numFourNine = 0
for i in range (0,100):
    this = (half**numHalf)*(fourNine**numFourNine)*half
    result = result + this
    numHalf = numHalf + 1
    numFourNine = numFourNine + 1
print result
