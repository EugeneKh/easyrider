schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "type": "object",
    "properties": {
        "bus_id": {
            "type": "integer"
        },
        "stop_id": {
            "type": "integer",
        },
        "stop_name": {
            "type": "string",
            "minLength": 1,
            "pattern": r"^([A-Z][a-z]* )+(Road|Street|Boulevard|Avenue)$"
        },
        "next_stop": {
            "type": "integer"
        },
        "stop_type": {
            # "type": "string",
            "enum": ["S", "O", "F", ""],
            # "maxLength": 1,
        },
        "a_time": {
            "type": "string",
            "pattern": r"^([0-1][0-9]|2[0-3]):[0-5][0-9]$"
        },
    }
}

fileds = {
    # "bus_id": 0,
    # "stop_id": 0,
    "stop_name": 0,
    # "next_stop": 0,
    "stop_type": 0,
    "a_time": 0}
