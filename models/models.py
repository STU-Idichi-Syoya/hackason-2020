from datetime import datetime



from sqlalchemy import create_engine, Column, Integer, String,DateTime,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Model=declarative_base()

class UUID_CO2(Model):

    __tablename__ = 'uuid_co2'

    uuid = Column(Integer, primary_key=True)
    co2 = Column(Integer, nullable=False,default=0)
    last_up_time=Column(DateTime,default=datetime.now,onupdate=datetime.now)

class UUID_LINE_ID(Model):
    __tablename__="uuid_lineID"

    uuid=Column(Integer,primary_key=True)
    line_id=Column(Text,nullable=True)

class UUID_MAIL(Model):
    __tablename__="uuid_mail"

    uuid=Column(Integer,primary_key=True)
    mail_address=Column(Text,nullable=True)


engine = create_engine('sqlite:///sample_db.sqlite3')
Model.metadata.create_all(engine)

def create_sesson():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session




if __name__ == "__main__":
    import random,string
    def randomname(n):
       randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
       return ''.join(randlst)

    s=create_sesson()
    result=s.query(UUID_CO2).all()
    
    if 1:
     id_line,id_mail,id_co2=[],[],[]
     for _ in range(500):

            uuid=_
            mail_addr=randomname(random.randint(4,6))+"@gmail.com"
            co2=random.randint(0,5000)
            line_id=randomname(30)

            id_line.append(UUID_LINE_ID(uuid=uuid,line_id=line_id))

            id_mail.append(UUID_MAIL(uuid=uuid,mail_address=mail_addr))

            id_co2.append(UUID_CO2(uuid=uuid,co2=co2))

     s.add_all(id_line)
     s.add_all(id_mail)
     s.add_all(id_co2)
     s.commit()

    else:
        for r in result:
            print(r.uuid,r.co2,r.last_up_time)
    s.close()