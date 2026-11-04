# My Book Recommendation Engine: 40 questions and answers

**Juan Luna Santibanez | CAI2100C-2267-6908 | Professor Beth Muturi**

I use these answers to explain my actual decisions in first person. This is a study guide, not an extra assignment requirement.

### 1. What is my project about?

I am comparing two ways of suggesting books based on their metadata and on patterns of readers' explicit ratings.

### 2. What is my project goal?

I want to build a reproducible educational recommendation engine and explain what each method can and cannot conclude.

### 3. Where can I acquire data?

I can obtain data from academic collections, authorized service records and public dataset repositories. I verify data format, permissions and provenance.

### 4. What kinds of machine learning are relevant?

I distinguish supervised, unsupervised and reinforcement learning. My two recommenders focus on metadata similarity and collaborative patterns.

### 5. Where is artificial intelligence useful?

I see it in navigation, accessibility, fraud monitoring, search, learning tools and relevant recommendations.

### 6. Why do I use three CSV tables?

I use Books to describe each book, Ratings to connect readers with books and Users for the available anonymized user information.

### 7. What is an ISBN?

I use ISBN as a text identifier for a book edition. I avoid converting it into an integer because leading zeros can be meaningful.

### 8. What does a rating of zero mean?

I treat zero as implicit interaction, not a zero-star dislike. I use explicit one-to-ten ratings for numeric prediction.

### 9. Why do I clean text encoding?

I repair broken accents, HTML entities and spacing so the displayed rankings better represent actual titles and authors.

### 10. Why do I normalize certain author names?

I consolidate a small, verifiable set of spelling and punctuation variants, without pretending to solve author identity for every record.

### 11. Why are editions relevant?

I can find two ISBN records for the same written work. I aggregate titles and authors for my work-level ranking but retain ISBN keys for the collaborative model.

### 12. What are the Top 20 books?

I rank title-and-author works using their average explicit scores after a minimum review-count requirement. I do not interpret this as global sales or literary quality.

### 13. What are the Top 20 authors?

I rank author names by the average explicit ratings linked to their recorded books, after applying a minimum review-count threshold.

### 14. Why use minimum review counts?

I want a title with one ten-star score to receive less weight than one with many consistently high reviews. This threshold is a transparent heuristic.

### 15. What is Content-Based Filtering?

I compare the text information available for books using TF-IDF and cosine similarity.

### 16. What does TF-IDF do?

I convert book metadata into numeric text features and emphasize terms that are more distinctive across the available catalog.

### 17. What does cosine similarity mean?

I measure the alignment of two feature vectors. I do not treat cosine similarity as a one-to-ten user rating.

### 18. Why do I use metadata rather than descriptions?

I only use fields that exist in my three input files. I do not invent genres, summaries or book descriptions.

### 19. What is Collaborative Filtering?

I estimate a reader's preferences by comparing how books were rated by readers and using the reader's available training history.

### 20. Why use a sparse matrix?

I avoid allocating a large dense table of missing ratings, because most user-book pairs have no recorded score.

### 21. What is an item-item neighborhood?

I find other books whose recorded rating patterns are similar to the target book and use the reader's known ratings of those neighbors.

### 22. How do the two recommendation methods differ?

My first approach compares item characteristics. My second approach uses rating behavior. They answer different questions.

### 23. How do I avoid test-data leakage?

I first reserve a holdout from all linked explicit ratings and then choose eligible books and readers using the development partition only.

### 24. Why is the evaluation a warm-start experiment?

I can evaluate only held-out pairs with enough training history for both the reader and the item. I report that population rather than generalizing to every reader.

### 25. Why do I use a baseline?

I compare my collaborative predictions with a simple book-average estimate to see whether the more complex method adds measurable value.

### 26. What is MAE?

I measure the average absolute number of rating points by which my predictions differ from the held-out ratings.

### 27. What is RMSE?

I take the square root of the mean squared error, which gives larger mistakes extra influence.

### 28. How do I interpret mixed MAE and RMSE results?

I report both honestly and do not claim that the collaborative model wins on every measure if the values disagree.

### 29. What is neighbor coverage?

I count the fraction of evaluated predictions that use useful rated neighbors instead of the average-rating fallback.

### 30. What is the cold-start problem?

I have limited evidence for a new reader or new book. My current candidate filters also restrict coverage of completely new, unrated books.

### 31. What does my website actually do?

I present stored results calculated by the Python notebooks. The site does not fit a new scikit-learn model in the visitor's browser.

### 32. Why do I record the SHA-256 input hashes?

I can tell whether two experiments used the same input file bytes instead of merely assuming matching filenames mean matching data.

### 33. Can I claim the public mirror is the professor's original file?

No. I use a documented public Book-Crossing copy when the class files are unavailable and keep that distinction explicit.

### 34. Is my academic notebook the instructor's original template?

No. I created a course-aligned response based on verified instructions, not a byte-identical copy of the unretrieved Project 2 ZIP.

### 35. Why do I keep a separate academic notebook?

I want the professor to find the course workflow without having to inspect optional portfolio features or website-export code.

### 36. What are the limitations of my results?

I use historical, sparse ratings and a constrained warm-start subset. My results are educational measurements, not evidence of production performance.

### 37. What would I improve before deployment?

I would examine fairness, privacy, new-user and new-book coverage, monitoring and time-aware validation on new interactions.

### 38. How would I explain the six project stages?

I identify the problem, acquire the data, prepare and explore the records, build the recommenders, evaluate the predictions and discuss responsible deployment.

### 39. What should I verify before Canvas submission?

I check the actual due date, file or URL format, team requirements, notebook outputs and permissions for Professor Muturi to open the work.

### 40. What did I learn?

I learned that transparent data cleaning, evaluation design and baseline comparisons matter as much as the recommendation algorithm itself.

