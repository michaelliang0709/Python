__author__ = 'liangdong'

import sqlite3
from sentimentImpl import *
from reviewstats import *
from commonphraseImpl import *
import textblobImpl

DATABASE_NAME1 = "reviews.db"
DATABASE_NAME2 = "Assignment7.db"

def main():
    input = prompt()
    business_name = input[0]
    option = input[1]
    # whether the database for this assignment has been built
    done = False
    while option != 7:
        # build the database
        if done == False:
            limit = int(raw_input("Please set a limit for the number of reviews: "))
            build_sentiment(limit)
            build_review_stats(limit)
            build_common_phrases(limit)
            done = True
        if option == 1:
            number = option1(business_name)
            print "The number of positive reviews is: ", number[0]
            print "The number of negative reviews is: ", number[1]
            print "The percentage of positive reviews is: ", number[3]
            print "The percentage of negative reviews is: ", number[4]
        elif option == 2:
            n = int(raw_input("Please set the number of examples. n = ? "))
            option2(business_name, n)
        elif option == 3:
            n = int(raw_input("Please set the number of examples. n = ? "))
            option3(business_name, n)
        elif option == 4:
            n = int(raw_input("Please set the number of examples. n = ? "))
            option4(business_name, n)
        elif option == 5:
            n = int(raw_input("Please set the number of examples. n = ? "))
            option5(business_name, n)
        elif option == 6:
            n = int(raw_input("Please set the number of examples. n = ? "))
            option6(business_name, n)
        input = prompt()
        business_name = input[0]
        option = input[1]
    exit(0)

# build the table sentiment
def build_sentiment(limit):
    conn = sqlite3.connect(DATABASE_NAME1)
    sql = "select review_id, business_id, text from yelp_review limit %d" % (limit)
    rows = conn.execute(sql)
    conn.commit()
    for row in rows:
        review_id = row[0]
        business_id = row[1]
        text = row[2]
        sentiment_instance = sentimentImpl(review_id, business_id, textblobImpl.analyze(text))
        sentiment_instance.insert_into_database()
    conn.close()

# build the table review_stats
def build_review_stats(limit):
    conn = sqlite3.connect(DATABASE_NAME1)
    sql1 = "select business_id from yelp_business limit %d" % (limit)
    rows = conn.execute(sql1)
    conn.commit()
    business_id = []
    for row in rows:
        business_id.append(row[0])
    business_name = []
    # get business_name by business_id in sequence
    for id in business_id:
        sql2 = "select name from yelp_business where business_id = " + "'" + id + "'"
        rows = conn.execute(sql2)
        conn.commit()
        for row in rows:
            business_name.append(row[0])
    # construct instances of reviewstats
    for i in range(0, len(business_id)-1):
        number = option1(business_name[i])
        if number[2] != 0:
            review_stats = reviewstats(business_id[i], number[0], number[1], number[3], number[4])
            review_stats.insert_into_database()
    conn.close()

# build the table common_phrases
def build_common_phrases(limit):
    conn = sqlite3.connect(DATABASE_NAME1)
    sql = "select review_id, business_id, text from yelp_review limit %d" % (limit)
    rows = conn.execute(sql)
    conn.commit()
    review_ids = []
    business_ids = []
    texts = []
    common_phrases = dict()
    for row in rows:
        review_ids.append(row[0])
        business_ids.append(row[1])
        texts.append(row[2])
    for text in texts:
        # delete whitespaces
        text = text.replace('\n', ' ')
        text = text.replace('\t', ' ')
        words = text.rstrip().split(' ')
        for word in words:
            # use a dictionary to store phrases and their frequency
            if word != "":
                if word not in common_phrases:
                    common_phrases[word] = 1
                else:
                    common_phrases[word] += 1
    # construct instances of commonphraseImpl
    for key in common_phrases:
        for i in range(0, len(texts)-1):
            if key in texts[i]:
                common_phrase = commonphraseImpl(review_ids[i], business_ids[i], key, common_phrases[key])
                common_phrase.insert_into_database()
    conn.close()

# show the number of pos and neg reviews and their percentage
def option1(business_name):
    business_id = getbusiness_id(business_name)
    conn = sqlite3.connect(DATABASE_NAME2)
    sql1 = "select count (review_id) from sentiment where sentiment = 'pos' and business_id = " + "'" + business_id + "'"
    sql2 = "select count (review_id) from sentiment where sentiment = 'neg' and business_id = " + "'" + business_id + "'"
    sql3 = "select count (review_id) from sentiment where business_id = " + "'" + business_id + "'"
    number = []
    num1 = conn.execute(sql1)
    num2 = conn.execute(sql2)
    num3 = conn.execute(sql3)
    conn.commit()
    # use a list to store number of pos and neg reviews and their percentage
    for row in num1:
        number.append(row[0])
    for row in num2:
        number.append(row[0])
    for row in num3:
        number.append(row[0])
    if number[2] != 0:
        number.append(float(number[0]) / float(number[2]))
        number.append(float(number[1]) / float(number[2]))
    conn.close()
    return number

# find the top n common phrases
def option2(business_name, n):
    business_id = getbusiness_id(business_name)
    conn = sqlite3.connect(DATABASE_NAME2)
    sql = "select distinct common_phrase from common_phrases where business_id = '%s' order by frequency_of_phrase desc limit %d" % (business_id, n)
    rows = conn.execute(sql)
    conn.commit()
    common_phrase = []
    for row in rows:
        common_phrase.append(row[0])
    for phrase in common_phrase:
        print phrase
    conn.close()

# find the top n common phrases for pos reviews
def option3(business_name, n):
    business_id = getbusiness_id(business_name)
    conn = sqlite3.connect(DATABASE_NAME2)
    sql = "select distinct common_phrase from common_phrases where business_id = '%s' and " \
          "review_id = (select review_id from sentiment where sentiment = 'pos')order by frequency_of_phrase desc limit %d" % (business_id, n)
    rows = conn.execute(sql)
    conn.commit()
    common_phrase = []
    for row in rows:
        common_phrase.append(row[0])
    for phrase in common_phrase:
        print phrase
    conn.close()

# find the top n common phrases for neg reviews
def option4(business_name, n):
    business_id = getbusiness_id(business_name)
    conn = sqlite3.connect(DATABASE_NAME2)
    sql = "select distinct common_phrase from common_phrases where business_id = '%s' and " \
          "review_id = (select review_id from sentiment where sentiment = 'neg')order by frequency_of_phrase desc limit %d" % (business_id, n)
    rows = conn.execute(sql)
    conn.commit()
    common_phrase = []
    for row in rows:
        common_phrase.append(row[0])
    for phrase in common_phrase:
        print phrase
    conn.close()

# find examples of pos reviews
def option5(business_name, n):
    business_id = getbusiness_id(business_name)
    conn = sqlite3.connect(DATABASE_NAME2)
    sql = "select review_id from sentiment where sentiment = 'pos' and business_id = " + "'" + business_id + "'"
    num = conn.execute(sql)
    conn.commit()
    review_id = []
    for row in num:
        review_id.append(row[0])
    conn.close()
    conn2 = sqlite3.connect(DATABASE_NAME1)
    review_text = []
    for review in review_id:
        sql = "select text from yelp_review where review_id = " + "'" + review + "'"
        texts = conn2.execute(sql)
        conn2.commit()
        for text in texts:
            review_text.append(text[0])
    # if the limit is bigger than the number of reviews, show all reviews
    if len(review_text) < n:
        n = len(review_text)
    if len(review_text) == 0:
        print "No such reviews"
    else:
        for i in range(0, n):
            print review_text[i] + "\n\n"
    conn2.close()

# find examples of neg reviews
def option6(business_name, n):
    business_id = getbusiness_id(business_name)
    conn = sqlite3.connect(DATABASE_NAME2)
    sql = "select review_id from sentiment where sentiment = 'neg' and business_id = " + "'" + business_id + "'"
    num = conn.execute(sql)
    conn.commit()
    review_id = []
    for row in num:
        review_id.append(row[0])
    conn.close()
    conn2 = sqlite3.connect(DATABASE_NAME1)
    review_text = []
    for review in review_id:
        sql = "select text from yelp_review where review_id = " + "'" + review + "'"
        texts = conn2.execute(sql)
        conn2.commit()
        for text in texts:
            review_text.append(text[0])
    # if the limit is bigger than the number of reviews, show all reviews
    if len(review_text) < n:
        n = len(review_text)
    if len(review_text) == 0:
        print "No such reviews"
    else:
        for i in range(0, n):
            print review_text[i] + "\n\n"
    conn2.close()

# get business_id by business_name
def getbusiness_id(business_name):
    conn = sqlite3.connect(DATABASE_NAME1)
    sql = "select business_id from yelp_business where name = " + "\"" + business_name + "\""
    rows = conn.execute(sql)
    conn.commit()
    business_id = ""
    for row in rows:
        business_id = row[0]
    conn.close()
    return business_id

# get user's input
def prompt():
    business_name_input = raw_input("\nPlease enter the name of a business: ")
    option = int(input('''Please choose an option:
    1. Show the number of positive and negative reviews, the percentage of positive and negative reviews
    2. Show the top n common phrases
    3. Show the top n common phrases for positive reviews
    4. Show the top n common phrases for negative reviews
    5. Show examples of positive reviews
    6. Show examples of negative reviews
    7. Exit\n'''))
    # use a list to store the business_name and user's option
    input_list = []
    input_list.append(business_name_input)
    input_list.append(option)
    return input_list

main()
