from datetime import datetime


def upsert_feed(cursor, feed, feed_type):
    cursor.execute("""
        INSERT IGNORE INTO feeds (title, xml_url, html_url, type)
        VALUES (%s, %s, %s, %s)
    """, (
        feed["title"],
        feed["xml_url"],
        feed["html_url"],
        feed_type
    ))

    cursor.execute("""
        SELECT id FROM feeds WHERE xml_url = %s
    """, (feed["xml_url"],))

    result = cursor.fetchone()

    if not result:
        return None

    return result[0]


def insert_entry(cursor, feed_id, entry):
    try:
        cursor.execute("""
            INSERT INTO entries
            (feed_id, title, link, published, summary, content, guid)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            feed_id,
            entry["title"],
            entry["link"],
            entry["published"],
            entry["summary"],
            entry["content"],
            entry["guid"]
        ))

        return True

    except Exception:
        return False


def update_feed_scan_time(cursor, feed_id):
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        UPDATE feeds
        SET last_updated = %s
        WHERE id = %s
    """, (now, feed_id))
