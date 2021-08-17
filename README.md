### How to run:
1. Create a new virtual environment using Python 3.6 
2. Activate your virtual environment and install the requirements using ```pip install -r requirements.txt```
3. Run the code using ```gunicorn -w 1 -b 0.0.0.0:9341 app:app --timeout 0```. Here ```9341``` is the port number.
4. Alternatively, you may use ```python app.py``` to run the code.

### ChatBot API:
```
Method: POST
Url: 127.0.0.1:9341/multiagent/1 # Here 1 is the user_id

Example JSON Request Body:

Example-1:
{
    "user_name": "mashrur",
    "chat_text": "Hi! How are you?"
}
```

### Using Code:
```
Example-1:
curl --location --request POST '127.0.0.1:9341/multiagent/1' \
--header 'Content-Type: application/json' \
--data-raw '{
    "user_name": "mashrur",
    "chat_text": "Hi! How are you?"
}'
```

### Sample response:
```
1. OnSuccess: status code 200
{
  "success": {
    "bot_response": "Yes, I am good."
  }
}

2. OnEmptyRequest: staus code 400
{
  "error": {
    "status": 400,
    "title": "Missing JSON in request."
  }
}

3. OnMissingField: status code 400
{
  "error": {
    "status": 400,
    "title": "Missing field in JSON request."
  }
}
```