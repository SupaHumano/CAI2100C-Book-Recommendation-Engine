# Running my Project 2 notebook in Google Colab

**Student:** Juan Luna Santibanez  
**Course:** CAI2100C-2267-6908, Machine Learning Foundations  
**Professor:** Beth Muturi

## Open and run

I open the [academic notebook in Google Colab](https://colab.research.google.com/github/SupaHumano/CAI2100C-Book-Recommendation-Engine/blob/main/academic/Project_2_Course_Submission.ipynb). I use **Runtime > Restart session**, then **Runtime > Run all**. A CPU runtime is sufficient.

I do not need to clone the GitHub repository, mount Google Drive, install anything manually or create a `requirements.txt` inside Colab. The notebook checks whether the `ftfy` package is available and, only when necessary, installs that text-cleaning dependency.

## Where my CSV files come from

I first look for `Books.csv`, `Ratings.csv` and `Users.csv` in the runtime's working directory or `data` folder. If the files are missing, the notebook retrieves the public three-file Book-Crossing copy documented by Microsoft Learn. I verify downloaded file fingerprints before using them.

If the public dataset service is blocked, I open Colab's **Files** sidebar, create or open `/content/data`, and upload the three original course CSVs. I then run all cells again. I use the same filenames and do not rename the CSV columns.

I do not publish the raw Users.csv or individual reader information on GitHub.

## What success looks like

I expect the notebook to display the three input file counts, the 20 highest-rated works and 20 highest-rated authors, the two corresponding charts, examples of content-based recommendations, a collaborative evaluation table with MAE and RMSE, a comparison chart and a concluding interpretation.

The notebook can take some time to obtain and process the Book-Crossing data, especially on its first run. I need no GPU.

## My troubleshooting guide

**Missing `ftfy`**: The notebook now installs it automatically when absent. I restart the session and select Run all rather than running later cells in isolation.

**Data-download error**: I check the full error message. I upload the three official CSV files into `/content/data` when the verified public dataset URL is unavailable.

**Missing `Books.csv` or other CSV file**: I check capitalization, filename extensions and folder location in the Files sidebar.

**Missing notebook variables**: I select **Runtime > Restart session** and **Run all**, ensuring all cells run from top to bottom.

**Unexpectedly different results**: I verify the input file counts and source SHA-256 hashes before assuming the algorithm changed. The official course files and a public mirror are not necessarily byte-identical.

## Scientific boundary

My Google Colab notebook uses a historical educational dataset and a bounded warm-start collaborative evaluation. I do not claim the web demo makes real-time predictions or that this notebook reproduces an unavailable instructor template.
