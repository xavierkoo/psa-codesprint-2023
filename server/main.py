from fastapi import FastAPI, HTTPException
from database import init_db
from pydantic import BaseModel
import models
import openai
import os

app = FastAPI()


@app.on_event("startup")
def on_startup():
    """
    The `on_startup` function is called when the application starts up and it initializes the database.
    """
    init_db()


@app.get("/")
async def root():
    return {"message": "The API has started successfully"}

class prompt(BaseModel):
    content: str
@app.post("/api/safe")
async def get_activities(prompt: prompt):
    openai.api_key = os.environ["OPENAI_API_KEY"]
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role":"user","content":prompt.content}
        ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content
class OpenAIRequest(BaseModel):
    content: str

@app.post("/generate_chat")
async def generate_chat(openai_request: OpenAIRequest):
    try:
        # Set the OpenAI API key from the request
        openai.api_key = os.environ["OPENAI_API_KEY"]
        # Create the chat completion
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
{
  "role": "system",
  "content": "Our system allows users to input their job interests and job requirements, encompassing both technical and soft skill descriptions. Your primary responsibility is to assess the user's job_fit and offer valuable recommendations for technical_skills_recommendations, soft_skills_recommendations, and provide a personalise_career_roadmap. Please return a JSON Object structured as follows: { job_fit: 'highly suitable/ suitable/ just right/ not suitable', technical_skills_recommendations: [ 'NA' ], soft_skills_recommendations: [ 'NA'], personalise_career_roadmap: ['NA']}. Ensure that you include your recommendations for each corresponding key."
},
                 
                {"role": "user", "content":openai_request.content }
            ]
        )

        # Extract and return the response message
        response_message = completion.choices[0].message["content"]
        print(response_message)
        return response_message
    except Exception as e:
        raise HTTPException(status_code=500, detail=str("hello world " + e ))
