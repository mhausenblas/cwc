# Coding with containers

## Running it locally

For local execution, Python `2.7.9` is required. You can then run `cwc` like so:

```
$ python cwc.py
```

If you fancy it you can run the containerized version of `cwc` on your local machine
which requires Docker being installed:

```
$ docker build -t "someuser/cwc:latest" .
$ docker run -P someuser/cwc:latest
```

## Invoking it

Once `cwc` is running you can invoke it like so (note that what is shown below is baed on a local service execution):

```
$ http localhost:9876/info
HTTP/1.1 200 OK
Content-Length: 61
Content-Type: application/json
Date: Mon, 22 May 2017 04:03:42 GMT
Etag: "3346244497b445fa61546cb911f578ece9408a18"
Server: TornadoServer/4.3

{
    "request_from": "127.0.0.1",
    "running_on": "localhost:9876"
}
```

And the output would then be something like:

```
$ python cwc.py
2017-05-22T02:03:25 INFO This is the CWC service in version v0.1 listening on port 9876 [at line 85]
2017-05-22T02:03:42 INFO /info serving from localhost:9876 has been invoked from 127.0.0.1 [at line 66]
2017-05-22T02:03:42 INFO 200 GET /info (127.0.0.1) 0.65ms [at line 1946]
...
```
