import os


def activate_venv():
    current_path = os.getcwd()
    if os.name == "posix":
        activation_file = os.path.join(current_path, "venv", "bin", "activate_this.py")
    else:
        activation_file = os.path.join(current_path, "venv", "Scripts", "activate_this.py")
    exec(open(activation_file).read(), {"__file__": activation_file})
