# My explanation guide — Project 2

**Juan Luna Santibanez · CAI2100C · Professor Beth Muturi**

This is my study guide for understanding the notebook and explaining its results. It is not a separate required live presentation.

**What problem am I solving?** I am trying to recommend books a reader might appreciate using either book information or patterns in other readers' ratings.

**Why do I use three CSV files?** Books gives me metadata; Ratings connects readers and books; Users gives me anonymized reader records. I keep them as separate input tables until they are needed.

**What does ISBN mean?** It is a book identifier. I preserve it as text so I do not drop leading zeros.

**Why does a zero rating matter?** In Book-Crossing, zero represents an implicit interaction, not an explicit zero-star rating. I use the explicit 1–10 ratings when I train and evaluate numerical predictions.

**What is Content-Based Filtering?** I convert a book's title, author, publisher and year into text features using TF-IDF. Cosine similarity helps find books with related metadata.

**Does cosine similarity mean I predicted a rating?** No. It measures similarity between book features. I do not compare this score directly with MAE or RMSE.

**What is Collaborative Filtering?** I look for books liked or rated in similar ways by readers. My item-item model uses a sparse book-reader matrix and cosine neighbors.

**Why did I use a sparse matrix?** Most readers have not rated most books. A sparse matrix stores only the available ratings rather than millions of meaningless zero entries.

**How did I evaluate the collaborative method?** I reserved 20% of the selected explicit ratings as a test set. I predicted them using training observations only and calculated MAE and RMSE.

**Why do I compare with a baseline?** If predicting a book's average score performs as well as, or better than, my collaborative model, I must acknowledge that rather than calling the advanced method automatically superior.

**What is the cold-start problem?** A new reader or book has too few past interactions for reliable collaborative similarities. Content information can help with new books if metadata is available.

**What makes my work practical?** I designed a single notebook that loads authentic CSVs, shows its assumptions, produces clear tables and plots, and stores results for a static website.

**What did I learn?** Recommendation quality depends on the data used, how missing and implicit feedback are interpreted, and whether a model beats a simple baseline on unseen observations.

**What should I be careful not to claim?** I do not claim my website trains models in the browser; I do not call a metadata similarity score a personal rating prediction; and I do not represent a public data mirror as the instructor's exact ZIP without comparing the actual files.