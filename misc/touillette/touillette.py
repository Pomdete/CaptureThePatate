flag = open("flag.txt").read()
assert len(flag) == 64

x = "".join([
    flag[-8::-8],
    flag[-7::-8],
    flag[-6::-8],
    flag[-5::-8],
    flag[-4::-8],
    flag[-3::-8],
    flag[-2::-8],
    flag[-1::-8],
])
print(f"{x=}")
print(x[1::2] + x[0::2])
input =x[1::2] + x[0::2]

input_ordered = []
for i in range(32):
    input_ordered.append(input[32 + i])
    input_ordered.append(input[i])
input_ordered = "".join(input_ordered)
print(f"{input_ordered=}")
