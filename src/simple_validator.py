import yaml
import json
from jsonschema import Draft4Validator
import sys
import glob
import re
import warnings

"""ARG1 = path to spec file.
ARG2 = path to directory with json files.
All files with .json file extension in this dir will be checked.
"""


def test_jschema(validator, test_pattern):
    if not validator.is_valid(test_pattern):
        es = validator.iter_errors(test_pattern)
        for e in es:
            warnings.warn(str(e))
            return False
    else:
        return True

f = open(sys.argv[1], 'r')

spec = yaml.load(f.read())

v = Draft4Validator(spec)

docs = glob.glob(sys.argv[2] + "*.json")

if not len(docs):
    warnings.warn("No .json files in " + sys.argv[2])
    sys.exit(1)

stat = True
for doc in docs:
    warnings.warn("Checking %s" % doc)
    file = open(doc, "r")
    pattern = json.loads(file.read())
    if not test_jschema(v, pattern): stat = False
  
if not stat:
    sys.exit(1)
