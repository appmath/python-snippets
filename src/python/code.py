users_list_resp, resp, err = await get_user()

# Check for errors
if err is not None:
    print(f"Error occurred: {err}")
else:
    # Assuming users_list_resp is correctly populated
    # If it's a list of users
    if isinstance(users_list_resp, list) and len(users_list_resp) > 0:
        user_id = users_list_resp[0].id  # Accessing the first user's ID
        print(f"First user ID: {user_id}")
    # If it's a single user object
    elif hasattr(users_list_resp, 'id'):
        user_id = users_list_resp.id
        print(f"User ID: {user_id}")
    else:
        print("Unexpected response format or empty list.")
