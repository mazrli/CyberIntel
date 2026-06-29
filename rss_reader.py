import feedparser
from hashlib import md5
from dateutil import parser as date_parser


def parse_date(value):
    if not value:
        return None

    try:
        dt = date_parser.parse(value)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return None


def build_guid(entry):
    raw = (
        entry.get("id")
        or entry.get("guid")
        or entry.get("link")
        or entry.get("title")
    )

    if not raw:
        return None

    return md5(raw.encode("utf-8")).hexdigest()


def read_entries(xml_url):
    parsed = feedparser.parse(xml_url)
    entries = []

    for entry in parsed.entries:
        guid = build_guid(entry)

        if not guid:
            continue

        content = ""

        if entry.get("content"):
            content = entry.get("content", [{}])[0].get("value", "")

        entries.append({
            "title": entry.get("title", "Untitled"),
            "link": entry.get("link"),
            "published": parse_date(
                entry.get("published")
                or entry.get("updated")
                or entry.get("created")
            ),
            "summary": entry.get("summary", ""),
            "content": content,
            "guid": guid
        })

    return entries