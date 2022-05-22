from app import app
from flask import redirect, url_for, render_template, request,flash
from app.utils.db import Paste, remove_from_db, get_paste,paste_exists, update_paste_views, get_latest_pastes_raw
from app.utils.helpers import gen_id,get_current_time


@app.route("/", methods=['GET','POST'])
def home():

    if request.method=="GET":
        pastes=get_latest_pastes_raw()
        
        return render_template('index.html',latest_pastes=pastes)

    elif request.method=="POST":
        content=request.form["content"]
        title=request.form["title"]
        is_priv=0
        is_otv=0

        if request.form.get("is_priv"):
            is_priv=1 
        else:
            is_priv=0

        if request.form.get("otv"):
                is_otv=1 
        else:
            is_otv=0

        id=gen_id()
        time=get_current_time()
        ip=str(request.remote_addr)
        paste=Paste(title,id,content,time,ip,is_priv,0,is_otv)


        if paste.paste_title !='' and paste.paste_content !='':
            paste.add_to_db()
        else:
            flash("Invalid Input!","danger")
            return redirect(url_for("home"))

        flash("Paste created!", "success")
        return redirect(f"/{id}")
        



@app.route('/<paste_id>', methods=['GET'])
def viewpaste(paste_id):
    if paste_exists(paste_id):
        paste=get_paste(paste_id)
        if paste.is_otv==1 and paste.visit_no>=2:
            flash("Paste is not available anymore!", "danger")
            return redirect(url_for("home"))

    else:
        flash("Invalid paste id", "danger")
        return redirect(url_for("home"))

    
    update_paste_views(paste, paste.visit_no+1)
    pastes=get_latest_pastes_raw()
    return render_template("template.html", paste=paste,latest_pastes=pastes)
    


@app.route("/faq", methods=["GET",])
def faq():
    pastes=get_latest_pastes_raw()
    return render_template("faq.html",latest_pastes=pastes)