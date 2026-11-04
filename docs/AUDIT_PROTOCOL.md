# My preaudit and postaudit record

**Student:** Juan Luna Santibanez | **Course:** CAI2100C-2267-6908

## Preaudit baseline

I verified that `main` began at commit `910e7d8fd5c8d780c05bbf2b700a98afc97eee86`, with a public portfolio, one executed research notebook, a successful notebook workflow and published charts. Historical MAE was 1.2319 and RMSE was 1.6914. Those numbers belonged to an earlier eligibility protocol and cannot be carried into a corrected experiment unchanged.

I observed duplicate title-and-author works in the Top 20, encoding damage in author labels, inconsistent author aliases, test-dependent item selection, missing introductory academic questions and no separately identified academic notebook.

## Calibration decisions

I keep the three sister projects unchanged. I introduce the academic notebook structure used by Project 1, use a training-only eligibility selection for collaborative filtering, repair common display text issues in memory, preserve ISBN-level model inputs, and aggregate work-level Top 20 rankings. I add the data hash, reproducibility controls and first-person question-and-answer guide.

## Three independent acceptance checks

**1. Academic:** My notebook covers the known instruction areas without pretending to be the unretrieved original ZIP. I keep the research extension separate.

**2. Scientific:** Both notebooks must execute; the source records and dataset hashes must be tracked; the Top 20 must contain unique title-author pairs; the holdout must be selected first; evaluated rows, metrics and neighbor coverage must be consistent.

**3. Public presentation:** The JSON and JS data must match; figures must exist; the README and live demo must link to real project files; the first-person guidance must be readable.

The GitHub Actions run is the execution record. A successful commit or Pages build alone is not scientific approval. I cannot guarantee a grade or certify exact correspondence to the unretrieved course ZIP.

## Verified postaudit result

My [GitHub Actions execution 41756624631](https://github.com/SupaHumano/CAI2100C-Book-Recommendation-Engine/actions/runs/41756624631) completed successfully after the calibrated notebooks were introduced. Its steps executed the academic and research notebooks and passed the repository verification script. The workflow wrote executed notebooks, calculated results and figure files back to the repository.

I checked the updated JSON results against the browser JavaScript data. The recalculated warm-start evaluation has **7,547 evaluated pairs** from a holdout pool of **76,769**. My collaborative predictions have **MAE 1.2235** and **RMSE 1.6734**, compared with baseline **MAE 1.3320** and **RMSE 1.6931**. I document **43.01%** neighbor support. These replace the earlier protocol's values.

I verified that both executed notebooks contain zero recorded Python errors, that my first-person guide contains 40 question-and-answer entries, and that a newly separated course-aligned notebook is available. My remaining external checks are direct Colab and Kaggle service execution, public browser navigation, and byte-for-byte comparison with the original Project 2 course ZIP if it becomes available.
