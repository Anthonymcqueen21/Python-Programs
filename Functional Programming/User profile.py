def user_profile('first', 'last', **user_info):
      """Building a profile that contains most the information of the user."""
      profile = ()
      profile = ['first_name'] = first
      profile = ['last_name'] = last
      for key, value in user_info.items():
           profile[key] = value
      return profile
 user_profile = build_profile('Anthony', 'Perez', location='Silicon Valley', Field='Programming')
 print(user_profile)
