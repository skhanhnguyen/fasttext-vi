import numpy as np
import io
import sys

def load_vectors(fname, num_words = 10000):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = fin.readline().split()
    print('Mô hình có',n,'từ vựng')
    print('Mỗi từ được biểu diễn bằng một vector',d,'chiều')
    print('Đang tải...')
    data = {}
    i=0
    for line in fin:
        i +=1
        tokens = line.rstrip().split(' ')
        data[tokens[0]] = np.array([float(val) for val in tokens[1:]])
        data[tokens[0]] /= np.linalg.norm(data[tokens[0]])
        if i > num_words:
            break
    print('Đã tải '+sys.argv[2]+' vector tiếng Việt')
    return data



data = load_vectors(sys.argv[1], num_words = int(sys.argv[2]))


while True:
    ref_w = input('Chọn một từ tiếng Việt, bấm Ctrl+C để thoát: ')
    if ref_w not in data:
        print(ref_w, 'không có trong mô hình')
        continue
    ref_v = data[ref_w]

    top_num = 20
    top_w = ['']*top_num
    top_s = [-1]*top_num

    for k in data.keys():
        if ref_w == k:
            continue
        score =  np.dot(ref_v, data[k])
        if score < np.min(top_s):
            continue
        for i in range(top_num):
            if score >= top_s[i]:
                top_w[i+1:] = top_w[i:top_num-1]
                top_w[i] = k
                top_s[i+1:] = top_s[i:top_num-1]
                top_s[i] = score
                break


    # In[7]:


    # print("từ tìm kiếm:", ref_w)
    for i in range(top_num):
        print(top_s[i], '\t', top_w[i])

