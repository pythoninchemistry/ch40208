# Adding Files to Noteable

When working with data files (such as CSV files containing experimental results), you need to get those files into your Noteable environment before you can read them with Python.

## Uploading Files from Your Computer

To upload a file from your computer to Noteable:

1. Click the upload button (↑ icon) in the toolbar at the top of the file browser
2. Select the file from your computer
3. The file will appear in your current directory

**Alternative method:** You can also drag and drop files directly from your computer into the Noteable file browser.
```{note}
Make note of which directory your file is uploaded to. You'll need to use this path when reading the file in Python.
```

## Downloading Files from the Internet

If you have a direct URL to a data file (for example, a CSV file hosted on GitHub), you can download it directly into Noteable:

1. Go to **File > Open from URL...**
2. Paste the URL of the file
3. Click **Open**

The file will be downloaded to your current directory.

### Example URLs

For CSV files on GitHub, make sure to use the "raw" URL. For example:
- Wrong: `https://github.com/user/repo/blob/main/data.csv`
- Correct: `https://raw.githubusercontent.com/user/repo/main/data.csv`

## Finding Your Files

Once uploaded or downloaded, files appear in the file browser on the left side of the Noteable interface. To use a file in your Python code, you reference it by its filename (if it's in the same directory as your notebook) or by its path.
```python
import numpy as np

# If the file is in the same directory as your notebook:
data = np.loadtxt('mydata.csv', delimiter=',')

# If the file is in a subdirectory:
data = np.loadtxt('data/mydata.csv', delimiter=',')
```
