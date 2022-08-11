class Constants:
    EXPECTED_STATUS_CODE = 200

    schema_for_breweries = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "array",
        "items": [
            {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "brewery_type": {"type": "string"},
                    "city": {"type": "string"},
                    "postal_code": {"type": "string"},
                    "country": {"type": "string"},
                    "phone": {"type": "string"},
                    "updated_at": {"type": "string"},
                    "created_at": {"type": "string"}
                },
                "required": ["id", "name", "brewery_type", "city", "postal_code", "country", "phone", "updated_at",
                             "created_at"]
            }
        ]
    }

    CITY_DICT = {"san_diego": "San Diego", "new_york": "New York", "chicago": "Chicago", "washington": "Washington"}
    STATE_DICT = {"new_york": "New York", "Idaho": "Idaho", "alabama": "Alabama"}
    TYPE_DICT = {"closed": "closed", "bar": "bar", "large": "large", "nano": "nano"}
