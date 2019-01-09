import torndb
import tornado

class MysqlHandler(object):

	async def matchUser(self,account,password):
		""" 从数据库查找用户
		@ account：帐号
		@ password: 密码
		@ return：True/Fase
		"""
		db = torndb.Connection(host='localhost', database='pay_loan', user='root', password='')
		phone_in_db = db.get('select user_phone from register_info where user_phone=%s', account)
		password_in_db = db.get('select password from register_info where user_phone=%s', account)
		if phone_in_db == account:
			map_key = '1'
		else:
			map_key = '0'
		if password_in_db == password:
			map_key2 = '1'
		else:
			map_key2 = '0'
		key = map_key + map_key2
		if key == '01':
			 resp = {'error': 'Phone_number not exists!'}
		elif key == '00':
			resp = {'error': 'Phone_number not exists!'}
		elif key == '10':
			resp = {'error': 'password not correct!'}
		elif key == '11':
			resp = {'error': 'password not correct!'}
		return resp

	async def searchUser(self,account):
		""" 从数据库搜索用户
		@ account：用户手机号
		@ return： True/Fase
		"""
		db = torndb.Connection(host='localhost', database='pay_loan', user='root', password='')
		phone_in_db = db.get('select * from register_info where user_phone=%s', account)
		return phone_in_db

	async def addUser(self,account,password):
		#往数据库表中添加新的用户
		db = torndb.Connection(host='localhost', database='pay_loan', user='root', password='')
		phone_in_db = db.get('select user_phone from register_info where user_phone=%s', account)
		if phone_in_db:
			resp = {'error': 'Phone_number already exists!'}
		else:
			resp = {'user_phone': account, 'Password': password}
			db.execute('insert into register_info(user_phone,password) values(%s,%s)', account, password)
		return resp
