import subprocess


def run_coq_command(command, coq_path="/Users/jonathansuru/.opam/default/bin/coqtop"):
    process = subprocess.Popen(
        [coq_path, "-quiet"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    stdout, stderr = process.communicate(command)
    return stdout, stderr


def print_result_and_return(message, stdout, stderr, return_value):
    print(message)
    print(stdout)
    print(stderr)
    return return_value


def check_theorem_proof(theorem, proof):
    command = f"{theorem}\n{proof}"
    stdout, stderr = run_coq_command(command)

    # Check for error messages
    if "Error" in stdout or "error" in stderr:
        return print_result_and_return("Proof contains errors:", stdout, stderr, False)

    # Check for successful proof completion
    if "is defined" in stdout or "No more goals." in stdout:
        print("Proof is correct!")
        return True

    return print_result_and_return(
        "Unable to determine if the proof is correct:", stdout, stderr, None
    )
