import arxiv

def fetch_arxiv_papers(query, max_results = 3):
    search = arxiv.Search(
        query = query,
        max_results = max_results,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )

    print(f"--- Fetching the latest papers for: '{query}' ---\n")

    for result in search.results():
        print(f"Title: {result.title}")
        print(f"Published: {result.published.date()}")
        print(f"Summary: {result.summary[:150]}")
        print(f"URL: {result.entry_id}")
        print("-" * 50)