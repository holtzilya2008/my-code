# Challenge Proposal Rules

If you are reading this it means you are interested in proposing a new challenge to our coding gym.Kudos to you!

- **Here you can use GenAI!** Since creating and documenting the challenge is time consuming, you are allowed to use any GenAI tool to help you find ideas and create a proper challenge description.

- Your challenge must be in submitted in a pull request from your own branch to master with the following content:
    - Your challenge directory `topics/<topic>/<YYYY-MM>_<challenge_name>`
    e.g. `topics/algorithms/2025-07_Longest_Substring_Without_Repeating`
    When `YYYY-MM` describes the next month

    - Inside the challenge directory:
        - `README.md` file that includes the challenge description. See for example: 
        `topics/algorithms/20241224_Longest_Substring_Without_Repeating/README.md`

        - Prepare the `solutions` directory with `.gitkeep` file so it would be included by git.
        e.g. `topics/algorithms/2025-07_Longest_Substring_Without_Repeating/solutions/.gitkeep`

    - The estimated time that needed to solve your challenge, Including, thinking, coding, writing tests, creating Dockerfile and submitting a PR, Should not exceed 8 hours. We are all busy people and not all of us can spend too much time in the Gym. 

    - Try to propose challenges on topics that different from those we already had. One of the goals here is to learn solving new kinds of problems. 

    - Each month the repository admin will choose a set of challenges for the month that incldes at least:
        - 1 LeetCode style Algorithmic challenge
        - 1 Architectural system design challenge
        - 1 Design pattern challenge
        - 1 Web development challenge

    - You don't have to think about all of these challenges, but you can propose one or more challenges that you think are interesting and valuable for the community.
    
## Example: 

See for example my first challenge that is proposed and solved by me in:
`topics/algorithms/2025-07_Longest_Substring_Without_Repeating`
- The challenge description is in `README.md` file.