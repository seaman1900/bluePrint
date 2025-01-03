# BluePrint

pip install streamlit streamlit_authenticator

streamlit run home.py

# 数据说明
## 用户数据
```json
{
    "user_id": "0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2",
    "username": "Rex",
    "email": "rex@example.com",
    "password_hash": "hashed_password_here",
    "registration_date": "2022-01-01T00:00:00Z",
    "last_login": "2023-10-01T12:34:56Z",
    "is_admin": true,
    "roles": ["admin", "content_creator"],
    "permissions": ["create_content", "delete_content", "manage_users"],
    "avatar_url": "https://cdn.img2ipfs.com/ipfs/QmQKq7c7jmmZpPjof7gmUQhjBoScYmD3KUW73Wj7eJtcEY?filename=myxj.jpg",
    "balance": 10,
    // 个人介绍
    "profile": {
        "description": "I am a blockchain developer.",
        "location": "New York, USA",
        "website": "https://rex.com",
        "bio": "Passionate about blockchain and decentralized technologies."
    },
    // 已购内容清单
    "shop_list": [
        {
            "content_id": "001",
            "added_time": "2022-01-01T00:00:00Z"
        }
    ],
    // 已收藏内容清单(想买但没买的内容)
    "mark_list": [
        {
            "content_id": "001",
            "added_time": "2022-01-01T00:00:00Z"
        }
    ],
    // 用户已认证的支付方式
    "payment_methods": ["Alipay", "WechatPay", "BankCard"],
    // 用户的投资内容清单
    "investments": [
        {
            "invest_id": "001",
            "invest_amount": 1000,
            "invest_time": "2022-01-01T00:00:00Z",
            "invest_type": "ad",
            "profit": 0
        }
    ],
    // 用户的充值、提现记录: charge充值 withdraw提现
    "orders": [
        {
            "order_id": "001",
            "order_amount": 1000,
            "order_time": "2022-01-01T00:00:00Z",
            "order_status": "paid",
            "order_type": "charge",
            "payment_method": "Alipay"
        }
    ],
    // 如果未来需要扩展功能（如用户等级、积分系统等），预留一些字段
    "metadata": {
        "user_level": "vip",
        "points": 1000,
        "preferences": {
            "language": "en",
            "theme": "dark"
        }
    }
}
```
## 内容数据
```json
{
    "content_id": "0001",
    "title": "hello world",
    "author_id": "0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2",
    "created_at": "2022-12-12T12:00:00Z",
    "price": 0.1,
    "description": "hello world, fucking code",
    "content_body": "hello world, fucking code",
    "metadata": {
        "views": 100000,
        "comments": 224,
        "likes": 1200,
        "dislikes": 12,
        "shares": 500
    },
    "pricing_type": "free",
    "tags": ["funny", "code"],
    "comments": ["12345", "67890"],
    "status": "approved"
}
```
## 评论数据

```json
{
    "comment_id": "12345",
    "user_id": "67890",
    "username": "JohnDoe",
    "avatar_url": "https://example.com/avatar.jpg",
    "content": "这是一个评论示例。",
    "media": [
      {
        "type": "image",
        "url": "https://example.com/image.jpg"
      }
    ],
    "timestamp": "2023-10-01T12:34:56Z",
    "updated_at": "2023-10-01T12:35:10Z",
    "likes": 10,
    "dislikes": 2,
    "replies": 3,
    "parent_comment_id": null,
    "root_comment_id": null,
    "status": "approved",
    "is_deleted": false
}
```

## 脚注
### status各个值的含义
approved（已审核）
已通过审核，对所有人可见。
pending（待审核）:
尚未审核，通常对普通用户不可见，仅管理员或审核人员可见。
rejected（已拒绝）:
未通过审核，通常是因为内容违规或不合适，对所有人不可见。
deleted（已删除）:
被删除，通常对所有人不可见，但可能在数据库中保留记录。
flagged（被标记）:
被用户标记为有问题，需要管理员进一步检查。
hidden（已隐藏）:
被隐藏，通常是因为违反了某些规则，但对管理员可见。