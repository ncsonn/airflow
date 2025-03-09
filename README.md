# Apache Airflow: LocalExecutor

Apache Airflow deployment using Docker Compose.

## Prerequisites

- Docker & Docker Compose installed on your machine
- Minimum 4GB of RAM

## Deployment

1. **Clone the repository:**

    ```sh
    git clone https://github.com/ncsonn/airflow.git
    cd airflow
    ```

2. **Configure Environment:**

    Create an `.env` file to configure Airflow:

    ```sh
    AIRFLOW_UID=50000

    _AIRFLOW_WWW_USER_USERNAME=airflow
    _AIRFLOW_WWW_USER_PASSWORD=airflow

    POSTGRES_USER=airflow
    POSTGRES_PASSWORD=airflow
    POSTGRES_DB=airflow
    ```

3. **Start Airflow services:**

    ```sh
    docker-compose up -d
    ```

4. **Access Airflow web interface:**

    Open your web browser and go to `http://localhost:8080`.

## Stopping the Services

To stop the services, run:

```sh
docker-compose down
```

## Cleaning Up

To remove all containers, networks, and volumes, run:

```sh
docker-compose down --volumes --remove-orphans
```
