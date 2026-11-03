# My methodology — Book Recommendation Engine

**Juan Luna Santibanez | CAI2100C Machine Learning Foundations | Professor Beth Muturi**

## The problem I solve

I compare two ways to recommend a book. Content-Based Filtering matches book information; Collaborative Filtering learns from patterns of reader ratings. I keep the two methods separate so I can explain why each recommendation appears.

## Data and preparation

I use three Book-Crossing tables: books (`ISBN`, title, author, publisher, publication year), ratings (`User-ID`, `ISBN`, `Book-Rating`), and anonymized users (`User-ID`, location, age). My notebook prefers local CSV files, with a public-source download fallback described in `data/README.md`.

I retain ISBN values as **strings**, not numbers, because ISBN can begin with `0`. I handle missing values and implausible years and ages, remove duplicate user-book ratings, and compare explicit and implicit interactions separately. For numerical predictions I use only explicit ratings **1–10**. An implicit rating of **0** does not mean the user disliked the book.

## Exploratory analysis

I calculate the 20 most highly rated books and 20 most highly rated authors. I apply minimum rating counts (25 and 50, respectively, for the full public dataset) so a single excellent score does not dominate the ranking. I report both average rating and number of reviews. These are ratings rankings, not counts of books authored or absolute popularity rankings.

## My first model — Content-Based

I make one text representation per book using title, author, publisher, and available publication year, then apply `TfidfVectorizer` and cosine similarity. I restrict the candidate catalog to books with sufficient interactions and a maximum of 6,000 candidate titles to keep the educational demo efficient. The scores express metadata similarity, not estimated reader ratings.

## My second model — Collaborative

I select up to 1,500 frequently rated books and sufficiently active readers. I split explicit ratings **80/20** using `random_state=42`, fit an item-user sparse matrix on training observations, find neighboring books using cosine similarity, and predict held-out ratings from the reader's training ratings for those neighbors.

If there are no overlapping positively similar neighbors, my function falls back to the training item mean (or global training mean for a new item). I report how many test predictions were supported by neighbors. I evaluate both the collaborative predictions and a book-mean baseline with MAE and RMSE, without using held-out values during fitting.

The subset selection is based on interaction counts before splitting; this is a reproducibility/performance compromise suitable for this introductory exercise, **not** an unbiased real-world performance estimate. A production evaluation would use a fully time-separated split and select eligible users and books from training data only.

## What the metrics mean

- **MAE:** Average absolute difference in rating points between a prediction and the actual held-out rating. Lower is better.
- **RMSE:** Square root of mean squared prediction error. Penalizes larger mistakes more heavily. Lower is better.
- **Neighbor coverage:** Percentage of test predictions that had at least one usable rated neighbor; other cases use the stated fallback.

I compare the model to a simple baseline, and I do not assume the collaborative model is better unless the measured result supports it.

## Results and browser demonstration

Running the notebook saves output tables, charts, `data/results.json`, and `data/results.js`. My GitHub Pages website only presents this saved computation. It does not execute scikit-learn or make new predictions inside the browser.

The charts and figures are student-facing explanations of a completed experiment; source documents, classroom slides, and personal data are not republished.

## Limitations

The dataset is historical; its demographic fields are incomplete; popularity affects which books are eligible; and cold start remains a limitation. Book-Crossing does not provide full descriptions or genres in this three-CSV format, so I use the metadata actually available. My work is an educational assignment, not a production recommendation platform.

## References

- Professor Beth Muturi, *Project 2: Practical Application of a Recommendation Engine*, CAI2100C, Miami Dade College.
- [GroupLens — Book-Crossing dataset](https://grouplens.org/datasets/book-crossing/).
- [Microsoft Learn — book recommendation data](https://learn.microsoft.com/en-us/fabric/data-science/retail-recommend-model).
- [scikit-learn: TF-IDF](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html).
- [scikit-learn: NearestNeighbors](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html).