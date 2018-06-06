#!/usr/bin/env python3

import psycopg2


"""Its the reporting tool which uses information from database "news"
   returns the result of top aarticle,top author,error on request more than 1 %
   search_engine method connects to the database and
   executes the query which gives back result in list format.
   top_article,top_author,error method uses list displays
   the required output"""

"""Performs query operation from database returns the output in list"""


def search_engine(search):
    try:
        db = psycopg2.connect("dbname=news")
        cursor = db.cursor()
        cursor.execute(search)
        rows = cursor.fetchall()
        db.close()
        return rows
    except Exception as e:
        print("Cannot connect to database")
        print(e)


"""Perform query and print top 3 popular articles"""


def top_article():
    search = """SELECT articles.title,COUNT(log.path) AS views FROM log
                JOIN articles ON log.path
                LIKE CONCAT('/article/',articles.slug)
                WHERE log.status = '200 OK'
                GROUP BY log.path,articles.title
                ORDER BY views DESC LIMIT 3; """

    search_result = search_engine(search)
    print("Popular Article Of All Time")
    print("")
    for i in search_result:
        print(str(i[0]) + "  --------  " + str(i[1]) + "  views  ")


"""Performs query and prints top 3 popular article author"""


def top_author():
    search = """SELECT articles.author,authors.name,COUNT(log.path)
                AS sum_new FROM articles
                JOIN authors ON articles.author = authors.id
                JOIN log ON log.path
                LIKE CONCAT('/article/',articles.slug)
                WHERE log.status = '200 OK'
                GROUP BY articles.author,authors.name
                ORDER BY sum_new DESC LIMIT 3;"""
    search_result2 = search_engine(search)
    print("Popular Authors Of All Time")
    print("")
    for i in search_result2:
        print(str(i[1]) + "  --------  " + str(i[2]) + "  views  ")


"""Perform query and prints day on which
    more than 1% error occured on requests"""


def error():
    search = """SELECT days_total.date_new,
                ROUND((errors.error_list*1.0)/days_total.total_entry,3)
                AS total_perc FROM
                (SELECT time::timestamp::date AS date_new,COUNT(*)
                AS total_entry
                FROM log GROUP BY date_new) AS days_total
                JOIN
                (SELECT time::timestamp::date
                AS date_new,COUNT(*) AS error_list
                FROM log WHERE status = '404 NOT FOUND'
                GROUP BY date_new) AS errors
                ON days_total.date_new = errors.date_new
                WHERE
                ROUND((errors.error_list*1.0)/days_total.total_entry,3) > 0.01;
                """

    search_result3 = search_engine(search)
    print("Request leading to more than 1% error")
    print("")
    for i in search_result3:
        print(str(i[0]) + "  --------  " + str(i[1] * 100) + "%")


print("LOG ANALYSIS")
print("")
top_article()
print("")
top_author()
print("")
error()
