class Constants:
    EXPECTED_STATUS_CODE = 200

    schema_for_dog_list_all_breeds = {
        "description": "example schema",
        "type": "object",
        "properties": {
            "message": {"type": "object"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }

    schema_for_dog_random_image = {
        "description": "example schema",
        "type": "object",
        "properties": {
            "message": {"type": "array"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }

    schema_for_dog_by_breed = {
        "description": "example schema",
        "type": "object",
        "properties": {
            "message": {"type": "array"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }

    schema_for_bred_hound_list = {
        "description": "example schema",
        "type": "object",
        "properties": {
            "message": {"type": "array"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }

    schema_for_specific_breed_images_random = {
        "description": "example schema",
        "type": "object",
        "properties": {
            "message": {"type": "string"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }
