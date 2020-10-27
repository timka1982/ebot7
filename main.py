from bs4 import BeautifulSoup
import argparse


class ServiceFunnel:
    def __init__(self):
        pass

    def scrape_html(self, html: str):
        """
        Scrape HTML, extract tags and snippet and store them in an appropriate data structure.
        
        Args:
            html (str) : Entire HTML content. Not the path to HTML document.
        """
        index = 0
        snippets_dict = {}
        soup = BeautifulSoup(html, 'lxml')

        for tag in soup.find_all():
            for attr in tag.attrs:
                if 'data-tags' == attr:
                    index = index + 1
                    snippets_dict[str(index)] = {}
                    snippets_dict[str(index)]['snippet'] = "<{}> {} </{}>".format(tag.attrs['class'][0], tag.text, tag.attrs['class'][0])
                    data_tags = [item.strip() for item in tag.attrs['data-tags'].split(',')]
                    snippets_dict[str(index)]['data-tags'] = sorted(data_tags)
                    break


    def handle_request(self, request: dict) -> dict:
        """
        Find out the correct snippet that maps to a set of input tags.
        
        Args:
            request (dict): Request object as specified in the readme.
        Returns:
            response (dict): Response object as specified in the readme.
        """
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--html_path",
        help="path leading to the html file",
        type=str,
        required=True,
    )
    args = parser.parse_args()
    with open(args.html_path, "r") as f:
        html_str = f.read()
    service_funnel = ServiceFunnel()
    service_funnel.scrape_html(html_str)
