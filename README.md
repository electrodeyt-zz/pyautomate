# PyAutomate

A tool written in Python to run other Python Scripts.

# Usage

python PyAutomate.py time repeat file

"time" is the time to run it in / the time between runs. Must be in seconds
"repeat" sets if the Python file should be run once or should be every X amount of seconds.
"file" is the Python file to run.

These Arguments must be in the specified order.

# Example:
Example 1:
python PyAutomate.py 10 true test.py

Would run the file test.py every ten seconds.

Example 2:
python PyAutomate.py 2 false prime.py

Would run the file prime.py once in two seconds.
