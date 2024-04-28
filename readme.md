# Fractal Trees Visualization

This Python script generates fractal trees using the Pygame library. Fractal trees are a fascinating mathematical concept that demonstrates self-similar patterns found in nature, such as tree branches or blood vessels.

## Requirements
- Python 3.11.x
- Pygame library

## Usage
1. Make sure you have Python installed on your system.
2. Install the Pygame library if you haven't already:
    ```
    pip install pygame
    ```
3. Run the script using the following command:
    ```
    python main.py --> for using handtracking to generate fractal tree
    python mouseTrackFractal.py --> for using mouse scroll to generate fractal tree
    ```
4. Once the Pygame window opens, you can observe the fractal tree visualization.
5. You can adjust the appearance of the fractal tree by moving the mouse within the window.

## How It Works

### Mouse Scrolling Feature

Move your mouse horizontally to see fractal trees at different angles

### HandTracking Feature
- The script captures webcam frames using OpenCV and performs hand tracking using MediaPipe.
- It detects the horizontal position of the hand and maps it to adjust the angle of the fractal tree branches.
- Fractal trees are generated using Pygame, with recursive algorithms for branch creation.
- To start generating trees, simply move your hands horizontally (preferably from right to left).

## TODOS
- [x] add mouse tracking feature
- [x] add handtracking feature
- [ ] refine further


## Credits
- This script was created by jeevanalok for educational purposes.

## License
- This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute it.
