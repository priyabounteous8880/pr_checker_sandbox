# security_violation.py

import subprocess
import pickle  # new violation: insecure deserialization

def run_command(user_input: str) -> None:
    # ⚠️ SECURITY RISK: shell=True + unsanitized input
    cmd = f"ls {user_input}"
    subprocess.run(cmd, shell=True)

def calculate(expression: str) -> float:
    # ⚠️ SECURITY RISK: eval of arbitrary input
    return eval(expression)

def insecure_pickle_load(data):  # new violation
    return pickle.loads(data)