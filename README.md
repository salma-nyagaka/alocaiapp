[![Build Status](https://app.travis-ci.com/salma-nyagaka/alocaiapp.svg?branch=develop)](https://app.travis-ci.com/salma-nyagaka/alocaiapp)
[![Coverage Status](https://coveralls.io/repos/github/salma-nyagaka/alocaiapp/badge.svg?branch=develop)](https://coveralls.io/github/salma-nyagaka/alocaiapp?branch=develop)

## Alocai backend recruitment task
A Video Game  application

### Description
A Django web application that tests db connection, creates games and gets the highest value of games that can be store in a pen drive

### Link to the documentation
 [Documentation](http://alocai.sapplication.link/docs/)

### Development set up

-   Check that python 3 is installed:

    ```
    python --version
    >> Python 3.7.10
    ```

-   Check that Docker is installed:

    ```
    docker --version
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
 
 #### Base url
    http://alocai.sapplication.link/

 #### Endpoints
| REQUEST | DESCRIPTION  | URL  |
| :-----: | :-: | :-: |
| GET | Get DB connection status |  {{BASE_URL}}}}/api/v1/status |
| GET | Get documentation|  {{BASE_URL}}}}/docs |
| POST | Create games|  {{BASE_URL}}}}/api/v1/games |
| GET | Get game values|  {{BASE_URL}}}}/api/v1/best_value_games?pen_drive_space={POSITIVE_INTEGER} |

