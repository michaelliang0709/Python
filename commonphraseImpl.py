__author__ = 'liangdong'

import sqlite3

DATABASE_NAME = "Assignment7.db"
TABLE_NAME = "common_phrases"

class commonphraseImpl:
    def __init__(self, review_id, business_id, common_phrase, frequency_of_phrase):
        self.review_id = review_id
        self.business_id = business_id
        self.common_phrase = common_phrase
        self.frequency_of_phrase = frequency_of_phrase

    def insert_into_database(self):
        conn = sqlite3.connect(DATABASE_NAME)
        conn.execute("INSERT INTO {0} ({1},{2},{3},{4}) VALUES (?,?,?,?);".
                     format(TABLE_NAME, "review_id", "business_id", "common_phrase", "frequency_of_phrase"),
                     (self.review_id, self.business_id, self.common_phrase, self.frequency_of_phrase))
        conn.commit()
        conn.close()
