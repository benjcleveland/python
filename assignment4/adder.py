import time
import json
from urlparse import parse_qs

def index( req ):
    
    #$return req.args
    # make sure that we have args passed in 
    if req.args == None:
        return 'No args'

    # parse the arguments 
    a = parse_qs( req.args )

    try:
        # try to add bot the numbers
        res = int(a['a'][0]) + int(a['b'][0])
    except:
        return 'Invalid argument',req.args
    
    # create a dictionary with all the information we want to return
    dic = {'time': time.time(), 'result': res, 'uwnetid':'cleveb'}

    # return the data in JSON 
    return json.dumps( dic, sort_keys=True, indent=4 ) 
