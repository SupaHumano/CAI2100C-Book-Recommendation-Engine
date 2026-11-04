# Book dataset for my Project 2

I analyze three files: `Books.csv`, `Ratings.csv`, and `Users.csv`.

I first use any matching course files already placed in this folder. If they are absent, the Jupyter notebook downloads a public Book-Crossing copy documented in [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/retail-recommend-model), which provides all three filenames and their schemas.

The notebook uses **1-10 as explicit ratings**. In this dataset, `0` means an implicit interaction and must not be treated as a zero-star opinion.

The public copy is an alternative source; I do not claim it is byte-identical to a classroom ZIP that was not available during preparation. The raw data files are not duplicated in Git history. The notebook exports measured metrics and the web presentation to `results.json` and `results.js` after an actual run.

## My data version controls

I record the SHA-256 hashes of Books.csv, Ratings.csv and Users.csv in the generated results. The notebook searches for locally supplied class files first, including the Kaggle input directory, then uses the documented public mirror if none are available. I leave the input bytes unchanged and do not commit raw user data to GitHub.
