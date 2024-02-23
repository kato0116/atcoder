# 2023.07.28
# 一回目の提出でTLE。どうやったらループとれるか思いつかない。

import numpy as np

H, W, N = map(int, input().split())
MAP = [[0] * (W + 2) for _ in range(H + 2)]
MAP[1][1] = 3

print(MAP)