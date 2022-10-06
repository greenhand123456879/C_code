

def ForElseExample(search_name, student):
    '''
    查找一个人
    :param seacrch_name:查找的人名
    :param student:需要查找的人群
    :return:无
    '''
    for find_name in student:

        print(student)

        if search_name == find_name["name"]:

            print("find it!")
            break
            pass
        pass
    else:
        print("can't find it!")
        pass


list1_name = [
    {"name" : "张三"},
    {"name" : "小美"},
    {"name" : "里斯"},
]

ForElseExample("张三", list1_name)

