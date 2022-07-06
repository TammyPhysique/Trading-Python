# Let us calculate FV, if the bond makes semi-annual payments
PV = 1000
r = 0.05
n = 2 # number of periods = 2 since bond makes semiannual payments
t = 1 # number of years
# Type your code below
FV = PV * ((1+(r/n)) ** (n*t))
print (FV)