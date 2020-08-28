import json
from collections import defaultdict

#with open('./newhouse.json', encoding='utf-8') as f:
#    line = f.readline()
#    d = json.loads(line)
#    district = d['district']
#    print(district)
#   f.close()

#file = open("./newhouse.json", 'r', encoding='utf-8')
#for line in file.readlines():
#    dic = json.loads(line)
#    district = d['district']
#    print(district)

#f.close()

filename = './newhouse.json'
#将数据加载到一个列表中
with open(filename,'r',encoding='utf8') as f:
    json_data = json.load(f)

# 每个区楼盘个数统计
district_dict={}
index=0

# 生成空的 dict, 这样生产的 dict 才能是 一键多值字典, 可以使用 append
# 以分区名作为 key, 值是所有改分区的楼盘 json 数据
# 方便以后做分区的价格图标
new_info = defaultdict(list)

p_list = defaultdict(list) # price
n_list = defaultdict(list) # name


#print(type(new_info), type(json_data))

#打印信息
for json_dict in json_data:
    district = json_dict['district']
    price = json_dict['price']
    name = json_dict['name']
    origin_url = json_dict['origin_url']
    #print(format(district), name, price, origin_url)

    p_list[district].append(price)
    n_list[district].append(name)

    if district in district_dict.keys():
        district_dict[district]+=1
    else:
        district_dict[district]=1
    new_info[district].append((json_data[index]))
    index += 1

# 打印每个区楼盘个数统计
#print(district_dict)

# json.dumps(p_list, indent=1) 是带缩进的格式化输出
#print(json.dumps(p_list, indent=1).encode('utf-8').decode('unicode_escape'))
#print(n_list)

# 打印第一个和最后一个 json
#print(0, json_data[0])
#print(index-1, json_data[index-1])

#print(json.dumps(new_info)) # 这里是打印的原始数据, 看不到正确的中文字符

# 这里的 data 数dict 数据, 可以打印出中文
data = json.loads(json.dumps(new_info))
#print(type(data), "\n", data)
#print(new_info)

test_dict = {
    'version': "1.0",
    'results': new_info,
    'explain': {
        'used': True,
        'details': "this is FangTianXia new houese data on NanNing.",
  }
}

#print(type(test_dict), type(test_dict['results']))
for res in test_dict['results'].items():
    #print('\n', type(res))
    if res is None:
        print("res None")
        continue
    for r in res:
        if isinstance(r, str):
            # python3 end="" 不换行输出
            # 打印市区名
            print(r, end="区 ")
        elif r is None:
            print("None", end=" ")
        elif isinstance(r, list):
            # 打印时区对应的盘数量
            print(len(r))
            if len(r) >= 1:
                # 打印其中一个
                #print(r[0]['price'])
                #print(json.dumps(r[len(r)-1], indent=1).encode('utf-8').decode('unicode_escape'))
                # 打印所有
                #print(json.dumps(r, indent=1).encode('utf-8').decode('unicode_escape'))
                for i in r:
                    if i['name'] is None or i['price'] is None:
                        continue
                    # 打印盘的 name 和 price, 格式化输出
                    print('\t{0:<30}\t{1:<3}'.format(i['name'], i['price']))
        else:
            print("r type is ", type(r))

json_str = json.dumps(test_dict, indent=1) # 写入的是原始数据, 看不到中文的
# json_str.encode('utf-8').decode('unicode_escape') 转换成显示正确中文字符
#print("write date type:", type(json_str), json_str.encode('utf-8').decode('unicode_escape')
with open('district_dict_data.json', 'w') as json_file:
    json_file.write(json_str.encode('utf-8').decode('unicode_escape'))
