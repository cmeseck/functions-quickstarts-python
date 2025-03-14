import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    response_data = {"message": "YESSSIR!!!!"}  # JSON response data
    return func.HttpResponse(
        json.dumps(response_data), 
        mimetype="application/json"
    )
