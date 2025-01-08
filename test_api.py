import requests
from datetime import datetime

# API 基础URL
BASE_URL = "http://127.0.0.1:8000"

# 测试用户注册
def test_register():
    url = f"{BASE_URL}/user/register"
    data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword"
    }
    response = requests.post(url, json=data)
    print("Register Response:", response.json())
    return response.json().get("user_id")

# 测试用户登录
def test_login(username, password):
    url = f"{BASE_URL}/user/login"
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(url, json=data)
    print("Login Response:", response.json())
    return response.json().get("user_id")

# 测试创建付费内容
def test_create_print(user_id):
    url = f"{BASE_URL}/print/create"
    data = {
        "content_id": "",
        "title": "hello world",
        "author_id": user_id,
        "created_at": datetime.now().isoformat(),
        "price": 0.1,
        "description": "hello world, fucking code",
        "content_body": "hello world, fucking code",
        "metadata": {
            "views": 0,
            "comments": 0,
            "likes": 0,
            "dislikes": 0,
            "shares": 0
        },
        "pricing_type": "free",
        "tags": ["funny", "code"],
        "comments": [""],
        "status": "approved"
    }
    response = requests.post(url, json=data)
    print("Create Print Response:", response.json())
    return response.json().get("content_id")

# 测试创建投资
def test_create_investment(user_id, content_id):
    url = f"{BASE_URL}/invest/create"
    data = {
        "invest_id": "001",
        "user_id": user_id,
        "content_id": content_id,
        "invest_amount": 1000,
        "invest_time": datetime.now().isoformat(),
        "invest_type": "Ad Placement",
        "profit": 0
    }
    response = requests.post(url, json=data)
    print("Create Investment Response:", response.json())
    return response.json().get("invest_id")

# 测试获取用户的所有投资
def test_get_user_investments(user_id):
    url = f"{BASE_URL}/invest/user/{user_id}"
    response = requests.get(url)
    print("User Investments Response:", response.json())

# 测试获取单个投资的详细信息
def test_get_investment(invest_id):
    url = f"{BASE_URL}/invest/{invest_id}"
    response = requests.get(url)
    print("Investment Details Response:", response.json())

# 主函数
def main():
    # 测试注册
    user_id = test_register()
    
    # 测试登录
    test_login("testuser", "testpassword")
    
    # 测试创建付费内容
    content_id = test_create_print(user_id)
    
    # 测试创建投资
    invest_id = test_create_investment(user_id, content_id)
    
    # 测试获取用户的所有投资
    test_get_user_investments(user_id)
    
    # 测试获取单个投资的详细信息
    test_get_investment(invest_id)

if __name__ == "__main__":
    main()