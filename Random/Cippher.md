### Question
Background story: this code was once used on a REAL site to encrypt REAL data. Thankfully, this code is no longer being used and has not for a long time.

A long time ago, one of the sites I was building needed to store some some potentially sensitive data. I did not know how to use any proper encryption techniques, so I wrote my own symmetric cipher.

The encrypted content in output.bin is a well-known, olde English quote in lowercase ASCII alphabetic characters. No punctuation; just letters and spaces.

The flag is key to understanding this message.
```
string =  "sf'gh;k}.zqf/xc>{j5fvnc.wp2mxq/lrltqdtj/y|{fgi~>mff2p`ub{q2p~4{ub)jlc${a4mgijil9{}w>|{gpda9qzk=f{ujzh$`h4qg{~my|``a>ix|jv||0{}=sf'qlpa/ofsa/mkpaff>n7}{b2vv4{oh|eihh$n`p>pv,cni`f{ph7kpg2mxqb"

```

```
<?php

function secure_crypt($str, $key) {
  if (!$key) {
    return $str;
  }

  if (strlen($key) < 8) {
    exit("key error");
  }

  $n = strlen($key) < 32 ? strlen($key) : 32;

  for ($i = 0; $i < strlen($str); $i++) {
    $str[$i] = chr(ord($str[$i]) ^ (ord($key[$i % $n]) & 0x1F));
  }

  return $str;
}
```
### Approach
On analysing the source code, one can figure out that we are repeatedly xoring the string with a given key.

The `(ord($key[$i % $n]) & 0x1F)` part ensures that only the last 5 bits are being affected by the xoring. From this for our calculation purposes, we can assume the "effective `key[i]`" to have 5 bits, and therefore range from 8 to 31(as they are rejecting keys with length < 8).

Our first task is to try and determine the length of the key.
For that, let's assume the length to be 8. It's quite evident that the 0th, 8th, 16th and so on... keys will get xored by the same number. Now, for a key of length 8, if for any group of indexes (like `[0, 8, 16....]`, `[1, 9, 17...]`, `[2, 10, 18...]` and so on...) there exists a group which does not yield all lower-case characters when xored individually with all integers in the range `[8, 31]` then we can conclude that for no number in that range, we can xor all characters of that group to a lower case alphabet, or in other words 8(in our example) CAN'T be a possible length.

For my convenience, for the 1st part, I considered only the 1st group of indexes i.e `[0, (0 + len), (0 + 2 * len)...]` and bruteforced the range `[0, 31]` to see the possible lengths...

```
for i in range(8, 33):
    for j in range(0, 33):
        index = 0
        while(index < len(shit)):
            s = chr(j ^ ord(shit[index]))
            index += i
            if s not in "qwertyuiopasdfghjklzxcvbnm ":
                break
        else:
            print("Length : ", i, "Possibility : ", j)
```
Output :
```
Length :  24 Possibility :  2
Length :  24 Possibility :  3
Length :  24 Possibility :  4
Length :  24 Possibility :  5
Length :  24 Possibility :  7
Length :  25 Possibility :  23
Length :  32 Possibility :  0
Length :  32 Possibility :  1
Length :  32 Possibility :  3
Length :  32 Possibility :  4
Length :  32 Possibility :  5
Length :  32 Possibility :  7
Length :  32 Possibility :  10
Length :  32 Possibility :  11
Length :  32 Possibility :  16
Length :  32 Possibility :  17
```
So it narrows down to three possible lengths, 24, 25 and 32.

Now, as I mentioned in the previous bit, I checked only for 1 group, now for these three lengths I checked for all the groups.

For example, for 25, I'll have to check for groups `[0, 25, 50...]`, `[1, 26, 51...]`....`[24, 49, 74...]`. Turns out 24 and 25 get rejected and I'm left out with only one possible length i.e 32.

Time to find out the exact key...
We know that the length of the key is 32. So we have to figure out `key[0]`, `key[1]`, `key[2]`....`key[31]`.
For the 1st group of indexes, we brute-force all the values in range `[8, 31]` and make a list of the possible `key[0]`s, same for all the groups. Whenever we have more than one element in the list, it's not easy to determine which is the correct key[i], but for only 1 element, it's easy to determine that, that is the key[i]. For all the groups corresponding to which I get a list containing only one key, I xor all members of that group with that key. For groups producing more than one possible keys, I replace the characters with underscores.

```
l1 = list(shit)
quote = ['_'] * len(shit)
for i in range(32):
    # print(i, end=":\n\t")
    l2 = []
    for j in range(33):
        index = i
        while index < len(shit):
            s = chr(ord(shit[index]) ^ j)
            index += 32
            if s not in "qwertyuiopasdfghjklzxcvbnm ":
                break
        else:
            l2.append(j)
    if len(l2) == 1:
        index1 = i
        while index1 < len(shit):
            quote[index1] = chr(l2[0] ^ ord(shit[index1]))
            index1 += 32
print(''.join(quote))
```
```
_o __ or no_ t_ b_ th_t __ the q_es__on whe_he_ t_s n_bl__ in th_ m__d to s_ff_r _he _li__s and _rr__s of o_tr_ge_us _or__ne or _o __ke arm_ a_ai_st _ s__ of tr_ub__s and _y _pp_sin_ e__ them
```
From this output, if I can figure out the 1st 32 characters and xor it with the cipher text, then BOOM, I get the key!

So...
`to be or not to be that is the question` (No punctuations, forget grammar, only lower-case and spaces, remember?) You can figure out the whole text but that's all I needed for the key, or the "effective key".

```
x = "to be or not to be that is the question"
for i in range(39):
    print(ord(shit[i]) ^ ord(x[i]), end=' ')
```
```
7 9 7 5 13 27 4 15 14 20 30 18 15 12 12 30 25 15 21 18 30 15 23 14 30 3 18 25 16 20 15 29 7 9 7 5 13 27 4
```
Now what about the real `key[i]`s. Scince the key is the flag, it has to consist of readable ascii characters, so 7 bit binaries. We have the last 5 bits. What about the 2 most significant ones? Well they can be 00, 01, 10 or 11 corresponding to which, we'll have to add 0, 32, 64 or 96 to our `key[i]`s. Also 0 can't be a possibility as then we'll have ascii lesser than 32.

```
l3 = [int(_) for _ in "7 9 7 5 13 27 4 15 14 20 30 18 15 12 12 30 25 15 21 18 30 15 23 14 30 3 18 25 16 20 15 29".split()]
for i in l3:
    print(chr(i + 32), chr(i + 64), chr(i + 96))
```
```
' G g
) I i
' G g
% E e
- M m
; [ {
$ D d
/ O o
. N n
4 T t
> ^ ~
2 R r
/ O o
, L l
, L l
> ^ ~
9 Y y
/ O o
5 U u
2 R r
> ^ ~
/ O o
7 W w
. N n
> ^ ~
# C c
2 R r
9 Y y
0 P p
4 T t
/ O o
= ] }
```
Looks like we only had to add 96...
```
l3 = [int(_) for _ in "7 9 7 5 13 27 4 15 14 20 30 18 15 12 12 30 25 15 21 18 30 15 23 14 30 3 18 25 16 20 15 29".split()]
for i in l3:
    print(chr(i + 96), end='')
```
```
gigem{dont~roll~your~own~crypto}
```
which, ladies and gentlemen is the flag!
