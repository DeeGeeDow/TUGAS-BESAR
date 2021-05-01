def split(line):
    data = []
    for i in range(1, len(line)):
        new_arr = []
        cc = ''
        for j in (line[i]):
            if (j == ";"):
                new_arr.append(cc)
                cc = ''
            else:
                cc += j
        if cc:
            new_arr.append(cc)
        arr_data = [data.strip() for data in new_arr]
        data.append(arr_data)
    return data