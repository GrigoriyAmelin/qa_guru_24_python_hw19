from schemas.get_clubs_reviews_response_schemas import unexisting_review_response_schema

response_schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Generated Schema",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "club": {
            "type": "integer"
        },
        "user": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "username": {
                    "type": "string"
                }
            },
            "required": [
                "id",
                "username"
            ]
        },
        "review": {
            "type": "string"
        },
        "assessment": {
            "type": "integer"
        },
        "readPages": {
            "type": "integer"
        },
        "created": {
            "type": "string",
            "format": "date-time"
        },
        "modified": {
            "type": "null"
        }
    },
    "required": [
        "id",
        "club",
        "user",
        "review",
        "assessment",
        "readPages",
        "created"
    ]
}

unexisting_review_response_schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Generated Schema",
    "type": "object",
    "properties": {
        "detail": {
            "type": "string"
        }
    },
    "required": [
        "detail"
    ]
}