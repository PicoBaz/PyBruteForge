# PyBruteForge

A powerful, modular brute-force login testing tool built for ethical security audits in Python. PyBruteForge enables developers and security enthusiasts to simulate password attacks on their own systems, identifying weak credentials to strengthen security.

⚠️ **Ethical Use Only**: This tool is for testing your own systems or with explicit permission. Misuse can lead to legal consequences. Always prioritize security best practices.

## Features
- **Modular Config**: All settings (URL, usernames, password rules) in a single `config.json` file for quick tweaks.
- **Smart Password Generation**: Combines common patterns with random strings for realistic testing.
- **Error Resilience**: Automatic retries on transient errors, with configurable delays to avoid locks.
- **CSV Reporting**: Detailed logs of attempts, including timestamps and response codes.
- **Python Powered**: Lightweight, runs anywhere with Python 3.6+.

## Installation
1. Clone the repo:
   ```
   git clone https://github.com/PicoBaz/PyBruteForge.git
   cd PyBruteForge
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Edit `config.json` to match your setup (e.g., login URL, usernames).

## Usage
Run the script:
```
python brute_force_login.py
```
- Output: Progress in console, results in `brute_force_results.csv`.
- Example config tweak: Increase `maxAttemptsPerUser` for deeper tests, but monitor for rate limits.

## Configuration
Edit `config.json`:
- `loginUrl`: Target login endpoint (API expecting JSON).
- `usernames`: Array of usernames to test.
- `characters`: Char sets for random passwords.
- `passwordConfig`: Tune lengths, attempts, delays, and retries.

## Extending PyBruteForge
- Add custom patterns in `brute_force_login.py`.
- Integrate with external password lists (e.g., load from TXT files).
- For advanced setups, fork and add parallel processing via `concurrent.futures`.

## Disclaimer
PyBruteForge is an educational tool. Use responsibly—test only what you own. The author assumes no liability for misuse.

## License

Star the repo if it helps your audits! 🌟 Contributions welcome.