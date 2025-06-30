import requests

def get_user_posts(user_id):
    url = f"https://jsonplaceholder.typicode.com/posts"
    params = {"userId": user_id}
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        posts = response.json()
        print(f"User {user_id} has {len(posts)} posts.")
        for post in posts[:3]:  # Show first 3 posts
            print(f"- {post['title']}")
    else:
        print("Something went wrong.")

# Try with a few user IDs
get_user_posts(1)
