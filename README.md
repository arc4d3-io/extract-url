# URL-EXTRACT-API Documentation

This project is a API-URL-EXTRACT that provides functionality to extract links and text content from a given URL. It includes automatic generation of Swagger documentation.

## Getting Started

These instructions will guide you on how to run this project on your local machine for development and testing purposes.

### Prerequisites

You need Python 3.6+ to run this project. You can download it from [here](https://www.python.org/downloads/).

You also need Flask, Flask-Swagger, Flask-Swagger-UI, BeautifulSoup, requests, and other dependencies of this project. They can be installed via pip.

```
pip install -r requirements.txt
```

### Installing

First, clone the repository to your local machine.

```
git clone https://github.com/<your-github-username>/api-url-extract.git
```

Navigate to the project directory.

```
cd api-url-extract
```

Install the required packages.

```
pip install -r requirements.txt
```

Run the application.

```
python3 app.py
```

The application should be up and running at [http://localhost:5000](http://localhost:5000).

For Swagger UI, navigate to [http://localhost:5000/api/swagger](http://localhost:5000/api/swagger).

## API Endpoints

The application has the following endpoints:

- `GET /api/extract-links?url=<URL>`: Extracts all the links from the provided URL.
- `GET /api/extract-text?url=<URL>`: Extracts all the text content from the provided URL.

In both endpoints, replace `<URL>` with the URL from which you want to extract the content.

## About ContentModel Class

The `ContentModel` class is responsible for fetching the content of the provided URL and extracting links and text from it.

It uses the `requests` library to send an HTTP request to the provided URL and `BeautifulSoup` to parse the response. It also uses regular expressions to clean the extracted text and the `validators` library to validate the extracted URLs.

## Running the Tests

Explain how to run the automated tests for this system.

## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [Swagger](https://swagger.io/) - API Documentation
* [Flask-Swagger](https://flask-swagger.readthedocs.io/en/latest/) - Flask extension to help with Swagger docs
* [Flask-Swagger-UI](https://flask-swagger-ui.readthedocs.io/en/latest/) - Flask extension for Swagger UI
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Library for parsing HTML and XML documents
* [Requests](https://docs.python-requests.org/en/latest/) - HTTP library for Python

## Authors

* **Your Name** - *Initial work* - [YourName](https://github.com/yourusername)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

Remember to replace placeholders like `<your-github-username>`, `YourName`, and other relevant parts with your actual information.
