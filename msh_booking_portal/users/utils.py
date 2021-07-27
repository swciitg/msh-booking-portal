import json


def load_from_user_data(user, form_object, fields_to_load):
    '''Loads the values from stored data into the given form.'''

    data = json.loads(user.data or '{}')
    for field in fields_to_load:
        if fields_to_load[field] in data:
            form_object.fields[field].initial = data[fields_to_load[field]]

    return form_object


def save_to_user_data(user, post_object, fields_to_save):
    '''Saves the `fields_to_save` for future use in the data attribute of `SiteUser`.'''

    data = json.loads(user.data or '{}')
    for field in fields_to_save:
        data[fields_to_save[field]] = post_object[field]

    user.data = json.dumps(data)
    user.save()
