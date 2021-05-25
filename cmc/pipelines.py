import psycopg2
from cmc.settings import DATABASE_HOST, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD, DATABASE_PORT


class DatabasePipeline(object):

    def open_spider(self, spider):
        self.connection = psycopg2.connect(
            host=DATABASE_HOST,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
            dbname=DATABASE_NAME,
            port=DATABASE_PORT
        )
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cur.execute('INSERT INTO coins(name, ticker, link) VALUES (%s, %s, %s)', (item['name'], item['ticker'], item['link']))
            self.connection.commit()
            return item
        except Exception:
            pass
