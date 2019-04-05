from xgoogle.search import GoogleImageSearch, SearchError
import webbrowser


def get_image_url(term):
    try:
        gs = GoogleImageSearch(term)
        gs.results_per_page = 1
        results = gs.get_results()
        for res in results:
            return res.trumb
    except SearchError as e:
        print("Search failed: %s" % e)


if __name__ == '__main__':
    url = get_image_url('dog')
    print(url)
    webbrowser.open(url)
