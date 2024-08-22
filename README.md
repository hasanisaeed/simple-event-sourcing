# Event Sourcing with FastAPI, PostgreSQL, and Redis

This project demonstrates a simple implementation of event sourcing using FastAPI, PostgreSQL as the event store, and Redis for event handling between the producer and consumer.

## Project Structure

- **`main.py`**: Core of the application, setting up FastAPI and database configuration.
- **`producer.py`**: Module for creating events and publishing them to the Event Bus.
- **`consumer.py`**: Module for listening to the Event Bus and processing incoming events.
- **`materialized_view.sql`**: SQL file to create the materialized view in PostgreSQL.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-repo/event-sourcing-project.git
    cd event-sourcing-project
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your PostgreSQL database and apply the `materialized_view.sql` script:

    ```bash
    psql -U <username> -d <database> -f materialized_view.sql
    ```

4. Run the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

5. Start the event consumer in a separate terminal:

    ```bash
    python consumer.py
    ```

## Usage

To produce events (e.g., deposits or withdrawals), use the `/event/` endpoint in FastAPI. The consumer will automatically process events and update the materialized view.

