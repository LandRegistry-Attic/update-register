#Update register

At the moment this is a spike to see how entries on the system of record can be created updated and deleted.

##how to run.

For now, python run.py.  

This will work in the devenv-casework environment is the following is added to the yaml.

```
    update-register:
    repo: https://github.com/LandRegistry/update-register.git
    branch: master
    port: 5003
    entrypoint: application:app
    vars:
```

##Migrate tables
From with the virtual machine you need to Export the environment variable to connect
to the database.

```
export SQLALCHEMY_DATABASE_URI="postgresql://workingregister:workingregister@localhost/workingregister"
```

Then run the command to upgrade the tables

```
python manage.py db upgrade
```

Ideally this would be scripted as part of the vagrant up (find a way to add to lr-setup-apps)

##Curls

###Amend an entry

```
curl -X POST -d '{"entry_id": "998","full_text": "dog"}' -H "Content-Type: application/json" http://localhost:5003/titles/dn100/groups/1/entries/1
```

###Insert an entry

```
curl -X PUT -d '{"entry_id": "998","full_text": "dog"}' -H "Content-Type: application/json" http://localhost:5003/titles/dn100/groups/1/entries
```

###Delete an entry

```
curl -X DELETE http://localhost:5003/titles/dn100/groups/1/entries/0
```

###Insert a group

```
curl -X PUT -d '{"group_id":"76","category":"ZVCF","entries":[{"entry_id":"498","full_text":"fly"},{"entry_id":"233","full_text":"bug"}]}' -H "Content-Type: application/json" http://localhost:5003/titles/dn100/groups
```


###Delete a group

```
curl -X DELETE http://localhost:5003/titles/dn100/groups/0
```

###Amend a group

```
curl -X POST -d '{"group_id":"76","category":"ZVCF","entries":[{"entry_id":"498","full_text":"fly"},{"entry_id":"233","full_text":"bug"}]}' -H "Content-Type: application/json" http://localhost:5003/titles/dn100/groups/1
```

###Start a new version of a title (work in progress).  Creates test data at the moment.

```
curl -X POST -d '{"application_reference": "testabr", "title_number": "tt12345"}' -H "Content-Type: application/json" http://localhost:5003/start
```


##Tests

install requirements_test.txt and run

```
source test.sh
```

##Todo

- Change service so that it updates working register - rather than add a new row.
- Ensure that only one row exists for a title number / abr combo (see SoR for example).
- Each amended entry needs to be flagged as such.


