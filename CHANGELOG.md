# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project has no version tags or releases yet, so every change is listed
under `Unreleased`.

## [Unreleased]

### Added

- The game itself: a pygame action game in which Asterix fights the Roman army and Julius Caesar, becoming invulnerable only while under the effect of the magic potion.
- Fullscreen gameplay with keyboard movement, magic-potion pickups, lives, score tracking, and a win/lose menu that restarts with Enter and exits with Esc.
- Configurable settings in `settings.py` for characters, speeds, lives, super-power duration, army size, and image/music paths, as documented in the README.
- Russian-language README with installation, launch, and configuration instructions.
- BSD 2-Clause license.
- `ROADMAP.md` describing the project's goals: easy installation on any platform and documentation in English as well as Russian (#10).
- `CHANGELOG.md` to track notable changes (#15).

### Fixed

- Removed the tracked `__pycache__/` directory from the repository and added `__pycache__/` and `*.pyc` to `.gitignore` (#5).
