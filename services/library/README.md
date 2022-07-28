# Library Service
Feature:
- List All Light Novel

GET http://192.168.158.254:8000/api/library/

RESPONSE
``` json
{
    "status": "success",
    "data": [
        {
            "id": 6,
            "title": "86 -eightysix-"
        },
        .
        .
        .
        {
            "id": 80,
            "title": "The Girl Who Was Supposed to Confess Her Love to Me as a Punishment Game, But No Matter How You Look at It, She’s in Love With Me!"
        }
    ]
}
```
- Get Light Novel Detail

GET http://192.168.158.254:8000/api/lightnovel/detail/1/
```json
{
    "status": "success",
    "data": {
        "id": 1,
        "title": "Gakusen Toshi Asterisk",
        "description": "In the previous century, an 
        .
        .
        .
        by some of the most talented Genestella on the planet.",
        "status": null,
        "verif": 1
    }
}

```
- Search Light Novel using Title

GET http://192.168.158.254:8000/api/library/search/title/Absolute Duo/

RESPONSE
```json
{
    "status": "success",
    "data": {
        "id": 8,
        "title": "Absolute Duo",
        "description": "Individuals who can materialize weapons from their soul are called \"Blazers,\" and  
        .
        .
        .
         of a foreign student named Julie Sigtuna.\n\n[Written by MAL Rewrite]",
        "status": null,
        "verif": 1
    }
}
```