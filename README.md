# FangTianXiaSpider
房天下数据，新房-二手房，位置、价格、城市、楼盘简介等

`python3 start.py`
运行

得到的 json 文件, 需要在开头和结尾加上 '[' 和 ']', 不然读取 json 会报错.
然后使用
`python3 read_json.py` 进行统计分区的套数, 以及生成按照分区名称归类的套房数据. 方便以后做数据分析.

导出项目 requirements.txt
```bash
pip install pipreqs
pipreqs ./ --encoding=utf-8
```
注意这个命令是导出系统中所有的 python 环境
```bash
pip freeze > requirements.txt
```

安装所需依赖包
```bash
pip install -r requirements.txt
```

