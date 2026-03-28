get_clubs_response_schema = {
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
                    "bookTitle": {
                        "type": "string"
                    },
                    "bookAuthors": {
                        "type": "string"
                    },
                    "publicationYear": {
                        "type": "integer"
                    },
                    "description": {
                        "type": "string"
                    },
                    "telegramChatLink": {
                        "type": "string",
                        "format": "uri"
                    },
                    "owner": {
                        "type": "integer"
                    },
                    "members": {
                        "type": "array",
                        "items": {
                            "type": "integer"
                        }
                    },
                    "reviews": {
                        "type": "array",
                        "items": {
                            "type": "object"
                        }
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
                    "bookTitle",
                    "bookAuthors",
                    "publicationYear",
                    "description",
                    "telegramChatLink",
                    "owner",
                    "members",
                    "reviews",
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

get_clubs_page_length_response_schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Generated Schema",
    "type": "object",
    "properties": {
        "count": {
            "type": "integer"
        },
        "next": {
            "type": "string",
            "format": "uri"
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
                    "bookTitle": {
                        "type": "string"
                    },
                    "bookAuthors": {
                        "type": "string"
                    },
                    "publicationYear": {
                        "type": "integer"
                    },
                    "description": {
                        "type": "string"
                    },
                    "telegramChatLink": {
                        "type": "string",
                        "format": "uri"
                    },
                    "owner": {
                        "type": "integer"
                    },
                    "members": {
                        "type": "array",
                        "items": {
                            "type": "integer"
                        }
                    },
                    "reviews": {
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
                    "bookTitle",
                    "bookAuthors",
                    "publicationYear",
                    "description",
                    "telegramChatLink",
                    "owner",
                    "members",
                    "reviews",
                    "created"
                ]
            }
        }
    },
    "required": [
        "count",
        "next",
        "results"
    ]
}

get_clubs_unexisting_page_response_schema = {
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