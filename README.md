# Automated Git Update

A Python-based automation tool that performs scheduled updates to a Git repository. This tool can be used for maintaining regular repository updates or keeping your GitHub contribution graph active.

## Features

- Automated file updates at configurable intervals
- Automatic git commit and push operations
- Error handling and logging
- Configurable through environment variables
- Runs as a background process

## Prerequisites

- Python 3.x
- Git repository access
- Required Python packages (install via requirements.txt):
  - GitPython==3.1.41
  - schedule==1.2.1

## Installation

1. Clone this repository:
```bash
git clone [your-repo-url]
cd automated_update
```
