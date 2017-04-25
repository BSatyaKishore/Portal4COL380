import requests

@request.restful()
def Compile():
    def POST(*args, **vars):
        #print request.vars
        #print request.vars['fileName']
        row = db(db.UploadDB.TarFile == request.vars['fileName']).select().first()
        row.update_record(CompiledAt=request.now, CompileErrorLog=request.vars['compileO'], CompileOutLog= request.vars['compileE'])
        #db.UploadDB.update_or_insert(TarFile=fileName, CompiledAt=request.now, CompileErrorLog=compileO, CompileOutLog= compileE)
        print request.vars

        #print compileO, compileE
        return dict()

    return locals()

@request.restful()
def SendStatus1():
    def POST(*args, **vars):
        row = db(db.UploadDB.TarFile == request.vars['fileName']).select().first()
        row.update_record(CompiledAt=request.now, TestCase1Log=request.vars['O1'], TestCase1Error= request.vars['E1'])
        return dict()
    return locals()

@request.restful()
def SendStatus2():
    def POST(*args, **vars):
        row = db(db.UploadDB.TarFile == request.vars['fileName']).select().first()
        row.update_record(CompiledAt=request.now, TestCase2Log=request.vars['O2'], TestCase2Error= request.vars['E2'])
        return dict()
    return locals()

@request.restful()
def SendStatus3():
    def POST(*args, **vars):
        row = db(db.UploadDB.TarFile == request.vars['fileName']).select().first()
        row.update_record(CompiledAt=request.now, TestCase3Log=request.vars['O3'], TestCase3Error= request.vars['E3'])
        return dict()
    return locals()

@request.restful()
def SendStatus4():
    def POST(*args, **vars):
        row = db(db.UploadDB.TarFile == request.vars['fileName']).select().first()
        row.update_record(CompiledAt=request.now, TestCase4Log=request.vars['O4'], TestCase4Error= request.vars['E4'])
        return dict()
    return locals()

@request.restful()
def SendStatus5():
    def POST(*args, **vars):
        row = db(db.UploadDB.TarFile == request.vars['fileName']).select().first()
        row.update_record(CompiledAt=request.now, TestCase5Log=request.vars['O5'], TestCase5Error= request.vars['E5'])
        return dict()
    return locals()
