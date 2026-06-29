import mysql.connector
from config import DB_CONFIG


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


def create_tables(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feeds (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title TEXT,
            xml_url VARCHAR(1000) UNIQUE,
            html_url VARCHAR(1000),
            type VARCHAR(100),
            last_updated DATETIME
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            feed_id INT NOT NULL,
            title TEXT,
            link VARCHAR(1000),
            published DATETIME NULL,
            summary TEXT,
            content LONGTEXT,
            guid VARCHAR(255) UNIQUE,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (feed_id) REFERENCES feeds(id)
        )
    """)
