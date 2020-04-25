# Weasyprint Server

HTTP API for [Weasyprint] to generate PDF and PNG out of HTML (using [Flask]).

## tl;dr

Start the Weasyprint Docker container in a terminal and expose the service on a _http://localhost:5000_:

    $ docker run -p 5000:5000 dimw/weasyprint

For PDF generation run a following _curl_ command, pass HTML a s part of JSON request (_html_ attribute), and define a desired output file (_wasyprint-test.pdf_):
    
    $ curl \
        -X POST http://localhost:5000/render \
        -H "Content-Type: application/json" \
        -d '{"html": "<html><body><h1>Hi!</h1></body></html>"}' \
        --output weasyprint-test.pdf

To switch to PNG generation the optional _outputFormat_ attribute passed must be "_png_":

    $ curl \
        -X POST http://localhost:5000/render \
        -H "Content-Type: application/json" \
        -d '{"html": "<html><body><h1>Hi!</h1></body></html>", "outputFormat": "png"}' \
        --output weasyprint-test.png

**Hint:** Please refrain of exposing the built-in Flask development server in the container directly to the 
public and read how to "[Run with a Production Server](https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/#run-with-a-production-server)"
in the Flask documentation.

## Endpoints

### Heath Check

The endpoint might be used for a simple health check of the application. 

Request:
    
    GET /healthcheck

Response:

    OK


### Render

This endpoint is used for generation of PDF or PNG out of HTML.

Request:

    POST /render
    Content-Type: application/json
    
    {
      "html": "<html>...</html>",
      "outputFormat": "pdf"
    }

Response:

    <<Binary content (PDF or PNG)>>

## How to Develop

For local development and testing of the Weasyprint server Docker Compose can be used. 
The service can be started in the development (debug) mode and exposed on _http://localhost:5000_ 
by running the following command:

    $ docker-compose up

The debug mode enables live reload of the endpoints defined in _./app/server.py_.  

## Run Rests

The following command can be used to execute the tests:

    $ docker-compose run weasyprint /app/run-tests.sh

## Licence

The content of this repository is under the MIT licence.

[Weasyprint]: https://weasyprint.org/
[Flask]: https://flask.palletsprojects.com/en/1.1.x/
