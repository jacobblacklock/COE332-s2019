# COE332 Fall 2019 Homework 2

This homework asks you to implement a Flask server that provides access to class information, contained inside of `coe332.json`, via REST endpoints. 

### Preliminary Steps

- Make a *private fork* of this repo
- Share it with `jchuahtacc`, `jismisk`
- Create a file called `HW2.md` with your name and EID. Make sure that you add, commit and push it with git
- Enable a pipeline on your private fork of this repository
- You may run the server locally by running `python3 main.py`
- IMPORTANT: Look at the unit tests that exist when you are reading these instructions. They will assist you with understanding what the API is supposed to provide.

### Task 1: The `/meeting` route

The `/meeting`route should provide a dictionary containing all of the data about the class meeting times and location. A client should also be able to retrieve individual items from this collection, such as `/meeting/days`.

### Task 2: `/instructors` route

The `/instructors` route should return a list containing all of the instructors for the course. The `/instructors/<int:number>` route should return an individual instructor from the collection of instructors, where the `number` corresponds to their index within the list of instructors. If an instructor doesn't exist at that list position, the route should return a 404 status.

### Task 3: The `/assignments` route

The `/assignments` route should return a list containing all of the assignments for the course. The `/assignments/<int:number>` route should return an individual instructor. A user should be able to retrieve a specific assignment's URL at an endpoint, such as `/assignments/1/url`. The API should support sending a POST to the `/assignments` route that adds a new assignment to the course.

### Task 4: Unit Tests

Provide complete coverage for `app.py` by filling in the missing unit tests and adding additional tests where necessary.

### How you will be graded

You will be graded on the basis of your Bitbucket Pipeline output. Full credit is awarded to repositories that demonstrate:
- All unit tests passing
- Full coverage of `app.py`
