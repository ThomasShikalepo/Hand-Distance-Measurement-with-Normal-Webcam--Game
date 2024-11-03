# Hand Distance Measurement with Normal Webcam - Game

![Game Screenshot](https://github.com/user-attachments/assets/56ef2d34-0892-4df6-a226-c773e780a484)

**This project demonstrates a fun, interactive game** that uses computer vision to measure the distance between a player's hand and a target circle on the screen. Built using Python and OpenCV, the game leverages hand tracking to calculate the distance of the player's hand from the webcam and integrates a scoring system for added excitement. The goal is to move your hand close to the target circle within a specified time limit to earn points.

## Features

- **Hand Tracking**: Utilizes `cvzone` and OpenCV to detect and track hands in real time through a standard webcam.
- **Distance Measurement**: Calculates the distance between specific landmarks on the hand, mapping the distance in pixels to real-world units (centimeters) using a polynomial function.
- **Dynamic Targeting**: Randomly relocates a target circle on the screen every time the player achieves a "hit," keeping the game challenging and engaging.
- **Real-Time Score and Timer**: Displays a live countdown timer and score on the game screen.
- **Game Restart**: Allows the player to restart the game by pressing the "R" key after a game-over screen is displayed.

## Dependencies

- **OpenCV**: For image processing and webcam integration.
- **cvzone**: For hand detection and positioning on the screen.
- **NumPy**: For handling mathematical functions and calculations.

## How It Works

1. **Webcam Setup**: The webcam captures live video, which is processed to detect hands and calculate distance.
2. **Hand Detection and Distance Calculation**: By identifying specific landmarks on the player's hand (index and pinky knuckles), the game calculates the distance and maps it to real-world units.
3. **Gameplay Logic**:
   - When the hand gets close to the target circle and within a certain distance threshold (under 40 cm), the player scores a point.
   - The target circle moves to a random location after each successful "hit."
4. **Scoring and Timing**: The player accumulates points by quickly reaching the target circle within a 20-second limit.
5. **Game Over Screen**: Once time runs out, a game-over screen shows the final score and gives the player the option to restart.

## Getting Started

To run this project, ensure you have Python installed on your machine, and then follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/hand-distance-game.git
   cd hand-distance-game
