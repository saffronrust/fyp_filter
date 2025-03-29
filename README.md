# Usage:
- Just run `fyp.py`, the user input prompts should speak for themselves
- Full names and titles are not necessary e.g. "shell ying" instead of "Dr Huang Shell Ying" is fine

# File Organisation and Guide
- `Final Year Project (CCDS).html` and `Final Year Project (CCDS)_files`: the raw data from the FYP portal
- `fyp_to_csv.ipynb`: converts the HTML file to CSV format
- `FYP.csv`: resulting CSV file from `fyp_to_csv.ipynb`
- `fyp.py`: script to filter out FYPs with user input

# Troubleshooting
- Q: My filters don't work!
    - A: Ensure that the names and phrases are spelled properly. It is not robust against human error (yet)
- Q: I got an error, "Permission denied: 'filtered_fyp.csv'"
    - A: Close `filtered_fyp.csv` and run the script again