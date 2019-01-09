
# coding: utf-8

# In[ ]:
from dbmanager.mysqlmanager import MysqlHandler

class UserInfo(object):

    id = ""
    user_phone = ""
    password = ""

    def test(self):

    @classmethod
    def deleteUser(cls):

    @classmethod
    def getUser(cls,account):
        manager = MysqlHandler()
        userinfo_db = await manager.searchUser(account)
        userinfo = UserInfo()
        userinfo.id = userinfo_db["id"]
        userinfo.user_phone = userinfo_db["ser_phone"]
        userinfo.password = userinfo_db["Password"]
        return userinfo


