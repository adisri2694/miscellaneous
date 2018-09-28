from flask import Flask
from flask import request
from flask import make_response
import pandas as pd
import os
import json
import string

df=pd.read_csv("/home/shabaz/Downloads/final_csv_library.csv")

app2 = Flask(__name__)

@app2.route('/static_reply', methods=['POST'])
def static_reply():
    req = request.get_json(silent=True, force=True)
    print(req) 
    if(req["queryResult"]["action"] == "fare_of_flight"):

        my_result = {
                   "source" : req["queryResult"]["fulfillmentText"],
                   "fulfillmentText" : 'The fare is '}
        res = json.dumps(my_result, indent=1)
        r = make_response(res)
        r.headers['Content-Type'] = 'application/json'
        return r


    if(req["queryResult"]["action"]=="available/not_available"):
        
        book=req["queryResult"]["parameters"]["any"]
        a=book + " is not available"
        for i in range(df.shape[0]):
            if(book.lower()==df.iloc[i][3].lower()):
                a=df.iloc[i][3] +" by "+df.iloc[i][2]+" is available"
                break
            
                
        my_result = {
                   "source" : req["queryResult"]["fulfillmentText"],
                   "fulfillmentText" : a }
        res = json.dumps(my_result, indent=4)
        r = make_response(res)
        r.headers['Content-Type'] = 'application/json'
        return r

    
    

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

app2.run(debug=False, port=port, host='0.0.0.0')


    
