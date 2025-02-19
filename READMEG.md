# HackDork

## Overview
HackDork is an automated Google Dorking tool that uses Playwright to extract potential links from web pages. It allows security researchers and ethical hackers to efficiently perform reconnaissance by leveraging various Google dorks.

## Features
- Automated Google Dorking
- Parallel execution with multiple browser tabs
- Categorized dork types (e.g., exposed files, vulnerabilities, login pages, etc.)
- Efficient result extraction and validation
- Logs for debugging and monitoring

## Installation
### Prerequisites
Ensure you have the following installed on your Kali Linux machine:
- Python 3.7+
- Playwright
- Requests
- Logging module

### Install Playwright
```bash
pip install playwright
playwright install
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
### Running HackDork
```bash
python dorking.py
```
You will be prompted to enter a domain and select dork types to perform automated Google dorking.

### Available Dork Categories
1. Information Gathering
2. Exposed Files
3. Vulnerability Detection
4. IoT & Camera Exposures
5. Cloud Storage Leaks
6. Code & Documentation
7. Subdomain Discovery
8. Open Directories
9. Sensitive Files
10. SQL Error Pages
11. Private Routers
12. Login Pages
13. Error Pages
14. Backup Files
15. All Dorks

### Example Run
```bash
Enter the domain to perform dorking on: example.com
Available dork types:
1: Information Gathering
2: Exposed Files
...
Enter the numbers corresponding to the dork types you want to use( press Enter twice to start script): 1
2
3
```

## License
MIT License

```
MIT License

Copyright (c) 2025 HackDork Developers

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Disclaimer
This tool is intended for security research and ethical hacking only. Unauthorized use on systems without permission is illegal and strictly prohibited.

