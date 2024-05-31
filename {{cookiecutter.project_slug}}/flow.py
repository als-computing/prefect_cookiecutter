from prefect import task, flow

# Load the Python code from the path provided by the user
with open('{{ cookiecutter.code_file }}', 'r') as f:
    user_code = f.read()

# Dynamically create a task from the user's code
@task
def user_task():
    """Prefect task to execute the user-provided code."""
    exec(user_code, globals())

# Create a flow with the user's task
@flow(name='{{ cookiecutter.project_slug }}-flow')
def user_flow():
    user_task()

# Run the flow
if __name__ == '__main__':
    user_flow()