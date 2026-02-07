from datetime import timedelta


DB_URI = "mysql+aiomysql://root:root@127.0.0.1:3306/zhiliao_ainame?charset=utf8mb4"


# 邮箱相关配置
MAIL_USERNAME="jlwang1998@163.com"
MAIL_PASSWORD="GFT6YTR4MpRVehVY"
MAIL_FROM="jlwang1998@163.com"
MAIL_PORT=465
MAIL_SERVER="smtp.163.com"
MAIL_FROM_NAME="jlwang"
MAIL_STARTTLS=False
MAIL_SSL_TLS=True


JWT_SECRET_KEY = "sfsadadafsjw"
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=15)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

