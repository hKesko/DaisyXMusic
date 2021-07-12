# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith

import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQA-aSKT09C56_FA18R9-6M9zsfLeEe7sChma5913Mt4iAwL-BbXwZk8YJ8FVIFjsA3KRx4h5jAamiaQfSnZT2QRUIhT8ZK5NP-CZ0Y4QAt5g_VAAeDiwRbtK3eR1Z-VCdCVUwwkDWj6MY-LXY0i3Dti9bW3FjOFvstsxclbhBsoJl7WoWCFIdDdXFPGAOdeiOM8TGyPJrBKIKEQHoUoJqUYYHcan8Xwzlg4oi_DPOYs8D7j-sf-RPbasIWgwFVUYXJFz-LPT29c665FL6_ALLhSf3DGcj6Glus-zAcWJPk-sridtjHMwffe0KKfaHz7tvvEgxJNDYcR5VP0kHFE7MNC6ePgA")
BOT_TOKEN = getenv("BOT_TOKEN", "1436379751:AAFq8G8HL0kJqVc3iRLssn8xY-O5bYuQZe0")
BOT_NAME = getenv("Vc Bot")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DaisyXupdates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/dcfdf612e499eef0e0b1f.png")
admins = {}
API_ID = int(getenv("API_ID", "3272504"))
API_HASH = getenv("bb682c5362ad3c5b10e355a8ccc58e91")
BOT_USERNAME = getenv("SongsOnVc_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "DaisyXhelper")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "DaisySupport_Official")
PROJECT_NAME = getenv("PROJECT_NAME", "DaisyXMusic v5")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/TeamDaisyX/DaisyXMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
ARQ_API_KEY = getenv("SSABHB-EZTGNX-ADJUXD-BUQWUL-ARQ", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
#SUDO_USERS = list(map(int, getenv("875470398").split()))
