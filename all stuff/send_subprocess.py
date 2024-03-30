import subprocess

# Function to run a command in a subprocess
def run_command(command):
    return subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Run two terminals as subprocesses
terminal1 = run_command(['gnome-terminal', '--'])
terminal2 = run_command(['gnome-terminal', '--'])

# Example: Sending a command from terminal1 to terminal2
command_to_send = "echo 'Hello from terminal1'"

# Write the command to the stdin of terminal1
terminal1.stdin.write(command_to_send.encode('utf-8'))
terminal1.stdin.close()

# Read the output from the stdout of terminal2
output_from_terminal2 = terminal2.stdout.read().decode('utf-8')
print("Output from terminal2:", output_from_terminal2)

# Close the subprocesses
terminal1.wait()
terminal2.wait()
