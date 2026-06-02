# Software Design Document (SDD) - Linux Hero: Virus Escape

## 1. Project Overview
Linux Hero is an educational game designed to teach Linux fundamentals. Unlike passive tutorials, it uses active gameplay mechanics to reinforce technical knowledge.

## 2. Technical Architecture
The project is built on **Python 3.x** and **Pygame**, utilizing a strict Object-Oriented approach.

### 2.1 Core Systems
- **Movement Engine:** Physics-based movement with gravity, acceleration, and friction.
- **Terminal Simulator:** A custom UI component that intercepts keyboard events to simulate a Bash environment.
- **Collision Manager:** Handles interactions between the Player, Environment, and Enemies.

## 3. Combat Mechanics (The Stomp System)
To provide a satisfying gameplay loop, the game implements a "Jump-to-Kill" mechanic inspired by classic platformers:
- **Detection:** The system checks if the `Player.rect.bottom` collides with `Enemy.rect.top` while the Player's vertical velocity is positive (descending).
- **Outcome:** If true, the `Enemy.kill()` method is triggered, and a small upward impulse is applied to the Player. 
- **Lateral Hit:** If collision occurs from the sides, the Player loses health.

## 4. Educational Syllabus
The game progress is tied to Linux command proficiency:
1. **Level 1 (Navigation):** `pwd`, `ls`
2. **Level 2 (Filesystem):** `cd`, `mkdir`
3. **Level 3 (Permissions):** `chmod`
4. **Level 4 (Data Mining):** `grep`, `find`

## 5. Visual Identity
The protagonist is a stylized fox (the "Linux Hero"), chosen to represent the intelligence and speed required in cybersecurity. 

## 6. Conclusion
By combining action-platformer mechanics with terminal-based puzzles, Linux Hero creates a unique learning environment that appeals to both students and gamers.
