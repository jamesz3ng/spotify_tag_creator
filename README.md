# Spotify Tag Creator

Easily create a custom 3D-printable keychain or tag featuring a Spotify code, so others can scan it to instantly open a track, album, or playlist in Spotify. This repository contains:

1. **A Fusion 360 script** that builds a rectangular keychain with filleted corners, imports an SVG (the Spotify code), extrudes it, and adds a keychain hole.  
2. **An interactive Python script** that generates the SVG assets to use with the Fusion 360 script.  

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Workflow](#workflow)
- [Interactive Asset Generation Script](#interactive-asset-generation-script)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

**Spotify Tag Creator** streamlines the process of generating a 3D model of a rectangular keychain that includes:

1. **Automated Tag Shape** – Creates a rectangular plate (e.g., 8.5 x 2) with filleted corners.  
2. **Spotify SVG Import** – Places a generated Spotify code on the top face of the tag.  
3. **Keychain Hole** – Automatically adds a circular hole for attaching it to keys or a bag.  
4. **Interactive Script** – Generates the necessary SVG assets (e.g., the Spotify code) so you can keep the entire process in-house.  

Once created, you can 3D-print the tag, and anyone can scan the code with Spotify’s mobile app.

---

## Features

- **Interactive Asset Generation**: A Python script interacts with the Spotify code generator to create the SVG for your desired track/album/playlist.  
- **Automated Tag Building in Fusion**: The Fusion 360 script draws and extrudes a rectangular plate with rounded corners.  
- **SVG Import & Extrusion**: The Spotify code SVG is imported, scaled, translated, and then extruded.  
- **Parametric Dimensions**: Easily change size, shape, and code location by editing Fusion parameters or script constants.  
- **Keychain Hole**: Automatic hole creation at a specified location.  

---

## Workflow

1. **Generate or Download Your Spotify Code**:  
   - Use the included interactive script (explained below) or [Spotify Codes](https://www.spotifycodes.com/) to get a Spotify code SVG.

2. **Run the Fusion 360 Script**:  
   - Builds the base plate, imports your generated code, extrudes it, and adds a keychain hole.

3. **3D Print**:  
   - Export your design as an STL (or another format) and print it.

4. **Enjoy & Share**:  
   - Anyone with a Spotify mobile app can scan the code on your printed tag to immediately open the track.

---

## Interactive Asset Generation Script

Inside this repository, you will find a **Python script** that helps you generate the SVG file for the Spotify code. This script can:

- Prompt you for a **Spotify track/album/playlist link**.  
- Fetch a **Spotify code**.  
- Output a properly sized **SVG** that the Fusion 360 script can import.  

### How to Use the Script

1. Make sure you have **Python 3** installed.  
2. From your terminal or command prompt, navigate to the script’s directory.  
3. Run the command (example):
   ```bash
   python generate_spotify_code.py --link "https://open.spotify.com/track/..."
   ```
4. The script will create an **SVG file** in the `assets/` folder (or another specified path). This file is then ready to be imported by the Fusion 360 script.

*Note:* Depending on your setup, you may need to configure the script with **Spotify API credentials** or rely on a direct code-generation approach that doesn’t require an API key. Check inside the script for any configuration steps or instructions.

---

## Requirements

1. **Autodesk Fusion 360**  
2. **Python 3.x**  
3. **Spotify Code SVG** (either generated via this repo’s script or from Spotify)  

---

## Installation

1. **Clone or Download** this repository:
   ```bash
   git clone https://github.com/jamesz3ng/spotify_tag_creator.git
   ```
2. **Install Dependencies**:  
     ```bash
     pip install -r requirements.txt
     ```
3. **Add the Fusion 360 Script**:  
   - Open Fusion 360 and go to **Scripts and Add-Ins**.  
   - Click **Add**, then select the folder with `spotify_tag_creator` containing the Python script(s).  
---

## Usage

1. **Generate the Spotify Code** (optional step if you don’t already have an SVG):  
   ```bash
   python main.py"
   ```
   Follow the prompt to input the required spotify link.
   This produces the necessary `.svg` file (e.g., in `assets/output.svg`).

2. **Open Fusion 360**, and in a new or existing design:  
   - Go to **Scripts and Add-Ins** → **My Scripts** → `spotify_tag_creator`.  
   - Click **Run**.

3. **Observe**:  
   - A rectangular plate with filleted corners is created.  
   - The Spotify code SVG is imported, scaled, and extruded.  
   - A keychain hole is added.

4. **Export & 3D Print**:  
   - Export the final body as `.stl` (or your desired format).  
   - Print using your favorite 3D printer.

---

## Customization

- **Tag Dimensions**: Modify the rectangle dimensions or fillet radii in the Fusion script.  
- **Extrusion Depth**: Adjust the extrude distances (`2.75 mm` for base, `1 mm` for code).  
- **SVG Transform**: Scale, rotate, or translate the SVG by tweaking the transformation matrix in the Fusion script.  
- **Keychain Hole**: Change the location and size (`hole_location`, `circle_radius`) in the Fusion script.  
- **Spotify Code Style**: If you’re programmatically generating the code, you can customize the color, size, or any other attributes in the Python script.  


Feel free to open an [issue](https://github.com/jamesz3ng/spotify_tag_creator/issues) if you have questions or suggestions.
---

## Contact

- **Author**: [@jamesz3ng](https://github.com/jamesz3ng)  
- **Repository**: [Spotify Tag Creator](https://github.com/jamesz3ng/spotify_tag_creator)
