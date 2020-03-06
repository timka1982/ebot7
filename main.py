import argparse


class ServiceFunnel:
    def __init__(self):
        pass

    def scrape_html(self, html: str):
        pass

    def handle_request(self, request: dict) -> dict:
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
