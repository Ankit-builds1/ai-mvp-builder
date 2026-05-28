from google import genai

# Configure Gemini client
client = genai.Client(api_key="")


def backend_agent(project_idea):

    prompt = f"""
    Generate a professional FastAPI backend structure for:
    {project_idea}

    Include:
    - API routes
    - CRUD operations
    - proper FastAPI code
    - clean architecture
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":

    idea = input("Enter your app idea: ")

    result = backend_agent(idea)

    print("\nGenerated Backend:\n")

    print(result)
