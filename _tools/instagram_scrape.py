import instaloader

# Create an instance
L = instaloader.Instaloader(download_comments=False, save_metadata=False, post_metadata_txt_pattern='')

L.login('tim_claessen_', 'Jenae41103!')  # Save your credentials or use .load_session_from_file

# Download posts from profile
username = "__tablemanners__"
L.download_profile(username, profile_pic=False, fast_update=True, download_stories=False)
