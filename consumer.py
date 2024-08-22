import json
from sqlalchemy import text


# consume Event Bus
def consume_event():
    pubsub = r.pubsub()
    pubsub.subscribe("event_channel")

    for message in pubsub.listen():
        if message['type'] == 'message':
            event_data = json.loads(message['data'].decode('utf-8'))
            user_id = event_data['user_id']
            event_type = event_data['event_type']
            amount = event_data['amount']

            print(f"Processing event for user {user_id}, type {event_type}, amount {amount}")

            # refresh Materialized View
            update_materialized_view()


def update_materialized_view():
    db = SessionLocal()
    db.execute(text("REFRESH MATERIALIZED VIEW user_balance;"))
    db.commit()
    print("Materialized view updated.")


if __name__ == "__main__":
    consume_event()
