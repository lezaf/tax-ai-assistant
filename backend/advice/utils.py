import uuid

# TODO: truncate old messages

def _create_or_update_history(chat, role, content):
    '''
    Creates or updates the chat messages.

    If chat is empty, then it defines model behavior and guidelines.
    Else, it includes current content in the history.
    '''
    # Define model behavior
    if not chat.messages:
        with open('./AIDeveloperSettings/setting1.txt', 'r') as f:
            setting_content = f.read().replace('\n', ' ')

        chat.messages.append(
            {
                "role": "developer",
                "content": setting_content
            }
        )

    # Add new message
    chat.messages.append(
        {
            "role": role,
            "content": content
        }
    )


def _create_user_content(user_data, user_prompt):
    '''Includes user data in user prompt.'''
    user_data_str = ", ".join(f"{k} = {user_data[k]}" for k in user_data)
    user_prompt = f"The user provided following data: {user_data_str}." \
                  f" User's message is : {user_prompt}"
    
    return user_prompt


def _set_user_id_session_attribute(request):
    '''Creates a user id for the session.'''
    if 'user_id' not in request.session:
        request.session['user_id'] = str(uuid.uuid4())
        request.session.modified = True