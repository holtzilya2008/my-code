# My Code - Our Coding Gym

In the past we needed to run away from predators and hunt for food. We did a lot of exercise, our muscles were strong and we ware a good shape. Nowadays we are sitting in front of the computer for hours, so we must go to the gym to maintain good health.

Today we are facing the revolution of Generative AI, which is a great tool that can help us in many ways, but in the same time it can make us lazy and dependent on it. We are losing our ability to think, to solve problems, to code, to create.

This is a place where a community of **Humans** solve coding challenges **Without AI Assistance**. Here we can solve them using our favorite technologies. There is no limitations as long as it works in a Docker container. A fresh set of problems will be released once a month.

## Motivation:

- Practice your coding skills without AI.
- Practice your Algorithmic thinking skills.
- Learning to code in new programming languages.
- Learn from other people's solutions.
- See different coding styles.
- Learn different problem solving patterns.
- Express your creativity.
- Stay prepared for coding interviews.
- Just have fun 

## The flow:

- On the first of each new moth, a new set of challenges will be released to master.
- The challenges must include at least: 
    - 1 LeetCode style Algorithmic challenge
    - 1 Architectural system design challenge
    - 1 Design pattern challenge
    - 1 Web development challenge

- The challenges will be placed in the following directory structure:
    - `topics/<topic>/<YYYY-MM>_<challenge_name>`
    e.g. `topics/algorithms/2025-07_Longest_Substring_Without_Repeating`
- The members must submit a pull request with a solution, that follows submission rules bellow.
- The earlier you submit the solution, the higher chances it will be reviewed by someone from the members.
- Everyone can review and comment on any Pull request.
- Only Repository admins may merge pull requests to master.
- We will start with that, and we will think how to enhance the repository in the future. See Future Enhancement Ideas bellow.
- Everyone is encouraged to contribute by proposing new challenges following the challenge proposal rules described in `challenge_proposal_rules.md`. 

## Solution Submission Rules

- You should develop your solution in a separate branch and submit under 
    - `topics/<topic>/<YYYY-MM>_<challenge_name>/solutions/<your_github_username>/`
    e.g. `topics/algorithms/2025-07_Longest_Substring_Without_Repeating/solutions/holtzilya2008/`
- You submit your solution using a Pull Request to the master branch
- Your solution should include a Dockerfile and `docker-compose.yml`. Everyone who wishes to run your solution should be able to do `docker compose up` and it should run your docker container with all the dependencies, run your tests and then shut down your container once all tests passed.

### Your Code:

- The usage of ChatGPT or any other GenAI for solving the challenges or writing any part of your code is **STRICTLY PROHIBITED!**. The whole idea is to make you practice coding with your human hands and thinking with your human head.
- There are no limitations on the language or technology you use here, as long as it runs in a  docker container.
- Your solution MUST include unit tests in the `tests` directory, along with your solution code. 
- Try to make the tests and the code verbose (add prints and logging), so the person running your solution could actually observe what's happening
- Make a separate Pull Request for every challenge you solve. You don't have to solve all of them. Pick what you find most relevant for you. 
- Try to follow best coding practices for the technology you are using. 
- For Architecture only challenges, you should provide a design document using the documentation as code approach, such as Markdown files, and include them in your solution directory. You can use GenAI to help you to draw PlantUML or SVG diagrams. 
