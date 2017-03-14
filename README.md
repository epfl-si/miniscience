# MiniScience > README

## Overview

### What is this repository for?

...

### How do I get set up? ###

...

### How do I check that everything went well ?

...

## Description

## Objectives

...

## Specifications

...

## Ratings

### How do I rate the application ?

...

### miniscience module
Pylint score: 9.60/10

### publications module
Pylint score: 6.79/10

(c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2017

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