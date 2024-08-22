import redis

r = redis.Redis()


@app.post("/event/")
def create_event(user_id: int, event_type: str, amount: float):
    # (Event Store) -> Save an event into database
    db = SessionLocal()
    new_event = Event(user_id=user_id, event_type=event_type, amount=amount)
    db.add(new_event)
    db.commit()

    # send event to the Event Bus
    event_data = {
        "user_id": user_id,
        "event_type": event_type,
        "amount": amount
    }
    r.publish("event_channel", str(event_data))

    return {"message": "Event created and published", "event": event_data}
