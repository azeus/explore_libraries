# Explore Libraries Repository

This repository is a growing collection of Python libraries, categorized by their functionality. The goal is to document my journey as I explore and experiment with Python's vast ecosystem, including standard library modules and external libraries. The target? Exploring up to 500 libraries (maybe more?). Each section includes a brief description of the libraries, their use cases, and links to relevant documentation.

## Table of Contents

1. Astronomical Computing Libraries
2. Data Processing Libraries
3. Math and Symbolic Computation Libraries
4. Visualization and UI Libraries
5. Text and Emoji Handling Libraries
6. Networking Libraries
7. Utilities and Tools
8. Movie Scraping and Rating Integration
9. Games
10. Generative Art
11. Text Analysis Libraries

## Astronomical Computing Libraries

Libraries for astronomical calculations, celestial object tracking, and astronomical data visualization.

### astro.py
- Description: A comprehensive toolkit using Astropy for astronomical calculations and visualizations. Features include:
  - Tracking Sun and Moon positions (altitude and azimuth)
  - Plotting celestial object paths over time
  - Calculating astronomical night duration
  - Customizable observation location settings
- Dependencies: Astropy, Matplotlib
- Documentation: Astropy Documentation

### moon_phase.py
- Description: A precise moon phase calculator that provides detailed lunar information. Features include:
  - Calculate moon phases for any given date
  - Display phase names with corresponding symbols (🌑🌒🌓🌔🌕🌖🌗🌘)
  - Calculate lunar age and illumination percentage
  - Find next occurrence of specific moon phases
  - Phase percentage and visible illumination calculations
- Dependencies: datetime, math
- Documentation: Built on astronomical algorithms for lunar cycle calculations

## Data Processing Libraries

Libraries focused on processing, transforming, and manipulating data.

### processing.py
- Description: Utility for handling and transforming datasets efficiently.
- Documentation: Processing Documentation

## Math and Symbolic Computation Libraries

Libraries for mathematical computations, symbolic algebra, and numerical processing.

### symbolic_math.py
- Description: Explore symbolic math with Python, including solving equations and symbolic differentiation.
- Documentation: Symbolic Math Documentation

## Visualization and UI Libraries

Libraries for creating visualizations, progress bars, and UI elements.

### progress_bar_test.py
- Description: Test progress bars for terminal and UI feedback.
- Documentation: Progress Bar Documentation

## Text and Emoji Handling Libraries

Libraries for text manipulation, emoji processing, and ASCII art.

### ascii.py
- Description: Create and manipulate ASCII art using Python.
- Documentation: ASCII Documentation

### emoji_test.py
- Description: Handle and process emoji in text data.

## Networking Libraries

Libraries for network communication, including Ethernet-based interactions.

### socket_test.py
- Description: A demonstration of Python's built-in socket module for TCP and UDP communication. Includes examples for creating a server and client within the same script.
- Documentation: Python socket Module Documentation

## Utilities and Tools

General-purpose libraries for enhancing productivity and the development experience.

### random_pwd_gen.py
- Description: Generate strong, customizable passwords. Allows users to specify the length and inclusion of uppercase letters, numbers, and special characters.
- Documentation: Python String Module Documentation

## Movie Scraping and Rating Integration

Libraries for fetching and processing movie data.

### movie_scraper.py
- Description: Fetch movies released two months ago from Wikipedia and integrate with OMDb API to retrieve IMDb ratings and other metadata.
- Documentation: OMDb API Documentation

## Games

Libraries and scripts for creating and playing games.

### jenga.py
- Description: A terminal-based Python implementation of Jenga. Players take turns removing blocks from the tower while trying to keep it stable. The game includes stability checks and random wobbles for added excitement.
- Features:
  - Displays the tower's current state
  - Allows block removal by specifying row and column
  - Implements a random chance of the tower wobbling or collapsing
- Documentation: Jenga Game Documentation

## Generative Art

Libraries and scripts for creating algorithmic art and visual patterns.

### spinograph.py
- Description: A script that generates spirograph patterns using mathematical formulas and Matplotlib for visualization.
- Features:
  - Produces colorful spirographs based on random parameters
  - Customizable with radius, offset, and step values for unique designs
  - Perfect for experimenting with generative art techniques
- Documentation: Matplotlib Documentation

## Text Analysis Libraries

Libraries for analyzing and processing text content.

### word_frequency.py
- Description: A sophisticated text analysis toolkit focusing on word starting letter frequencies. Features include:
  - Statistical analysis of word starting letters
  - Visualization of frequency distributions
  - Text preprocessing and cleaning
  - Support for large text documents
  - Customizable visualization options
- Dependencies: matplotlib, typing, collections, re
- Documentation: Built-in docstrings and type hints
- Features:
  - Calculate frequency distribution of starting letters
  - Generate statistical reports with percentages
  - Create bar plots of letter frequencies
  - Handle edge cases and special characters
  - Support for case-insensitive analysis

## Notes

- This list will grow as I explore more libraries. Stay tuned!
- Feedback and suggestions for libraries to explore are always welcome.
- Libraries included in this repository are thoroughly tested to provide examples and insights.
