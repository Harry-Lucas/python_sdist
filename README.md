
# python_sdist

对python代码进行打包与注释,同时对python3.7新功能进行测试

##使用说明

1.打包命令：
setup.py目录下执行python setup.py sdist

2.安装包：
setup.py 目录下的dist文件夹下执行pip install 打包后的压缩文件名

3.隐藏配置与调用
script文件下的con.ini文件为配置文件,在read_config.py为读取配置文件脚本。引用配置在类中注意使用双下划线配置成无法读取参数