__author__ = 'liangdong'

import sqlite3

DATABASE_NAME = "Assignment7.db"
TABLE_NAME = "review_stats"

class reviewstats:
    def __init__(self, business_id, number_of_pos, number_of_neg, percentage_of_pos, percentage_of_neg):
        self.business_id = business_id
        self.number_of_pos = number_of_pos
        self.number_of_neg = number_of_neg
        self.percentage_of_pos = percentage_of_pos
        self.percentage_of_neg = percentage_of_neg

    def insert_into_database(self):
        conn = sqlite3.connect(DATABASE_NAME)

        conn.execute("INSERT INTO {0} ({1},{2},{3},{4},{5}) VALUES (?,?,?,?,?);".
                     format(TABLE_NAME, "business_id", "number_of_positive_reviews", "number_of_negative_reviews",
                            "percentage_of_positive_reviews", "percentage_of_negative_reviews"),
                     (self.business_id, self.number_of_pos, self.number_of_neg, self.percentage_of_pos,
                      self.percentage_of_neg))
        conn.commit()
        conn.close()
