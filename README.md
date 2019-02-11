

# 你的代码行数记录

## 一，介绍

用python实现的记录你代码文件中特定后缀文件的代码行数和文件数的小项目

需要的第三方库：

- matplotlib
- numpy

## 二，使用方法

### 配置文件的说明-config.json_

```
{
#运行的文件目录，即你保存代码的文件位置
  "PATH": "C:\\Users\\Maozu\\dust",
#需要忽略掉的文件名称
  "IGNORE_FILE": [
    "jquery.js",
    "jquery.min.js"
  ],
#需要忽略的目录名称
  "IGNORE_DIR": [
  	".git",
  	".idea",
    "venv",
    "cmake-build-debug"
  ],
#需要记录的文件后缀
  "COUNT_FILE": [
    ".c",
    ".cpp",
    ".h",
    ".hpp",
    ".js",
    ".py",
    ".md",
    ".json",
    ".css",
    ".less",
    ".scss",
    ".html",
  ]
}
```

### way.json

```
{
  "c": [7102, 7102, 20, 32, 43],
  "cpp": [325, 325, 30, 23, 45],
  "h": [526, 526, 3, 34, 23],
  "css": [2400, 2400, 4, 3, 65],
  "md": [150, 150, 44, 3, 4],
  "html": [100, 100, 43, 43, 4],
  "py": [80, 80, 43, 56, 76],
  "json": [62, 62, 54, 67, 4],
  "scss": [4, 4, 34, 54, 34],
  "less": [700, 700, 32, 56, 43],
  "js": [58, 58, 54, 23, 3]
  #第一个数字为最近一次记录到的代码行数之后的数字为每一次运行时改变的行数，可为负值
}
```

## 实例



### 代码组成饼状图

![](https://github.com/Maozu/count_line/blob/master/pie.png)

### 每一次运行代码改变情况

![](https://github.com/Maozu/count_line/blob/master/line.png)

## 最后

关于它的碎碎念会发布在我博客(blog.maozu.ink)