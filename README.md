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
git clone https://github.com/Kanustu/automated_update.git
```
```bash
cd automated_update
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the automation script:

```bash 
python automation.py
```

The script will:
- Update a date.txt file every 6 hours (configurable)
- Commit and push changes if any are detected
- Log all activities to automation.log

## Configuration

- **Update Interval**: Modify `SCHEDULE_INTERVAL` in `automation.py` (default: 6 hours)
- **Repository Path**: Set through `GIT_REPO_PATH` environment variable

## Project Structure

- `automation.py`: Main script that handles scheduling and execution
- `git_functions.py`: Contains Git-related operations
- `date.txt`: Target file that gets updated
- `requirements.txt`: Python package dependencies
- `automation.log`: Activity log file (created when script runs)

## Error Handling

The script includes comprehensive error handling:
- Git operation failures
- Repository access issues
- General execution errors
- All errors are logged to automation.log

## License

[Your chosen license]

## Contributing

Feel free to open issues or submit pull requests for any improvements.