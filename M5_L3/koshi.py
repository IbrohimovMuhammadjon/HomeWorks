from math import sqrt
a,b = map(int, input().split(" "))
geometrik = sqrt(a*b)
arifmetik = (a+b)/2
if arifmetik > geometrik:
  print(">")
elif geometrik > arifmetik:
  print("<")
else:
  print("=")