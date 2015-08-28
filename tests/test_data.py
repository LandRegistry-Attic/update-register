import json

# This is the target of the unit tests.  Read only getter function, so that it can't be modified.
def get_target_json():
    return {
        "title_number" : "dn100",
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
    "title_number" : "dn100",
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
    "title_number" : "dn100",
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
    "title_number" : "dn100",
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
    "title_number" : "dn100",
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
    "title_number" : "dn100",
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
    "title_number" : "dn100",
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

TEST_REGISTER = {
    "filed_plan_format": "PAPER",
    "edition_date": "2003-07-25",
    "last_app_timestamp": "2003-07-25T16:20:01+01:00",
    "class": "Absolute",
    "title_number": "AV239038",
    "dlr": "Gloucester Office",
    "application_reference": "F737RBF",
    "groups": [
        {
            "category": "PROPERTY",
            "entries": [
                {
                    "entry_id": "2015-02-03 12:48:29.760945",
                    "sub_register": "A",
                    "status": "Current",
                    "sequence_number": 1,
                    "role_code": "RDES",
                    "language": "ENG",
                    "category": "PROPERTY",
                    "infills": [
                        {
                            "address": {
                                "address_string": "the Incorporeal hereditaments known as The Manor or Lordship or Reputed Manor or Lordship of Littleton-upon-Severn in the former Parish of Littleton-upon-Severn",
                                "auto_uppercase_override": "true"
                            },
                            "type": "Address"
                        }
                    ],
                    "full_text": "The Freehold land being the Incorporeal hereditaments known as The Manor or Lordship or Reputed Manor or Lordship of Littleton-upon-Severn in the former Parish of Littleton-upon-Severn.",
                    "entry_date": "1994-05-25",
                    "template_text": "The Freehold land being *AD*"
                }
            ]
        },
        {
            "category": "OWNERSHIP",
            "entries": [
                {
                    "entry_id": "2015-02-03 12:48:31.495975",
                    "sub_register": "B",
                    "status": "Current",
                    "sequence_number": 1,
                    "role_code": "RPRO",
                    "language": "ENG",
                    "category": "OWNERSHIP",
                    "infills": [
                        {
                            "proprietors": [
                                {
                                    "addresses": [
                                        {
                                            "postal_county": "London",
                                            "address_string": "Flat 113, Eaton Rise, Eton College Road, London NW3 2DD",
                                            "address_type": "UK",
                                            "auto_uppercase_override": "true"
                                        }
                                    ],
                                    "name": {
                                        "surname": "HILL",
                                        "forename": "MARIE",
                                        "name_category": "PRIVATE INDIVIDUAL",
                                        "auto_uppercase_override": "true"
                                    }
                                }
                            ],
                            "type": "Proprietor"
                        }
                    ],
                    "full_text": "PROPRIETOR: %MARIE HILL% of Flat 113, Eaton Rise, Eton College Road, *London* NW3 2DD.",
                    "entry_date": "2003-07-25",
                    "template_text": "PROPRIETOR: *RP*"
                }
            ]
        }
    ],
    "geometry": {

    },
    "tenure": "Freehold",
    "raster_plan_quality": "INSUFFICIENT",
    "districts": [
        "SOUTH GLOUCESTERSHIRE"
    ]
}

TEST_REGISTER2 = {
    "filed_plan_format": "PAPER",
    "edition_date": "2003-07-25",
    "last_app_timestamp": "2003-07-25T16:20:01+01:00",
    "class": "Absolute",
    "title_number": "AV239040",
    "dlr": "Gloucester Office",
    "application_reference": "F737RBF",
    "groups": [
        {
            "category": "PROPERTY",
            "entries": [
                {
                    "entry_id": "2015-02-03 12:48:29.760945",
                    "sub_register": "A",
                    "status": "Current",
                    "sequence_number": 1,
                    "role_code": "RDES",
                    "language": "ENG",
                    "category": "PROPERTY",
                    "infills": [
                        {
                            "address": {
                                "address_string": "the Incorporeal hereditaments known as The Manor or Lordship or Reputed Manor or Lordship of Littleton-upon-Severn in the former Parish of Littleton-upon-Severn",
                                "auto_uppercase_override": "true"
                            },
                            "type": "Address"
                        }
                    ],
                    "full_text": "The Freehold land being the Incorporeal hereditaments known as The Manor or Lordship or Reputed Manor or Lordship of Littleton-upon-Severn in the former Parish of Littleton-upon-Severn.",
                    "entry_date": "1994-05-25",
                    "template_text": "The Freehold land being *AD*"
                }
            ]
        },
        {
            "category": "OWNERSHIP",
            "entries": [
                {
                    "entry_id": "2015-02-03 12:48:31.495975",
                    "sub_register": "B",
                    "status": "Current",
                    "sequence_number": 1,
                    "role_code": "RPRO",
                    "language": "ENG",
                    "category": "OWNERSHIP",
                    "infills": [
                        {
                            "proprietors": [
                                {
                                    "addresses": [
                                        {
                                            "postal_county": "London",
                                            "address_string": "Flat 113, Eaton Rise, Eton College Road, London NW3 2DD",
                                            "address_type": "UK",
                                            "auto_uppercase_override": "true"
                                        }
                                    ],
                                    "name": {
                                        "surname": "HILL",
                                        "forename": "MARIE",
                                        "name_category": "PRIVATE INDIVIDUAL",
                                        "auto_uppercase_override": "true"
                                    }
                                }
                            ],
                            "type": "Proprietor"
                        }
                    ],
                    "full_text": "PROPRIETOR: %MARIE HILL% of Flat 113, Eaton Rise, Eton College Road, *London* NW3 2DD.",
                    "entry_date": "2003-07-25",
                    "template_text": "PROPRIETOR: *RP*"
                }
            ]
        }
    ],
    "geometry": {

    },
    "tenure": "Freehold",
    "raster_plan_quality": "INSUFFICIENT",
    "districts": [
        "SOUTH GLOUCESTERSHIRE"
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

TEST_COMPLETE = json.dumps({
    "title_number": "DN93232",
    "application_ref": "H0l333"
}

)
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
