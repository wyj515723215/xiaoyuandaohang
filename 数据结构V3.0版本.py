class MyString:
    def __init__(self, data=""):
        self.str = list(data)

    def get_len(self):
        return len(self.str)

    def get_char(self, idx):
        if 0 <= idx < self.get_len():
            return self.str[idx]
        return None


def bf_search(main_str: MyString, pat_str: MyString):
    n = main_str.get_len()
    m = pat_str.get_len()
    count = 0
    i, j = 0, 0
    while i < n and j < m:
        count += 1
        if main_str.get_char(i) == pat_str.get_char(j):
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    return (i - j, count) if j == m else (-1, count)


def get_next(pat: MyString):
    m = pat.get_len()
    nxt = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pat.get_char(i) != pat.get_char(j):
            j = nxt[j - 1]
        if pat.get_char(i) == pat.get_char(j):
            j += 1
            nxt[i] = j
    return nxt


def kmp_search(main_str: MyString, pat_str: MyString):
    n, m = main_str.get_len(), pat_str.get_len()
    count = 0
    nxt = get_next(pat_str)
    i, j = 0, 0
    while i < n and j < m:
        count += 1
        if main_str.get_char(i) == pat_str.get_char(j):
            i += 1
            j += 1
        else:
            if j != 0:
                j = nxt[j - 1]
            else:
                i += 1
    return (i - j, count) if j == m else (-1, count)


if __name__ == "__main__":
    import time
    nav_data = """
1#教学楼:位于校园北区,紧邻南门公交站;路线:南门直行300米;简介:本科上课主楼
2#食堂:校园中区,图书馆西侧;路线:北门右转200米;简介:三餐就餐场所
实训五号楼后侧小路:西区实训楼后方连通操场;简介:非机动车近道
    """ * 120  # 批量扩充数据至9w+字符
    main_s = MyString(nav_data)
    key = input("输入要查找的校园地点：")
    pat_s = MyString(key)

    t1 = time.time()
    pos_bf, cnt_bf = bf_search(main_s, pat_s)
    t_bf = (time.time() - t1) * 1000

    t2 = time.time()
    pos_kmp, cnt_kmp = kmp_search(main_s, pat_s)
    t_kmp = (time.time() - t2) * 1000

    print(f"【BF算法】耗时：{t_bf:.2f}ms,比对次数：{cnt_bf},匹配下标：{pos_bf}")
    print(f"【KMP算法】耗时：{t_kmp:.2f}ms,比对次数：{cnt_kmp},匹配下标：{pos_kmp}")
