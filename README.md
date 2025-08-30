# Space Game

A 2D space shooter game built with Python and Pygame where you control a spaceship to survive in space.

## 🎮 Game Description

Space Game is a classic arcade-style space shooter where you pilot a spaceship through space. The game features smooth controls, engaging gameplay, and a clean, modern interface.

## 🚀 Features

- **Smooth Player Movement**: Responsive controls for spaceship navigation
- **Modern UI**: Clean, dark-themed interface with smooth graphics
- **Sprite-Based Graphics**: Efficient rendering using Pygame sprites
- **Modular Code Structure**: Well-organized, maintainable codebase

## 📋 Requirements

- Python 3.7 or higher
- Pygame 2.0 or higher

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd SpaceGame
   ```

2. **Install dependencies**:
   ```bash
   pip install pygame
   ```

3. **Run the game**:
   ```bash
   python main.py
   ```

## 🎯 Controls

- **Arrow Keys** or **WASD**: Move the spaceship
- **ESC** or **Close Window**: Exit the game

## 📁 Project Structure

```
SpaceGame/
├── main.py          # Main game loop and initialization
├── player.py        # Player spaceship class and logic
├── space_ship.py    # Base spaceship functionality
├── assets/          # Game assets (images, sounds, etc.)
│   └── player.png   # Player spaceship sprite
├── README.md        # This file
└── .gitignore       # Git ignore rules
```

## 🎨 Game Assets

The game uses sprite-based graphics stored in the `assets/` directory:
- `player.png`: The player's spaceship sprite

## 🔧 Development

### Adding New Features

1. **New Sprites**: Add sprite images to the `assets/` directory
2. **New Classes**: Create new Python files for game objects
3. **Game Logic**: Extend the `Game` class in `main.py`

### Code Style

- Follow PEP 8 Python style guidelines
- Use descriptive variable and function names
- Add comments for complex logic
- Keep classes focused and single-purpose

## 🐛 Known Issues

- Screen variable scope issue in Game class (needs to be passed as parameter)
- Missing sprite update calls in game loop
- Redundant pygame.quit() calls

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Created with ❤️ using Python and Pygame

---

**Enjoy playing Space Game!** 🚀
