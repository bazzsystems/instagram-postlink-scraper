from concurrent.futures import ThreadPoolExecutor
from instaloader import Instaloader, ProfileNotExistsException, Profile

L = Instaloader()

L.login("USER", "PASS")

def process_profile(L, PROFILE):
    try:
        posts = Profile.from_username(L.context, PROFILE).get_posts()
        try:
            most_recent_post = next(posts)

            post_url = f"https://www.instagram.com/p/{most_recent_post.shortcode}"

            with open('post_urls.txt', 'a') as output_file:
                print("Printing to file...")
                output_file.write(f"1172 | {post_url} | 2 | comment | comment \n")
                print("Done")
        except StopIteration:
            return
    except ProfileNotExistsException:
        return


with open('users.txt') as file:
    with ThreadPoolExecutor() as executor:
        for i in range(2000):#5 = 2 line of urls
            PROFILE = file.readline().strip()
            executor.submit(process_profile, L, PROFILE)
