# Testing sync libraries in async context within fastapi

## Run benchmarks

Task have to performed one at a time. I don't know how to do this with locust so I've just been commenting the tasks and running only one task.

Launch sleepy server
```sh
fastapi run --workers 8 sleepy.py
```

Launch main server
```sh
fastapi run --workers 2 --port 8001 main.py
```

Go to localhost:8089 and run the benchmark
