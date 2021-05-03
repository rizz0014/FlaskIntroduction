# Flask Introduction Tutorial

This is a tutorial by ***[freeCodeCamp.org](https://www.youtube.com/watch?v=Z1RJmh_OqeA&list=PLhrA5PWEN63K5vBSz3YmL3IElsKLEoBE9&index=3)***.

## Task Master

The application ***Task Master*** is hosted at Heroku - https://rizzo-flaskcrudapptutorial.herokuapp.com/

## Github Repo

https://github.com/rizz0014/RaspAssist

This repo has been updated to work with 'Python v3.0' and up.

### How to run

1. Install 'virtualenv':

```bash
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:

```bash
$ py -m virtualenv env (windows)
$ virtualenv env (Mac)
```

3. Then run the command to activate the virtual environment:

```bash
$ .\env\Scripts\activate (windows)
$ source env\bin\activate (when Mac)
```

4. Then install the dependencies:

```bash
(env) pip install -r requirements.txt
```

5. Finally start the web server:

```bash
$ (env) python app.py
```

This server will start on port 5000 by default. You can change this in 'app.py' by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```
