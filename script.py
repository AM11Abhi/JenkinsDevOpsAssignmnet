import os

os.makedirs("output", exist_ok=True)

with open("output/result.txt", "w") as f:
    f.write("Python script executed successfully")

print("Python script executed")