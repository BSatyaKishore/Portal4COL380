# -*- coding: utf-8 -*-
# try something like
import os

@auth.requires_login()
def index():
#     module_load_str = "export MODULEPATH='/usr/share/Modules/modulefiles:/etc/modulefiles:/opt/mellanox/bupc/2.18.0/modules:/home/soft/modules' && /usr/bin/modulecmd bash load mpi/mpich/3.1.4/gcc/mpivars && /usr/bin/modulecmd bash load compiler/cuda/8.0/compilervars && /usr/bin/modulecmd bash load compiler/gcc/5.1.0/compilervars"
    form = SQLFORM(db.UploadDB)
    form.vars.Name= auth.user.first_name+' '+auth.user.last_name
    if form.process().accepted:
        response.flash = 'form accepted'
        # print the file name
        print form.vars.TarFile
        # Extracting Files
        os.system("cd applications/COL380/uploads/ && mkdir "+ form.vars.TarFile[:-7] + ' && tar -xvzf '+ form.vars.TarFile + ' -C '+ form.vars.TarFile[:-7] )
        # Update the folder according to the problem statement
        os.system("cd applications/COL380/uploads/ && bash Main.sh "+form.vars.TarFile[:-7] +" "+ form.vars.TarFile)
        # Copy the folder to hpc
        os.system("cd applications/COL380/uploads/ && scp -r " + form.vars.TarFile[:-7] + " cs5120284@hpc.iitd.ac.in:~/"+form.vars.TarFile[:-7])
        # Compile on hpc
        print 'ssh cs5120284@hpc.iitd.ac.in "source /etc/profile; cd '+ form.vars.TarFile[:-7] +' && bash compile.sh > compile.o 2> compile.e"'
        os.system('ssh cs5120284@hpc.iitd.ac.in "source /etc/profile; cd '+ form.vars.TarFile[:-7] +' && bash compile.sh > compile.o 2> compile.e"')
        # Start Jobs on hpc
        print 'ssh cs5120284@hpc.iitd.ac.in "cd '+ form.vars.TarFile[:-7] +' && python run.py '+form.vars.TarFile+'"'
        redirect(URL('Next', args=(form.vars.TarFile)))
    elif form.errors:
        response.flash = 'form has errors'
    return locals()

def Next():
    os.system('ssh cs5120284@hpc.iitd.ac.in "cd '+ request.args[0][:-7] +' && python run.py '+request.args[0]+'"')
    redirect(URL('Manage'))


def ScoreBoard():
    score_max = db.UploadDB.Score.max()
    score_max.tablename = 'UploadDB' #I removed the underscore _tablename
    score_max.readable = True
    score_max.represent = False
    score_max.formatter = lambda value:value
    score_max.label = T('Best Score')
    score_max.table = db.UploadDB
    grid = SQLFORM.grid(db.UploadDB,deletable=False,editable=False,details=False,create=False,fields=[db.UploadDB.Name,score_max,db.UploadDB.Status,db.UploadDB.SubmissionTime], groupby=db.UploadDB.UserId)
    return locals()

@auth.requires_login()
def Manage():
    grid = SQLFORM.grid(db.UploadDB.UserId==auth.user_id,deletable=False,editable=False,create=False)
    return locals()
