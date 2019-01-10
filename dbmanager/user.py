
# coding: utf-8

# In[ ]:
from dbmanager.mysqlmanager import MysqlHandler

class UserInfo(object):

    id = ""
    user_phone = ""
    password = ""

    # def test(self):
        # return 0

    # @classmethod
    # def deleteUser(cls):
        # return 0

    @classmethod
    async def getUser(cls,account):
        manager = MysqlHandler()
        userinfo_db = await manager.searchUser(account)
        userinfo = UserInfo()
        userinfo_data = userinfo_db[0]
        userinfo.id = userinfo_data["id"]
        userinfo.user_phone = userinfo_data["user_phone"]
        userinfo.password = userinfo_data["Password"]
        return userinfo
    @classmethod
    async def check_password(cls,account,password):
        manager = MysqlHandler()
        userinfo_db = await manager.searchUser(account)
        userinfo = UserInfo()
        if userinfo_db:
            userinfo_data = userinfo_db[0]
            if userinfo_data["Password"] == password:
                return True
            else:
                return False
        else:
            return False
		

	
	


