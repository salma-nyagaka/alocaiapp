[![Build Status](https://app.travis-ci.com/salma-nyagaka/alocaiapp.svg?branch=develop)](https://app.travis-ci.com/salma-nyagaka/alocaiapp)
[![Coverage Status](https://coveralls.io/repos/github/salma-nyagaka/alocaiapp/badge.svg?branch=develop)](https://coveralls.io/github/salma-nyagaka/alocaiapp?branch=develop)


## Alocai backend recruitment task
A Video Game  application

### Description
A Django web application that ....


### Development set up

-   Check that python 3 is installed:

    ```
    python --version
    >> Python 3.7.10
    ```

-   Check that Docker is installed:

    ```
    python --version
    >> Docker  20.10.12
    ```

-   Clone the repo and cd into it:

    ```
    git clone https://github.com/salma-nyagaka/alocaiapp
    ```

- Access the project

    ```
    cd alocaiapp/alocai
    ```

-   Run Docker to install dependancies and start the project:

    ```
    docker-compose up
    ```
 

 #### Endpoints
| REQUEST | DESCRIPTION  | URL  |
| :-----: | :-: | :-: |
| GET | Get DB connection status |  http://{{BASE_URL}}}}/api/v1/status |
| GET | Get DB connection status |  http://{{BASE_URL}}}}/api/v1/status |
| GET | Get documentation|  http://{{BASE_URL}}}}/docs |
| GET | Get games|  http://{{BASE_URL}}}}/api/v1/games |
