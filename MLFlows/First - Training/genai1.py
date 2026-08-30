from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import mlflow


mlflow.set_experiment('GenAI First experiment')
mlflow.set_tracking_uri("http://127.0.0.1:5000/")


mlflow.openai.autolog()

client = OpenAI()
resp = client.chat.completions.create(
    model = 'o4-mini',
    messages = [
        {'role':'system', 'content': 'You are helpful enviormental assistant'},
        {'role':'user', 'content': 'How to clean the river banks'},
    ],
)
print(resp)