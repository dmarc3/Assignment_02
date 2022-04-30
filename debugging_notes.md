# Debugging Notes: #
Below are all bugs found and fixes incorporated for `menu.py`.

1. `load_users`:
2. `load_status_updates`:
3. `add_user`:
4. `udpate_user`:
5. `search_user`:
6. `delete_user`:
7. `save_user`:
8. `add_status`:
9. `update_status`:
    - Marcus: `update_status` method is incorrectly calling `main.add_status` when it should be calling `main.update_status`.
    - Marcus: Argument order is different between `main.update_status` and `main.add_status`. Updated accordingly.
10. `search_status`:
11. `delete_status`:
12. `save_status`:
13. `quit_program`: