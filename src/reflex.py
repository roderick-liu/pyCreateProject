# -*- coding: utf-8 -*-
import os

class One:
    """
    test reflex
    """
    def __init__(self):
        self.name = "laozhang"
        pass

    def func(self, msg):
        """
        disp message 
        """
        lstr = str(msg)
        print(lstr.upper())

    def login(self):
        print("这是一个登陆页面")
 
    def logout(self):
        print("这是一个退出页面")
 
    def home(self):
        print("这是一个主页面")

if __name__ == '__main__':
    obj = One()
    #判断ｏｂｊ中是否有第二个参数
    #如果第二个只是属性，则返回属性值，如果是方法名，则返回方法的内存地址，如果第二个参数没有在对象中找到，程序崩溃
    # res = getattr(obj,"name１") #程序崩溃
    # res = getattr(obj,"name") #返回属性值 并同时可省略r = res()
    res = getattr(obj,"func") #res为ｆｕｎｃ的内存地址
    r = res("lll")
    print(r)

    #检查ｏｂｊ中是否存在func成员,当找到第二个参数时返回ｔｒｕｅ，否则返回ｆａｌｓｅ
    res = hasattr(obj,"func")
    print(res)

    print(obj.name) #查看之前obj的ｎａｍｅ
    #设置obj中ｎａｍｅ为laowang
    res = setattr(obj,"name","laowang")
    print(obj.name)
    #当设置的值不存在时，会自动添加到实例对象中
    #setattr需要三个参数: x,y,z　==> x.y =z
    #相当于obj.age = 10
    setattr(obj,"age","10")
    print("name=%s,age=%s"%(obj.name,obj.age))  #laowang 10

    #删除对象的属性
    delattr(obj,"age")
    print("name=%s,age=%s"%(obj.name,obj.age))  #程序崩溃
    print(os.path.abspath())

    # duo can shu
    # try:
    #     command_act()
    #     except TypeError:
    #         V1 = input('Missing Variable:')
    #         try:
    #            command_act(V1)
    #         except TypeError:
    #             V2 = input('Missing Variable2:')
    #             command_act(V1,V2)



