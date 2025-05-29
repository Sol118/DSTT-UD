#1.2.1
import numpy as np
danhsach1 = [1. , 3.]
danhsach2 = [5. , 7.]
danhsach = danhsach1 + danhsach2
print(danhsach)
danhsach_gapdoi = 2 * danhsach
print(danhsach_gapdoi)
print(danhsach * 2)
dsc2 = np.array(danhsach)/2
print(dsc2)

print("\n")

mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
thu_tu = [2, 3, 4, 1]
diem_so = [10, 9, 8, 7]
anh_xa = list(zip(thu_tu, mon_hoc, diem_so))
print(anh_xa)
tap_hop = set(anh_xa)
print(tap_hop)
lay_TT, lay_monhoc , lay_diem = zip(*anh_xa)
print(lay_monhoc)

print("\n")

import itertools
tap_sinh = list(itertools.chain(range(4), range(5,10), range(15,20)))
print(tap_sinh)
print(list(zip(range(4), range(7, 12), reversed(range(11)))))

print("\n")

#1.2.2
mylist = [100, 200, 300]
a, b, c = mylist
print(a, b, c)
a = b = c = 0
mylist = []
print(mylist)

