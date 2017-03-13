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


<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
