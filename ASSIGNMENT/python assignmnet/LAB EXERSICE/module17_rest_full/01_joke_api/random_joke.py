import requests

def get_random_joke():
    """Fetch a random joke from a public API and return setup & punchline.

    This uses the Official Joke API.
    """
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data.get("setup"), data.get("punchline")

if __name__ == "__main__":
    try:
        setup, punchline = get_random_joke()
        print("Here is your random joke:")
        print(setup)
        print(punchline)
    except Exception as e:
        print("Error while fetching joke:", e)
