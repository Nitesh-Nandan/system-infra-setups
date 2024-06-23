# Creating docker-image from docker file 

```commandline
docker build -t <image_name>:<tag> .

docker build -t cli:1.0 .

docker exec -it docker-cli-cli-1 /bin/bash
```


# mysql-cli

```commandline
mysql -u root -h mysql-db-1 -p < id-generator-schema.sql
```

