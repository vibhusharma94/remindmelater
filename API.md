
 Rest API Documentation
-----------------------------

#### **Add Reminder**


    http://127.0.0.1:8000/api/add/reminder

##### **POST**

*Request*

    #!shell
    curl -X POST -H "Content-Type: application/json" -d '{
    "message":"Good Morning",
    "scheduled_on":1466624510,
    "email":"vibhuindian@gmail.com",
    "number":7022158873
    }' "http://127.0.0.1:8000/api/add/reminder"


*Response*
```
#!json
{
    "id": 19,
    "scheduled_on": 1466624510,
    "message": "Good Morning",
    "email": "vibhuindian@gmail.com",
    "number": 7022158873,
    "is_delivered": false,
    "created": "2016-06-22T19:38:55.451274"
}
```