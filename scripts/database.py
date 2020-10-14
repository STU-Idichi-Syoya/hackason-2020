
from models.models import Place
from sqlalchemy.sql.functions import mode
from models import models

from sqlalchemy import distinct



def update_co2(uuid,co2):
    ses=models.create_sesson()
    q=[models.Record(place=uuid,co2=co2)]
    ses.add_all(q)
    ses.commit()
    q=ses.query(models.Record).filter(models.Record.place==uuid).order_by(models.Record.created_at.desc()).all()
    
    s=0
    c=0
    for count, qq in enumerate(q):
        if count >=5:
            break
        c+=1
        s+=qq.co2
    
    ave=s/c
    q=ses.query(models.Place).filter(models.Place.id==uuid).first()
    q.average=ave

    ses.commit()

def get_co2(uuid):
    ses=models.create_sesson()

    q=ses.query(models.Record).filter(models.Record.place==uuid).order_by(models.Record.created_at.desc()).first()
    
    
    if q is not None:
        return q.co2
    else:
        return None
    

    



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
    
   return list(set(mail_list))

def get_Line_id(uuid):
   ses=models.create_sesson()
   q=ses.query(models.Line).filter(models.Line.place==uuid).all()
   line_ids=[]
   for d in q:
       line_ids.append(d.LineID)
    
   return list(set(line_ids))

def get_react_map():
    ses=models.create_sesson()
    
    aa=[]
    q=ses.query(models.Place).all()
    for qq in q:
        ss={"lat":qq.lat,"lng":qq.lng,"name":qq.name,"average":qq.average}
        aa.append(ss)
    
    return {"places":aa}

    
if __name__ == "__main__":
    print("start")
    ses=models.create_sesson()
    q=ses.query(models.Record).order_by(models.Record.created_at.desc()).all()
    
    s=0
    c=0
    for count, qq in enumerate(q):
        if count >=10:
            break
        c+=1
        s+=qq.co2
    print(s/c,c)


    


