import mysql.connector
from flask import flash
db=mysql.connector.connect(host="localhost",user="root",db="anonpaste_db",passwd="")
cursor=db.cursor()


class Paste:

    def __init__(self,pastetitle:str, pasteid:int, pastecontent:str,pastetime:str, ipaddr:str,ispriv:int,visitno:int,isotv:int):
        self.paste_title=pastetitle
        self.paste_id=pasteid
        self.paste_content=pastecontent
        self.paste_time=pastetime
        self.ip_addr=ipaddr
        self.is_private=ispriv
        self.visit_no=visitno
        self.is_otv=isotv
    
    def add_to_db(self):
        query="INSERT INTO `pastes` (`paste_number`, `paste_title`, `paste_id`, `paste_content`, `time_of_paste`, `ip_address`, `is_private`, `visit_no`, `is_otv`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query,(None,str(self.paste_title),str(self.paste_id),str(self.paste_content),str(self.paste_time),str(self.ip_addr),int(self.is_private),int(self.visit_no),int(self.is_otv)))
        db.commit()


def remove_from_db(paste_id):
    cursor.execute("DELETE FROM pastes WHERE `pastes`.`paste_id` = %s", (paste_id, ))
    db.commit()



def get_paste(paste_id):
    cursor.execute("SELECT * FROM `pastes` WHERE `paste_id`=%s", (paste_id, ))
    pest=list(cursor.fetchone())
    paste=Paste(pest[1],pest[2],pest[3],pest[4],pest[5],pest[6],pest[7],pest[8])
    return paste



def paste_exists(paste_id):
    cursor.execute("SELECT * FROM `pastes` WHERE `paste_id`=%s", (paste_id, ))
    resp=cursor.fetchone()
    if resp==None:
        return False
    else:
        return True


def update_paste_views(paste:Paste, view_no):
    paste_id=paste.paste_id
    cursor.execute("UPDATE `pastes` SET `visit_no` = %s WHERE `pastes`.`paste_id` = %s; ",(int(view_no),paste_id))
    db.commit()

def get_latest_pastes_raw():
    cursor.execute("SELECT * FROM `pastes` WHERE `is_private`=%s AND `is_otv`=%s ORDER BY `paste_number` DESC", (int(0),int(0)))
    raw_data=cursor.fetchmany(size=7)

    return raw_data





        