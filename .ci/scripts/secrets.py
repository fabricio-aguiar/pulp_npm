import json
import os
import sys

secrets = json.loads(sys.argv[1])
for key, value in secrets.items():
    os.system(f'echo "{key}={value}" >> $GITHUB_ENV')

os.system("cat $GITHUB_ENV")
