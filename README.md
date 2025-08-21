# Packaging and Installing Your Theme Extension

1. Install VSCE (VS Code Extension Manager):
	```sh
	npm install -g vsce
	```

2. Ensure your theme has a valid `package.json` in its root directory.

3. Run the installer script:
	```sh
	python install_themes.py
	```

This will automatically:
- Package your theme as a VSIX
- Install it into your local VS Code
# Python venv Setup for Theme Installer

To use the theme installer script, set up a Python virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python install_themes.py
```

This will ensure all dependencies are installed and the script runs in an isolated environment.
# Oceanic Themes

Oceanic Themes is a collection of ocean-inspired color themes for Visual Studio Code. Dive into the depths with a collection of different color schemes!

## Themes Included

- Bathypelagic
- Neon Reef
- Copper Shark
- Green Moray

## Installation

1. Clone this repository:
	```sh
	git clone https://github.com/YOUR_GITHUB_USERNAME/oceanic-themes.git
	```
2. Open the folder in VS Code.
3. Press `F5` to launch an Extension Development Host and test the themes.

## Usage

After installing, go to `Preferences: Color Theme` and select your favorite Oceanic Theme.

## Publishing

1. Update the `publisher` field in `package.json` to your VS Code publisher name.
2. Run:
	```sh
	npm install -g vsce
	vsce package
	vsce publish
	```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

MIT
