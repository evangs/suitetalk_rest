from flask import Flask
from flask import request
from suds.client import Client

from utils import object_to_dict

import json
import settings
app = Flask(__name__)

client = Client(settings.NETSUITE_WSDL, faults=False)


"""
{
    "passport": {
        "email": "test@test.com",
        "password": "p@s$w0rd",
        "account": "1234567_SB2",
        "role": "3"
    }
}
"""
@app.route('/login', methods=['POST'])
def login():

    passport = request.get_json().get('passport', {})
    email = passport.get('email', '')
    password = passport.get('password', '')
    account = passport.get('account', '')
    role = passport.get('role', '')

    ns4_passport = client.factory.create('ns4:Passport')
    ns4_passport.email = email
    ns4_passport.password = password
    ns4_passport.account = account
    ns4_passport.role._internalId = role

    result = client.service.login(ns4_passport)
    from ipdb import set_trace; set_trace()
    result_dict = object_to_dict(result[1])

    ret = {
        'status': result[0],
        'result': result_dict
    }

    return json.dumps(ret)


# """
# {
#     "fileupload": {
#         "name": "test.js",
#         "content": "b64 encoded binary string",
#         "folder": "3",
#         "file_size": "in megabytes",
#         "media_file": "",
#     }
#
#
# upload_file.attachFrom = '_computer'
# upload_file.content = content
# upload_file.fileSize = 0.0025634765625
# upload_file.fileType = '_JAVASCRIPT'
# upload_file.folder.name = 'SuiteScripts>360'
# upload_file.folder._type = 'folder'
# upload_file.folder._internalId = '18'
# upload_file.isPrivate = False
# upload_file.createdDate = datetime.utcnow()
# upload_file.name = 'test.js'
# }
# """
# @app.route('/login', methods=['POST'])
# def login():
#
#     passport = request.get_json().get('passport', {})
#     email = passport.get('email', '')
#     password = passport.get('password', '')
#     account = passport.get('account', '')
#     role = passport.get('role', '')
#
#     ns4_passport = client.factory.create('ns4:Passport')
#     ns4_passport.email = email
#     ns4_passport.password = password
#     ns4_passport.account = account
#     ns4_passport.role._internalId = role
#
#     result = client.service.login(ns4_passport)
#
#     result_dict = object_to_dict(result[1])
#
#     ret = {
#         'status': result[0],
#         'result': result_dict
#     }
#
#     return json.dumps(ret)

if __name__ == '__main__':
    app.run()
