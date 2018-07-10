from dataclasses import dataclass
import datetime
import script.read_config
@dataclass
class USER:
    '''
    根据python3.7新功能所做个一个简单类
    '''
    __code=0.1
    _data=0.2
    pwd=script.read_config.mail_password#未加密可直接查询的配置
    __pwd1=script.read_config.mail_password#加密后私有的配置
    name:str#指定数据类型与参数名称
    age:int
    nick_name:str
    number:datetime

    def say(self):
        print(self.name,self.name,self.nick_name,self.number)
        print(script.read_config.mail_password)

if __name__ == '__main__':
    user1=USER('linluyang',25,'lly',datetime.datetime.now())
    user1.say()