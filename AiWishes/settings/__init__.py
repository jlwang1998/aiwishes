from datetime import timedelta


DB_URI = "mysql+aiomysql://root:123456@127.0.0.1:3306/aiwishes?charset=utf8mb4"


# 邮箱相关配置
MAIL_USERNAME="jlwang1998@163.com"
MAIL_PASSWORD="GFT6YTR4MpRVehVY"
MAIL_FROM="jlwang1998@163.com"
MAIL_PORT=465
MAIL_SERVER="smtp.163.com"
MAIL_FROM_NAME="jlwang"
MAIL_STARTTLS=False
MAIL_SSL_TLS=True

# JWT_SECRET_KEY：JWT签名密钥
# 作用：用于签名和验证JWT令牌的密钥，确保令牌的完整性和安全性
JWT_SECRET_KEY = "sfsadadafsjw"
# JWT_ACCESS_TOKEN_EXPIRES：访问令牌的过期时间
# 值：timedelta(days=15) 表示15天的时间间隔
# 作用：设置访问令牌的有效期为15天
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=15)
# JWT_REFRESH_TOKEN_EXPIRES：刷新令牌的过期时间
# 值：timedelta(days=30) 表示30天的时间间隔
# 作用：设置刷新令牌的有效期为30天
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

#大模型api_key
DeepSeek_API_KEY = "sk-***********************"

