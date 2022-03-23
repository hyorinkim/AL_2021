num = int(input())
text = []
result = []
for i in range(num):
    text.append(input())
    score = 0
    sc = 0
    for c in text[i]:
        if c == "O":
            sc += 1
            score += sc
        elif c == 'X':
            sc = 0
    result.append(score)
for i in range(num):
    print(result[i])