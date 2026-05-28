from google import genai

# Configure Gemini client
client = genai.Client(api_key="")


def frontend_agent(project_idea):

    prompt = f"""
    Generate a professional React frontend structure for:
    {project_idea}

    Include:
    - modern UI
    - React components
    - clean design
    - responsive layout
    - buttons/cards/forms where needed
    - proper JSX code
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":

    idea = input("Enter your app idea: ")

    result = frontend_agent(idea)

    print("\nGenerated Frontend Code:\n")

    print(result)
