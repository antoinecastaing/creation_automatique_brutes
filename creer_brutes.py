import sys
import json
from playwright.sync_api import sync_playwright

username = "username"
password = "password"
user_id = int(sys.argv[1])
nombre_essais = int(sys.argv[2])
bonus_legendaires = ['flail', 'leek', 'piopio', 'whip', 'chef', 'flashFlood', 'hypnosis', 'immortality', 'reconnaissance', 'sabotage', 'untouchable', 'bear', 'panther']


def creer_compte_et_brute():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        creer_compte(page)
        se_connecter(page)
        creer_brute(page)

        browser.close()

def creer_compte(page):

    #print(f"\nCréation d'un compte. ({essai + 1}/{nombre_essais})")
    page.goto("https://eternaltwin.org/register/username", wait_until="networkidle")
    page.wait_for_selector('input[name="username"]')
    page.fill('input[name="username"]', f"{username}{user_id}")
    page.fill('input[name="display_name"]', f"{username}{user_id}")
    page.fill('input[name="password"]', password)
    page.fill('input[name="password2"]', password)
    page.get_by_role("button", name="Register").click()

def se_connecter(page):

    games_link = page.get_by_role("link", name="Games").click()
    page.locator('a.btn[href="https://brute.eternaltwin.org/"]').click()
    page.get_by_role("button", name="Connect").click()

def creer_brute(page):

    #print(f"Création de {username.capitalize()}{user_id}.")

    page.wait_for_selector('svg[data-testid="PersonIcon"]', state="visible")
    field = page.locator("input.css-15yrxak")
    field.fill(f"{username}{user_id}")

    envoyer_au_camp_si_talent(page)
    
def recupere_bonus_brute(page):

    with page.expect_response(lambda reponse: f"https://brute.eternaltwin.org/api/brute/{username}{user_id}/for-hook?" in reponse.url) as reponse_info:
        page.get_by_text("Validate").click()

    reponse = reponse_info.value.json()

    bonus, = next(i for i in (reponse["weapons"], reponse["skills"], reponse["pets"]) if i)

    print(f"Une brute a obtenu: {bonus.capitalize()} {"🔥🔥🔥🔥🔥" if bonus in bonus_legendaires else "👎"}")

    return bonus

def envoyer_au_camp_si_talent(page):

    bonus = recupere_bonus_brute(page)

    if bonus in bonus_legendaires:

        with open("stockage_brutes/camp_talents.json", "r", encoding="utf-8") as f: camp_talents = json.load(f)

        camp_talents.update({f"{username}{user_id}": bonus.capitalize()})

        with open("stockage_brutes/camp_talents.json", "w", encoding="utf-8") as f: json.dump(camp_talents, f, indent=4)


for essai in range(nombre_essais):

    creer_compte_et_brute()

    user_id += 1
