from dataclasses import dataclass
import datetime
import script.read_config
@dataclass
class USER:
    __code=0.1
    _data=0.2
    pwd=script.read_config.mail_password
    __pwd1=script.read_config.mail_password
    name:str
    age:int
    nick_name:str
    number:datetime

    def say(self):
        print(self.name,self.name,self.nick_name,self.number)
        print(script.read_config.mail_password)

if __name__ == '__main__':
    user1=USER('linluyang',25,'lly',datetime.datetime.now())
    user1.say()