import arxiv

def fetch_arxiv_papers(query, max_results = 3):
    search = arxiv.Search(
        query = query,
        max_results = max_results,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )