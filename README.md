
git repogistory pull

```
$git clone {this repo}
```

docker build 

```
$ docker build -t python-buha .
```

docker run 

```
$ docker run python-buha
```

idle check

```
$ vmstat -n 10 | awk '{now=strftime("%m/%d/%Y%T"); printf("%s %s\n", now, $0); fflush();}'


exmaple 
$ vmstat -n 10 | awk '{now=strftime("%m/%d/%Y%T"); printf("%s %s\n", now, $0); fflush();}' > {YYYYMMDD}_{Server}.txt
```

