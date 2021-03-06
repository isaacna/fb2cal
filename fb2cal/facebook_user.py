class FacebookUser:
    def __init__(self, id, name, profile_url, profile_picture_uri, birthday_day, birthday_month):
        self.id = id
        self.name = name
        self.profile_url = profile_url
        self.profile_picture_uri = profile_picture_uri
        self.birthday_day = birthday_day
        self.birthday_month = birthday_month

    def __str__(self):
        return f'{self.name} ({self.birthday_day}/{self.birthday_month})'
    
    def __unicode__(self):
        return u'{self.name} ({self.birthday_day}/{self.birthday_month})'