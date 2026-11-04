from pathlib import Path
import json, math, re, nbformat

root=Path(__file__).resolve().parents[1]
results=json.loads((root/'data/results.json').read_text())
web=(root/'data/results.js').read_text().strip()
prefix='window.BOOK_ENGINE_RESULTS = '
assert web.startswith(prefix)
assert json.loads(web[len(prefix):].rstrip(';'))==results
assert len(results['top_books'])==20 and len(results['top_authors'])==20
works={(x['title'].casefold(),x['author'].casefold()) for x in results['top_books']}
assert len(works)==20, 'Duplicate work in book ranking'
assert len({x['author'].casefold() for x in results['top_authors']})==20
assert not any('Ã' in x['author'] for x in results['top_authors']), 'Corrupted top-author text'
assert results['evaluation_protocol'].startswith('Split explicit linked ratings first')
assert results['holdout_pool_rows']>=results['collaborative_evaluable_rows']>100
assert 0<=results['collaborative_neighbor_coverage']<=1
for k in ('collaborative_MAE','collaborative_RMSE','baseline_MAE','baseline_RMSE'):
    assert math.isfinite(results[k]) and results[k]>=0
for name,sha in results['source_sha256'].items():
    assert name in ('Books.csv','Ratings.csv','Users.csv')
    assert re.fullmatch(r'[a-f0-9]{64}',sha)
for group in ('top_books','top_authors'):
    scores=[r['rating'] for r in results[group]]
    assert all(1<=v<=10 for v in scores)
    assert all(a>=b for a,b in zip(scores,scores[1:]))
for p,num in [('academic/Project_2_Course_Submission.ipynb',8),
              ('notebooks/Project_2_Book_Recommendation_Engine.ipynb',9)]:
    nb=nbformat.read(root/p,as_version=4)
    cells=[x for x in nb.cells if x.cell_type=='code']
    assert len(cells)==num
    assert all(x.execution_count is not None for x in cells)
    assert not any(o.output_type=='error' for c in cells for o in c.get('outputs',[]))
    assert chr(0x2014) not in '\n'.join(c.source for c in nb.cells)
for p in ('top-books.png','top-authors.png','model-comparison.png'):
    b=(root/'assets'/p).read_bytes()
    assert len(b)>5000 and b[:8]==bytes.fromhex('89504e470d0a1a0a')

# I cross-check the numbers explained in my README against the values in my executed research.
readme=(root/'README.md').read_text(encoding='utf-8')
for key in ('collaborative_MAE','collaborative_RMSE','baseline_MAE','baseline_RMSE'):
    assert f"{results[key]:.4f}" in readme, 'README metric does not match research results: '+key
assert format(results['collaborative_evaluable_rows'],',') in readme
assert f"{results['collaborative_neighbor_coverage']*100:.2f}%" in readme
assert (root/'docs/PRESENTATION_GUIDE.md').read_text(encoding='utf-8').count('### ') >= 40
assert 'academic/Project_2_Course_Submission.ipynb' in readme

print('PASS: two executed notebooks, ranked works, metrics, source hashes, presentation synchronization')
