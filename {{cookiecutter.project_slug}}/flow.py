from prefect import task, Flow

# Load the Python code from the path provided by the user
with open('{{ cookiecutter.code_file }}', 'r') as f:
    user_code = f.read()

# Dynamically create a task from the user's code
@task
def user_task():
    """
    Prefect task to execute the user-provided code.
    """
    exec(user_code, globals())

# Create a flow with the user's task
with Flow('{{ cookiecutter.flow_name }}') as flow:
    user_task()

# Run the flow
if __name__ == '__main__':
    flow.run()