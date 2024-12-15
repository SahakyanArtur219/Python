import requests

base_url = "https://jsonplaceholder.typicode.com"

def count_words_in_title(title):
    return len(title.split())


def count_lines_in_body(body):
    return body.count("\n") + 1




def get_filtered_posts():

    response = requests.get(f"{base_url}/posts")
    if response.status_code == 200:
        posts = response.json()
        filtered_posts = []
        for post in posts:
            if count_words_in_title(post['title']) <= 6 and count_lines_in_body(post['body']) <= 3:
                filtered_posts.append(post)

        print(f"Filtered Posts ({len(filtered_posts)}):", filtered_posts)
    else:
        print("GET request failed!")

def create_post():
    new_post = {
        "title": "New post for NPUA",
        "body": "Best university ever.",
        "userId": 219
    }
    response = requests.post(f"{base_url}/posts", json=new_post)
    if response.status_code == 201:
        print("Post Created:", response.json())
    else:
        print("POST request failed!")

def update_post(post_id):
    updated_post = {
        "id": post_id,
        "title": "Updated Post Title",
        "body": "Updated post body.",
        "userId": 1
    }
    response = requests.put(f"{base_url}/posts/{post_id}", json=updated_post)
    if response.status_code == 200:
        print("Post Updated:", response.json())
    else:
        print("PUT request failed!")

def delete_post(post_id):
    response = requests.delete(f"{base_url}/posts/{post_id}")
    if response.status_code == 200:
        print(f"Post {post_id} deleted successfully!")
    else:
        print("DELETE request failed!")

if __name__ == "__main__":


    print("\n GET Filtered Posts: ")
    get_filtered_posts()

    print("\n POST Create New Post: ")
    create_post()

    print("\n PUT Update Post: ")
    update_post(1)

    print("\n DELETE Post: ")
    delete_post(1)
