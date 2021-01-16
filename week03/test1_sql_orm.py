
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



Base = declarative_base()

class Student_table(Base):
    __tablename__ = 'student'
    uid = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(15), nullable=True)
    age = Column(Integer(), nullable=False)
    birthday = Column(DateTime())
    sex = Column(Boolean(), nullable=False)
    edu = Column(Enum("中学", "专科","本科", "硕士", "博士"))
    create_on = Column(DateTime(), default=datetime.now)
    update_on = Column(DateTime(), default=datetime.now,
                       onupdate=datetime.now)

    def __repr__(self):
        return f'id={self.uid}, name={self.name}, age={self.age}, ' \
               f'birthday={self.birthday}, sex={self.sex}, edu={self.edu}, ' \
               f'create_on={self.create_on}, update_on={self.update_on}'


dburl="mysql+pymysql://root:zk123456@localhost:3306/testdb?charset=utf8mb4"
engine=create_engine(dburl,  encoding="utf-8")

SessionClass = sessionmaker(bind=engine)
session = SessionClass()
Base.metadata.create_all(engine)


student = Student_table(name='Song',
                        age=20,
                        birthday=datetime(2001, 1, 1),
                        sex=True,
                        edu="本科",
                        )
session.add(student)
result = session.query(Student_table).filter(Student_table.name=='Song').all()
print(result)
session.commit()