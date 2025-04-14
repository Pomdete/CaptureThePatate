x0=True
x1=False
x2=False
x3=True
x4=True

y0=x0 ^ (x3 & (not x4))
y1=x1 ^ (x4 & (not x0))
y2=x2 ^ (x0 & (not x1))
y3=x3 ^ (x1 & (not x2))
y4=x4 ^ (x2 & (not x3))

print(f"{y0}, {y1}, {y2}, {y3}, {y4}")