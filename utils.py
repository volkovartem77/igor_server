
import simplejson

from config import MEMORY_CACHE, MEM_USERS


def set_mem_cache(var, prefix, data):
    MEMORY_CACHE.set(f'{var}:{prefix}', simplejson.dumps(data))


def get_mem_cache(var, prefix):
    data = MEMORY_CACHE.get(f'{var}:{prefix}')
    return simplejson.loads(data) if data is not None else None


def delete_mem_cache(var, prefix):
    MEMORY_CACHE.delete(f'{var}:{prefix}')


def mem_get_users():
    prefix = f''.lower()
    return get_mem_cache(MEM_USERS, prefix)


def mem_set_users(users: list):
    prefix = f''.lower()
    set_mem_cache(MEM_USERS, prefix, users)


def mem_add_user(user: dict):
    users = mem_get_users()
    if users is not None:
        users.append(user)
        mem_set_users(users)


def mem_get_user_by_id(user_id: int):
    users = mem_get_users()
    if users is not None:
        users_filtered = list(filter(lambda u: u['id'] == user_id, users))
        return users_filtered[0] if users_filtered else None


def mem_get_user_by_name(user_name: int):
    users = mem_get_users()
    if users is not None:
        users_filtered = list(filter(lambda u: u['name'] == user_name, users))
        return users_filtered[0] if users_filtered else None


def mem_remove_user_by_id(user_id: int):
    users = mem_get_users()
    if users is not None:
        users_filtered = list(filter(lambda u: u['id'] != user_id, users))
        mem_set_users(users_filtered)


def mem_update_user_by_id(user_id: int, user: dict):
    users = mem_get_users()
    if users is not None:
        users_filtered = list(filter(lambda u: u['id'] == user_id, users))
        if users_filtered:
            mem_user = users_filtered[0]
            mem_user.update(user)
            users_filtered_out = list(filter(lambda u: u['id'] != user_id, users))
            users_filtered_out.append(mem_user)
            mem_set_users(users)
