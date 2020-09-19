
from sqlalchemy.sql.functions import mode
from models import models




def update_co2(uuid,co2):
    ses=models.create_sesson()
    q=[models.Record(place=uuid,co2=co2)]
    ses.add_all(q)
    ses.commit()


def add_line(uuid,line_id):
    ses=models.create_sesson()
    q=[models.Line(place=uuid,LineID=line_id)]
    ses.add_all(q)
    ses.commit()

def add_mail(uuid,mail_addr):
    ses=models.create_sesson()
    q=[models.Mail(place=uuid,Mail_addr=mail_addr)]
    ses.add_all(q)
    ses.commit()




def get_mail_addr(uuid):
   ses=models.create_sesson()
   q=ses.query(models.Mail).filter(models.Mail.place==uuid).all()
   mail_list=[]
   for d in q:
       mail_list.append(d.Mail_addr)
    
   return mail_list

def get_Line_id(uuid):
   ses=models.create_sesson()
   q=ses.query(models.Line).filter(models.Line.place==uuid).all()
   line_ids=[]
   for d in q:
       line_ids.append(d.LineID)
    
   return line_ids

def get_react_map():
    ses=models.create_sesson()
    
    aa=[]
    q=ses.query(models.Place).all()
    for qq in q:
        ss={"lat":qq.lat,"lng":qq.lng,"name":qq.name,"average":qq.average}
        aa.append(ss)
    
    return {"places":aa}

    
if __name__ == "__main__":
    
    print(get_react_map())


    


