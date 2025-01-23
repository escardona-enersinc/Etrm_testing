import os
from dotenv import load_dotenv
load_dotenv()

URL_ETRM = os.getenv('URL_ETRM')

TENANT_CREDENTIALS = {
    "tmfg":  {
        "username": "",
        "password": ""
    },
    "socg":  {
        "username": "",
        "password": ""
    },
    "tbsg":  {
        "username": os.getenv('USER_TBSG_TENANT'),
        "password": os.getenv('PASSWORD_TBSG_TENANT')
    },
    "endg":  {
        "username": os.getenv('USER_ENDG_TENANT'),
        "password": os.getenv('PASSWORD_ENDG_TENANT')
    },
}



