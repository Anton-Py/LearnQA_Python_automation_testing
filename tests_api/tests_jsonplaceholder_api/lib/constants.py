class Constants:
    EXPECTED_STATUS_CODE_GET = 200
    EXPECTED_STATUS_CODE_POST = 201

    schema_for_jsonplaceholder_getting_resource = {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"},
        },
        "required": ["userId", "id", "title", "body"]
    }

    schema_for_jsonplaceholder_creating_resource = {
        "type": "object",
        "properties": {
            "userId0": {"type": "string"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"},
        },
        "required": ["userId0", "id", "title", "body"]
    }

    schema_for_jsonplaceholder_updating_resource = {
        "type": "object",
        "properties": {
            "userId0": {"type": "string"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"},
        },
        "required": ["userId0", "id", "title", "body"]
    }

    schema_for_jsonplaceholder_delete_resource = {
        "type": "object"
    }

    schema_for_jsonplaceholder_comments = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "array",
        "items": [
            {
                "type": "object",
                "properties": {
                    "postId": {"type": "integer"},
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "email": {"type": "string"},
                    "body": {"type": "string"},
                },
                "required": ["postId", "id", "email", "body"]
            }
        ]
    }
