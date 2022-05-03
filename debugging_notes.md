# Debugging Notes: #
Below are all bugs found and fixes incorporated for `menu.py`.<br>
Kathleen Wong focused on 1-10 and the `user.py` portion of code.<br>
Marcus Bakke focused on 11-21 and the `user_status.py` portion of code.

## Testing ``menu.py`` ##

1. Load the users database.
2. Add a new user and confirm you get a success message.
3. Try to add the same user ID again and confirm you get an error message.
4. Update the name of an existing user.
5. Try to update the name of a non-existing user and confirm you get an error message.
6. Search for an existing user and return that user's email, name and last name.
7. Search for a non-existing user and return a message indicating that the user does not exist.
8. Delete an existing user.
9. Try to delete a non-existing user and confirm you get an error message.
10. Save the users database.
11. Load the status database.
12. Add a new status and confirm you get a success message.
13. Try to add the same status ID again and confirm you get an error message.
14. Update the text of an existing status ID.
    - `update_status` method is incorrectly calling `main.add_status` when it should be calling `main.update_status`.
    - Argument order is different between `main.update_status` and `main.add_status`. Updated accordingly.
15. Try to update the text of a non-existing status ID and confirm you get an error message.
16. Search for an existing status ID and return the ID of the user that created the status and the status text.
    - `search_status` method assumed result is always a `StatusCollection`. However, `main.search_status` returns `None` when `status_id` doesn't exist. Changed if statement line to `if not result` since it will return `False` if a `StatusCollection` class is supplied.
17. Search for a non-existing status ID and return a message indicating that the status ID does not exist.
18. Delete an existing status.
19. Try to delete a non-existing status and confirm you get an error message.
20. Save the status database.
21. Make sure menu options are case-insensitive (i.e., typing "a" or "A" works in the same way).
    - The key used in the `menu_options` call in `__main__` needs to be changed to upper case in order to call the correct method. Changed `user_selection` to upper case before if statement and `menu_options`.
    