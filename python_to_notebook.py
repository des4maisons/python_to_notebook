import sys
import json

if not len(sys.argv) == 2:
    print "usage: %s file_to_convert" % sys.argv[0]
    sys.exit(1)

filename = sys.argv[1]

with open(filename, 'r') as code_file:
    code = code_file.read()

code_lines = map(lambda x: x + '\n', code.split("\n"))

notebook_template = """
{{
 "metadata": {{
  "name": {filename}
 }},
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {{
   "cells": [
    {{
     "cell_type": "code",
     "collapsed": false,
     "input": {code_lines_str},
     "language": "python",
     "metadata": {{}},
     "outputs": []
    }}
   ],
   "metadata": {{}}
  }}
 ]
}}
"""

notebook = notebook_template.format(
        filename=json.dumps(filename),
        code_lines_str=json.dumps(code_lines),
        )

loaded = json.loads(notebook)
pretty = json.dumps(loaded, indent=2)
print pretty
