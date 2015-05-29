#Update register

At the moment this is a spike to see how entries on the system of record can be created updated and deleted.

##how to run.

For now, python run.py.  

This will work in the devenv-casework environment is th following is added to the yaml.

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
curl -X POST -d '{"a":"1"}' -H "Content-Type: application/json" http://localhost:5003/titles/dn100/groups/1/entries/1
```
