This part of the project documentation focuses on a
**problem-oriented** approach. You'll tackle common
tasks that you might have, with the help of the code
provided in this project.

## How To Add Two Numbers?

You have two numbers and you need to add them together.
You're in luck! The `python101` package can help you
get this done.

Download the code from this GitHub repository and place
the `python101/` folder in the same directory as your
Python script:

    your_project/
    │
    ├── python101/
    │   ├── __init__.py
    │   └── python.py
    │
    └── your_script.py

Inside of `your_script.py` you can now import the
`add()` function from the `python101.python`
module:

    # your_script.py
    from python101.python import add

After you've imported the function, you can use it
to add any two numbers that you need to add:

    # your_script.py
    from python101.python import add

    print(add(20, 22))  # OUTPUT: 42.0

You're now able to add any two numbers, and you'll
always get a `float` as a result.