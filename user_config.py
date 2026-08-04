# https://www.freecodecamp.org/learn/python-v9/#lab-user-configuration-manager

def add_setting(settings, key_value):
    key = key_value[0].lower()
    value = key_value[1].lower()

    for setting in settings:
        if setting == key:
            return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value

    return f"Setting 'volume' added with value 'high' successfully!"

def update_setting(settings, key_value):
    key = key_value[0].lower()
    value = key_value[1].lower()

    for setting in settings:
        if setting == key:
            settings[setting] = value
            return f"Setting '{key}' updated to '{value}' successfully!"

    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()

    for setting in settings:
        if setting == key:
            settings.pop(key)
            return f"Setting '{key}' deleted successfully!"
    
    return "Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."
    
    settings_str = "Current User Settings:\n"

    for key, value in settings.items():
        settings_str += f"{key.capitalize()}: {value}\n"

    return settings_str

test_settings = {'theme': 'light'}

add = add_setting(test_settings, ('volume', 'high'))

print(add)

update = update_setting(test_settings, ('notifications', 'enabled'))

print(update)

delete = delete_setting(test_settings, 'notifications')

print(delete)

print(view_settings(test_settings))
