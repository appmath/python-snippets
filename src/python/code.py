async def process_user():
    users_list_resp, resp, err = await get_user()

    if err is not None:
        print(f"Error occurred: {err}")
        return

    if isinstance(users_list_resp, list) and len(users_list_resp) > 0:
        user_id = users_list_resp[0].id
        print(f"First user ID: {user_id}")
    elif hasattr(users_list_resp, 'id'):
        user_id = users_list_resp.id
        print(f"User ID: {user_id}")
    else:
        print("Unexpected response format or empty list.")
