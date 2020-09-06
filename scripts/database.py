
from models import models




def update_co2(uuid,co2):
    ses=models.create_sesson()
    q=ses.query(models.UUID_CO2).filter(models.UUID_CO2.uuid==uuid)
    q.co2=co2
    ses.commit()

def get_mail_addr(uuid):
   ses=models.create_sesson()
   q=ses.query(models.UUID_MAIL).filter(models.UUID_MAIL.uuid==uuid).all()
   mail_list=[]
   for d in q:
       mail_list.append(d.mail_address)
    
   return mail_list

def get_Line_id(uuid):
   ses=models.create_sesson()
   q=ses.query(models.UUID_LINE_ID).filter(models.UUID_LINE_ID.uuid==uuid).all()
   line_ids=[]
   for d in q:
       line_ids.append(d.line_id)
    
   return line_ids

    


