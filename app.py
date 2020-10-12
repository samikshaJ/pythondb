from flask import Flask,render_template,request,redirect,url_for
import socket
import platform
import mysql.connector

app = Flask(__name__)


#getting the details
@app.route('/machineinfo')

def machineinfo():
    #get machine details
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    os_name = platform.system()



    return render_template("machineinfo.html", host_name=host_name, host_ip=host_ip, os_name=os_name)




@app.route('/linuxos')

def linuxos():
    #get machine details
  
    conn=mysql.connector.connect(host="mysql",user="root",passwd="root",database="linuxos_db");
    curs=conn.cursor();
    query="select * from linuxos_tbl";
    curs.execute(query);
    data=curs.fetchall();
    print("Data Received")
    print(data)
    len1=len(data)
    
   
 
    
     


    return render_template("linuxos.html", len1=len1, data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
