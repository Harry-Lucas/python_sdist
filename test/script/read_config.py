import os
import configparser

# 获取文件的当前路径（绝对路径）
cur_path = os.path.dirname(os.path.realpath(__file__))

# 获取config.ini的路径
config_path = os.path.join(cur_path, 'conf.ini')

#获取配置文件的参数
conf = configparser.ConfigParser()
conf.read(config_path)

mail_server = conf.get('test_conf', 'mail_server')
mail_username = conf.get('test_conf', 'mail_username')
mail_password = conf.get('test_conf', 'mail_password')
mail_receiver = conf.get('test_conf', 'mail_receiver')