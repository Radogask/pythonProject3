#№21-667
#Вариант 0
def lcs_length(str1, str2):
    m = len(str1)
    n = len(str2)
    lengths = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                lengths[i][j] = lengths[i - 1][j - 1] + 1
            else:
                lengths[i][j] = max(lengths[i - 1][j], lengths[i][j - 1])

    return lengths[m][n]

def lcs(str1, str2):
    m = len(str1)
    n = len(str2)
    lengths = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                lengths[i][j] = lengths[i - 1][j - 1] + 1
            else:
                lengths[i][j] = max(lengths[i - 1][j], lengths[i][j - 1])

    i = m
    j = n
    lcs_str = ''
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs_str = str1[i - 1] + lcs_str
            i -= 1
            j -= 1
        elif lengths[i - 1][j] > lengths[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs_str

str1 = "ABCDGH"
str2 = "AEDFHR"

length = lcs_length(str1, str2)
subsequence = lcs(str1, str2)

print("Наибольшая общая подпоследовательность:")
print(subsequence)
print("Длина наибольшей общей подпоследовательности:")
print(length)