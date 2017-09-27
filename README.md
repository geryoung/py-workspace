




## 使用过程

1. 使用 unittest discover 进行单元测试
`python load-test.py` 执行

2. 使用 nose 执行单元测试
安装 nose 后，在项目 tests 目录执行 `nosetests` 命令执行

`nosetests -v` 显示执行过程
`nosetests -vs` 显示执行过程

mac 上安装 nose 最好使用easy_install 命令安装 `sudo easy_install nose`

3. 安装 rednose 高亮输出内容
`pip install rednose`
执行：  `nosetests -vs --rednose`









