import psycopg2                                                 # STEP 1
import psycopg2.extras as ext                                   # STEP 2

def run_sql(sql, values = None):                                # STEP 3
    
    conn = None
    results = []

    try:
        conn = psycopg2.connect ("dbname='music_manager'")       # USED TO CONNECT TO DATABASE
        cur = conn.cursor (cursor_factory=ext.DictCursor)
        cur.execute (sql, values) 
        conn.commit ()                                          # SAVES/COMMITS DB CHANGES
        results = cur.fetchall()
        cur.close ()                                            # CLOSES DB CONNECTION

    except (Exception, psycopg2.DatabaseError) as error:
        print (error)
    
    finally:
        if conn is not None:
            conn.close()
    
    return results