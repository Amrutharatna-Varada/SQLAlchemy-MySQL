import sqlalchemy as db

engine = db.create_engine("mysql://root:12345678@localhost:3306/organisation")
c=engine.connect()
md=db.MetaData()
org=db.Table(employee,md,autoload=True,autoload_with=engine)
wh=db.select([employee]).where(employee.columns.salary < 15000)
rw=c.execute(wh).fetchall()
i_n=db.select(employee]).where(employee.columns.salary.in_([2500,5000,7500]))
rin=c.execute(i_n).fetchall()
ob=db.select([employee]).order_by(db.desc(employee.columns.salary))
rob=c.execute(ob).fetchall()
