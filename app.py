from flask import Flask,render_template
import sys,os



sys.path.extend(["models","scripts"])
import models

app = Flask(__name__)



@app.route("/show-db-count")
def root():
    s=models.create_sesson()
   
    result=s.query(models.UUID_CO2).all()
    result2=s.query(models.UUID_LINE_ID).all()
    result3=s.query(models.UUID_MAIL).all()

    if len(result)==0:
        s.add(models.UUID_CO2(uuid=1234,co2=5000))
        s.commit()
   
    s.close()

    return render_template("idx.html",uuidco2=result,uuid_mail=result3,uuid_line=result2)

   






if __name__ == '__main__':
    
    app.run(
        host="0.0.0.0", port=int(os.environ.get("PORT", 5000))
    )
