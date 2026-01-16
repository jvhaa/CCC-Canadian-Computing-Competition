# Canadian Computing Competition (CCC) — Solutions in Python

A personal collection of solutions to problems from the Canadian Computing Competition (CCC) and related contest practice, implemented in Python. This repository collects solved problems, organized by year and problem name, with short explanations where useful.

- My solved problems on DMOJ: https://dmoj.ca/user/jvhaa/solved
- My submissions on Codeforces: https://codeforces.com/submissions/jvhaa

Table of Contents
- <a>About</a>
- <a>Repository structure</a>
- <a>How to run a solution</a>
- <a>Naming &amp; contribution guideline</a>
- <a>License</a>
- <a>Contact</a>

About
This repository is intended for:
- Reviewing past CCC problems and solutions.
- Practicing problem-solving and Python techniques.
- Sharing solutions and explanations with others learning contest programming.

Solutions focus on clarity and correctness rather than optimized micro-performance. Where helpful, short comments or explanations are included.

Repository structure
Assumed structure (example):
- /2024/
  - S1_easy_problem.py
  - S2_mid_problem.py
- /scripts/         (optional helper scripts)
- /notes/           (optional written explanations)
- README.md

Each solution file:
- Is self-contained and reads from standard input.
- Contains the problem name, a short description or link to the problem statement (if public), and a solution implementation.

How to run a solution
Prerequisites
- Python 3.8+ recommended.

Run a solution directly:
- With input redirection from a file:
  python3 2024/S1_easy_problem.py &lt; samples/input1.txt
- Using a pipe:
  cat samples/input1.txt | python3 2024/S1_easy_problem.py

If you prefer a virtual environment:
- python3 -m venv .venv
- source .venv/bin/activate
- python3 2024/S1_easy_problem.py &lt; samples/input1.txt

Example
Assuming a solution at `2024/S1_sum.py` and a sample input file `samples/sum1.txt`:
- python3 2024/S1_sum.py &lt; samples/sum1.txt

Naming &amp; contribution guideline
If you want to contribute or submit new solutions, please follow these conventions:
- Place solutions by year in a top-level folder named with the year (e.g., `2024/`).
- File names: `S{problem-number}_{short-name}.py` (e.g., `S1_magic_numbers.py`) or `J{problem-number}_...` for Junior problems if you prefer.
- Add a short comment at the top with:
  - Problem name and source (CCC Year, Senior/Junior, problem number)
  - Link to problem statement if available
  - A one- or two-line explanation of the approach

Pull request checklist
- [ ] Code runs with Python 3.x
- [ ] Input/output uses standard in/out (no interactive prompts)
- [ ] Add sample input (optional) and expected output to `samples/` if helpful
- [ ] Add short explanation in a comment near the top of the file

License
If you want a permissive license, consider adding an MIT license. If you prefer no license, add a statement here describing allowed usage. Example (recommended): MIT License.

Contact
GitHub: <a href="https://github.com/jvhaa">jvhaa</a>

Acknowledgements
- Problems and test cases come from CCC and online judges like DMOJ and Codeforces.
- This repository is for learning and practice.
