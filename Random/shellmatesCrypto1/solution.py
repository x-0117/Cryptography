# -*- coding: utf-8 -*-
import random

for day in range(26, 28):
    for h in range(24):
        for m in range(60):
            s = int('202205' + str(day) + str(h).rjust(2, '0') + str(m).rjust(2, '0'))
            # print(s)
            l1 = list("N_gs{aesD_he_3AtrsOLlh3ROT1sECRl0m}s")
            
            random.seed(s)
            l2 = list(range(len(l1)))
            random.shuffle(l2)
            ans = [-1 for _ in range(len(l1))]
            for i in range(len(l1)):
                ans[i] = l1[l2.index(i)]
            
            ans = ''.join(ans)
            if 'shellmates' in ans:
                print(ans)

# shellmates{N1ghT_C0D3Rs_ArE_LOOs3Rs}