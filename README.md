# Space-Dodge: Python Edition
A fully function space game where you move a spaceship to avoid incoming asteroids

This Space Dodge project is an innovative and fun project that provides
an engaging and entertaining experience. This project is built with Python and VSCode, offering easy controls. Whether you're a student or a developer 
looking to explore programming in Python, Space Dodge provides a fun interractive experience

### Windows

1. **Install Git:**
   - Download and install Git from the official website: [Git Downloads](https://git-scm.com/downloads).
   - During installation, make sure to select the option to "Use Git from the Windows Command Prompt" or "Use Git and optional Unix tools from the Windows Command Prompt."
   - Complete the installation.

### macOS

1. **Install Git:**
   - Git is pre-installed on macOS. Open the Terminal and proceed with cloning

## Installation

Make sure you have Python and pygame installed. Then, install the required dependencies using:

```bash
pip install pygame
git clone https://github.com/jguzman42/Space-Dodge.git
cd Space-Dodge
python main.py

```
## Usage

Use the WASD keys or arrow keys to control the spaceship's movement:

- **W or Up Arrow:** Move the spaceship upward.
- **A or Left Arrow:** Move the spaceship to the left.
- **S or Down Arrow:** Move the spaceship downward.
- **D or Right Arrow:** Move the spaceship to the right.

Example command to run the game:

```bash
python main.py

```

## Troubleshooting

### Known Issues

#### Asteroids Deletion Inconsistency

**Issue:**
Asteroids are getting deleted when they reach the halfway point of the screen instead of when they go completely off-screen.

**Possible Cause:**
This issue may be related to the logic responsible for detecting when an asteroid should be deleted.

**Solution/Workaround:**
If you encounter this issue, consider reviewing the asteroid deletion logic in the code. 
Ensure that the condition for asteroid deletion is based on its position going completely 
off-screen rather than reaching the halfway point.

#### Score Incrementation Issue

**Issue:**
The score is getting incremented when asteroids are deleted in the middle of the screen, 
contrary to the expected behavior of incrementing the score only when asteroids go completely off-screen.

**Possible Cause:**
This issue may be due to the scoring logic being triggered at the wrong point in the asteroid lifecycle.

**Solution/Workaround:**
To address this issue, check the scoring logic in the code. Make sure that the score is incremented only when an asteroid is successfully navigated off-screen. Adjust the scoring logic accordingly.

### Reporting Issues

If you encounter any issues not mentioned above or have suggestions for improvements, 
please [open an issue](https://github.com/yourusername/yourproject/issues) on GitHub. 
Provide detailed information about the problem, steps to reproduce it, and any relevant error messages. 
Your feedback is valuable in improving the game for everyone.

## Future Features and Enhancements

I have exciting plans for the future development of this game! Here are some features and enhancements that I plan to add:

### Power-Ups

I'm working on introducing power-ups to enhance the gaming experience. Power-ups will provide players with unique abilities, such as invincibility, speed boosts. 
Stay tuned for updates on when these power-ups will be implemented!

### Leaderboard

A leaderboard system is in the pipeline to track and display the top scores of players. 
Compete with others and see how your skills compare to the rest of the gaming community. 
I'm actively working on implementing this feature to make the game even more competitive and enjoyable.
*Found in highscores.py file

### How You Can Contribute

We welcome contributions from the community! If you have ideas for additional features or enhancements, feel free to [open an issue](https://github.com/jguzman42/Space-Dodge/issues) on GitHub. 
Your feedback and suggestions are valuable in shaping the future of the game.

Stay tuned for updates as I continue to improve and expand the game. I appreciate your support and look forward to delivering an even more engaging gaming experience.


## Contributing

I welcome contributions from the community! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository by clicking the "Fork" button on the top right of this page.

2. Clone your forked repository:

    ```bash
    git clone https://github.com/your-username/your-project.git
    cd your-project
    ```

3. Create a new branch for your feature or bug fix:

    ```bash
    git checkout -b feature/new-feature
    ```

4. Make your changes and test thoroughly.

5. Commit your changes:

    ```bash
    git add .
    git commit -m "Add new feature"  # Use a descriptive commit message
    ```

6. Push your branch to your fork:

    ```bash
    git push origin feature/new-feature
    ```

7. Submit a Pull Request (PR) by navigating to the original repository and clicking on the "New Pull Request" button.

8. Provide a clear title and description for your PR. Be sure to reference any related issues.

9. Your PR will be reviewed, and once approved, it will be merged into the main branch.

Thank you for contributing to our project! 🚀

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact Me
For any questions or concerns, feel free to contact me:

- <a href="mailto:guzmanjose3456@gmail.com" target="blank"><img align="center" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="guzmanbjose" height="35" width="100" /></a>
- <a href="https://linkedin.com/in/guzmanbjose" target="blank"><img align="center" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="guzmanbjose" height="35" width="100" /></a>
- <a href="https://github.com/jguzman42" target="blank"><img align="center" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="guzmanjose42" height="35" width="100" /></a>
- <a href="https://instagram.com/guzmanjose42" target="blank"><img align="center" src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="guzmanjose42" height="35" width="100" /></a>
