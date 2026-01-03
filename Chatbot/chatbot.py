from .decision import process_message


def chatbot_responses(msg):
    return process_message(msg, user_id="default")

