import web

db_host = 'z1ntn1zv0f1qbh8u.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 's3icpvk5swtsrx6f'
db_user = 'c2410og4t3mifdju'
db_pw = 'obq28rtba4cgb8dv'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )
