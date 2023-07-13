import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

import time

# article


# split
# def processor(article: str):
#     """
#     we will split a 1000 words article into 4 (300+300+300+100)

#     upon sending the next article to rewrite , send 150 words from the previous article (150+300=450) and then send it to rewrite.
#     then join it with previous rewritten article but first  remove first 150 words prior

#     repeat this process
#     """
#     words: list = article.split(" ")
#     total_words: int = words.__len__()

#     # we will split a 1000 words article into 4 (300+300+300+100)
#     first = words[:300]
#     first_joined = " ".join(first)

#     # then we will send it to rewrite

#     part: str = send(first_joined)

#     second = words[(300 - 150) : 600]
#     second_joined = " ".join(second)
#     second_draft: str = send(second_joined)
#     second_draft_splitted = second_draft.split(" ")
#     second_draft_splitted_removed_150 = second_draft_splitted[150:]
#     second_part = " ".join(second_draft_splitted_removed_150)

#     third = words[(600 - 150) :]
#     third_joined = " ".join(third)

#     third_draft = send(third_joined)
#     third_draft_splitted = third_draft.split(" ")
#     third_draft_splitted_removed_150 = third_draft_splitted[150:]
#     third_part = " ".join(third_draft_splitted_removed_150)

#     return part + second_part + third_part


def rewrite_chunk(chunk):
    draft = send(" ".join(chunk))
    return " ".join(draft.split(" ")[150:])


def processor(article: str):
    """
    we will split a 1000 words article into 4 (300+300+300+100)

    upon sending the next article to rewrite , send 150 words from the previous article (150+300=450) and then send it to rewrite.
    then join it with previous rewritten article but first  remove first 150 words prior

    repeat this process
    """
    words: list = article.split(" ")

    # Split the article into chunks and process each chunk
    rewritten_parts = []
    for i in range(0, len(words), 300):
        if i == 0:
            draft = send(" ".join(words[i : i + 300]))
            rewritten_parts.append(draft)
        time.sleep(4)
        rewritten_parts.append(rewrite_chunk(words[i - 150 : i + 300]))

    return " ".join(rewritten_parts)


# send
def send(article):
    """for sending requests to openai"""

    rewrite_instruction = "Rewrite below given article. Do not change sentence structure.Just use synonyms to rewrite it.go sentence by sentence and rewrite each sentence.the goal is to avoid Ai detection by Ai content detectors. The request article is this: \n"

    complete_prompt: str = rewrite_instruction + article

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=complete_prompt,
        temperature=0.55,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0.6,
        presence_penalty=0,
    )
    return response.choices[0].text
