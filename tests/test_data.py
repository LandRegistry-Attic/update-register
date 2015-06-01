import json

# This is the target of the unit tests.
TARGET = {
    "groups": [
        {
            "group_id": "12",
            "category": "ABCD",
            "entries": [
                {
                    "entry_id": "998",
                    "full_text": "foo"
                },
                {
                    "entry_id": "999",
                    "full_text": "bar"
                }
            ]
        },
        {
            "group_id": "22",
            "category": "EFGH",
            "entries": [
                {
                    "entry_id": "999",
                    "full_text": "cat"
                },
                {
                    "entry_id": "998",
                    "full_text": "mat"
                }
            ]
        }
    ]
}

TITLE_WITH_AMENDED_ENTRY = {
    "groups": [
        {
            "group_id": "12",
            "category": "ABCD",
            "entries": [
                {
                    "entry_id": "998",
                    "full_text": "foo"
                },
                {
                    "entry_id": "999",
                    "full_text": "bar"
                }
            ]
        },
        {
            "group_id": "22",
            "category": "EFGH",
            "entries": [
                {
                    "entry_id": "999",
                    "full_text": "cat"
                },
                {
                    "entry_id": "998",
                    "full_text": "dog"
                }
            ]
        }
    ]
}

# dump this to string to fire at http
ENTRY_AMENDMENT = json.dumps({
    "entry_id": "998",
    "full_text": "dog"
})

