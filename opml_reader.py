import opml


def read_feeds_from_opml(opml_path):
    outline = opml.parse(opml_path)
    feeds = []

    for item in outline:
        xml_url = getattr(item, "xmlUrl", None)

        if not xml_url:
            continue

        feeds.append({
            "title": getattr(item, "text", "Untitled"),
            "xml_url": xml_url,
            "html_url": getattr(item, "htmlUrl", None)
        })

    return feeds
