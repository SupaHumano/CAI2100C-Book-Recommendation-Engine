# My methodology and reproducibility

**Juan Luna Santibanez | CAI2100C-2267-6908 | Professor Beth Muturi**

## My problem and project cycle

I compare metadata-based and reader-rating-based recommendations within the six stages described in class: problem, acquisition, preparation and EDA, modeling, evaluation and responsible deployment.

## My source and dataset checks

I load three Book-Crossing tables: Books, Ratings and Users. I prefer available local files and use a documented public mirror otherwise. I retain the unmodified file inputs and record a SHA-256 digest of each source in the research results. I never claim a public mirror is identical to an instructor ZIP I have not verified.

I preserve ISBN as text, clean damaged character encodings with `ftfy` and HTML decoding, and separate implicit interactions (0) from explicit ratings (1 through 10).

## My rankings

I treat a book ranking as a ranking of distinct **work title and author combinations**. Different ISBN editions contribute their explicit ratings to the same work when that pairing is identical. My recommendation engine continues to model ISBN editions separately. I combine only a documented small set of author aliases and spelling variants. I require 25 explicit ratings for a ranked work and 50 for a ranked author when I use the full public dataset. These thresholds are modeling choices and not universal rules.

## My content model

I use available title, author, publisher and year fields. I convert a bounded candidate catalog into TF-IDF features and compute cosine similarity. The 6,000-item bound and positive-interaction screening make the educational experiment practical, but I acknowledge that this restricts coverage of cold-start books.

## My collaborative model

I divide all linked explicit interactions into an 80 percent development pool and a 20 percent holdout **before selecting eligible items or readers**. I select up to 1,500 eligible ISBNs and readers with enough ratings from the development data only. I build an item-user sparse matrix and find neighbors using cosine similarity.

I evaluate the held-out pairs with reader and item history in training. I report the total holdout and the subset eligible for warm-start evaluation. I compare my predictions to a book-average baseline on the same rows, using MAE, RMSE and usable-neighbor coverage. Where useful neighbors are missing I use the book training mean or the global development mean.

I do not force my new results to reproduce values from the earlier protocol. Changing the evaluation selection can change both metrics and coverage.

## My published outputs

I generate the figures, `data/results.json` and `data/results.js` from the research notebook. My GitHub Pages interface displays stored Python results and does not retrain a model. The academic notebook is the separately identifiable classroom response; the research notebook includes optional website output.

## My limitations

I study historical data with incomplete metadata and uneven user activity. My evaluation favors books and readers with training histories. My limited name normalization does not claim universal identity matching. I do not interpret the prototype as a production recommendation service.

## References

- Beth Muturi, Miami Dade College, CAI2100C, Project 2 class discussion, October 14 and November 2, 2026.
- [GroupLens Book-Crossing dataset](https://grouplens.org/datasets/book-crossing/).
- [Microsoft Learn Book-Crossing walkthrough](https://learn.microsoft.com/en-us/fabric/data-science/retail-recommend-model).
- [scikit-learn: common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html).
- [scikit-learn: nearest neighbors](https://scikit-learn.org/stable/modules/neighbors.html).
