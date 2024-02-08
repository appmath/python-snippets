users_list_resp, resp, err = await get_user()

# Check for errors first
if err is not None:
    print(f"Error occurred: {err}")
    # Handle the error appropriately
else:
    # Assuming resp has a status or similar attribute to indicate success
    if resp.status == 200:  # Example, adjust based on actual attribute
        # Check if users_list_resp is a list and not empty
        if isinstance(users_list_resp, list) and len(users_list_resp) > 0:
            user_id = users_list_resp[0].id
            print(f"First user ID: {user_id}")
        elif hasattr(users_list_resp, 'id'):  # It's a single user object
            user_id = users_list_resp.id
            print(f"User ID: {user_id}")
        else:
            print("Unexpected response format.")
    else:
        print(f"Failed to get user, response status: {resp.status}")
        # Handle unsuccessful response appropriately
