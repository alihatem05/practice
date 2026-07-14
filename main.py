from fastapi import FastAPI
import os

app = FastAPI()

COUNTER_FILE = "counter.txt"


def get_count():
    if not os.path.exists(COUNTER_FILE):
        return 0

    with open(COUNTER_FILE, "r") as f:
        return int(f.read())


def save_count(count):
    with open(COUNTER_FILE, "w") as f:
        f.write(str(count))


@app.get("/")
def home():
    count = get_count() + 1
    save_count(count)

    return {
        "visits": count
    }