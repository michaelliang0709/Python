__author__ = 'liangdong'

import sqlite3

DATABASE_NAME = "Assignment7.db"
TABLE_NAME = "sentiment"

class sentimentImpl:
    def __init__(self, review_id, business_id, sentiment):
        self.review_id = review_id
        self.business_id = business_id
        self.sentiment = sentiment

    def insert_into_database(self):
        conn = sqlite3.connect(DATABASE_NAME)

        conn.execute("INSERT INTO {0} ({1},{2},{3}) VALUES (?,?,?);".
                     format(TABLE_NAME, "review_id", "business_id", "sentiment"),
                     (self.review_id, self.business_id, self.sentiment))
        conn.commit()
        conn.close()
