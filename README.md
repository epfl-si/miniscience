# MiniScience > README
[![Travis built status](https://travis-ci.org/ffy/miniscience.svg?branch=master)](https://travis-ci.org/ffy/miniscience)

## Overview

### What is this repository for?

Create a publication cluster factory: from import to presentation to the author, all through microservices and APIs.

### How do I get set up? ###

Either with Docker

```
make docker-init
```

Or without

```
make init run
```

### How do I check that everything went well ?

Either go to [localhost](http://localhost:8000)

Or (if the server runs localy) run the test

```
python manage.py test
```

## Description

## Objectives

Base repo for microservices that will suppor the factory-chain to create cluster of publications.

## Specifications

See [Trello board](https://trello.com/b/3Mq7J5sK/publichain)

## Ratings

### How do I rate the application ?

Install pylint first (```pip install pylint```), and run

```
pylint miniscience publications
...
Your code has been rated at 1.78/10
```

## API documentation

### Authors

#### Show all authors

URL: /api/authors  
Method: GET  
URL params: None  
Data params: None  
Response Codes: Success (200 OK)

#### Show an author

URL: /api/authors/:id  
Method: GET  
URL params: id=[integer]  
Data params: None  
Response Codes: Success (200 OK), Failure (404 Not Found)

#### Add an author

URL: /api/authors  
Method: POST  
URL params: None  
Data params:

    {
      "first_name": "First name",
      "last_name": "Last name",
      "email": "name@provider.com"
    }
    
Response Codes: Success (201 Created)

#### Edit an author

URL: /api/authors/:id  
Method: PUT  
URL params: id=[integer]  
Data params:

    {
      "first_name": "First name",
      "last_name": "Last name",
      "email": "name@provider.com"
    }
    
Response Codes: Success (201 Created)

#### Delete an author

URL: /api/authors/:id  
Method: DELETE  
URL params: id=[integer]  
Data params: None  
Response Codes: Success (204 No Content)

### Publications

#### Show all publications

URL: /api/publications  
Method: GET  
URL params: None  
Data params: None  
Response Codes: Success (200 OK)

#### Show a publication

URL: /api/publications/:id  
Method: GET  
URL params: id=[integer]  
Data params: None  
Response Codes: Success (200 OK), Failure (404 Not Found)

#### Add a publication

URL: /api/publications  
Method: POST  

URL params: None  
Data params:

    {
        "title": "Title",
        "pub_date": "YYYY-mm-dd",
        "author": [
            "http://127.0.0.1:8000/publications/api/authors/<id>/",
            "http://127.0.0.1:8000/publications/api/authors/<id>/"
        ]
    }
    
Response Codes: Success (201 Created)

#### Edit a publication

URL: /api/publications/:id  
Method: PUT  
URL params: id=[integer]  
Data params:

    {
        "title": "Title",
        "pub_date": "YYYY-mm-dd",
        "author": [
            "http://127.0.0.1:8000/publications/api/authors/<id>/",
            "http://127.0.0.1:8000/publications/api/authors/<id>/"
        ]
    }
    
Response Codes: Success (201 Created)

#### Delete a publication

URL: /api/authors/:id  
Method: DELETE  
URL params: id=[integer]  
Data params: None  
Response Codes: Success (204 No Content)

### Relations

### Get publications of an author

URL: /api/authors/:id/publications  
Method: GET  
URL params: id=[integer]  
Data params: None  
Response Codes: Success (200 OK), Failure (404 Not Found)

### Add publication to an author

URL: /api/authors/:id/publications  
Method: POST  
URL params: id=[integer]  
Data params:

    {
        "title": "Title",
        "pub_date": "YYYY-mm-dd"
    }

Response Codes: Success (200 OK), Failure (404 Not Found)

#### Delete relation between an author and a publication

URL: /api/authors/:id_author/publications/:id_publication  
Method: GET  
URL params: id_author=[integer], id_publication=[integer]  
Data params: None  
Response Codes: Success (200 OK), Failure (404 Not Found)

(c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2017