import psycopg2
from vsd_website.settings import base


class CategoryCount():
    def load_category_count():

        # Get the status of Postgres
        postgres_conn = psycopg2.connect(
            host=base.DATABASES["default"]["HOST"],
            port=base.DATABASES["default"]["PORT"],
            dbname=base.DATABASES["default"]["NAME"],
            user=base.DATABASES["default"]["USER"],
            password=base.DATABASES["default"]["PASSWORD"],
        )

        with postgres_conn.cursor() as cursor:
            cursor.execute("""
            SELECT Trim(Cat.blogCategory) As blogCategory, 
                        Count(*) totalBlogItem
                    FROM app_blog_blogpost As Blog
                        LEFT OUTER JOIN 
                        (SELECT DISTINCT
                        Trim((regexp_split_to_table(category, ',')))
                            As blogCategory
                FROM app_blog_blogpost 
                ORDER BY blogCategory ASC) As Cat
                    ON Blog.category LIKE 
                        concat('%', Cat.blogCategory,'%')
                    GROUP BY Trim(Cat.blogCategory)
                        ORDER BY Trim(Cat.blogCategory) ASC; 
            """)
            
            fields = [field_name[0] for field_name in cursor.description]
            select = [dict(zip(fields, row)) for row in cursor.fetchall()]
            cursor.close()
            return select
