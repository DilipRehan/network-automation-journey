import subprocess

result = subprocess.run(["ping", "-n", "10", "8.8.8.8"],
capture_output=True, 
text=True
)

print(result.stdout)