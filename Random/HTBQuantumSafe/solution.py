# ct(1 * 3) = x(1 * 3) * pubKey(3 * 3) + r(1 * 3)
# x = [ord(c), randint(0, 100), randint(0, 100)]
# Knowing the flag format to be "HTB{...}", we knew flag[0], flag[1], flag[2] and flag[-1]
# Taking all the possible values of x[1] and x[2] all possible values of r were bruteforced.

# For random numbers r1 and r2, r(1 * 3) = pt(1 * 3) - [ord(ct[i]), r1, r2] * pubKey(3 * 3)
# A set of r is created which satisfies the conditions of flag[0], flag[1], flag[2] and flag[-1]

# For valid flag[i], 
# [pt, r1, r2] = (ct(1 * 3) - r(1 * 3)) * inverse(pubKey(3 * 3)), such that :
#     pt is in range(32, 127) [Printable ascii]
#     r1 is in range(0, 100)
#     r2 is in range(0, 100)

import numpy as np

h = np.array([[-981, 1395, -1668]])
t = np.array([[6934, -10059, 4270]])
b = np.array([[3871, -5475, 3976]])
bOpen = np.array([[4462, -7368, -8954]])
bClose = np.array([[5322, -8614, -8334]])

s1 = set()
# m1 = np.array([[1,4,7],[2,5,8]])
# m2 = np.array([[1,4],[2,5],[3,6]])
# m3 = np.dot(m1,m2)

for r1 in range(1, 100):
    for r2 in range(1, 100):
        m1 = np.array([[ord('H'), r1, r2]])
        m2 = np.array([[47, -77, -85],
                       [-49, 78, 50],
                       [57, -78, 99]
                       ])
        m3 = np.dot(m1, m2)
        shit = [_ for _ in np.subtract(h, m3)[0]]
        # print(shit)
        s1.add(str(shit))
print(len(s1))

s2 = set()
for r1 in range(1, 100):
    for r2 in range(1, 100):
        m1 = np.array([[ord('T'), r1, r2]])
        m2 = np.array([[47, -77, -85],
                       [-49, 78, 50],
                       [57, -78, 99]
                       ])
        m3 = np.dot(m1, m2)
        shit = [_ for _ in np.subtract(t, m3)[0]]
        if str(shit) in s1:
            s2.add(str(shit))
print(len(s2))

s3 = set()
for r1 in range(1, 100):
    for r2 in range(1, 100):
        m1 = np.array([[ord('B'), r1, r2]])
        m2 = np.array([[47, -77, -85],
                       [-49, 78, 50],
                       [57, -78, 99]
                       ])
        m3 = np.dot(m1, m2)
        shit = [_ for _ in np.subtract(b, m3)[0]]
        if str(shit) in s2:
            s3.add(str(shit))
print(len(s3))

s4 = set()
for r1 in range(1, 100):
    for r2 in range(1, 100):
        m1 = np.array([[ord('{'), r1, r2]])
        m2 = np.array([[47, -77, -85],
                       [-49, 78, 50],
                       [57, -78, 99]
                       ])
        m3 = np.dot(m1, m2)
        shit = [_ for _ in np.subtract(bOpen, m3)[0]]
        if str(shit) in s3:
            s4.add(str(shit))
print(len(s4))

s5 = set()
for r1 in range(1, 100):
    for r2 in range(1, 100):
        m1 = np.array([[ord('}'), r1, r2]])
        m2 = np.array([[47, -77, -85],
                       [-49, 78, 50],
                       [57, -78, 99]
                       ])
        m3 = np.dot(m1, m2)
        shit = [_ for _ in np.subtract(bClose, m3)[0]]
        if str(shit) in s4:
            s5.add(str(shit))


possibleR = []
for i in s5:
    possibleR.append([int(_) for _ in i[1:-1].split(',')])

ct = [(2794, -4413, -3461),
(5175, -7518, 3201),
(3102, -5051, -5457),
(7255, -10884, -266),
(5694, -8016, 6237),
(4160, -6038, 2582),
(4940, -7069, 3770),
(3185, -5158, -4939),
(7669, -11686, -2231),
(5601, -9013, -7971),
(5600, -8355, 575),
(1739, -2838, -3037),
(2572, -4120, -3788),
(8055, -11985, 1137),
(7088, -10247, 5141),
(8384, -12679, -1381),
(-785, 1095, -1841),
(4250, -6762, -5242),
(3716, -5364, 2126),
(5673, -7968, 6741),
(5877, -9190, -4803),
(5639, -8865, -5356),
(1980, -3230, -3366),
(6183, -9334, -1002),
(2575, -4068, -2828),
(7521, -11374, -1137),
(5639, -8551, -1501),
(4194, -6039, 3213),
(2072, -3025, 383),
(2444, -3699, -502),
(6313, -9653, -2447),
(4502, -7090, -4435),
(-421, 894, 2912),
(4667, -7142, -2266),
(4228, -6616, -3749),
(6258, -9719, -4407),
(6044, -9561, -6463),
(266, -423, -637),
(3849, -6223, -5988),
(5809, -9021, -4115),
(4794, -7128, 918),
(6340, -9442, 892)]

ans = ''
for i in ct:
    for j in possibleR:
        ctNew = np.subtract(np.array(i), j)
        m2 = np.array([[47, -77, -85],
               [-49, 78, 50],
               [57, -78, 99]
               ])
        m2Inv = np.linalg.inv(m2) 
        m4 = np.dot(ctNew, m2Inv)
        m4 = [int(round(_)) for _ in m4]
        if m4[0] in range(32, 128) and m4[1] in range(0, 101) and m4[2] in range(0, 101):
            ans += chr(m4[0])
            break
        # else:
        #     print(m4)
    else:
        ans += ' '
print(ans)

# r3du 1nG_tH3_l4tTicE_l1kE_n0b0dY's_pr0bl3M
# The output doesn't contain flag[0], flag[1], flag[2] and flag[-1]
# Observe, one of the characters is missing in the flag, so maybe this wasn't the intended solution
# But I observed a lot of others were facing the same problem as me in the HTB discussion.
# Grammatically, it should be a 'c'. Try 'c' and 'C'
# HTB{r3duc1nG_tH3_l4tTicE_l1kE_n0b0dY's_pr0bl3M}