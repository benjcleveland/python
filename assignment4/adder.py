import time
import json
from urlparse import parse_qs

def index( req ):
    
    a = parse_qs( req.args )

    res = int(a['a'][0]) + int(a['b'][0])
    dic = {'time': time.time(), 'result': res, 'uwnetid':'cleveb'}

    return json.dumps( dic ) 
