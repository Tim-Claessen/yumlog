import instaloader

# Create an instance
L = instaloader.Instaloader(download_comments=False, save_metadata=False, post_metadata_txt_pattern='')

L.login('tim_claessen_', 'Jenae41103!')  # Save your credentials or use .load_session_from_file

# Target profile to scrape
target_profile = "__tablemanners__"

# Download posts (safely - without fast_update)
L.download_profile(target_profile, profile_pic=False, download_stories=False)