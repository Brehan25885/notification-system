# Notify service
FastAPI based application to notification system, complete with tests, local deployment environment

**Swagger** /docs

### Local Development:
- Create a `.env` file in project root directory (see `.env.example` for sample)

- Create 2 mysql database and add configurations in .env 

    ```
    DB_HOST = "localhost"
    DB_USER = 
    DB_PASS = 
    DB_SCHEMA = 
    db_schema_test="test"
    ```

- create TWILIO account for sms and add config in .env

    ```
    TWILIO_ACCOUNT_SID=
    TWILIO_AUTH_TOKEN=
    TWILIO_PHONE_NUMBER=
    ```

- add smtp config in .env

    ```
    MAIL_USERNAME=
    MAIL_PASSWORD=
    MAIL_FROM=
    MAIL_PORT=587
    MAIL_SERVER=smtp.gmail.com
    MAIL_FROM_NAME=test
    ```

- add firebase server key for push notifications

    ```
        FIREBASE_API_KEY=<server key>
    ```

- Create a virtual environment.

    ```
    $ pipenv shell
    ```



    ## Run
    ```
    $ uvicorn app.main:app --reload
    ```

    ## Redis

    in a seperate terminal run 

    ```
    $ rq worker --with-scheduler --path <project path>
    ```

    in a seperate terminal run 

    ```
    $ cd redis-5.0.5
    $ src/redis-server


    ```

    ## To run tests
    ```
    $ cd app/tests
    $ pytest
    ```

