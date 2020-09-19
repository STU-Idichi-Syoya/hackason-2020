from datetime import datetime


from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text,Float,DateTime
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

Model = declarative_base()

class Place(Model):
    
    __tablename__ = 'Place'

    ## id== uuid
    id=Column(Text,primary_key=True)
    lat=Column(Float)
    lng=Column(Float)
    name=Column(Text)
    average = Column(Integer, nullable=False, default=0)
    last_up_time = Column(DateTime, default=datetime.now,
                          onupdate=datetime.now)

class Line(Model):
    
    __tablename__ = 'Line'

    ## id== uuid
    id=Column(Integer,primary_key=True,autoincrement=True)
    place=Column(Text,ForeignKey("Place.id"),primary_key=True)
    LineID = Column(Text)

class Mail(Model):
    
    __tablename__ = 'Mail'

    ## id== uuid
    id=Column(Integer,primary_key=True,autoincrement=True)
    place=Column(Text,ForeignKey("Place.id"),primary_key=True)
    Mail_addr = Column(Text)
import datetime
class Record(Model):
    
    __tablename__ = 'Record'

    ## id== uuid
    id=Column(Integer,primary_key=True,autoincrement=True)
    place=Column(Text,ForeignKey("Place.id"),primary_key=True)
    created_at=Column(DateTime,default=datetime.datetime.now)
    co2 = Column(Integer)


import os


## DB のURIは環境変数から取得
URI=os.getenv("DB_URI")
if URI is not None:
    engine = create_engine(URI)
    Model.metadata.create_all(engine)


def create_sesson():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


if __name__ == "__main__":
    import random
    import string

    def randomname(n):
        randlst = [random.choice(string.ascii_letters + string.digits)
                   for i in range(n)]
        return ''.join(randlst)

    s = create_sesson()
    result = s.query(Place).all()



    print("chk")

    if len(result)==0:
        place_db,Line_db,Mail_db = [], [], []
        for _ in range(500):

            uuid = randomname(50)
            mail_addr = randomname(random.randint(4, 6))+"@gmail.com"
            ave = random.randint(500,2000)
            line_id = randomname(30)
            name=randomname(10)
            lat=random.randrange(130,145)
            lng=random.randrange(35,45)


            place_db.append(Place(id=uuid,name=name,lat=lat,lng=lng))
            Line_db.append(Line(place=uuid,LineID=line_id))
            Mail_db.append(Mail(place=uuid,Mail_addr=mail_addr))

            # id_line.append(UUID_LINE_ID(uuid=uuid, line_id=line_id))

            # id_mail.append(UUID_MAIL(uuid=uuid, mail_address=mail_addr))

            # id_co2.append(UUID_CO2(uuid=uuid, co2=co2))

        
        print("chk2.0")
        s.add_all(place_db)
        s.commit()

        s.add_all(Line_db)
        s.add_all(Mail_db)
        print("chk2")
        s.commit()

    # if 1:
    #     for r in result:
    #         print(r.uuid, r.co2, r.last_up_time)
    s.close()
