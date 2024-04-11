# dx=x1-x0
# dy=y1-y0
# D = 2*dy - dx
# plot(x0,y0)
# y=y0
# for x from x0+1 to x1
#     if D >= 0
#         y = y+1
#         D = D - (2*dx)
#     D = D + (2*dy)
#     plot(x,y)

x0 = 20
y0 = 10
x1 = 30
y1 = 18

dx = x1 - x0
dy = y1 - y0
D = 2 * dy - dx
print(f"x: {x0}, y: {y0}, d: {D}")
y = y0
for x in range(x0 + 1, x1):
    if D >= 0:
        y = y + 1
        D = D - (2 * dx)
    D = D + (2 * dy)
    print(f"x: {x}, y: {y}, d: {D}")
