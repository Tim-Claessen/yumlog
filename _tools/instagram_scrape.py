import instaloader

# Create an instance
L = instaloader.Instaloader(download_comments=False, save_metadata=False, post_metadata_txt_pattern='')

# Optional: login to access private profiles or higher rate limits
# L.login('your_username', 'your_password')

# Download posts from profile
username = "instagram_username_here"
L.download_profile(username, profile_pic=False, fast_update=True, download_stories=False)
