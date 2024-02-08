from icecream import ic


async def process_user():
    users_list_resp, resp, err = await get_user()

    if err is not None:
        ic(err)
        return

    if isinstance(users_list_resp, list) and len(users_list_resp) > 0:
        user_id = users_list_resp[0].id
        ic(user_id)
    elif hasattr(users_list_resp, 'id'):
        user_id = users_list_resp.id
        ic(user_id)
    else:
        ic("Unexpected response format or empty list.")
