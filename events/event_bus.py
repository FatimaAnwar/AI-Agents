import json
import redis


class EventBus:
    """Responsible only for publishing and subscribing to events."""

    def __init__(self):
        self.redis = redis.Redis(
            host="localhost",
            port=6379,
            decode_responses=True
        )

    def publish(self, event_type, data):
        event = {
            "type": event_type,
            "data": data
        }

        self.redis.publish(
            "cooking_events",
            json.dumps(event)
        )