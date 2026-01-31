import os

# create folders
os.makedirs("output", exist_ok=True)
os.makedirs("test-results", exist_ok=True)

# artifact file
with open("output/result.txt", "w") as f:
    f.write("Python script executed successfully")

# junit xml
xml = """<?xml version="1.0" encoding="UTF-8"?>
<testsuite name="SampleTest" tests="1" failures="0">
    <testcase classname="SampleTest" name="test_example"/>
</testsuite>
"""

with open("test-results/results.xml", "w") as f:
    f.write(xml)

print("Build + test files generated")