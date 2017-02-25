# -*- coding: utf-8 -*-
# try something like

@auth.requires_login()
def index(): 
    form = SQLFORM(db.UploadDB)
    form.vars.Name= auth.user.first_name+' '+auth.user.last_name
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    return locals()

def ScoreBoard():
    grid = SQLFORM.grid(db.UploadDB,deletable=False,editable=False,details=False,create=False,fields=[db.UploadDB.Name,db.UploadDB.Score,db.UploadDB.Status,db.UploadDB.SubmissionTime])
    return locals()

@auth.requires_login()
def Manage():
    grid = SQLFORM.grid(db.UploadDB.UserId==auth.user_id,deletable=False,editable=False,create=False)
    return locals()
