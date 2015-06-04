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

###Delete a group

```
curl -X DELETE http://localhost:5003/titles/dn100/groups/0
```

###Amend a group

```
curl -X POST -d '{"group_id":"76","category":"ZVCF","entries":[{"entry_id":"498","full_text":"fly"},{"entry_id":"233","full_text":"bug"}]}' -H "Content-Type: application/json" http://localhost:5003/titles/dn100/groups/1
```



##Tests

install requirements_test.txt and run

```
source test.sh
```
