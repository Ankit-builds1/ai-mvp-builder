from agents.planner_agent import planner_agent
from agents.backend_agent import backend_agent
from agents.frontend_agent import frontend_agent


def run_mvp_builder():
    idea = input("Enter your app idea: ")

    print("\n[Planner Agent Running...]\n")
    planner_output = planner_agent(idea)
    print(planner_output)

    print("\n[Backend Agent Running...]\n")
    backend_output = backend_agent(idea)
    print(backend_output)

    print("\n[Frontend Agent Running...]\n")
    frontend_output = frontend_agent(idea)
    print(frontend_output)

    print("\n[MVP Generation Completed]")


if __name__ == "__main__":
    run_mvp_builder()