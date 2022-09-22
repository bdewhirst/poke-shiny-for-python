import subprocess


def run_shiny() -> None:
    """
    Wrap the command to (re)start shiny in a bit of python code

    :return: display output of the command to STDOUT

    future work: make this reentrant
    """
    result = subprocess.run(["shiny", "run", "--reload", "my_app/app.py"])
    print(result.decode('utf-8'))


if __name__ == '__main__':
    run_shiny()

