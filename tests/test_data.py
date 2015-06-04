import json

# This is the target of the unit tests.  Read only getter function, so that it can't be modified.
def get_target_json():
    return {
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

TITLE_WITH_INSERTED_ENTRY = {
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
                },
                {
                    "entry_id": "709",
                    "full_text": "cow"
                }
            ]
        }
    ]
}

TITLE_WITH_DELETED_ENTRY = {
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
                    "entry_id": "998",
                    "full_text": "mat"
                }
            ]
        }
    ]
}

TITLE_WITH_INSERTED_EMPTY_GROUP = {
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
        },
        {
            "group_id": "76",
            "category": "ZVCF",
            "entries": [
            ]
        }
    ]
}

TITLE_WITH_DELETED_GROUP = {
    "groups": [
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

TITLE_WITH_REPLACED_GROUP = {
    "groups": [
        {
            "group_id": "76",
            "category": "ZVCF",
            "entries": [
                {
                    "entry_id": "498",
                    "full_text": "fly"
                },
                {
                    "entry_id": "233",
                    "full_text": "bug"
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

# dump these json arguments to string to fire at http
ENTRY_AMENDMENT = json.dumps({
    "entry_id": "998",
    "full_text": "dog"
})

ENTRY_INSERT = json.dumps({
    "entry_id": "709",
    "full_text": "cow"
})

GROUP_INSERT = json.dumps({
    "group_id": "76",
    "category": "ZVCF",
    "entries": []
})

GROUP_REPLACE = json.dumps({
    "group_id": "76",
    "category": "ZVCF",
    "entries": [
        {
            "entry_id": "498",
            "full_text": "fly"
        },
        {
            "entry_id": "233",
            "full_text": "bug"
        }
    ]
})
