# Fractural VNE Docs

Documentation for the [Fractural Visual Novel Engine](https://github.com/Fractural/FracturalVisualNovelEngine).

Built with [Sphinx](https://www.sphinx-doc.org/en/master/), [Read the Docs](https://readthedocs.org/) and a customized version of the [Godot Docs' sphinx theme](https://github.com/godotengine/godot-docs).

Available on:

- [Github Pages](https://fractural.github.io/FracturalVNEDocs)
- [Read the Docs](https://fracturalvne.readthedocs.io/)

## How to Build
1. To build it you'll need [Python](https://www.python.org/downloads/), [CMake](https://cmake.org/install/), and some other libraries.

2. Install libraries with:
    `python -m pip install -r requirements.txt`

3. Build:
    - Linux/Mac:
        ```bash
        > make html
        ```
    - Windows:
        ```bat
        > make.bat html
        ```
