response_schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Generated Schema",
    "type": "object",
    "properties": {
        "count": {
            "type": "integer"
        },
        "next": {
            "type": "null"
        },
        "previous": {
            "type": "null"
        },
        "results": {
            "type": "array",
            "items": {
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
        }
    },
    "required": [
        "count",
        "results"
    ]
}

all_reviews_response_schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Generated Schema",
    "type": "object",
    "properties": {
        "count": {
            "type": "integer"
        },
        "next": {
            "type": ["string", "null"]
        },
        "previous": {
            "type": "null"
        },
        "results": {
            "type": "array",
            "items": {
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
                        "type": ["string", "null"],
                        "format": "date-time"
                    }
                },
                "required": [
                    "id",
                    "club",
                    "user",
                    "review",
                    "assessment",
                    "readPages",
                    "created",
                    "modified"
                ]
            }
        }
    },
    "required": [
        "count",
        "results"
    ]
}

unexisting_review_response_schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Generated Schema",
    "type": "object",
    "properties": {
        "count": {
            "type": "integer"
        },
        "next": {
            "type": "null"
        },
        "previous": {
            "type": "null"
        },
        "results": {
            "type": "array",
            "items": {
                "type": "object"
            }
        }
    },
    "required": [
        "count",
        "results"
    ]
}