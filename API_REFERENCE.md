API Endpoint: http://ecostamp.naist.jp/api/
*All API return
  {
    "success": true
  }
in case of success or
  {
    "success": false,
    "reason": "error message"
  }
in case of failure


/dummy [POST]
Return input JSON plus some dummy stamp information


/register [POST]
Create new user
Input:
  {
    "username": "foo",
    "email": "fooemail",
    "password": "foopassword"
  }


/collect [POST]
Add stamp to user collection
Input:
  {
    "username": "foo",
    "key": "stamp_key",
  }


/authenicate
Authenticate user
Input:
  {
    "username": "foo",
    "password": "foopassword",
  }



/stamp/<key> [GET, POST]
Return stamp information
Output:
  {
    "image_url": "/url/to/stamp/imaage.jpg",
    "name": "stamp name",
    "short_description": "blah",
    "description": "blah",
    "url": "/url/to/get/more/info/can/be/empty",
    "success": True
  }


/user/<username>
Get user information and stamps
Output:
  {
    "username": "foo",
    "success": True
    "stamps": [
      {
        "image_url": "/url/to/stamp/imaage.jpg",
        "name": "stamp name",
        "short_description": "blah",
        "description": "blah",
        "url": "/url/to/get/more/info/can/be/empty",
        "collected_at": "2014-08-30T17:26:18.031033"
      }, ...
    ]
  }
