import requests
import asyncio
import json

url = "https://opentdb.com/api.php?amount=10&type=boolean"

question_data = []

async def get_question_bank():
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()["results"]
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

async def main():

    question_bank = await get_question_bank()

    if question_bank:
        question_data.extend(question_bank)
    else:
        print("Failed to retrieve triva questions.")


asyncio.run(main())
