from google import genai

# Configure Gemini Client
client = genai.Client(
    api_key=""
)


def planner_agent(project_idea):

    prompt = f"""
    You are a senior AI software architect.

    Create a complete MVP execution plan for:
    {project_idea}

    Include:
    - problem statement
    - target users
    - core features
    - frontend requirements
    - backend requirements
    - recommended tech stack
    - database requirements
    - API requirements
    - MVP roadmap
    - user workflow

    Keep it startup-focused and practical.
    """

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"""
Planner Agent Error

Reason:
{str(e)}

Fallback MVP Plan:

Project Idea:
{project_idea}

Core Features:
- User authentication
- Dashboard
- AI-powered analysis
- File upload support
- Backend API integration

Recommended Stack:
- Frontend: React
- Backend: FastAPI
- Database: PostgreSQL
- AI Model: Gemini API

Workflow:
User → Upload/Input → AI Processing → Results Dashboard
"""


if __name__ == "__main__":

    idea = input("Enter your app idea: ")

    result = planner_agent(idea)

    print("\nGenerated MVP Plan:\n")

    print(result)
