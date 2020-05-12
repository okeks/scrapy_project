# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# import sqlite3
#
#
# class QuotetutorialPipeline(object):
#
#     def __init__(self):
#         self.create_connection()
#         self.create_table()
#     # create a connection and cursor in the class
#
#     def create_connection(self):
#         self.conn = sqlite3.connect("myquotes.db")
#         self.curr = self.conn.cursor()
#
#     #create a table if it does not exist
#
#     def create_table(self):
#         self.curr.execute("""DROP TABLE IF EXISTS quotes_table""")
#         self.curr.execute("""CREATE TABLE quotes_table(
#         title text,
#         author text,
#         tags text
#         )""")
#
#  #storing our items in the database
#
#     def process_item(self, item, spider):
#         self.store_db(item)
#         #print("Pipelines " + item['title'][0])
#         return item
#
#     def store_db(self, item):
#         self.curr.execute("""INSERT INTO quotes_table values (?,?,?)""", (
#             item['title'][0], item['author'][0], item['tags'][0]))
#         self.conn.commit()
#
# import mysql.connector
#
#
# class QuotetutorialPipeline(object):
#
#     def __init__(self):
#         self.create_connection()
#         self.create_table()
#     # create a connection and cursor in the class
#
#     def create_connection(self):
#         self.conn = mysql.connector.connect(
#             host ='localhost',
#             user = 'root',
#             passwd = 'Prince009#',
#             database = 'myquotes'
#
#         )
#
#         self.curr = self.conn.cursor()
#
#     #create a table if it does not exist
#
#     def create_table(self):
#         self.curr.execute("""DROP TABLE IF EXISTS quotes_table""")
#         self.curr.execute("""CREATE TABLE quotes_table(
#         title text,
#         author text,
#         tags text
#         )""")
#
#  #storing our items in the database
#
#     def process_item(self, item, spider):
#         self.store_db(item)
#         #print("Pipelines " + item['title'][0])
#         return item
#
#     def store_db(self, item):
#         self.curr.execute("""INSERT INTO quotes_table values (%s,%s,%s)""", (
#             item['title'][0], item['author'][0], item['tags'][0]))
#         self.conn.commit()
#
import psycopg2
from psycopg2 import Error

class QuotetutorialPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()
    # create a connection and cursor in the class

    def create_connection(self):
        self.conn = psycopg2.connect(
            user = 'postgres',
            password = 'prince009',
            host = 'localhost',
            port = 5432,
            database = 'myquotes'
        )
        self.curr = self.conn.cursor()

    #create a table if it does not exist

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_table""")
        self.curr.execute("""CREATE TABLE quotes_table(
        title text,
        author text,
        tags text
        )""")

 #storing our items in the database

    def process_item(self, item, spider):
        self.store_db(item)
        #print("Pipelines " + item['title'][0])
        return item

    def store_db(self, item):
        self.curr.execute("""INSERT INTO quotes_table values (%s,%s,%s)""", (
            item['title'][0], item['author'][0], item['tags'][0]))
        self.conn.commit()

