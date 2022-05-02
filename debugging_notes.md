# Debugging Notes: #
Below are all bugs found and fixes incorporated for `menu.py`. Kathleen focused on 1-10 and the `user.py` portion of code. Marcus focused on 11-21 and the `user_status.py` portion of code.

1. `load_users`:
2. `load_status_updates`:
3. `add_user`:
4. `update_user`:
5. `search_user`:
6. `delete_user`:
7. `save_user`:
8. `add_status`:
9. `update_status`:
    - Marcus: `update_status` method is incorrectly calling `main.add_status` when it should be calling `main.update_status`.
    - Marcus: Argument order is different between `main.update_status` and `main.add_status`. Updated accordingly.
10. `search_status`:
    - Marcus: `search_status` method assumed result is always a `StatusCollection`. However, `main.search_status` returns `None` when `status_id` doesn't exist. Changed if statement line to `if not result` since it will return `False` if a `StatusCollection` class is supplied.
11. `delete_status`:
    - None
12. `save_status`:
13. `quit_program`:
14. `__main__`:
    - Marcus: The key used in the `menu_options` call needs to be changed to upper case in order to call the correct method. Changed `user_selection` to upper case before if statement and `menu_options`.