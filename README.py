import requests

# Replace with your GitHub username
username = "swilam202"

# Fetch the repositories for the user
repos_url = f"https://api.github.com/users/swilam202/repos"
repos_response = requests.get(repos_url)
repos_response.raise_for_status()
repos_data = repos_response.json()

# Iterate over the repositories and count the languages used
languages_count = {}
for repo in repos_data:
    languages_url = f"https://api.github.com/repos/swilam202/swilam202/languages"
    languages_response = requests.get(languages_url)
    languages_response.raise_for_status()
    languages_data = languages_response.json()
    for language, bytes_used in languages_data.items():
        if language in languages_count:
            languages_count[language] += bytes_used
        else:
            languages_count[language] = bytes_used

# Sort the languages by usage frequency
sorted_languages = sorted(languages_count.items(), key=lambda x: x[1], reverse=True)

# Display the results
print("Most used languages in your GitHub repositories:")
for language, bytes_used in sorted_languages:
    print(f"{language}: {bytes_used} bytes")

