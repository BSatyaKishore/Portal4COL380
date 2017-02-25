# -*- coding: utf-8 -*-
db.define_table('UploadDB',
                Field('UserId', default=auth.user_id, readable=True, writable=False),
                Field('Name', readable=True, writable=False),
                Field('TarFile', 'upload', default='path/',requires=IS_NOT_EMPTY()),
                Field('SubmissionTime','datetime', default=request.now, writable=False),
                Field('Evaluation_Started_At','datetime', writable=False),
                Field('Evaluated_At','datetime', writable=False),
                Field('Score','integer',writable=False),
                Field('Error_Log','text',writable=False),
                Field('Console','text',writable=False),
                Field('Status','string',writable=False))