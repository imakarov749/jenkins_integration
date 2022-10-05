from selene import have, command
from selene.support.shared import browser


def close_app():
    ads = browser.all('[id^=google_ads_][id$=container__]')
    if ads.wait.until(have.size_greater_than_or_equal(2)):
        ads.perform(command.js.remove)